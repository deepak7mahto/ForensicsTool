import random_functions, os, Forensics_tool_redesigned_using_oops
import argparse
from socket import *

#Port Scanner

class Port_Scanner_class( random_functions.random_functions_class):
    def module7(self):
        self.seperator()
        print "Port Scanner Module"
        self.seperator()

        def printBanner(connSock,tgtPort):
            try:
                # Send data to target
                if(tgtPort == 80):
                    connSock.send("GET HTTP/1.1 \r\n")
                else:
                    connSock.send("\r\n")
            
                # Receive data from target
                results = connSock.recv(4096)
                # print the banner
                print '[+] Banner:' + str(results)
            except:
                print '[-] Banner not available\n'

        def connScan(tgtHost,tgtPort):
            try:
                # Create the socket object
                connSock=socket(AF_INET,SOCK_STREAM)
                # try to connect with the target
                connSock.connect((tgtHost,tgtPort))
                print '[+] %d tcp open'% tgtPort
                printBanner(connSock,tgtPort)
            except:
                # Print the failure results
                print '[+] %d tcp closed'% tgtPort
            finally:
                # close the socket object
                connSock.close()

        def portScan(tgtHost,tgtPorts):
            try:
                #if -a was not an IP address this will resolve it to an IP/ if it's an IP that's fine it will return the same IP
                tgtIP = gethostbyname(tgtHost)
            except:
                print "[-] Error: Unknown Host"
                exit(0)

            try:
                # if the domain can be resolved that's good, the results will be something like: ('domain.com', [], ['20.13.64.15'])
                tgtName = gethostbyaddr(tgtIP)
                print "[+]--- Scan result for: " + tgtName[0] + " ---"
            except:
                print "[+]--- Scan result for: " + tgtIP + " ---"

            setdefaulttimeout(10)

            # For each port number call the connScan function
            for tgtPort in tgtPorts:
                connScan(tgtHost, int(tgtPort))

        self.seperator()
        add = str(raw_input("Enter Address (ex. 192.168.1.100) :-> "))
        self.seperator()
        ports = str(raw_input("Enter Port (ex. 80, 21, 8080, 443) :-> "))
        self.seperator()
        try:
            portScan(add,ports.split(","))
        except Exception as e:
            print e

        self.module7()