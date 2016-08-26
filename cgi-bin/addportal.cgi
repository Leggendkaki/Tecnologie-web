#!C:\Perl64\bin\perl.exe
use warnings;
use XML::LibXML;
use HTML::Entities;
use CGI;
use CGI::Carp qw(fatalsToBrowser);

my $cgi = new CGI;

my $nickname = $cgi->param('nickname');
my $email = $cgi->param('email');
my $portalname = $cgi->param('portalname');
my $description = $cgi->param('description');
my $latitude = $cgi->param('latitude');
my $longitude = $cgi->param('longitude');
my $portalimage = $cgi->param('portalimage');

print "Content-type: text/html \n\n";
print "<html><body>";


my $fileDati = "../www/xml/portals.xml";
my $parser = XML::LibXML->new();
my $doc = $parser-> parse_file($fileDati) || die("Operazione di parsificazione fallita");
my $root = $doc->getDocumentElement || die("Radice non recuperata");


my $frammento = "	<portal>
		<nickname>" . $nickname . "</nickname>
    <email>" . $email . "</email>
    <portalname>" . $portalname . "</portalname>
    <description>" . $description . "</description>
    <latitude>" . $latitude . "</latitude>
    <longitude>" . $longitude . "</longitude>
    <portalimage>" . $portalimage . "</portalimage>
	</portal>\n";

my $padre = $root;
$frammento = $parser->parse_balanced_chunk($frammento);
$padre->appendChild($frammento);


open(OUT, ">$fileDati");
print OUT $doc->toString;
close(OUT);

print "<p>Portale aggiunto<p>";

print " </body> </html>";
