import random_functions, os, exifread, Forensics_tool_redesigned_using_oops
from PIL import Image
from PIL.ExifTags import TAGS

#module 4 - JPEG Forensics

class Jpeg_forensics_class( random_functions.random_functions_class):

    
    def module4(self):
        data_list = list()
        try:
            self.seperator()
            print "JPEG Forensics"
            self.seperator()
            print "JPEG EXIF Extractor"
            self.seperator()
            self.seperator()

            print "Select File "
            self.seperator()
            temp_file_array = []
            
            if not os.path.exists("Image_folder"):
                os.mkdir("Image_folder")    

            self.seperator()
            print "Paste Files whose exif to be generated"
            self.seperator()
            os.system("explorer Image_folder")  
            
            for root, dirs, files in os.walk("Image_folder", topdown=False):
                for name in files:
                    if "jpeg" in name or "jpg" in name:
                        temp_file_array.append(name)

            if not temp_file_array:
                self.seperator()
                print "\n\nPaste Files , No files in Image_Folder"
                self.seperator()

            file_array = list(set(temp_file_array))

            #print file_array

            for item in file_array:
                print str(int(file_array.index(item))+1)+" : "+(os.path.basename(item))
            file_choice = int(raw_input("\nEnter Choice : "))
            file_choice_name = file_array[file_choice-1]
            print "\n\nYou Selected file : "+file_choice_name

            try:
                f = open("Image_folder//"+file_choice_name, 'r')
                data = exifread.process_file(f)
                for k, v in data.items():
                    
                    data_list.append(str(k)+" : "+str(v))
                    print "|-------------------------------------------|---------------------------------|"
                    print "|---"+str("{:40}".format(k)) +"|"+str("{:<20}".format(v))+""
                    print "|-------------------------------------------|---------------------------------|"

                o = str(raw_input("\n\nDo you want to generate report ? (y/n) : "))
                if o == "y":
                    self.report_generator("Exif_Data_"+file_choice_name+".pdf", "Exif Data for "+file_choice_name, data_list)
                else :
                    pass
            except Exception as e:
                print e
            Forensics_tool_redesigned_using_oops.tool_menu_front()
        except KeyboardInterrupt as e:
            os.system("cls")
            self.seperator()
            print colorama.Fore.GREEN + "Shutting Down"
            self.seperator()
        except Exception as e:
            pass
        