import pyAesCrypt, getpass
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
from colorama import Fore, Back, Style, init
import os, time, ctypes, random, string, glob, datetime
from tqdm import tqdm

import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("647-ED")

init() # Windows Colorama Support
def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)
def getfilename(file):
        return file.partition("\\")[2]   
print(Fore.GREEN + Style.BRIGHT +
"  /$$$$$$  /$$   /$$ /$$$$$$$$      /$$$$$$$$ /$$$$$$$\n" + 
" /$$__  $$| $$  | $$|_____ $$/     | $$_____/| $$__  $$\n"+
"| $$  \__/| $$  | $$     /$$/      | $$      | $$  \ $$\n"+
"| $$$$$$$ | $$$$$$$$    /$$//$$$$$$| $$$$$   | $$  | $$\n"+
"| $$__  $$|_____  $$   /$$/|______/| $$__/   | $$  | $$\n"+
"| $$  \ $$      | $$  /$$/         | $$      | $$  | $$\n"+
"|  $$$$$$/      | $$ /$$/          | $$$$$$$$| $$$$$$$/\n"+
" \______/       |__/|__/           |________/|_______/\n" +
"                  The Drag&Drop Encryptor\n"+ Fore.CYAN  +                                                    
"\n* What do you want to do?" + Style.RESET_ALL)
option = ""
enc = ["encrypt", "e"]
dec = ["decrypt", "d"]
yes = ["yes", "y"]
no = ["no", "n"]
while option.lower() not in enc and option.lower() not in dec:
    option = input("<[e]ncrypt> or <[d]ecrypt> ")
os.system('cls')

if (option.lower() in enc):
    files = []
    file_str = ""
    numberOFiles = 0
    rand_key = 'default'
    keytype = ''
    print(Style.BRIGHT + Fore.CYAN + "* Key type?"+Style.RESET_ALL +"\n> Random 32Char Key (recommended)\n> Custom Key\n")
    ran = ["random", "r"]
    cus = ["custom", "c"]
    while keytype.lower() not in ran and keytype.lower() not in cus:
        keytype = input("<[r]andom> or <[c]ustom> ")
    os.system('cls')
    if keytype.lower() in cus:
        rand_key_confirm = "000"
        while rand_key != rand_key_confirm:
            print(Style.BRIGHT +Fore.CYAN)
            rand_key = getpass.getpass(prompt='Custom Encryption Key: ')
            rand_key_confirm = getpass.getpass(prompt='Custom Encryption Key (confirm): ')
            if rand_key != rand_key_confirm:
                os.system('cls')
                print(Fore.RED + "Keys do not match, please try again.")  
    else:
        print("Your key is ready to be generated, press <Enter> to show it.")
        input()
        os.system('cls')
        rand_key = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=32))
        print("Secret Encryption key : {}{}{}\nBE CAREFUL, this is the only time the encryption key is displayed. (excluding exportation)\n".format(Style.BRIGHT + Fore.MAGENTA, rand_key, Style.RESET_ALL))
        input("Press <Enter> to continue")
    os.system('cls')
    exportType = ''   
    print(Style.BRIGHT + Fore.CYAN + "* Do you want the key to be exported?\n"+ Style.RESET_ALL +"> YES, the key will be exported as a file in the current directory\n> NO, do not export the encryption key (recommended)\n")
    while exportType.lower() not in yes and exportType.lower() not in no:
        exportType = input("<[y]es> or <[n]o> ")
    os.system('cls')
        
    
    print(Style.BRIGHT + Fore.YELLOW + "Scanning in progress..." + Style.RESET_ALL)
    # Scanning files
    for file in glob.iglob('./**', recursive=True):
        if os.path.isfile(file) and "647-ED" not in file and (file[-4:]) != ".647" and file != "Desktop.ini":
            files.append(file)
            numberOFiles+=1
    for file_path in files:
        file_str += "{}\n".format(file_path)
    os.system('cls')
    if numberOFiles == 0:
        print("No files to encrypt detected.")
    else:
        print("Cryptable files detected : \n\n{}\nENCRYPTION KEY : {}\n\n{} file(s) will be encrypted, proceed?".format(file_str, "[hidden]", numberOFiles))
        option2 = ""
        
        while option2.lower() not in yes and option2.lower() not in no:
            option2 = input("<[y]es> or <[n]o> ")
        os.system('cls')   
        if option2.lower() in yes:
            
            if exportType in yes:
                key_file = open(rand_key + ".647key", "x") 
                key_file.close()
            for file in tqdm(files, desc="Status"):
                file_enc = file + ".647"
                print("\n\nENCRYPTING...\n")
                print("FILE              : {}".format(getfilename(file)))
                size = os.path.getsize(file)
                print("FILE SIZE         : {} BYTES".format(size))
                mod = modification_date(file)
                print("LAST MODIFICATION : {}".format(mod))
                print("DECRYPTION KEY    : {}".format("[hidden]"))
                try:
                    pyAesCrypt.encryptFile(file, file_enc, rand_key, bufferSize)
                    os.remove(file)
                except Exception as e:
                    print("Cannot encrypt file : {}".format(e))
                os.system('cls')
    
if (option.lower() in dec):
    files = []
    file_str = ""
    numberOFiles = 0
    
    print(Style.BRIGHT + Fore.YELLOW + "Scanning in progress..." + Style.RESET_ALL)
    # Scanning files
    for file in glob.iglob('./**', recursive=True):
        if os.path.isfile(file) and "647-ED" not in file and (file[-4:]) == ".647" and file.lower() != "desktop.ini":
            files.append(file)
            numberOFiles+=1
    for file_path in files:
        file_str += "{}\n".format(file_path)
    os.system('cls')
    
    if numberOFiles == 0:
        print("No Encrypted files detected.\nCheck the existence of files in the same directory of this program")
    else:
        rand_key = getpass.getpass(prompt='DECRYPTION KEY : ')
        os.system('cls') 
        print("Crypted files detected : \n\n{}\nDECRYPTION KEY : {}\n\n{} file(s) will be decrypted, proceed?".format(file_str, "[hidden]", numberOFiles))
        option2 = ""
        while option2.lower() not in yes and option2.lower() not in no:
            option2 = input("<[y]es> or <[n]o> ")
        os.system('cls')
        if option2.lower() in yes:
            error = 0
            for file in tqdm(files, desc="Status"):
                print("\n\nDECRYPTING...\n")
                print("FILE              : {}...".format(getfilename(file)))
                size = os.path.getsize(file)
                print("FILE SIZE         : {} BYTES".format(size))
                mod = modification_date(file)
                print("LAST MODIFICATION : {}".format(mod))
                print("ENCRYPTION KEY    : {}".format("[hidden]"))
                try:
                    pyAesCrypt.decryptFile(file, file[:-4], rand_key, bufferSize)
                    os.remove(file)
                except Exception as e:
                    print("Cannot decrypt file : {}".format(e))
                    os.remove(file[:-4])
                    error += 1
                os.system('cls')
            try:
                if error == 0:
                    print("Decryption has completed with no errors.")
                    os.remove(rand_key + ".647key")
                else:
                    print("{} files are still encrypted due to errors!\nThis may be caused by a duplicated file, or an invalid key".format(error))
            except Exception as e:
                pass
print(Fore.YELLOW + "\nTask done\nPress <Enter> to quit.\n")
input()
                

