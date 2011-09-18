from urllib2 import  urlopen
import sys, os, datetime, socket, time

socket.setdefaulttimeout(20)
def checkExternalSites(sites):
	logfile=open('logfile.txt','a')
	logtime=time.strftime("%a, %d %b %y %H:%M:%S")
	print logtime
	logfile.write(logtime + '\n')
	for site in sites:
		try:
		
			start=time.time()
			data=urlopen('https://'+site)
			stuff=data.read()
			end=time.time()
			difference=end-start
			report='%s took %2.2f seconds to load' %( site, difference )
			logfile.write(report + '\n')
			print report
		except:
			
			error_type, error_value = sys.exc_info()[:2]
			if error_type == socket.timeout :
				timeouterror + "There was a timeout"
				logfile.write(timeouterror +'\n')
				print "timeouterror +'\n'"
				raw_input("Press enter to continue ")
				return
			else:
				connection_error = "Error connecting to %s" %(site)
				logfile.write(connection_error + '\n')
				print connection_error + '\n'
				raw_input("Plz enter to continue")

def checkInternalWebservers(servers,port):
	logfile = open("logfile.txt", "a")
	logtime=time.strftime("%a, %d %b %y %H:%M:%S")
	print logtime
	logfile.write(logtime + '\n')
	files = ['textfile.txt', 'binaryfile.exe']
	
	
	
	try:
		for server in servers:
			start = time.time()
			serveroutput = server + ':'
			logfile.write(serveroutput + '\n')
			print serveroutput
			for each_file in files:
				url = 'http://' + '%s:%s/%s'%(server,port,each_file)
				print "Now downloading %s"%(url)
				data=urlopen(url)
				stuff=data.read()
				end=time.time()
				difference=end-start
				print '%s took %2.2f seconds to load' %(each_file, difference )
				logfile.write('%s took %2.2f seconds to load'%( each_file,difference )) 
	except:
		error_type, error_value = sys.exc_info()[:2]
		if error_type== socket.timeout:
			timeouterror = 'there was a timeout'
			logfile.write(timeouterror + '\n\n')
			print timeouterror
			logfile.close()
			raw_input('Press Enter to continue: ')
			return
		else:
			connection_error = 'Error connecting to server ' + server
			logfile.write(connection_error + '\n\n')
			print connection_error
			raw_input('Press Enter to Continue: ')
			return
	print '\n'
	logfile.write('\n')
	logfile.close()
	raw_input('Press Enter to Continue: ')

				


			
			
	
		
	

			
	

	

