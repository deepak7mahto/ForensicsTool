import _winreg, random_functions, colorama, _winreg, re, Forensics_tool_redesigned_using_oops 

#module 1 - registry forensics

class Registry_Forensics_module1 (random_functions.random_functions_class):
    
    def module1(self):
        try:
            self.seperator()
            print "Registry Module"
            self.seperator()
            print "1. Recently Connected Usb Devices"
            print "2. Recent Docs"
            print "3. Mounted Devices"

            options_to_be_presented = [self.usb_module, self.recent_docs_module, self.mounted_devices_module]
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
        try:
            i=0
            while(Exception):
                i+=1
                usb_key_name = _winreg.EnumKey(usbstor_key,i)
                print str(usb_key_name[9:-9])
                usb_key_val = init_key+"\\"+usb_key_name
        except Exception as e:
            print "\n"
        self.module1()

    def recent_docs_module(self):
        print "Recent Docs And Folders\n"
        try:
            i=0
            while(Exception):
                i=i+1
                raw_data = _winreg.QueryValueEx(_winreg.OpenKey(_winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs', 0,  _winreg.KEY_READ), str(i))[0]            
                processed_data = str(re.findall(r"\b[ \[\]\(\)\-\.\w]*.lnk\b", raw_data)[0]).strip(r".lnk")
                print (str(i)+r". "+str(processed_data)+"\n")
        
        except Exception as e:
            print (e)
        self.module1()

    def mounted_devices_module(self):
        print "Mounted Devices\n"
        i=0
        try:
            while (Exception):
                i=i+1
                data = str(i)+". "+str(_winreg.EnumValue(_winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\MountedDevices', 0,  _winreg.KEY_READ), i)[1])+"\n" 
                print re.sub(r" ", "", data, flags=0)
        except Exception as e:
            print e
        self.module1()