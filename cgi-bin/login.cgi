#!/usr/bin/perl
use warnings;
use XML::LibXML;
use HTML::Entities;
use CGI;
use CGI::Carp qw(fatalsToBrowser);

my $cgi = new CGI;

print $cgi->header;
print $cgi->start_html('Area Amministratore');


my $username = $cgi->param("username");
my $pwd = $cgi->param("password");

my $file = "../www/xml/login.xml";
my $parser = XML::LibXML->new();

my $doc = $parser-> parse_file($file) || die("Ci sono problemi con il database xml");

my $login=0;
foreach $j ($doc->findnodes('/administrator/id')) {
	my $user = $j->findnodes('./user');
	my $password = $j->findnodes('./password');
	if($user eq $username && $password eq $pwd) {
		$login=1;
	}
}
if($login==0){
	print '<script>alert("Utente non trovato"); location.href = "../login.html";</script>';
}
else 	{
	print "<script type=\"text/javascript\">document.cookie='UTENTE=ok' ;</script>";
	print '<script>location.href = "admin.cgi";</script>';
}

print $cgi->end_html;
exit;
