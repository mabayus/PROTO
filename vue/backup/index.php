<!DOCTYPE html>
<html lang="fr">
<head>
	
	<meta http-equiv="content-type" content="text/html; charset=utf-8" />
	<title></title>
	<link rel="stylesheet" href="http://code.jquery.com/mobile/1.3.2/jquery.mobile-1.3.2.min.css" />
      <script src="http://code.jquery.com/jquery-1.9.1.min.js"></script> 
      <link rel="stylesheet" href="style.css" />
      <script src="http://code.jquery.com/mobile/1.3.2/jquery.mobile-1.3.2.min.js"></script> 
	<link rel="stylesheet" href="css/reset.css" type="text/css" media="screen">
	<link rel="stylesheet" href="css/style.css" type="text/css" media="screen">
	<link rel="stylesheet" href="css/grid.css" type="text/css" media="screen"> 
	<link href='http://fonts.googleapis.com/css?family=PT+Sans' rel='stylesheet' type='text/css'>  
	<script src="js/jquery-1.6.3.min.js" type="text/javascript"></script>
	<script src="js/cufon-yui.js" type="text/javascript"></script>
	<script src="js/cufon-replace.js" type="text/javascript"></script>
	<script src="js/PT_Sans_400.font.js" type="text/javascript"></script>
	<script src="js/PT_Sans_italic_400.font.js" type="text/javascript"></script> 
	<script src="js/Satisfy_400.font.js" type="text/javascript"></script>
	<script src="js/NewsGoth_400.font.js" type="text/javascript"></script>
	<script src="js/FF-cash.js" type="text/javascript"></script> 
	<script src="js/script.js" type="text/javascript"></script>  
	<script src="js/tms-0.3.js" type="text/javascript"></script>
	<script src="js/tms_presets.js" type="text/javascript"></script>
	<script src="js/jquery.easing.1.3.js" type="text/javascript"></script>	 
	<script src="js/easyTooltip.js" type="text/javascript"></script>
	<!--[if lt IE 7]>
	<div style=' clear: both; text-align:center; position: relative;'>
		<a href="http://windows.microsoft.com/en-US/internet-explorer/products/ie/home?ocid=ie6_countdown_bannercode">
			<img src="http://storage.ie6countdown.com/assets/100/images/banners/warning_bar_0000_us.jpg" border="0" height="42" width="820" alt="You are using an outdated browser. For a faster, safer browsing experience, upgrade for free today." />
		</a>
	</div>
	<![endif]-->
	<!--[if lt IE 9]>
   		<script type="text/javascript" src="js/html5.js"></script>
	<![endif]-->
</head>
<body id="page1">
	<div class="extra">
<!--==============================header=================================-->
		<header>
			<div class="menu-row">
				<div class="main">
					<div class="container_12">
						<div class="grid_12">
							<nav class="fleft">
								<ul class="services-menu">
									<li class="m1"><a href="index.php"></a></li>
									
								</ul>
							</nav>
							<nav class="fright">
						<!--		<ul class="main-menu">
									<li class="active"><a href="">Upload </a></li>
									<li><a href="">Charger un design</a></li>
									<li><a href="">Gallerie</a></li>
									<li><a href="">Services</a></li>
									<li><a href="">Deconnection</a></li>
								</ul> -->
							</nav>
							<div class="clear"></div>
						</div>
						<div class="clear"></div>
					</div>
				</div>
			</div>
			<div class="header-row"><div class="ic"></div>
				<div class="main">
					<h1>
						<a href="index.html">aaaaaa</a>
						<em>ACCELERATEUR DE LA TRANSFORMATION NUMERIQUE</marquee></em> 
					</h1> 
					<div class="">
						<div class="">
							<!-- ici se trouve la fenetre principale-->
							<?php include('auth.html') ?>
						</div>
						
					</div>
					<div class="container_12">
						<div class="wrapper">
							<article class="grid_4">
								<h4>About Us</h4>
							</article>
							<article class="grid_4">
								<div class="indent-left">
									<h4>Our Gallery</h4>
								</div>
							</article>
							<article class="grid_4">
								<div class="indent-left2">
									<h4>About Theme</h4>
								</div>
							</article>
							
						</div>
					</div>				   
				</div>
			</div>
			
		</header>
		
<!--==============================content================================-->
		
<!--==============================footer=================================-->
	<footer>
		<div class="footer-bg">
			<div class="main">
				<div class="container_12">
					<div class="wrapper">
						<div class="grid_12">
							<div class="wrapper">
								<span class="footer-text"> Website Template by <a href="http://www.templatemonster.com/" target="_blank" rel="nofollow">georges MPOUANS</a></span>
								<ul class="list-services">
									<li>Follow Us:</li>
									<li class="item-1"><a class="tooltips" title="facebook" href="#"></a></li>
									<li class="item-2"><a class="tooltips" title="twitter" href="#"></a></li>
									<li class="item-3"><a class="tooltips" title="picasa" href="#"></a></li>
								</ul>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</footer>
	<script type="text/javascript"> Cufon.now(); </script>
	<script type="text/javascript">
		$(window).load(function() {
			$('.slider')._TMS({
				duration:800,
				easing:'easeOutQuad',
				preset:'simpleFade',
				slideshow:7000,
				banners:false,
				pauseOnHover:true,
				pagination:'.pagination',
				pagNums:false
			});
		});
	</script>
</body>
</html>
