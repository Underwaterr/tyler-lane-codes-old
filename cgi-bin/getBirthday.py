#!/usr/bin/python

import cgi, cgitb
cgitb.enable()

print "Content-type: text/html\n\n"
#form = cgi.FieldStorage()
#print form + "\n"

import login
birthday = login.login()
print birthday[1] + "/" + birthday[0] + "/" + birthday[2]