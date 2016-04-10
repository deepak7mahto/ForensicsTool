import random_functions, os, exifread, Forensics_tool_redesigned_using_oops
from PIL import Image
from PIL.ExifTags import TAGS

#module 4 - JPEG Forensics

class Jpeg_forensics_class( random_functions.random_functions_class):

    
    def module4(self):
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
            for root, dirs, files in os.walk("Image_folder", topdown=False):
                for name in files:
                    if "jpeg" in name or "jpg" in name:
                        temp_file_array.append(name)

            file_array = list(set(temp_file_array))

            print file_array

            for item in file_array:
                print str(int(file_array.index(item))+1)+" : "+(os.path.basename(item))
            file_choice = int(raw_input("\nEnter Choice : "))
            file_choice_name = file_array[file_choice-1]
            print "You Selected file : "+file_choice_name

            try:
                f = open("Image_folder//"+file_choice_name, 'r')
                data = exifread.process_file(f)
                for k, v in data.items():
                    print "|-------------------------------------------|---------------------------------|"
                    print "|---"+str("{:40}".format(k)) +"|"+str("{:<20}".format(v))+""
                    print "|-------------------------------------------|---------------------------------|"
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