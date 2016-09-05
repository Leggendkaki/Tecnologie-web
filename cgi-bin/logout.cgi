#!/usr/bin/perl
use warnings;
use XML::LibXML;
use HTML::Entities;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use CGI::Cookie;

my $cgi = new CGI;

print $cgi->header;
print $cgi->start_html('Logout Amministratore');
print "<script type=\"text/javascript\">document.cookie='UTENTE=no' ;</script>";
print '<script>location.href = "../login.html";</script>';
print $cgi->end_html;
exit;
