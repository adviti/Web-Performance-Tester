import os
import webperformancetester


def menu():
	
	print	'''========================================================
	WEB PERFORMANCE TESTER
	========================================================
	1 - Test client connection to external web sites
	2 - Test internal web server performance
	3 - Display log file
	4 - Exit
	========================================================
	Enter a choice and press enter:'''

	choice= raw_input()
	return choice


choice=''

def manager():
	choice=menu()
	while choice != '4':

	

		
		if choice == '1':
			print "WEB PERFORMANCE TESTER - EXTERNAL SITE CHECK"
			sites=[]
		        s=raw_input("Enter the sites seperated by space")
		        sites=s.split(' ')
		        webperformancetester.checkExternalSites(sites)
	
		elif choice=='2':
			print "WEB PERFORMANCE TESTER - INTERNAL WEBSERVER CHECK"
			servers=[]
			s=raw_input("Enter the IP adresses of the systems on which python webserver is running seperated by spaces")
			servers=s.split(' ')
			port=raw_input("Enter the port webserver is listening on  ")
			webperformancetester.checkInternalWebservers(servers,port)
	
		elif choice=='3':
			os.system('gedit logfile.txt')
	
manager()
		        
		                
	

