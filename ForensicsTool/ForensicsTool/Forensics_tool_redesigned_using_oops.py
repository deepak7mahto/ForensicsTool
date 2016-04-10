import os, colorama, random_functions, module1, module2, module3, module4, module5


class Main1(random_functions.random_functions_class): 
    def tool_menu_front(self):
        try:
            colorama.init(autoreset=True)
            self.seperator()
            self.logo()
            self.seperator()
            print "Select the Module"
            self.seperator()

            print "1. Registry Forensics"
            print "2. Event Manager Forensics"
            print "3. File Hashing"
            print "4. JPEG Forensics"
            print "5. Browser Forensics"
            
            self.m1 = module1.Registry_Forensics_module1()
            self.m2 = module2.event_manager_module()
            self.m3 = module3.File_hashing_class()
            self.m4 = module4.Jpeg_forensics_class()
            self.m5 = module5.Browser_forensics_class()

            options_to_be_presented = [self.m1.module1, 
                                       self.m2.module2, 
                                       self.m3.module3, 
                                       self.m4.module4, 
                                       self.m5.module5]
            self.seperator()
            choice = int(raw_input("Enter Choice : "))-1
            print colorama.ansi.clear_screen(2)    
            self.choice_logic(options_to_be_presented, choice)
            self.tool_menu_front()
            
        except KeyboardInterrupt as e:
            os.system("cls")
            self.seperator()
            print colorama.Fore.GREEN + "Shutting Down"
            self.seperator()
        except Exception as e:
            pass

def main():
    Forensics_tool_object = Main1()
    Forensics_tool_object.tool_menu_front()

if __name__ == "__main__":
    main() 

"""

+-----------------------------------------+
| random_functions.random_functions_class |
+-----------------------------------------+
        .                                                                                                                                                                                                                                                                                                                   
       /_\                                                                                                                                                                                                                                                                                                                  
        |                                                                [ random_functions.random_functions_class ]       [ random_functions.random_functions_class ]       [ random_functions.random_functions_class ]       [ random_functions.random_functions_class ]       [ random_functions.random_functions_class ]
        |                                                                               .                                               .                                              .                                                .                                                  .                                
        |                                                                              /_\                                             /_\                                            /_\                                              /_\                                                /_\                               
        |                                                                               |                                               |                                              |                                                |                                                  |                                
        |                                                                               |                                               |                                              |                                                |                                                  |                                
+-----------------+                                                      +-------------------------------+                 +----------------------------+                    +----------------------+                          +--------------------+                            +----------------------+                   
|      Main1      |                                                      |    Browser_forensics_class    |                 | Registry_Forensics_module1 |                    | event_manager_module |                          | File_hashing_class |                            | Jpeg_forensics_class |                   
|-----------------|                                                      |-------------------------------|                 |----------------------------|                    |----------------------|                          |--------------------|                            |----------------------|                   
| m1              |  ---->  [ module2.event_manager_module ]             | module5                       |                 | module1                    |                    | module2              |                          | __init__           |                            | module4              |                   
| m2              |  ---->  [ module4.Jpeg_forensics_class ]             | chrome_forensics              |                 | usb_module                 |                    | Evtx_dumper          |                          | module3            |                            +----------------------+                   
| m3              |  ---->  [ module1.Registry_Forensics_module1 ]       | autofill_data_module          |                 | recent_docs_module         |                    | spinning_cursor      |                          | hash_genertion     |                                                                       
| m4              |  ---->  [ module3.File_hashing_class ]               | top_sites_module              |                 | mounted_devices_module     |                    | login_analyzer       |                          | hash_comparison    |                                                                       
| m5              |  ---->  [ module5.Browser_forensics_class ]          | history_module                |                 +----------------------------+                    +----------------------+                          +--------------------+                                                                       
|-----------------|                                                      | downloads_module              |                                                                                                                                                                                                                  
| tool_menu_front |                                                      | keyword_module                |                                                                                                                                                                                                                  
+-----------------+                                                      | generic_data_viewer           |                                                                                                                                                                                                                  
                                                                         | tables_name_fetch             |                                                                                                                                                                                                                  
                                                                         | copy_chrome_db_file           |                                                                                                                                                                                                                  
                                                                         | fetch_data_from_table         |                                                                                                                                                                                                                  
                                                                         | mozilla_forensics             |                                                                                                                                                                                                                  
                                                                         | firefox_generic_data_viewer   |                                                                                                                                                                                                                  
                                                                         | firefox_tables_name_fetch     |                                                                                                                                                                                                                  
                                                                         | firefox_fetch_data_from_table |                                                                                                                                                                                                                  
                                                                         | firefox_history_module        |                                                                                                                                                                                                                  
                                                                         | firefox_form_data_module      |                                                                                                                                                                                                                  
                                                                         | copy_firefox_db_file          |                                                                                                                                                                                                                  
                                                                         +-------------------------------+                                                                                                                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
+------------------------------------+       +------------------------------+       +----------------------------+
| module1.Registry_Forensics_module1 |       | module2.event_manager_module |       | module3.File_hashing_class |
+------------------------------------+       +------------------------------+       +----------------------------+
                                                                                                           
                                                                                                           
                                                                                                           
                                                                                                           
+------------------------------+       +---------------------------------+       +------------------------+
| module4.Jpeg_forensics_class |       | module5.Browser_forensics_class |       | random_functions_class |
+------------------------------+       +---------------------------------+       |------------------------|
                                                                                 | options_list           |
                                                                                 | options_dict           |
                                                                                 |------------------------|
                                                                                 | __init__               |
                                                                                 | get_windows_terminal   |
                                                                                 | get_linux_terminal     |
                                                                                 | seperator              |
                                                                                 | logo                   |
                                                                                 | default_func           |
                                                                                 | choice_logic           |
                                                                                 +------------------------+


"""