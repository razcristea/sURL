# sURL
Simple URL shortener

This is a simple URL shortener app.

I used python 3.5.1 and Flask.

## Implementation under WSGI:
WSGI stands for Web Server Gateway Interface. Actually, it's Python Web Server Gateway Interface, because WSGI is a Python standard, born as a PEP (Python Enhancement Proposal) from the need of a simple and universal interface between web servers and web applications or frameworks (Flask, Django, Bottle and so forth).

WSGI has to be implemented on both server and framework sides in order to use its interface so that web server will know how to communicate with web application, and how scripts within the web application can be chained together to process one request.

On server side, in Apache implementation is made using configuration files that specify where an application should be imported from, and how URL requests are passed (sort of URL mapping).

MOD_WSGI shoul be installed in order to use WSGI with Apache. Just run in terminal:
`apt-get install libapache2-mod-wsgi`

The first route we need to declare is the WSGI application. If we would like to point our app at the root of web server (eg. http://domain.com), we use:
`WSGIScriptAlias / /var/www/surl/surl.wsgi`

Instead, if we would like to make it available at a suburl (eg. http://domain.com/ourapp), we declare as:
`WSGIScriptAlias /ourapp /var/www/surl/surl.wsgi`

We need to declare permissions; under previous line, add:
`WSGIScriptAlias / /var/www/surl/surl.wsgi

<Directory /var/www/surl>
	Order deny, allow
	Allow from all
</Directory>`

Add a few more directories:

`WSGIScriptAlias / /var/www/surl/surl.wsgi

<Directory /var/www/surl>
	Order deny, allow
	Allow from all
</Directory>`
