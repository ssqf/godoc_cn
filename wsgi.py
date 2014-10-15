
from os.path import isfile,isdir
import os

def application(environ, start_response):
	status = '200 OK'
	path='static'+environ['PATH_INFO']
	if path=='static/':
		path='static/index.html'
	if path[-3:]=='css':
		response_headers = [('Content-type','text/css')]
	else:
		response_headers = [('Content-type','text/html')]
	start_response(status, response_headers)
	if isfile(path):
		with open(path,'r') as file:
			return [file.read()]
	if isdir(path):
		dir=os.listdir(path)
		return ['<html><body>','\r\n'.join(['<a href="./%s" traget=_blank>%s</a><br/>'%(d,d) for d in dir]),'</body></html>']
	return ['<h1>not find</h1>']