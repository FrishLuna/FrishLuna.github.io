# -*- coding: utf-8 -*-
"""生成 FrishLuna 站点：index + docs 四页。共享同一套样式与导航。"""
import io, os

ROOT = os.path.dirname(os.path.abspath(__file__))

def page(title, desc, body, active='', crumb=''):
    nav = ''
    items = [('index.html', '首页'), ('docs/quickstart.html', '跑起来'), ('docs/onebot.html', 'OneBot'), ('docs/config.html', '配置'), ('docs/faq.html', '问题')]
    for href, name in items:
        cls = ' class="on"' if href == active else ''
        nav += f'<a href="{href}"{cls}>{name}</a>'
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0d0f14">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ccircle cx='16' cy='16' r='14' fill='%230e1016'/%3E%3Cpath d='M20 7a10 10 0 1 0 5 12A8 8 0 0 1 20 7z' fill='%23e8e6f0'/%3E%3C/svg%3E">
<style>
  :root{{
    --bg:#0d0f14; --panel:#131722; --panel-2:#171c28; --line:#242b3a;
    --text:#e6e8ef; --dim:#96a0b5; --accent:#9d8cff; --accent-2:#6ee7c8;
    --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,"Liberation Mono",monospace;
  }}
  *{{box-sizing:border-box}}
  html{{scroll-behavior:smooth}}
  html,body{{margin:0;padding:0}}
  body{{background:var(--bg);color:var(--text);
    font:16px/1.75 -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;
    -webkit-font-smoothing:antialiased;overflow-x:hidden}}
  a{{color:var(--accent);text-decoration:none}}
  a:hover{{color:#b3a8ff}}
  .wrap{{max-width:860px;margin:0 auto;padding:0 24px}}
  #progress{{position:fixed;top:0;left:0;right:0;height:2px;z-index:999;
    background:linear-gradient(90deg,var(--accent),var(--accent-2));
    transform:scaleX(0);transform-origin:0 50%;pointer-events:none}}
  header{{border-bottom:1px solid var(--line);
    background:radial-gradient(700px 200px at 50% -80px, rgba(157,140,255,.18), transparent 70%),var(--bg)}}
  .bar{{display:flex;align-items:center;justify-content:space-between;padding:18px 0}}
  .brand{{display:flex;align-items:center;gap:10px;font-weight:600;letter-spacing:.02em;color:var(--text)}}
  .brand svg{{display:block}}
  .bar nav{{display:flex;gap:16px;font-size:14px;flex-wrap:wrap}}
  .bar nav a{{color:var(--dim)}}
  .bar nav a:hover{{color:var(--text)}}
  .bar nav a.on{{color:var(--text);border-bottom:2px solid var(--accent);padding-bottom:2px}}
  .hero{{padding:48px 0 56px}}
  .hero h1{{font-size:34px;line-height:1.3;margin:0 0 14px;font-weight:650;letter-spacing:-.01em}}
  .hero p{{color:var(--dim);font-size:16px;max-width:640px;margin:0}}
  .kicker{{display:inline-flex;align-items:center;gap:9px;font:600 12px/1 var(--mono);
    letter-spacing:2px;color:var(--accent);margin-bottom:14px}}
  .kicker i{{width:16px;height:2px;background:linear-gradient(90deg,var(--accent),var(--accent-2));border-radius:2px}}
  section{{padding:44px 0}}
  h2{{font-size:19px;margin:0 0 8px;font-weight:600}}
  .lead{{color:var(--dim);margin:0 0 24px;font-size:15px}}
  h3{{font-size:15.5px;margin:30px 0 8px;font-weight:600}}
  p{{color:var(--dim);font-size:15px}}
  table{{border-collapse:collapse;width:100%;font-size:14px}}
  th,td{{border:1px solid var(--line);padding:9px 12px;text-align:left;vertical-align:top}}
  th{{background:var(--panel-2);color:var(--text);font-weight:600}}
  td{{color:var(--dim)}}
  td code,p code,li code{{font-family:var(--mono);font-size:12.5px;color:var(--accent-2);
    background:#0a1118;border:1px solid var(--line);border-radius:5px;padding:1px 6px}}
  pre{{background:var(--panel-2);border:1px solid var(--line);border-radius:10px;
    padding:14px 16px;overflow:auto;font-family:var(--mono);font-size:12.5px;line-height:1.8;color:#cfd6e6}}
  pre code{{background:none;border:0;padding:0;color:inherit}}
  .card{{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:18px 20px 16px;
    transition:transform .25s,border-color .25s}}
  .card:hover{{transform:translateY(-3px);border-color:#39425a}}
  .card h3{{margin:0 0 6px;font-size:15px}}
  .card p{{margin:0;font-size:14px;line-height:1.7}}
  .grid{{display:grid;gap:14px}}
  @media(min-width:720px){{.grid.two{{grid-template-columns:1fr 1fr}}}}
  ol.steps{{list-style:none;counter-reset:s;margin:0;padding:0}}
  ol.steps li{{counter-increment:s;position:relative;padding:0 0 20px 44px;color:var(--dim);font-size:15px}}
  ol.steps li:last-child{{padding-bottom:0}}
  ol.steps li::before{{content:counter(s);position:absolute;left:0;top:2px;width:26px;height:26px;border-radius:50%;
    border:1px solid var(--line);background:var(--panel-2);display:flex;align-items:center;justify-content:center;
    font:600 12px/1 var(--mono);color:var(--accent)}}
  ol.steps b{{color:var(--text);font-weight:600}}
  ul.plain{{margin:0;padding:0;list-style:none}}
  ul.plain li{{padding:9px 0;border-bottom:1px dashed var(--line);color:var(--dim);font-size:15px}}
  ul.plain li:last-child{{border-bottom:0}}
  ul.plain b{{color:var(--text);font-weight:600}}
  .qa{{margin:0 0 14px}}
  .qa dt{{color:var(--text);font-weight:600;font-size:15px;padding:10px 0 4px}}
  .qa dd{{margin:0;color:var(--dim);font-size:14.5px}}
  .note{{background:linear-gradient(180deg, rgba(157,140,255,.07), transparent);
    border:1px solid var(--line);border-left:3px solid var(--accent);
    border-radius:8px;padding:16px 20px;font-size:14.5px;color:var(--dim)}}
  .note b{{color:var(--text)}}
  .note p{{margin:0 0 10px;font-size:14.5px}}
  .note p:last-child{{margin:0}}
  footer{{border-top:1px solid var(--line);padding:26px 0 46px;color:#6f788c;font-size:13.5px}}
  footer .row{{display:flex;flex-wrap:wrap;gap:16px;justify-content:space-between}}
  footer a{{color:#8d96ab}}
  .pager{{display:flex;justify-content:space-between;gap:12px;padding:28px 0 6px;font-size:14px}}
  [data-reveal]{{opacity:0;transform:translateY(20px);
    transition:opacity .55s ease,transform .55s cubic-bezier(.2,.7,.2,1)}}
  [data-reveal="left"]{{transform:translateX(-24px)}}
  [data-reveal="zoom"]{{transform:scale(.95)}}
  [data-reveal].in{{opacity:1;transform:none}}
  @media (prefers-reduced-motion: reduce){{
    html{{scroll-behavior:auto}}
    [data-reveal]{{opacity:1;transform:none;transition:none}}
    .card{{transition:none}}
    #progress{{display:none}}
  }}
</style>
</head>
<body>
<div id="progress"></div>
<header>
  <div class="wrap bar">
    <a class="brand" href="{'../index.html' if crumb else 'index.html'}">
      <svg width="22" height="22" viewBox="0 0 32 32" aria-hidden="true">
        <circle cx="16" cy="16" r="15" fill="#141824" stroke="#2b3346"/>
        <path d="M20.5 7a10 10 0 1 0 4.8 12.4A8 8 0 0 1 20.5 7z" fill="#cfc6ff"/>
      </svg>
      FrishLuna
    </a>
    <nav>{nav}</nav>
  </div>
</header>
{body}
<footer>
  <div class="wrap row">
    <div>© 2026 FrishLuna · 代码以 <a href="https://github.com/FrishLuna/FrishLuna/blob/main/LICENSE">MIT</a> 许可发布</div>
    <div><a href="https://github.com/FrishLuna">GitHub</a> · <a href="https://github.com/FrishLuna/FrishLuna/issues">问题反馈</a></div>
  </div>
</footer>
<script>
(function(){{
  var rm = matchMedia('(prefers-reduced-motion: reduce)').matches
  var io = new IntersectionObserver(function(es){{
    es.forEach(function(e){{
      if (e.isIntersecting){{ e.target.classList.add('in'); io.unobserve(e.target) }}
    }})
  }}, {{ threshold: .12 }})
  document.querySelectorAll('[data-reveal]').forEach(function(el){{
    if (rm){{ el.classList.add('in'); return }}
    var d = el.getAttribute('data-delay')
    if (d) el.style.transitionDelay = d + 'ms'
    io.observe(el)
  }})
  var bar = document.getElementById('progress')
  var ticking = false
  function frame(){{
    ticking = false
    var h = document.documentElement
    var max = h.scrollHeight - h.clientHeight
    bar.style.transform = 'scaleX(' + (max > 0 ? h.scrollTop / max : 0) + ')'
  }}
  addEventListener('scroll', function(){{
    if (ticking) return
    ticking = true
    requestAnimationFrame(frame)
  }}, {{ passive: true }})
  frame()
}})()
</script>
</body>
</html>
'''

def sec(kicker, title, lead, inner, reveal='data-reveal'):
    return f'''<section>
  <div class="wrap">
    <div class="kicker"{reveal}><i></i>{kicker}</div>
    <h2{reveal} data-delay="60">{title}</h2>
    <p class="lead"{reveal} data-delay="120">{lead}</p>
    {inner}
  </div>
</section>'''

P = {}

# ---------- 快速开始 ----------
P['docs/quickstart.html'] = page(
  '跑起来 · FrishLuna',
  'FrishLuna 从零到发出第一条消息：环境要求、启动步骤、初始令牌、验证方法。',
  sec('01 · 环境', '需要什么',
      '全是本机的东西，不碰云端。',
      '''<table data-reveal>
<tr><th>项目</th><th>要求</th></tr>
<tr><td>系统</td><td>Windows 10 / 11，x64</td></tr>
<tr><td>QQ</td><td>QQNT 桌面版，普通安装即可，不用改任何安装文件</td></tr>
<tr><td>Node.js</td><td>装一个较新的 LTS 版本即可，项目零 npm 依赖，不需要 <code>npm install</code></td></tr>
<tr><td>ffmpeg（可选）</td><td>只有群相册上传视频要拿它抽首帧封面；发文本、图片、语音都用不上</td></tr>
</table>''')
  + sec('02 · 四步', '从零到发出第一条消息',
      '每一步都发生在本机。',
      '''<ol class="steps">
<li data-reveal="left"><b>正常启动并登录 QQ。</b>界面、聊天照常用，这个客户端你该干嘛干嘛。</li>
<li data-reveal="left" data-delay="90"><b>双击 <code>app\\启动 FrishLuna.vbs</code>。</b>面板在后台常驻（关窗口不会停），浏览器自动打开 <code>127.0.0.1:5701</code>。想看日志就用 <code>app\\前台运行.cmd</code>，关窗口即停。</li>
<li data-reveal="left" data-delay="180"><b>输入初始令牌。</b>首次启动会生成一个初始令牌并在控制台打印一次——后台方式看不到输出，所以第一次建议用「前台运行.cmd」跑一遍，把令牌抄下来。</li>
<li data-reveal="left" data-delay="270"><b>改掉初始令牌。</b>登录后第一件事：面板设置 → 访问令牌，设置你自己的。设置成功即换盐换哈希，初始令牌立刻作废。</li>
</ol>''')
  + sec('03 · 令牌', '访问令牌规则',
      '面板不是公开服务，令牌是唯一门锁。',
      '''<ul class="plain">
<li data-reveal><b>8 到 64 位，必须同时含字母和数字。</b>可以加 <code>!@#$%^&amp;*()-_+=[]{{}};:,.?/~</code> 里的符号。不合规的输入前后端都会拦。</li>
<li data-reveal data-delay="70"><b>只存哈希。</b>项目根 <code>.env</code> 里只有 16 字节盐 + scrypt 哈希，没有明文，也没有能解密回来的副本。</li>
<li data-reveal data-delay="140"><b>强度提示。</b>设置页有实时强度条：字母+数字为低，大小写+数字为中，再加特殊字符为高。</li>
<li data-reveal data-delay="210"><b>忘了怎么办。</b>删掉 <code>.env</code> 里 <code>FL_AUTH_*</code> 那几行重启，会重新发一个初始令牌。令牌不可回显，没有找回这回事。</li>
<li data-reveal data-delay="280"><b>登录态。</b>只存浏览器 sessionStorage，关浏览器即失效。</li>
</ul>''')
  + sec('04 · 验证', '怎么确认装好了',
      '三分钟就能验完。',
      '''<ul class="plain">
<li data-reveal><b>看概览页。</b>连接状态、QQ 进程、消息服务三张卡正常，没有红色报错。</li>
<li data-reveal data-delay="70"><b>发条测试消息。</b>实验台 → 发消息，挑一个你自己的小群发一句，群里能看到就通了。</li>
<li data-reveal data-delay="140"><b>验 OneBot。</b>按 <a href="onebot.html">OneBot 接入</a> 那页的 curl 示例调一次 <code>get_login_info</code>，能拿到本号 QQ 号就说明协议端也通了。</li>
</ul>
<p data-reveal data-delay="210">后台挂着不怕掉：计划任务 <code>FrishLuna Keepalive</code> 每分钟探一次端口，不在就静默拉起，日志在 <code>app\\data\\keepalive.log</code>。</p>''')
)

# ---------- OneBot 接入 ----------
P['docs/onebot.html'] = page(
  'OneBot 接入 · FrishLuna',
  'FrishLuna 内置 OneBot v11 协议端：HTTP / 正向 WS / 反向 WS 三种接法、令牌配置、调用示例与事件说明。',
  sec('01 · 三种接法', '怎么连',
      '协议端在 <code>app/server/onebot-server.js</code>，默认端口 5760。',
      '''<table data-reveal>
<tr><th>方式</th><th>地址</th><th>适合</th></tr>
<tr><td>HTTP API</td><td><code>POST http://127.0.0.1:5760</code></td><td>脚本、单次调用、不想保持连接</td></tr>
<tr><td>正向 WS</td><td><code>ws://127.0.0.1:5760</code></td><td>本机机器人框架主动连进来</td></tr>
<tr><td>反向 WS</td><td>本端连到你的框架地址</td><td>AstrBot 一类支持 aiocqhttp 的框架</td></tr>
</table>
<p data-reveal data-delay="120">令牌在「面板设置 → 协议端令牌」配置；HTTP 和正向 WS 走 <code>Authorization: Bearer</code> 头，反向 WS 也可以直接把令牌写进 URL 的 <code>access_token=</code> 参数。</p>''')
  + sec('02 · 调用', '发一个 action',
      '和 OneBot v11 规范一致：<code>{action, params, echo}</code>。',
      '''<pre data-reveal><code>curl -s http://127.0.0.1:5760 \\
  -H "Authorization: Bearer 你的协议端令牌" \\
  -H "Content-Type: application/json" \\
  -d '{
    "action": "send_group_msg",
    "params": { "group_id": 123456, "message": "hello" },
    "echo": "t1"
  }'</code></pre>
<p data-reveal data-delay="120">回包按 echo 配对：<code>{ status, retcode, data, echo }</code>。</p>''')
  + sec('03 · 能力', '常用 action',
      '完整的 action ↔ 内部调用对应关系以面板实验台为准——实验台里的每一项就是一个 action。',
      '''<ul class="plain">
<li data-reveal><b>消息：</b><code>send_private_msg</code> / <code>send_group_msg</code> / <code>delete_msg</code> / <code>get_msg</code> / <code>get_msg_list</code></li>
<li data-reveal data-delay="70"><b>账号：</b><code>get_login_info</code> / <code>get_status</code></li>
<li data-reveal data-delay="140"><b>群管理：</b><code>set_group_ban</code> / <code>set_group_whole_ban</code> / <code>set_group_kick</code> / <code>set_group_admin</code> / <code>set_group_card</code> / <code>set_group_name</code> / <code>send_group_notice</code></li>
<li data-reveal data-delay="210"><b>查询：</b><code>get_group_list</code> / <code>get_group_member_list</code> / <code>get_friend_list</code></li>
<li data-reveal data-delay="280"><b>媒体：</b><code>get_image</code> / <code>get_record</code> / <code>get_file</code> / <code>upload_group_file</code> / <code>send_video</code></li>
<li data-reveal data-delay="350"><b>互动：</b>戳一戳、表情回应、名片赞等，实验台「互动」页签里的每一项都可直接调用。</li>
</ul>''')
  + sec('04 · 事件', '收方向',
      'HTTP 只做调用；收到消息这类事件走 WS 推。',
      '''<ul class="plain">
<li data-reveal><b>事件实时推。</b>群聊、私聊消息经内置协议端推给已连接的 WS 订阅方，格式按 OneBot v11 事件规范。</li>
<li data-reveal data-delay="70"><b>本号自己发的消息没有回显。</b>QQ 只推它收到的消息，所以外部框架不会响应当前账号自己发的内容——这是客户端行为，不是 bug。</li>
<li data-reveal data-delay="140"><b>self_id 的来路。</b>OneBot 事件里的 <code>self_id</code> 要等本号发过一条消息后才能从消息记录里学出来；学到前后反向 WS 会重连换请求头，面板重启后一般半分钟内恢复。</li>
</ul>''')
  + sec('05 · 反向 WS', '接 AstrBot',
      '反向 WS 是手写的 RFC6455 客户端（Node 全局 WebSocket 加不了自定义头）。',
      '''<ul class="plain">
<li data-reveal><b>握手头。</b>按 aiocqhttp 的校验要求带 <code>Authorization: Bearer</code>、<code>X-Self-ID</code>、<code>X-Client-Role: Universal</code> 三个头。</li>
<li data-reveal data-delay="70"><b>配置。</b>面板设置 → 反向 WS 地址，填你框架的 ws 地址（令牌可并入 <code>access_token=</code>）。</li>
<li data-reveal data-delay="140"><b>验证。</b><code>get_login_info</code> / <code>get_status</code> 按规范应答；连上后事件实时流入框架。</li>
</ul>''')
)

# ---------- 配置与数据 ----------
P['docs/config.html'] = page(
  '配置与数据 · FrishLuna',
  'FrishLuna 的配置项、令牌存储、数据目录与环境变量说明。',
  sec('01 · 面板配置', 'config.json',
      '位置 <code>app/data/config.json</code>，设置页可改。',
      '''<table data-reveal>
<tr><th>键</th><th>说明</th></tr>
<tr><td><code>port</code> / <code>host</code></td><td>面板监听，默认 <code>127.0.0.1:5701</code>；端口被占自动 +1</td></tr>
<tr><td><code>qqExe</code></td><td>QQ 可执行文件路径，需在设置页手动指定</td></tr>
<tr><td><code>autoInject</code></td><td>面板发现 QQ 在跑但没挂载荷时自动注入</td></tr>
<tr><td><code>blockedGroups</code></td><td>禁止发送的群号列表。只拦发送、收消息照常。<b>默认空数组＝不拦任何群，用之前务必填上。</b></td></tr>
<tr><td><code>obServerPort</code> / <code>obServerToken</code> / <code>obServerReverse</code></td><td>OneBot 服务端：端口（默认 5760）、令牌、反向 WS 地址列表</td></tr>
</table>''')
  + sec('02 · 令牌存储', '.env',
      '项目根目录的 <code>.env</code> 只和令牌有关。',
      '''<ul class="plain">
<li data-reveal><code>FL_AUTH_*</code>：16 字节盐 + scrypt 哈希（N=16384/r=8/p=1，64 字节输出）。没有明文令牌。</li>
<li data-reveal data-delay="70">删掉这几行重启＝重置令牌，会重新生成初始令牌并打印一次。</li>
<li data-reveal data-delay="140">这个文件不要提交到任何仓库，<code>.gitignore</code> 已经排除了。</li>
</ul>''')
  + sec('03 · 数据目录', 'app/data',
      '运行时产生的文件都在这儿。',
      '''<table data-reveal>
<tr><th>文件</th><th>内容</th></tr>
<tr><td><code>config.json</code></td><td>上面的面板配置</td></tr>
<tr><td><code>panel.port</code></td><td>面板真实端口（自动顺延后以它为准），看门狗靠它探测</td></tr>
<tr><td><code>keepalive.log</code></td><td>看门狗日志</td></tr>
<tr><td><code>frishluna.db</code></td><td>本地消息与 ID 映射缓存（SQLite）</td></tr>
</table>''')
  + sec('04 · 环境变量', '可选',
      '没有必须设置的，这些都是可选项。',
      '''<table data-reveal>
<tr><th>变量</th><th>作用</th></tr>
<tr><td><code>FL_FFMPEG</code> / <code>FL_FFPROBE</code></td><td>ffmpeg 不在 PATH 里时指定完整路径；只有群相册传视频用得到</td></tr>
<tr><td><code>FL_QQ_APP</code> / <code>FL_QQ_VER</code></td><td>注入器脚本里 QQ 安装路径与版本的覆盖项</td></tr>
</table>''')
)

# ---------- 常见问题 ----------
P['docs/faq.html'] = page(
  '常见问题 · FrishLuna',
  'FrishLuna 常见问题：面板起不来、令牌忘了、注入失败、消息发不出去、QQ 升级后失效怎么办。',
  sec('01 · 启动', '面板相关',
      '先看「前台运行.cmd」的输出，大部分答案就在日志里。',
      '''<dl class="qa">
<dt data-reveal>双击 vbs 没反应？</dt>
<dd data-reveal>用 <code>app\\前台运行.cmd</code> 跑一遍，报什么看什么。多半是 Node.js 没装或不在 PATH。</dd>
<dt data-reveal>端口 5701 被占了？</dt>
<dd data-reveal>自动顺延 +1，真实端口以 <code>app\\data\\panel.port</code> 为准。</dd>
<dt data-reveal>访问令牌忘了？</dt>
<dd data-reveal>删掉项目根 <code>.env</code> 里 <code>FL_AUTH_*</code> 那几行重启，会重新发一个初始令牌（前台运行才能看到）。</dd>
</dl>''')
  + sec('02 · 注入', '载荷相关',
      '注入失败十有八九和 QQ 版本或权限有关。',
      '''<dl class="qa">
<dt data-reveal>注入失败 / 概览卡显示未连接？</dt>
<dd data-reveal>确认 QQ 正在运行且是 QQNT 桌面版；试试以管理员身份跑面板；确认 <code>qqExe</code> 在设置页填对了。</dd>
<dt data-reveal>QQ 刚升级完，功能全空了？</dt>
<dd data-reveal>载荷按版本定位内部函数，大版本更新后可能要重新适配。先别反复重试注入，去仓库看有没有适配公告。</dd>
<dt data-reveal>面板会重复注入吗？</dt>
<dd data-reveal>看门狗和自动注入只处理「QQ 在跑但没挂载荷」的情况，不会对已注入的进程二次注入。</dd>
</dl>''')
  + sec('03 · 消息', '收发相关',
      '',
      '''<dl class="qa">
<dt data-reveal>消息发不出去？</dt>
<dd data-reveal>先查 <code>blockedGroups</code>——默认空数组不拦任何群，但一旦填了群号，发送就会被拦，收消息照常。</dd>
<dt data-reveal>机器人框架不响应我自己发的消息？</dt>
<dd data-reveal>正常。QQ 只推它收到的消息，本号自己发的拿不到回显，所以外部框架不会响应当前账号自己发的内容。</dd>
<dt data-reveal>反向 WS 半分钟才连稳？</dt>
<dd data-reveal>self_id 要等本号发过一条消息才能学出来，学到前后会重连换请求头，属正常流程。</dd>
</dl>''')
  + sec('04 · 其他', '剩下的问题',
      '',
      '''<dl class="qa">
<dt data-reveal>群相册传视频报找不到 ffmpeg？</dt>
<dd data-reveal>装 ffmpeg，或用 <code>FL_FFMPEG</code> / <code>FL_FFPROBE</code> 指定完整路径。纯文本、图片链路用不上它。</dd>
<dt data-reveal>能批量加好友、抢红包吗？</dt>
<dd data-reveal>不能，这类功能没有实现，以后也不加。相关用途见使用须知，别试。</dd>
<dt data-reveal>数据会上传到哪里？</dt>
<dd data-reveal>哪儿都不去。面板只监听 127.0.0.1，消息缓存是本地 SQLite，没有云端组件。</dd>
</dl>
<div class="note" data-reveal style="margin-top:26px">
  <p><b>没解决的？</b>带上「前台运行.cmd」的输出到 <a href="https://github.com/FrishLuna/FrishLuna/issues">Issues</a> 提问。</p>
  <p>还是要那句：要稳定、合规的机器人，用官方的 <a href="https://q.qq.com/">QQ 机器人开放平台</a>。</p>
</div>''')
)

for rel, html in P.items():
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    io.open(path, 'w', encoding='utf-8', newline='\n').write(html)
    print('wrote', rel, len(html))
print('done')
