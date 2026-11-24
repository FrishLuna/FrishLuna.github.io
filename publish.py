# -*- coding: utf-8 -*-
"""通过 Git Data API 发布站点：单提交、作者用 noreply，覆盖带 QQ 邮箱的旧历史。"""
import base64, json, subprocess, sys, os

REPO = 'FrishLuna/FrishLuna.github.io'
ROOT = os.path.dirname(os.path.abspath(__file__))
AUTHOR = {'name': '晚晴', 'email': '215231231+wanqing-last@users.noreply.github.com'}

def api(method, path, payload=None):
    cmd = ['gh', 'api', '--method', method, path]
    if payload is not None:
        cmd += ['--input', '-']
    r = subprocess.run(cmd, input=json.dumps(payload) if payload else None,
                       capture_output=True, text=True, encoding='utf-8')
    if r.returncode != 0:
        print(r.stderr[:500]); sys.exit(1)
    return json.loads(r.stdout)

files = ['index.html', 'docs/quickstart.html', 'docs/onebot.html', 'docs/config.html',
         'docs/faq.html', 'gen.py', '.nojekyll']

tree = []
for f in files:
    p = os.path.join(ROOT, f)
    data = open(p, 'rb').read()
    blob = api('POST', f'/repos/{REPO}/git/blobs',
               {'content': base64.b64encode(data).decode(), 'encoding': 'base64'})
    tree.append({'path': f, 'mode': '100644', 'type': 'blob', 'sha': blob['sha']})
    print('blob', f)

t = api('POST', f'/repos/{REPO}/git/trees', {'tree': tree})
c = api('POST', f'/repos/{REPO}/git/commits', {
    'message': '站点：首页与文档（快速开始 / OneBot / 配置 / 常见问题）',
    'tree': t['sha'], 'parents': [], 'author': AUTHOR})
api('PATCH', f'/repos/{REPO}/git/refs/heads/main', {'sha': c['sha'], 'force': True})
print('commit', c['sha'])

# 开 Pages（幂等：已开就忽略 409/422）
r = subprocess.run(['gh', 'api', '--method', 'POST', f'/repos/{REPO}/pages',
                    '--input', '-'],
                   input=json.dumps({'source': {'branch': 'main', 'path': '/'}}),
                   capture_output=True, text=True, encoding='utf-8')
print('pages:', r.stdout[:120] or r.stderr[:200])
