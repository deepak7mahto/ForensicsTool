import shutil, os, Evtx, mmap, contextlib, sys, xml, random_functions, colorama, Forensics_tool_redesigned_using_oops
from Evtx.Evtx import FileHeader
from Evtx.Views import evtx_file_xml_view
from xml.dom import minidom

#module2 - event manager module

class event_manager_module( random_functions.random_functions_class):
    
    def module2(self):
        try:
            self.seperator()
            print "Event Manager Module"
            self.seperator()
            print "1. Evtx Dump"
            print "2. Login Analyzer"
            options_to_be_presented = [self.Evtx_dumper, self.login_analyzer]
            self.seperator()
            choice = int(raw_input("Enter Choice : "))-1
            print colorama.ansi.clear_screen(2)    
            self.choice_logic(options_to_be_presented, choice)
            self.seperator()
            Forensics_tool_redesigned_using_oops.tool_menu_front()
        except KeyboardInterrupt as e:
            os.system("cls")
            self.seperator()
            print colorama.Fore.GREEN + "Shutting Down"
            self.seperator()
        except Exception as e:
            pass

    def Evtx_dumper(self):
        self.seperator()
        evtx_file_name = str(raw_input("Enter the file name or press enter to select \"Security.evtx : "))
        if evtx_file_name == "":
            evtx_file_name = "Security.evtx"
        dumped_logs_path = "C:\\Windows_Event_logs\\Logs\\"+evtx_file_name
        self.seperator()
        print "Dumped log file path : "+dumped_logs_path

        #creating directory in same folder
        if not os.path.exists("Windows_Event_logs"):
            os.mkdir("Windows_Event_logs")    
        log_path = shutil.abspath("Windows_Event_logs")
        #copying security.evtx log file to current directory

        if os.path.exists("C:\Windows_Event_logs\Logs"):
            shutil.copy(dumped_logs_path , log_path)
            self.seperator()
            print "File Copied : "+evtx_file_name
        else:    
            self.seperator()
            print r"Please run dump_logs.bat first to dump Security.evtx in C:\Windows_Event_logs\Logs"        
        #parsing evtx
        file = open("logs.xml", "w")
        file_rec = open("rec.txt", "w")
        i=0

        def spinning_cursor(self):
            while True:
                for cursor in '|/-\\':
                    yield cursor

        spinner = spinning_cursor()
        event_id_in = str(raw_input("Enter the event id or press enter for all events : "))
        self.seperator()
        no_of_records = str(raw_input("Enter no of records or press enter for 10 records : "))
        self.seperator()
        print "Starting Conversion of Evtx to XML"
        self.seperator()
        print "\n\"#\" - for record found \n\"-\" for no record found \n\"_\" for all records \n"
        with open("Windows_Event_logs\\"+evtx_file_name, 'r') as f:
            with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as buf:
                fh = FileHeader(buf, 0x0)
                file.write("<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"yes\" ?>")
                file.write("<Events>")
                self.seperator()
    
                i = 0
                if no_of_records == "":
                    no_of_records = 10

                for xml, record in Evtx.Views.evtx_file_xml_view(fh):            
                    #print xml
                    if i<int(no_of_records):
                        if event_id_in == "":
                            file.write(xml)
                            sys.stdout.write("_")
                        else:
                            xmldoc = minidom.parseString(xml)
                            event_id = xmldoc.getElementsByTagName('EventID')[0].childNodes[0].nodeValue
                            if int(event_id) == int(event_id_in):                
                                file.write(xml)
                                sys.stdout.write("#")            
                            else:
                                sys.stdout.write("-")
                        sys.stdout.write(spinner.next())
                        sys.stdout.flush()
                        sys.stdout.write('\b')
                        #file_rec.write(str(record)+"\n")         
                        i=i+1
                    else:
                        break
                file.write("</Events>")
                print "\n"
                self.seperator()
                print "\nFile Writing Finished"
        self.module2()

    def login_analyzer(self):
        #xml events analyzer
        self.seperator()
        print "Login Analyzer"
        self.seperator()
        xmldoc = xml.dom.minidom.parse("logs.xml")
        flag = 0
        i=0
        l_ = [0,0,0,0,0,0,0,0,0,0]
        try:    
            while(Exception):
                #print xmldoc.getElementsByTagName("Data")[4].childNodes[0].nodeValue
                event_id = str(xmldoc.getElementsByTagName("System")[i].childNodes[2].childNodes[0].nodeValue)
                if int(event_id) == 4624:
                    logon_type = str(xmldoc.getElementsByTagName("EventData")[i].childNodes[16].childNodes[0].nodeValue)
                    if int(logon_type) == 2:
                        l_[0] = l_[0]+1
                    elif int(logon_type) == 3:
                        l_[1] = l_[1]+1
                    elif int(logon_type) == 4:
                        l_[2] = l_[3]+1
                    elif int(logon_type) == 5:
                        l_[4] = l_[4]+1
                    elif int(logon_type) == 6:
                        l_[5] = l_[5]+1
                    elif int(logon_type) == 7:
                        l_[6] = l_[6]+1
                    elif int(logon_type) == 8:
                        l_[7] = l_[7]+1
                    elif int(logon_type) == 9:
                        l_[8] = l_[8]+1
                    elif int(logon_type) == 10:
                        l_[9] = l_[9]+1
                    elif int(logon_type) == 11:
                        l_[10] = l_[10]+1
                    else:
                        print "Invald Logon Type"
                i=i+1
        except Exception as e:
            print e

        self.seperator()
        print "\nLogins Chart\n"
        self.seperator()
        print "\nInteractive  : "+str(l_[0])
        print "\nNetwork : "+str(l_[1])
        print "\nBatch : "+str(l_[2])
        print "\nService : "+str(l_[3])
        print "\nUnlock : "+str(l_[4])
        print "\nNetworkCleartext : "+str(l_[5])
        print "\nNewCredentials : "+str(l_[6])
        print "\nRemoteInteractive : "+str(l_[7])
        print "\nCachedInteractive : "+str(l_[0])
        self.seperator()
        self.module2()