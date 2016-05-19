import random_functions, os, Forensics_tool_redesigned_using_oops
import binascii
import optparse
from PIL import Image


#module 6 - Staganography

class Staganography_class( random_functions.random_functions_class):
    
    def module6(self):
        data_list = list()
        try:

            def rgb2hex(r, g, b):
                return '#{:02x}{:02x}{:02x}'.format(r, g, b)

            def hex2rgb(hexcode):
                return tuple(map(ord, hexcode[1:].decode('hex')))

            def str2bin(message):
                binary = bin(int(binascii.hexlify(message), 16))
                return binary[2:]

            def bin2str(binary):
                message = binascii.unhexlify('%x' % (int('0b'+binary,2)))
                return message

            def encode(hexcode, digit):
                if hexcode[-1] in ('0','1', '2', '3', '4', '5'):
                    hexcode = hexcode[:-1] + digit
                    return hexcode
                else:
                    return None

            def decode(hexcode):
                if hexcode[-1] in ('0', '1'):
                    return hexcode[-1]
                else:
                    return None

            def hide(filename, message):
                print "flag"
                img = Image.open(filename)
                binary = str2bin(message) + '1111111111111110'
                if img.mode in ('RGBA'):
                    img = img.convert('RGBA')
                    datas = img.getdata()
                    newData = []
                    digit = 0
                    temp = ''
                    for item in datas:
                        if (digit < len(binary)):
                            newpix = encode(rgb2hex(item[0],item[1],item[2]),binary[digit])
                            if newpix == None:
                                newData.append(item)
                            else:
                                r, g, b = hex2rgb(newpix)
                                newData.append((r,g,b,255))
                                digit += 1
                        else:
                            newData.append(item)
                    img.putdata(newData)
                    img.save(filename, "PNG")
                    return "Completed!"
                return "Incorrect Image Mode, Couldn't Hide"
            def retr(filename):
                img = Image.open(filename)
                binary = ''
                if img.mode in ('RGBA'):
                    img = img.convert('RGBA')
                    datas = img.getdata()
                    for item in datas:
                        digit = decode(rgb2hex(item[0],item[1],item[2]))
                        if digit == None:
                            pass
                        else:
                            binary = binary + digit
                            if (binary[-16:] == '1111111111111110'):
                                print "Success"
                                return bin2str(binary[:-16])
                    return bin2str(binary)
                return "Incorrect Image Mode, Couldn't Retrieve"


            print "Staganography module"
            """
            parser = optparse.OptionParser('usage %prog -e/-d <target file>')
            parser.add_option('-e', dest='hide', type='string', help='target picture path to hide text')
            parser.add_option('-d', dest='retr', type='string', help='target picture path to retrieve text')
            (options, args) = parser.parse_args()
            if (options.hide != None):
               text = raw_input("Enter a message to hide: ")
               print hide(options.hide, text)
            elif (options.retr != None):
                print retr(options.retr)
            else:
                print parser.usage
                exit(0)
            """

            self.seperator()

            print "Select File "
            self.seperator()
            temp_file_array = []
            
            if not os.path.exists("Steganography_folder"):
                os.mkdir("Steganography_folder")    

            self.seperator()
            print "Paste Files"
            self.seperator()
            os.system("explorer Steganography_folder")  
            
            for root, dirs, files in os.walk("Steganography_folder", topdown=False):
                for name in files:
                    temp_file_array.append(name)

            if not temp_file_array:
                self.seperator()
                print "\n\nPaste Files , No files in Steganography_folder"
                self.seperator()

            file_array = list(set(temp_file_array))

            for item in file_array:
                print str(int(file_array.index(item))+1)+" : "+(os.path.basename(item))
            file_choice = int(raw_input("\nEnter Choice : "))
            file_choice_name = file_array[file_choice-1]
            print "\n\nYou Selected file : "+file_choice_name
            self.seperator()

            self.seperator()
            print "Choose Option : \n1.Encrypt\n2.Decrypt"
            self.seperator()
            choice = str(raw_input("Enter your choice :-> "))
            self.seperator()
            self.seperator()
            if choice == "1":
                msg = str(raw_input("Enter the Message :-> "))
                print hide(str("Steganography_folder"+"\\"+file_choice_name), msg)
            elif choice == "2":
                print retr(str("Steganography_folder"+"\\"+file_choice_name))
            else:
                self.module6()            
        except Exception as e:
            pass
        