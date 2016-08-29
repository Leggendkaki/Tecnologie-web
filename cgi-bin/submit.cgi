#!C:\Perl64\bin\perl.exe
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
my $upload_dir = "../www/uploads";

my $cgi = new CGI;

my $nickname = $cgi->param('nickname');
my $email = $cgi->param('email');
my $title = $cgi->param('title');
my $description = $cgi->param('description');
my $latitude = $cgi->param('latitude');
my $longitude = $cgi->param('longitude');
my $filename = $cgi->param("photo");
my $timestamp= strftime '%Y-%m-%d', localtime();


print "Content-type: text/html \n\n";
print "<html><body>";

if ( !$filename )
{
print $cgi->header ( );
print "There was a problem uploading your photo (try a smaller file).";
exit;
}

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


my $fileDati = "../www/xml/portals.xml";
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

print "<p>Portale aggiunto<p>";

print " </body> </html>";
