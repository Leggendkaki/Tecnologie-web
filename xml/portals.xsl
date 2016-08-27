<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">

	<html xmlns="http://www.w3.org/1999/xhtml" lang="it">
		<head>
			<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />	<!--Inserito subito, regola 512B-->
			<title>Lista portali</title>
			<meta name="title" content="Ingress Level up - Lista portali" />
			<meta name="description" content="Lista dei portali registrati sul sito" />
			<meta name="keywords" content="Ingress Level up, Ingress, progetto, tecnologie web" />
			<meta name="language" content="italian it" />
			<meta name="author" content="Lorenzo Bellemo, Tommaso Solani" />

			<meta name="HandheldFriendly" content="True"/>		<!--ottimizzazione mobile-->
			<meta name="MobileOptimized" content="320"/>		<!--ottimizzazione mobile-->
			<meta http-equiv="cleartype" content="on"/>

			<link href='https://fonts.googleapis.com/css?family=Coda:400,800' rel='stylesheet' type='text/css' />

			<!-- Link foglio di stile-->
			<link href="../css/style_base.css" rel="stylesheet" type="text/css" media="screen"/>
			<meta name="viewport" content="width=device-width, initial-scale=1"/>	<!-- Website responsive -->


			<script type="text/javascript" src="../js/jquery-1.7.1.min.js"></script>
			<script type="text/javascript">
				$(document).ready(function(){

				//When btn is clicked prova
				$(".navbar_button").click(function() {
				$(".navbar").toggleClass("show");;
				});
				});
			</script>

		</head>

		<body>
												<!-- HEADER -->
			<div id="header_container">
				<img src="../images/icons/button_mobile.png" class="navbar_button" alt="mobile menu"/>
				<img src="../images/logo_UP_noback.png" alt="Level UP" class="banner"/>
				<div class="titles">
					<h1 class="maintext" xml:lang="en">Ingress Level UP</h1>
					<p class="maintext" xml:lang="en">"The world around you is not what it seems"</p>
				</div>

				<div class="breadcrumb">
					<ol>
						<li>Ti trovi in:</li>
						<li><a href="index.html"><span xml:lang="en">Home</span></a></li>
						<li>/</li>
						<li>Portali</li>
					</ol>
				</div>
			</div>

			<div><a class="skip-main" href="#container_index">Salta al contenuto</a></div>					<!-- pulsante ad alto contrasto per lo skip -->

			<div class="navbar" id="menu">
				<ul>
					<li><a href="../index.html"><span xml:lang="en">Home</span></a></li>
					<li><a href="../description.html">Il gioco</a></li>
					<li><a href="../guide_list.html">Guide</a></li>
					<li class="portals.xml not_link">Portali</li>
					<li><a href="../submit.html"><span xml:lang="en">Submit</span></a></li>
				</ul>
			</div>
												<!-- CONTENT -->
		<div id="container_portal_list">


			<div id="container_guide_list">
				<xsl:for-each select="//portal">
				<div class="card card_animation">
						<span class="card_title"><xsl:value-of select="title"/> </span>
						<xsl:variable name="picture">/<xsl:value-of select="img"/></xsl:variable>
						<img src="../uploads/{$picture}" class="card_img" alt="Interfaccia di gioco"/>
						<dt class="card_text">Descrizione</dt>
						<dd class="card_text"><xsl:value-of select="description"/></dd>
						<dt class="card_text">Latitude</dt>
						<dd class="card_text"><xsl:value-of select="latitude"/></dd>
						<dt class="card_text">Longitude</dt>
						<dd class="card_text"><xsl:value-of select="longitude"/></dd>
						<dt class="card_text">Nickname</dt>
						<dd class="card_text"><xsl:value-of select="nickname"/></dd>
					</div>
				</xsl:for-each>
				</div>


		</div>
														<!-- FOOTER -->
		<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
		<script type="text/javascript" src="http://arrow.scrolltotop.com/arrow26.js"></script>
		<div id="footer_container">
			<a href="http://validator.w3.org/check?uri=referer">
				<img src="images/icons/valid-xhtml11.png"  class="valid" alt="Valid XHTML 1.1"/>
			</a>
			<a href="http://jigsaw.w3.org/css-validator/check/referer">
				<img src="images/icons/vcss-blue.gif"  class="valid" alt="Valid CSS" />
			</a>
		</div>
		<div class="login_button"><a href="login.html"><span xml:lang="en">Admin login</span></a></div>
		</body>
	</html>
</xsl:template>
</xsl:stylesheet>
