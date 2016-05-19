import random_functions, hashlib, os, Forensics_tool_redesigned_using_oops

#module 3 File Hashing

class File_hashing_class( random_functions.random_functions_class):

    
    def module3(self):
        try:
            self.seperator()
            print "File Hashing"
            self.seperator()
            print "\nSecuring Evidences \n"
            print "1. Generate Hashes\n2. Compare Hashes\n"
            choice = int(raw_input("\nEnter Choice : "))

            if "nt" in os.name:
                os.system("cls")
            else:
                os.system("clear")

            if choice == 1:
                self.hash_genertion()
            elif choice == 2:
                self.hash_comparison()
            else:
                print "\nWrong Option"
            print "\n"
            Forensics_tool_redesigned_using_oops.tool_menu_front()
        except KeyboardInterrupt as e:
            os.system("cls")
            self.seperator()
            print colorama.Fore.GREEN + "Shutting Down"
            self.seperator()
        except Exception as e:
            pass

    def collect_files(self):
        print "Collecting Files"
        if not os.path.exists("Files_to_be_hashed"):
            os.mkdir("Files_to_be_hashed")
        print ""

    def hash_genertion(self):
        data_list = list()
        print "\nGenerate Hashes"
    
        if not os.path.exists("Files_to_be_hashed"):
            os.mkdir("Files_to_be_hashed")    

        print "Paste Files To be Hashed"
        os.system("explorer Files_to_be_hashed")        
        dir_choice_name = "Files_to_be_hashed"
                
        try:
            BLOCKSIZE = 65536
            hasher_md5 = hashlib.md5()
            hasher_sha1 = hashlib.sha1()
            i=0
            for x in os.listdir(dir_choice_name):
                i=i+1
                print str(i) +" : "+ x + "\n"
                with open(dir_choice_name+r"/"+x, 'rb') as afile:
                    buf = afile.read(BLOCKSIZE)
                    while len(buf) > 0:
                        hasher_md5.update(buf)
                        buf = afile.read(BLOCKSIZE)
                    while len(buf) > 0:
                        hasher_sha1.update(buf)
                        buf = afile.read(BLOCKSIZE)
                print "\nMD5 : "+(hasher_md5.hexdigest())
                print "\nSHA1 : "+(hasher_sha1.hexdigest())
                print "\n"
        except Exception as e:
            print e
        self.module3()
    
    def hash_comparison(self):
        print "\nCompare Hashes"

        if not os.path.exists("Files_to_be_hashed"):
            os.mkdir("Files_to_be_hashed")    

        print "\nSelect File \n"
        temp_file_array = []
        for root, dirs, files in os.walk("Files_to_be_hashed", topdown=False):
            for name in files:
                temp_file_array.append(name)            
                print str(int(files.index(name))+1)+" : "+(os.path.basename(name))
        print "\n"+str(temp_file_array)
        file_choice = int(raw_input("\nEnter Choice : "))
        file_choice_name = temp_file_array[file_choice-1]
        print "You Selected file : "+file_choice_name
        user_hash = str(raw_input("\nEnter MD5 HASH : \n"))

        try:
            BLOCKSIZE = 65536
            hasher_md5 = hashlib.md5()
            hasher_sha1 = hashlib.sha1()
            print file_choice_name
            with open(r"Files_to_be_hashed"+r"/"+file_choice_name, 'rb') as afile:
                    buf = afile.read(BLOCKSIZE)
                    while len(buf) > 0:
                        hasher_md5.update(buf)
                        buf = afile.read(BLOCKSIZE)
                    while len(buf) > 0:
                        hasher_sha1.update(buf)
                        buf = afile.read(BLOCKSIZE)
            if user_hash == hasher_md5.hexdigest():
                print "MD5 Hash Verified"
            print "\n"
        except Exception as e:
            print e
        self.module3()