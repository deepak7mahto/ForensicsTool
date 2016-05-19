from __future__ import print_function
import os, colorama, random, reportlab
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont   
from reportlab.lib import styles
from reportlab.lib.pagesizes import A4, letter
from reportlab.platypus import (
    BaseDocTemplate, 
    PageTemplate, 
    Frame, 
    Paragraph,
    PageBreak
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.colors import (
    black,
    purple,
    white,
    yellow
)


class random_functions_class():
    def __init__(self):
        colorama.init(autoreset = True)
        self.options_list =[]
        self.options_dict = {}
            
    def get_windows_terminal(self):
        from ctypes import windll, create_string_buffer
        h = windll.kernel32.GetStdHandle(-12)
        csbi = create_string_buffer(22)
        res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
     
        #return default size if actual size can't be determined
        if not res: return 80, 25 
 
        import struct
        (bufx, bufy, curx, cury, wattr, left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
        width = right - left + 1
        height = bottom - top + 1
 
        return width, height

    def get_linux_terminal(self):
        width = os.popen('tput cols', 'r').readline()
        height = os.popen('tput lines', 'r').readline()
 
        return int(width), int(height)

    #seperator

    def seperator(self):
        dim = self.get_linux_terminal() if os.name == 'posix' else self.get_windows_terminal()
        for i in range(int(dim[0])):
            print (colorama.Fore.GREEN  + "-", end = "")

    #logo

    def logo(self):
        print (colorama.Fore.GREEN + """
      ______                       _            _______          _ 
     |  ____|                     (_)          |__   __|        | |
     | |__ ___  _ __ ___ _ __  ___ _  ___ ___     | | ___   ___ | |
     |  __/ _ \| '__/ _ \ '_ \/ __| |/ __/ __|    | |/ _ \ / _ \| |
     | | | (_) | | |  __/ | | \__ \ | (__\__ \    | | (_) | (_) | |
     |_|  \___/|_|  \___|_| |_|___/_|\___|___/    |_|\___/ \___/|_|                            
    """)

    #module chooser function
    def default_func(self):
        #default run
        print (colorama.Back.GREEN + "\nOption Not Recognized\n")

    def choice_logic(self, options_list, choice):
              
        try:
            #implementing switching using dictionary
            for index, item in enumerate(options_list):
                self.options_dict[options_list.index(item)] = options_list[index]
            self.options_dict.get(int(choice), self.default_func)()
        except Exception as e:
            print (e)

    def report_generator(self, file_name, file_heading, file_content):
        self.seperator()
        if not os.path.exists("Files_to_be_hashed"):
            os.mkdir("Files_to_be_hashed")
        print ("Report Generator Started")        
        c = canvas.Canvas("Files_to_be_hashed"+"\\"+file_name, pagesize = letter)
        c.setFont("Helvetica", 20)
        c.drawCentredString(300, 750, "Report : "+str(file_heading))
        c.setFontSize(10)
        h = 700
        for item in file_content:
            i = file_content.index(item)   
            item = unicode(item, 'utf-8', 'ignore')
            h = h -20
            c.drawString(50, h , str(i+1)+" : "+str(item)) 
            if h < 100:
                c.showPage()  
                h = 700  
                c.setFontSize(10)      
        
        c.save()
        self.seperator()
        print ("Report Generation Finished")