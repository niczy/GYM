
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
<title>{{ text_home_page_title }}</title>
<link rel="stylesheet" type="text/css" media="screen" href="static/css/desktop/main.css" media="all"/>

<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no" />

</head>
<body id="login">
<!--[if lte IE 6]>
<div id="ie6-warning" style="color:red;font-size:18px">你正在使用的浏览器版本太低，将不能正常浏览本站及使用知乎的所有功能。请升级 <a href="http://windows.microsoft.com/zh-CN/internet-explorer/downloads/ie">Internet Explorer</a> 或使用 <a href="http://www.google.com/chrome/">Google Chrome</a> 浏览器。</div>
<![endif]-->
<div id="page">
<h1>{{ text_home_page_title }}</h1>
<div id="login_form">
<form action="/login" method="post">
<input type="hidden" name="_xsrf" value="bf127eb4e078478c868d749141f68838"/>
<ul class="clearfix">
<li>
<label for="email">邮箱</label>
<input type="email" id="email" class="text r5px" name="email" spellcheck="false" placeholder="yourname@example.com" autofocus />
</li>
<li>
<label for="password">密码</label>
<input type="password" id="password" class="text r5px" name="password" />
</li>
<li class="last">
<label for="">&nbsp;</label>
<input type="submit" id="button_login" class="r5px button_blue" value="登 录" />
</li>
<li>
<input id="remember_me" type="checkbox" name="rememberme" />
<label for="remember_me" class="remember_me">记住我的登录状态</label>
</li>
<li>
<a href="/resetpassword">忘记密码？</a>
</li>
</ul>
</form>
<div class="zu-index-link-apply-x2 r5px">
<a href="/apply" class="zu-index-link-apply r5px"><span class="r5px zu-index-link-apply-x1">申请注册</span></a>
</div>
</div>
<div id="footer">
<p>&copy; 2011 GYM &middot; <a href="http://blog.zhihu.com/" target="_blank">GYM博客</a> &middot; <a href="http://weibo.com/wenzhihu" target="_blank" rel="nofollow">新浪微博</a>
<br />
<a href="http://www.miibeian.gov.cn/" target="_blank">京ICP备12345678号</a></p>
</div>
</div>
<!--[if lt IE 7 ]>
<script src="http://static.zhihu.com/static/js/dd_fix.js"></script>
<script>DD_belatedPNG.fix('#login, #page, ##page h1');</script>
<![endif]-->
</body>
</html>