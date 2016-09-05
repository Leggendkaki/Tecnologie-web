#!/usr/bin/perl -w
use strict;
use warnings;
use XML::LibXML;
use HTML::Entities;
use POSIX qw(strftime);
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use File::Basename;


$CGI::POST_MAX = 5000 * 5000;

my $safe_filename_characters = "a-zA-Z0-9_.-";
my $upload_dir = "../public_html/images/uploads";

my $cgi = new CGI;

my $nickname = $cgi->param('nickname');
my $email = $cgi->param('email');
my $title = $cgi->param('title');
my $description = $cgi->param('description');
my $latitude = $cgi->param('latitude');
my $longitude = $cgi->param('longitude');
my $filename = $cgi->param("picture");
my $timestamp= strftime '%Y-%m-%d', localtime();


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
			<img src="images/icons/button_mobile.png" class="navbar_button" alt="mobile menu"/>
			<img src="images/logo_UP_noback.png" alt="Level UP" class="banner"/>
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
											<!-- CONTENT -->
	<div id="container_submit">

EOF

if ( !$filename )
{
print $cgi->header ( );
print "<div class=\"center\"><h3>ERRORE - Dimensione file troppo grande</h3></div>";
exit;
}
else {
my ( $name, $path, $extension ) = fileparse ( $filename, '..*' );
$filename = $name . $extension;
$filename =~ tr/ /_/;
$filename =~ s/[^$safe_filename_characters]//g;

my $upload_filehandle = $cgi->upload("photo");

open ( UPLOADFILE, ">$upload_dir/$filename" ) or die "$!";
binmode UPLOADFILE;

while ( <$upload_filehandle> )
{
print UPLOADFILE;
}

close UPLOADFILE;


my $fileDati = "../public_html/xml/portals.xml";
my $parser = XML::LibXML->new();
my $doc = $parser-> parse_file($fileDati) || die("Operazione di parsificazione fallita");
my $root = $doc->getDocumentElement || die("Radice non recuperata");

my $frammento = "	<portal>
		<date>" . $timestamp . "</date>
		<img>" . $filename . "</img>
		<title>" . $title . "</title>
		<description>" . $description . "</description>
		<latitude>" . $latitude . "</latitude>
		<longitude>" . $longitude . "</longitude>
		<nickname>" . $nickname . "</nickname>
    <email>" . $email . "</email>
	</portal>\n";

my $padre = $root;
$frammento = $parser->parse_balanced_chunk($frammento);
$padre->appendChild($frammento);


open(OUT, ">$fileDati");
print OUT $doc->toString;
close(OUT);

print "<div class=\"center\"><h3>Portale aggiunto correttamente</h3></div>";
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
