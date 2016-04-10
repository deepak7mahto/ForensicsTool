import random_functions, colorama, Forensics_tool_redesigned_using_oops
import sqlite3, getpass, os

#module 5 - Browser Forensics

class Browser_forensics_class(random_functions.random_functions_class):

    
    def module5(self):
        try:
            self.seperator()
            print "Browser Forenscics"
            self.seperator() 
            self.seperator() 
            print "1. Chrome Forensics"
            print "2. Mozilla Forensics"
            options_to_be_presented = [self.chrome_forensics,self.mozilla_forensics]
            self.seperator()
            choice = int(raw_input("Enter Choice : "))-1
            print colorama.ansi.clear_screen(2)
            self.choice_logic(options_to_be_presented, choice)
            self.seperator()
            self.top_sites_module()
            Forensics_tool_redesigned_using_oops.tool_menu_front()
        except KeyboardInterrupt as e:
            os.system("cls")
            self.seperator()
            print colorama.Fore.GREEN + "Shutting Down"
            self.seperator()
        except Exception as e:
            pass

    #chrome_tool_start

    def chrome_forensics(self):
        self.seperator() 
        print "Chrome forensics"
        self.seperator() 
        self.seperator() 
        print "1. History"
        print "2. Downloads"
        print "3. KeyWord Searched"
        print "4. Top Sites"
        print "5. AutoFill Data"
        print "6. Generic Data Viwer"
        options_to_be_presented = [self.history_module , 
                                   self.downloads_module, 
                                   self.keyword_module , 
                                   self.top_sites_module ,
                                   self.autofill_data_module,
                                   self.generic_data_viewer]
        self.seperator()
        choice = int(raw_input("Enter Choice : "))-1
        print colorama.ansi.clear_screen(2)    
        self.choice_logic(options_to_be_presented, choice)
        self.seperator()
        self.module5()

    def autofill_data_module(self):
        print "AutoFill Data"
        db_name = "Web Data"
        self.copy_chrome_db_file(db_name)
        print "Fetching Data from Table"
        db_name_conn = sqlite3.connect(db_name+".db")
        db_name_cursor = db_name_conn.cursor()
        data = db_name_cursor.execute('SELECT name, value FROM autofill ORDER BY date_created DESC')
        for item in data:
            print str(item[0].encode("ascii", "replace")) +" : " + str(item[1].encode("ascii", "replace")) 
            self.seperator()

    def top_sites_module(self):
        print "Top Sites"
        db_name = "Top Sites"
        self.copy_chrome_db_file(db_name)
        print "Fetching Data from Table"
        db_name_conn = sqlite3.connect(db_name+".db")
        db_name_cursor = db_name_conn.cursor()
        data = db_name_cursor.execute('SELECT title, url FROM thumbnails ORDER BY url_rank ASC')
        for item in data:
            print str("Title : ")+str(item[0].encode("ascii", "replace")) +"\n" + str("URL : ") + str(item[1].encode("ascii", "replace")) 
            self.seperator()

    def history_module(self):
        print "Printing Chrome History"
        db_name = "History"
        self.copy_chrome_db_file(db_name)
        print "Fetching Data from Table"
        db_name_conn = sqlite3.connect(db_name+".db")
        db_name_cursor = db_name_conn.cursor()
        data = db_name_cursor.execute('SELECT title, url FROM urls ORDER BY last_visit_time DESC')
        for item in data:
            print str("Title : ")+str(item[0].encode("ascii", "replace")) +"\n" + str("URL : ") + str(item[1].encode("ascii", "replace")) 
            self.seperator()

    def downloads_module(self):
        print "Printing Chrome Downloads History"
        db_name = "History"
        self.copy_chrome_db_file(db_name)
        print "Fetching Data from Table"
        db_name_conn = sqlite3.connect(db_name+".db")
        db_name_cursor = db_name_conn.cursor()
        data = db_name_cursor.execute('SELECT target_path, referrer, last_modified FROM downloads ORDER BY start_time DESC')
        for item in data:
            print str("Target Path : ")+str(item[0].encode("ascii", "replace")) +"\n" + str("Target Referrer : ")+str(item[1].encode("ascii", "replace")) +"\n" + str("Last Modified : ") + str(item[2].encode("ascii", "replace"))
            self.seperator()

    def keyword_module(self):
        print "Printing Searched Keywords"
        db_name = "History"
        self.copy_chrome_db_file(db_name)
        print "Fetching Data from Table"
        db_name_conn = sqlite3.connect(db_name+".db")
        db_name_cursor = db_name_conn.cursor()
        data = db_name_cursor.execute('SELECT DISTINCT term FROM keyword_search_terms ORDER BY url_id DESC')
        for item in data:
            print str(item[0].encode("ascii", "replace")) +"\n"
            self.seperator()

    def generic_data_viewer(self):
        self.seperator()
        print "Generic Data Viwer"
        self.seperator()
        print "Select DB Name"
        self.seperator()
        print "1. Web Data"
        print "\n2. History"
        print "\n3. Top Sites"
        print "\n4. Cookies"
        self.seperator()
        db_choice = (raw_input("\nEnter DB Number : "))    
        if int(db_choice) == 1:    
            db_name = "Web Data"        
        elif int(db_choice) == 2:    
            db_name = "History"        
        elif int(db_choice) == 3:    
            db_name = "Top Sites"        
        elif int(db_choice) == 4:    
            db_name = "Cookies"        
        else:
            print "Invalid Option"

        self.copy_chrome_db_file(db_name)
        table_data = self.tables_name_fetch(db_name)
        self.fetch_data_from_table(db_name ,table_data[0][int(table_data[1])])

    def tables_name_fetch(self, db_name):
        print "\ntable fetch function\n\n"
        table_list = []
        db_name_conn = sqlite3.connect(db_name+".db")
        db_name_cursor = db_name_conn.cursor()
        data = db_name_cursor.execute('''select name from sqlite_master where type = \'table\'''')
        for item in data:
            table_list.append( str(item[0].encode("ascii", "replace")))
        print "Select Table to be explored"
        for item in table_list:
            print str(table_list.index(item))+" : "+str(item)
        choice = str(raw_input("\nEnter your choice : "))
        return table_list, choice

    def copy_chrome_db_file(self, db_name):
        print "get databse files"
        username = getpass.getuser()
        chrome_data_path = "C:\\Users\\"+username+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\"
        os.system("copy "+"\""+chrome_data_path+db_name+"\" \""+db_name+".db\"")
        print "File Copied"

    def fetch_data_from_table(self, db_name,table_name):
        print "Fetching Data from Table"
        db_name_conn = sqlite3.connect(db_name+".db")
        db_name_cursor = db_name_conn.cursor()
        data = db_name_cursor.execute('SELECT * FROM '+table_name)
        for item in data:
            print item
            self.seperator()
        
    #chrome_tool_end


    #mozilla_tool_start

    def mozilla_forensics(self):
        self.seperator() 
        print "Firefox forensics"
        self.seperator() 
        self.seperator() 
        print "1. History"
        print "2. Form Data"
        print "3. Generic Data Viwer"
        options_to_be_presented = [self.firefox_history_module, 
                                   self.firefox_form_data_module,
                                   self.firefox_generic_data_viewer]
        self.seperator()
        choice = int(raw_input("Enter Choice : "))-1
        print colorama.ansi.clear_screen(2)    
        self.choice_logic(options_to_be_presented, choice)
        self.seperator()
        module5()

    def firefox_generic_data_viewer(self):
        self.seperator()
        print "Generic Data Viwer"
        self.seperator()
        print "Select DB Name"
        self.seperator()
        print "1. places.sqlite"
        print "\n2. formhistory.sqlite"
        self.seperator()
        db_choice = (raw_input("\nEnter DB Number : "))    
        if int(db_choice) == 1:    
            db_name = "places.sqlite"        
        elif int(db_choice) == 2:    
            db_name = "formhistory.sqlite"             
        else:
            print "Invalid Option"

        self.copy_firefox_db_file(db_name)
        table_data = self.firefox_tables_name_fetch(db_name)
        self.firefox_fetch_data_from_table(db_name ,table_data[0][int(table_data[1])])

    def firefox_tables_name_fetch(self ,db_name):
        print "\ntable fetch function\n\n"
        table_list = []
        db_name_conn = sqlite3.connect(db_name)
        db_name_cursor = db_name_conn.cursor()
        #db_name_cursor.execute('''PRAGMA journal_mode=DELETE''')
        data = db_name_cursor.execute('''select name from sqlite_master where type = \'table\'''')
        for item in data:
            table_list.append( str(item[0].encode("ascii", "replace")))
        print "Select Table to be explored"
        for item in table_list:
            print str(table_list.index(item))+" : "+str(item)
        choice = str(raw_input("\nEnter your choice : "))
        return table_list, choice

    def firefox_fetch_data_from_table(self, db_name,table_name):
        print "Fetching Data from Table"
        db_name_conn = sqlite3.connect(db_name)
        db_name_cursor = db_name_conn.cursor()
        data = db_name_cursor.execute('SELECT * FROM '+table_name)
        for item in data:
            print item

    def firefox_history_module(self):
        print "Printing Firefox History"
        db_name = "places.sqlite"
        self.copy_firefox_db_file(db_name)
        print "Fetching Data from Table"
        db_name_conn = sqlite3.connect(db_name)
        db_name_cursor = db_name_conn.cursor()
        data = db_name_cursor.execute('SELECT title, url, visit_count FROM moz_places ORDER BY last_visit_date DESC')
        for item in data:
            try:
                print str("Title : ")+str(item[0]) +"\n" + str("URL : ") + str(item[1].encode("ascii", "replace")) +"\n" + str("Visit Count : ") + str(item[2])
            except Exception as e:
                print e        
            self.seperator()

    def firefox_form_data_module(self):
        print "Printing Form Data"
        db_name = "formhistory.sqlite"
        self.copy_firefox_db_file(db_name)
        print "Fetching Data from Table"
        db_name_conn = sqlite3.connect(db_name)
        db_name_cursor = db_name_conn.cursor()
        data = db_name_cursor.execute('SELECT fieldname, value FROM moz_formhistory')
        for item in data:
            try:
                print str("Title : ")+str(item[0]) +"\n" + str("URL : ") + str(item[1].encode("ascii", "replace"))
            except Exception as e:
                print e
            self.seperator()

    def copy_firefox_db_file(self, db_name):
        print "getting databse files"
        username = getpass.getuser()    
        firefox_data_path = "C:\\Users\\"+username+"\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\"
        try:
            firefox_profiles_list = os.listdir(firefox_data_path)
            print "\nSelect Firefox Profile\n"
            for item in firefox_profiles_list:
                print str(firefox_profiles_list.index(item))+" : "+str(item)    
            try:
                choice = int(raw_input("\nEnter choice : "))
                firefox_data_path = firefox_data_path+str(firefox_profiles_list[int(choice)])+"\\"
                print firefox_data_path
                os.system("copy "+"\""+firefox_data_path+db_name+"\" \""+db_name+"\"")
                print "File Copied"
            except Exception as e:
                print "Wrong Choice Entered, Please Start Over"
        except Exception as e:
            print e

    #mozilla_tool_end