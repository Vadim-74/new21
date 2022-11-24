import subprocess
import argparse


def arg()
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interfacePars", help="Interface 2 change mac address")
    parser.add_argument("-m", "--mac", dest="newMacPars", help="New MAC address")
    parser.add_argument("-j", "--jj", dest="jjjj", help="New MAC address")

    options = parser.parse_args()
    if not options.interfacePars:
        parser.error("[-] pls specify an interface, use --help or -h for more info")
    elif not options.newMacPars:
        parser.error("[-] pls specify new MAC address, use --help or -h for more info")
    else:
        return options

options = arg()
newmac = options.newMacPars
interface = options.interfacePars

print("[+] Changing MAC address for " + interface + " to" + newmac)
print("-> shooting down " + interface)
subprocess.call("sudo ifconfig " + interface + " down", shell=True)
print("-> changing mac to " + newmac)
subprocess.call("sudo ifconfig " + interface + " hw ether " + newmac, shell=True)
print("-> powering up " + interface)
subprocess.call("sudo ifconfig " + interface + " up", shell=True)
print("result: ")
subprocess.call("sudo ifconfig " + interface, shell=True)
