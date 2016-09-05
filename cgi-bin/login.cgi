#!/usr/bin/perl
use warnings;
use XML::LibXML;
use HTML::Entities;
use CGI;
use CGI::Carp qw(fatalsToBrowser);


my $cgi = new CGI;

my $username = $cgi->param("username");
my $pwd = $cgi->param("password");

my $file = "../public_html/xml/login.xml";
my $parser = XML::LibXML->new();

my $doc = $parser-> parse_file($file) || die("Operazione di parsificazione fallita");


my $login=0;
foreach $j ($doc->findnodes('/administrator/id')) {
	my $user = $j->findnodes('./user');
	my $password = $j->findnodes('./password');
	if($user eq $username && $password eq $pwd) {
		$login=1;
	}
}

print $cgi->header;
print $cgi->start_html('Area Amministratore');
print <<EOF;


<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="it">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />	<!--Inserito subito, regola 512B-->
		<title>Submit portali</title>
		<meta name="title" content="Ingress Level up - Richiedi portali" />
		<meta name="description" content="Form per richiedere un portale da inserire nel sito" />
		<meta name="keywords" content="Ingress Level up, Ingress, progetto, tecnologie web" />
		<meta name="language" content="italian it" />
		<meta name="author" content="Lorenzo Bellemo, Tommaso Solani" />

		<meta name="HandheldFriendly" content="True"/>		<!--ottimizzazione mobile-->
		<meta name="MobileOptimized" content="320"/>		<!--ottimizzazione mobile-->
		<meta http-equiv="cleartype" content="on"/>

															<!--Fix IE LABORATORIO-->
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
		
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
				<h1 class="maintext">Ingress Level UP</h1>
				<p class="maintext">"The world around you is not what it seems"</p>
			</div>

			<div class="breadcrumb">
				<ol>
					<li>Ti trovi in:</li>
					<li><a href="../index.html">Home</a></li>
					<li>/</li>
					<li>Area Amministratore</li>
				</ol>
			</div>
		</div>

		<div><a class="skip-main" href="#container_submit">Salta al contenuto</a></div>					<!-- pulsante ad alto contrasto per lo skip -->

		<div class="navbar" id="menu">
			<ul>
				<li><a href="../index.html">Home</a></li>
				<li><a href="../description.html">Il gioco</a></li>
				<li><a href="../guide_list.html">Guide</a></li>
				<li><a href="../xml/portals.xml">Portali</a></li>
				<li class="../submit.html">Submit</li>
			</ul>
		</div>
EOF
if($login==1) {
print <<EOF;
		<!-- CONTENT -->


	<div class="center"><h2>Rimuovi portale</h2></div>

	<div class="form">
	<form method="post" action="login.cgi" method="post">
		<label for="latitude">Latitudine</label>
		<input type="text" id="latitude" name="latitude" tabindex="5" accesskey="a">

		<label for="longitude">Longitudine</label>
		<input type="text" id="longitude" name="longitude" tabindex="6" accesskey="o">
		<div class="input_button"><input type="submit" value="Invia" tabindex="8" accesskey="v"></div>
	</form>
	</div>
EOF


my $lat = $cgi->param("latitude");
my $lon = $cgi->param("longitude");

my $fileDati = "../public_html/xml/portals.xml";
$doc = $parser-> parse_file($fileDati) || die("Operazione di parsificazione fallita");

my $portal = $doc->findnodes("//portal[latitude=\'$lat\'\n and longitude=\'$lon\'\n]")->get_node(1);
if(defined $portal) {$portal = $portal->parentNode->removeChild($portal);}


open(OUT, ">$fileDati");
print OUT $doc->toString;
close(OUT);



print "<table>";
print "<tr><th>Nome portale</th><th>Latitudine</th><th>Longitudine</th><tr>";
foreach $a ($doc->findnodes('portal_list/portal')) {
	print "<tr>";
	my $title = $a->findnodes('./title');
	print "<td>". $title ."</td>";
	my $latitude = $a->findnodes('./latitude');
	print "<td>". $latitude ."</td>";
	my $longitude = $a->findnodes('./longitude');
	print "<td>". $longitude ."</td>";
	print "</tr>";
}
print "</table>";
}
else {
  print "<div class=\"center\"><h2>Utente o password errati</h2></div>"
}

print <<EOF;
	</div>
											<!-- FOOTER -->
	<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
	<script type="text/javascript" src="http://arrow.scrolltotop.com/arrow26.js"></script>
	<div id="footer_container">
		<a href="http://validator.w3.org/check?uri=referer">
			<img src="../images/icons/valid-xhtml11.png"  class="valid" alt="Valid XHTML 1.1"/>
		</a>
		<a href="http://jigsaw.w3.org/css-validator/check/referer">
			<img src="../images/icons/vcss-blue.gif"  class="valid" alt="Valid CSS" />
		</a>
	</div>
	<div class="login_button"><a href="login.html"><span xml:lang="en">Admin login</span></a></div>
	</body>
</html>
EOF

print $cgi->end_html;
