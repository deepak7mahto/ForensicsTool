import _winreg, random_functions, colorama, _winreg, re, Forensics_tool_redesigned_using_oops 
from unidecode import unidecode

#module 1 - registry forensics

class Registry_Forensics_module1 (random_functions.random_functions_class):
    
    def module1(self):
        try:
            self.seperator()
            print "Registry Module"
            self.seperator()
            print "1. Recently Connected Usb Devices"
            print "2. Recent Docs"
            print "3. AutoRun Files At Startup"
            print "4. Run Commands History"
            print "5. Mounted Devices"
            options_to_be_presented = [self.usb_module, 
                                       self.recent_docs_module, 
                                       self.autorun_module,
                                       self.run_commands,
                                       self.mounted_devices_module]
            self.seperator()
            choice = int(raw_input("Enter Choice : "))-1
            print colorama.ansi.clear_screen(2)    
            self.choice_logic(options_to_be_presented, choice)
            Forensics_tool_redesigned_using_oops.tool_menu_front()
        except KeyboardInterrupt as e:
            os.system("cls")
            self.seperator()
            print colorama.Fore.GREEN + "Shutting Down"
            self.seperator()
        except Exception as e:
            pass

    def usb_module(self):
        print "Recently Connected USB Devices\n"
        hkey = _winreg.HKEY_LOCAL_MACHINE
        init_key = "SYSTEM\\ControlSet001\\Enum\\USBSTOR"
        usbstor_key = _winreg.OpenKey(hkey, init_key)

        data_list = list()
        
        try:
            i=0
            while(Exception):
                i+=1
                usb_key_name = _winreg.EnumKey(usbstor_key,i)
                connected_usb = str(i)+r". "+str(usb_key_name[9:-9])
                data_list.append(connected_usb)
                print connected_usb
                usb_key_val = init_key+"\\"+usb_key_name            
        except Exception as e:
            print "\n"

        o = str(raw_input("Do you want to generate report ? (y/n) : "))
        if o == "y":
            self.report_generator("Connected_USB.pdf", "Connected USB Devices", data_list)
        else :
            pass
        self.module1()

    def recent_docs_module(self):
        print "Recent Docs And Folders\n"
        data_list = list()
        try:
            i=0
            while(Exception):
                i=i+1
                raw_data = _winreg.QueryValueEx(_winreg.OpenKey(_winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs', 0,  _winreg.KEY_READ), str(i))[0]            
                processed_data = str(re.findall(r"\b[ \[\]\(\)\-\.\w]*.lnk\b", raw_data)[0]).strip(r".lnk")
                data = str(processed_data)+"\n"
                print str(i)+r". "+data
                data_list.append(data)
        except Exception as e:
            print (e)

        o = str(raw_input("Do you want to generate report ? (y/n) : "))
        if o == "y":
            self.report_generator("Recent_Docs.pdf", "Recently Accessed Documents", data_list)
        else :
            pass
        self.module1()

    def mounted_devices_module(self):
        data_list = list()
        print "Mounted Devices\n"
        i=0
        try:
            while (Exception):
                i=i+1
                data = str(_winreg.EnumValue(_winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\MountedDevices', 0,  _winreg.KEY_READ), i)[1])+"\n" 
                if "\xB1" in data or "\xB6" in data:
                    pass
                else:
                    d = data.replace("\x00", "")
                    print d
                    data_list.append(d)
        except Exception as e:
            print e

        o = str(raw_input("Do you want to generate report ? (y/n) : "))
        if o == "y":
            self.report_generator("Mounted_Devices.pdf", "Mounted Devices", data_list)
        else :
            pass
        self.module1()

    def autorun_module(self):
        data_list = list()
        self.seperator()
        print "\nAutoRun on Windows Startup \n"
        self.seperator
        self.seperator
        print "\nAutoRun Files at HKLM\Software\Microsoft\Windows\CurrentVersion\Run"

        Key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run") 
        for i in range(1024):                                           
            try:
                n,v,t = _winreg.EnumValue(Key,i)
                self.seperator()
                data = str(n)+" at "+str(v)
                print str(i+1)+". "+data
                data_list.append(data)
            except EnvironmentError:                                               
                print "You have",i," tasks starting at logon..."
                break          
        _winreg.CloseKey(Key)

        self.seperator()
        self.seperator()

        print "\nAutoRun Files at HKCU\Software\Microsoft\Windows\CurrentVersion\Run "

        Key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run") 
        for i in range(1024):                                           
            try:
                n,v,t = _winreg.EnumValue(Key,i)
                self.seperator()
                data = str(n)+" at "+str(v)
                print str(i+1)+". "+data
                data_list.append(data)
            except EnvironmentError:                                               
                print "You have",i," tasks starting at logon..."
                break          
        _winreg.CloseKey(Key)
        
        
        o = str(raw_input("Do you want to generate report ? (y/n) : "))
        if o == "y":
            self.report_generator("AutoRun_Programs.pdf", "AutoRun Programs", data_list)
        else :
            pass
            
        self.module1()

    def run_commands(self):
        data_list = list()
        self.seperator()
        print "Run Commands \n"
        self.seperator()
        Key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\RunMRU") 
        mru_list = list(_winreg.QueryValueEx(Key, "MRUList")[0])
        for i in range(1024):                                           
            try:            
                n,v,t = _winreg.EnumValue(Key,i)
                if n == "MRUList":
                    pass
                else:
                    self.seperator()
                    data = str(n)+" : " +str(v).strip("\\1")
                    print data
                    data_list.append(data)
            except EnvironmentError:     
                break          
        _winreg.CloseKey(Key)             
        self.seperator()
        print "Most Recently Used Commands"
        self.seperator()
        for i in mru_list:
            print "\t"+i
        self.seperator()


        o = str(raw_input("Do you want to generate report ? (y/n) : "))
        if o == "y":
            self.report_generator("Run_Commmands_History.pdf", "Run Commands History", data_list)
        else :
            pass