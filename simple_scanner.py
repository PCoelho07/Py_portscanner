# -*- coding: utf-8 -*-
from socket import *
import sys

def scan(targetIP):
	port = []
	for i in range(20, 1025): 
        	try:
                    print '[!] Tentando se conectar a porta ',str(i)
                    s = socket(AF_INET, SOCK_STREAM)
                    result = s.connect_ex((targetIP, i))
        
                    if result == 0:
                        print "[+] Porta "+str(i)+" aberta!"
                        port.append("[+] Porta "+str(i)+"aberta!")
                        
                    s.close()       

                except KeyboardInterrupt: 
                        print '\n\n[*] Aplicacao encerrada pelo usuario!!'
			sys.exit(1)
	
	return port

def showReport(port):
	if port not null:
		for p in port:
			print p	


if __name__ == 	"__main__":
	try:
		target = raw_input('Digite o host: ')
		targetIP = gethostbyname(target) 

	except KeyboardInterrupt:	
		print "\n\n[!] Aplicacao encerrada pelo usuario!"
		sys.exit(1)
	
	except:	
		print '\n\n[!] Ocorreu um erro!'
		sys.exit(1)

	print 'Começando processo de scanner no host ', targetIP
	port = scan(targetIP)
	showReport(port)

