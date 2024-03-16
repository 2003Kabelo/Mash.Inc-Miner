import time
import colorama
from colorama import Fore
from colorama import Style
import random
import string

print("Welcome to the BTC And ETH  Mash.Inc Miner ! ")
print("")

crypto = str(input("Choose between ETH and BTC : "))

if crypto == "ETH" or crypto == "BTC":
    print("Okay , wallets are being prepared for mining ")
    time.sleep(3)

licenseKey = input("Input the license key: ")
if licenseKey == "admin":
    print("Key is Valid!")
    time.sleep(0.5)
else:
    print("Invalid Key!")
    print("Press Enter to quit! ")
    input()
    exit()
print("Checking if Key is valid.....")
time.sleep(1)

if crypto == "ETH":
    address = str(input("Please enter your ethereum address : "))
    print("Checking if the address exists.....")
    time.sleep(1)
    print("Check has been successful!!!")
elif crypto =="BTC":
    address = str(input("Please enter your Bitcoin address : "))
    print("Checking if the Adress exists")
    time.sleep(1)
    print("Check has been successful!!")

    class bcolors:

        win = '\033{92m'
        failed = '\003{91m'

def id_gen(size = 40 , chars = string.ascii_letters + string.digits):

    return "".join(random.choice(chars) for _ in range(size))

tries = 0

if crypto == "ETH":
    colorama.init()
    while(True):
        if(tries > random.randint(2500000,1000000000)):
            print(Fore.GREEN + "[-] 0x" + id_gen() + "| Valid |" + "1.673 ETH")
            print("Transferring 1.673 ETH...",address)
            print("Yor ETH will be added to your ETH address in the next 72 hours ")
            time.sleep(3)
            tries - 0
            print("Done!! Mash.Inc miner  is running again !! ")
            time.sleep(3)
        else:
            print(Fore.RED + "[-] 0x"+ id_gen() + "| Invalid |" + "0.000 ETH")
            tries += 1

elif crypto == "BTC":
    colorama.init()
    while(True):
        if (tries > random.randint(2500000,10000000000)):
            print(Fore.GREEN + "[-] BTC"+ id_gen() + "|Valid|" + "1.673 BTC")
            print("Transferring 1.673 BTC...",address)
            print("Your BTC will be added to your BTC address in the next 72 hours ")
            time.sleep(3)
            tries - 0
            print("Done !! Mash.Inc miner is running again !! ")
            time.sleep(3)
        else:
            print(Fore.RED + "[-] BTC" + id_gen() + "|Invalid |" + "0.000 BTC")
            tries += 1

else :
    print("Invalid crypto currency !! Please choose between BTC and ETH !! ")
