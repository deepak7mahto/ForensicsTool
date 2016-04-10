from __future__ import print_function
import os, colorama, random

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
            print (colorama.Fore.RED  + "-", end = "")

    #logo

    def logo(self):
        print (colorama.Fore.RED + """
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
        print (colorama.Back.RED + "\nOption Not Recognized\n")

    def choice_logic(self, options_list, choice):
              
        try:
            #implementing switching using dictionary
            for index, item in enumerate(options_list):
                self.options_dict[options_list.index(item)] = options_list[index]
            self.options_dict.get(int(choice), self.default_func)()
        except Exception as e:
            print (e)