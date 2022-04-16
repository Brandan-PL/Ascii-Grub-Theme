
import sys
from colorama import Fore, Style


def readColor() :
    print("\nSelect the color of the interface: \n")

    print(Fore.WHITE + "    1 - " + Fore.RED + "RED")
    print(Fore.WHITE + "    2 - " + Fore.GREEN + "GREEN")
    print(Fore.WHITE + "    3 - " + Fore.BLUE + "BLUE")
    print(Fore.WHITE + "    4 - " + Fore.YELLOW + "ORANGE")
    print(Fore.WHITE + "    5 - " + Fore.WHITE + "WHITE")
    print(Fore.WHITE + "    6 - OTHER")

    print("\n")

    return input("Number: ")

def checkColor(color:str) :
    if (len(color) == 7) :
        if (color[0] == '#') :
            i = 0
            for c in color[1:] :
                ordC = ord(c)
                if (ordC >= 48 and ordC <= 57) or (ordC >= 65 and ordC <= 70) or (ordC >= 97 and ordC <= 102) :
                    i += 1

            if i == 6 : return color
    else : return 0


def selectColor() :
    switch = {
        '1': "#db191b", # RED
        '2': "#15c21c", # GREEN
        '3': "#2773ad", # BLUE
        '4': "#b56117", # ORANGE
        '5': "#ffffff", # WHITE
        '6': "6",
        }

    c = 0
    while c == 0 :
        color = readColor()
        c = switch.get(color, 0)

        if c == "6" :
            print("\nWrite your color. Ej: #ffffff")
            c = checkColor(input("Color: "))

        if c == 0 :
            print(Fore.RED + "\nNumber not valid")
            print(Style.RESET_ALL)

    return c


def readHeading(headers) :
    print("\nSelect the heading: \n")

    for i in range(len(headers)) :
        print(f"    {i+1} -")
        print("".join(headers[i]).replace('@', ' '))

    print("\n")

    return input("Number: ")


def selectHeading() :
    headFile = open("./headings.txt", "r")

    lines = headFile.readlines()
    headFile.close()

    heads = []
    ini = 0
    for l in range(len(lines)) :
        if lines[l] == "\n" :
            heads.append([lines[i] for i in range(ini, l)])
            ini = l+1
        elif l == len(lines)-1 :
            heads.append([lines[i] for i in range(ini, l+1)])

    h = 0
    while h > len(heads) or h <= 0 :
        try:
            h = int(readHeading(heads))
        except Exception as e:
            print(Fore.RED + "\nNumber not valid")
            print(Style.RESET_ALL)
            h = 0

    return heads[h-1]


def createFile(color:str, header) :
    fileD = open("./ascii_theme/theme.txt", "w")

    fileD.write('\n# Global Property\n' + 'title-text: ""\n' + 'desktop-image: "background.png"\n' +
                'desktop-color: "#0c0c0c"\n' + 'terminal-font: "Hack Regular 16"\n' +
                'terminal-box: "terminal_box_*.png"\n' + 'terminal-left: "10%"\n'+ 'terminal-top: "10%"\n' +
                'terminal-width: "80%"\n' + 'terminal-height: "80%"\n' + 'terminal-border: "0"\n')

    fileD.write('\n# Title\n' + '+ vbox {\n' + '  left = 33%\n' + '  top = 10%\n' + '  width = 40%\n')

    for i in header :
        hLine = i[:-1].replace('@', ' ')
        fileD.write('  + label { width = 400 align = "center" ' + f'color = "{color}" font = "Hack Regular 16" text = "{hLine}"' + ' }\n')

    fileD.write('}\n')

    fileD.write('\n# Show the boot menu\n' + '+ boot_menu {\n' + '  left = 30% # 50% - (40% / 2)\n' +
	            '  top = 29%\n' + '  width = 40%\n' + '  height = 50%\n' + '  item_font = "Hack Regular 16"\n' +
                f'  item_color = "{color}"\n' + '  selected_item_color = "#ffffff"\n' + '  selected_item_font = "Hack Bold Italic 16"\n' +
                '  icon_width = 60\n' + '  icon_height = 60\n' + '  item_height = 72\n' + '  item_spacing = 30\n}\n')

    fileD.write('\n+ hbox {\n' + '  left = 43%\n' + '  top = 80%\n' + '  width = 30%\n' +
	'  + label { width = 25% align = "center"' + f' color = "{color}" ' + 'font = "Hack Regular 10" text = "[E] Edit Selection " }\n' +
	'  + label { width = 25% align = "center"' + f' color = "{color}" ' + 'font = "Hack Regular 10" text = " [C] GRUB Command Line" }\n}\n')

    fileD.write('\n# Show a countdown message\n' + '+ label {\n' + '  top = 85%\n' + '  left = 36%\n' + '  width = 30%\n' +
	            '  align = "center"\n' + '  id = "__timeout__"\n' + '  text = "Booting in %d seconds"\n' +
	            f'  color = "{color}"\n' + '  font = "Hack Regular 16"\n}\n')


def main() :
    print("\nWelcome to the Ascii Theme Generator")

    color = selectColor()
    head = selectHeading()

    print(Fore.GREEN + "\nCreating file... \n")

    createFile(color, head)

    print(Fore.GREEN + "\nCreated\n")
    print(Style.RESET_ALL)


if __name__ == "__main__":
    sys.exit(main())
