#!C:\Perl64\bin\perl.exe
use warnings;
use XML::LibXML;
use HTML::Entities;
use CGI;
use CGI::Carp qw(fatalsToBrowser);

my $cgi = new CGI;
my $username = $cgi->param("username");
my $pwd = $cgi->param("password");

my $file = "../www/xml/login.xml";
my $parser = XML::LibXML->new();

my $doc = $parser-> parse_file($file) || die("Operazione di parsificazione fallita");

my $login=0;
foreach $j ($doc->findnodes('/administrator/id')) {
	my $user = $j->findnodes('./username');
	my $password = $j->findnodes('./password');
	if($user eq $username && $password eq $pwd) {
		$login=1;
	}
}

print "Content-type: text/html \n\n";
print "<html><body>";


print " </body> </html>";
