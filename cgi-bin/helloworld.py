#!/usr/bin/python

import cgi, cgitb
cgitb.enable()

print "Content-type: text/html\n\n"
form = cgi.FieldStorage()
print "I have " + form.getvalue('quantity') + " " + form.getvalue('name') + "s"