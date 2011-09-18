import SimpleHTTPServer, sys, SocketServer
portNo=sys.argv[1]

def runMachineAsServer():
	try:
		httphandler=SimpleHTTPServer.SimpleHTTPRequestHandler
		http_server=SocketServer.TCPServer(("", int(portNo)), httphandler)
		print 'System is working as http_server at %d'%int(portNo)
		http_server.serve_forever()
	except:
		print "There was a problem starting the webserver at port %s" %portNo


runMachineAsServer()
