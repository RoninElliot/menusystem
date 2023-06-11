# menu system v0.1 # 

import readchar,os,colorama,readchar
import xml.etree.ElementTree as ET

configxml = ET.parse('menuconfig.xml')
xml = configxml.getroot()


def cleare():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        

banner = """{}
 _                                                  _ 
| |_____                _____         _            | |
| |     |___ ___ _ _   |   __|_ _ ___| |_ ___ _____| |
| | | | | -_|   | | |  |__   | | |_ -|  _| -_|     | |
| |_|_|_|___|_|_|___|  |_____|_  |___|_| |___|_|_|_| |
|_| {}              |___|                 |_|
{}\n""".format(colorama.Fore.GREEN ,colorama.Style.RESET_ALL + colorama.Fore.RED + "RoninElliot" + colorama.Style.RESET_ALL + colorama.Fore.GREEN, colorama.Style.RESET_ALL)


menuitem1,menuitem2,menuitem3,menuitem4 = 'mainmenu/item1','mainmenu/item2','mainmenu/item3','mainmenu/item4' #default query (mainmenu)

statselector = 1
def printer(slot1,slot2,slot3,slot4):
    global statselector,statemenuint,statemenustr
    cleare()
    print(banner)

    if statemenuint == 0:
        statemenustr = "MainMenu"
    if statemenuint == 1:
        statemenustr = "MainMenu/Play"
    if statemenuint == 2:
        statemenustr = "MainMenu/Load"
    if statemenuint == 3:
        statemenustr = "MainMenu/Options"
    if statemenuint == 4:
        statemenustr = "MainMenu/Quit"

    print('({})'.format(statemenustr))
    print("{}---------------------------{}".format(colorama.Fore.BLUE,colorama.Style.RESET_ALL))
    if statemenuint == 4:
        print("{} {}".format(colorama.Fore.RED , "Are You Sure ?" + colorama.Style.RESET_ALL))

    if statselector == 1:
        print("{} {}".format(colorama.Fore.YELLOW , slot1 + colorama.Style.RESET_ALL))
    else:
        print(slot1)


    if statselector == 2:
        print("{} {}".format(colorama.Fore.YELLOW , slot2 + colorama.Style.RESET_ALL))
    else:
        print(slot2)


    if statselector == 3:
        print("{} {}".format(colorama.Fore.YELLOW , slot3 + colorama.Style.RESET_ALL))
    else:
        print(slot3)


    if statselector == 4:
        print("{} {}".format(colorama.Fore.YELLOW , slot4 + colorama.Style.RESET_ALL))
    else:
        print(slot4)


    print("{}---------------------------{}\n".format(colorama.Fore.BLUE,colorama.Style.RESET_ALL))

statsel = 1
def selector():
    global statsel

    keyb = readchar.readkey()
    
    if keyb == readchar.key.UP:
        statsel -= 1
    
    if keyb == readchar.key.DOWN:
        statsel += 1
    
    if keyb == readchar.key.ENTER:
        enterm()

    if keyb == readchar.key.BACKSPACE:
        backm()

    if statsel <= 0:
        statsel = 1
    if statsel >= 4:
        statsel = 4
    
    return statsel

#------------ menu function ------------#
statemenuint = 0

def get_data_menu(get1,get2,get3,get4):
    item1 = xml.find('{}/title'.format(get1))
    item2 = xml.find('{}/title'.format(get2))
    item3 = xml.find('{}/title'.format(get3))
    item4 = xml.find('{}/title'.format(get4))

    

    printer(item1.text if item1 is not None else "NotFound",
            item2.text if item2 is not None else "NotFound",
            item3.text if item3 is not None else "NotFound",
            item4.text if item4 is not None else "notFound"
            )

def menugo():
    def enter():
        global statemenuint,statsel,menuitem1,menuitem2,menuitem3,menuitem4
        
        # ---- main menu ---- #
        if statemenuint == 5: 
            menuitem1,menuitem2,menuitem3,menuitem4 = 'mainmenu/item1','mainmenu/item2','mainmenu/item3','mainmenu/item4' #default query (mainmenu)

        if statsel == 1 and statemenuint == 0: 
            statsel = 1
            statemenuint = 1
            menuitem1 = 'playmenu/item1'
            menuitem2 = 'playmenu/item2'
            menuitem3 = 'playmenu/item3'
            menuitem4 = 'playmenu/item4'
        if statsel == 2 and statemenuint == 0:
            statsel = 1
            statemenuint = 2
            menuitem1 = 'loadmenu/item1'
            menuitem2 = 'loadmenu/item2'
            menuitem3 = 'empty/emptys'
            menuitem4 = 'empty/emptys'
        if statsel == 3 and statemenuint == 0:
            statsel = 1
            statemenuint = 3
            menuitem1 = 'optionmenu/item1'
            menuitem2 = 'optionmenu/item2'
            menuitem3 = 'optionmenu/item3'
            menuitem4 = 'empty/emptys'
        if statsel == 4 and statemenuint == 0:
            statsel = 4
            statemenuint = 4
            menuitem1 = 'quitmenu/item1'
            menuitem2 = 'quitmenu/item2'
            menuitem3 = 'empty/emptys'
            menuitem4 = 'empty/emptys'
        if statsel == 1 and statemenuint == 4:
            os._exit(0)
        if statsel == 2 and statemenuint == 4:
            menuitem1,menuitem2,menuitem3,menuitem4 = 'mainmenu/item1','mainmenu/item2','mainmenu/item3','mainmenu/item4' #default query (mainmenu)
            statemenuint = 0

    def back():
        global statemenuint,statselector
        statemenuint = 5
        enter()
        statemenuint = 0

    return enter,back
enterm , backm = menugo()

while True:
    get_data_menu(menuitem1,menuitem2,menuitem3,menuitem4)
    statselector = selector()


#End in 02,3,22;1:24 