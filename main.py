from ipaddress import ip_interface
import argphase 

def main():


   parser = argparse.ArgumentParser()
   parser.add_argument("-a", "--address", help="host address", required=True)
   parser.add_argument("-n", "--netmask", help="Network mask", required=True)
   args = parser.parse_args()
   iface = ip_interface(f"{args.address}/{args.netmask}")
   network = iface.network.network_address
   broadcast = iface.network.broadcast_address
   hostmask = iface.hostmask
   netmask = iface.netmask
   hosts = list(iface.network.hosts())
   minimum_host = min(hosts, default=None)
   maximum_host = max(hosts, default=None)
   print(
   f"""
Network: {network}/{netmask}
Broadcast: {broadcast}
Minimum Host: {minimum_host}
Maximum Host: {maximum_host}

   Hosts per Network: {len(hosts)}
"""
)
if __name__ == "__main__":
main(

from scapy import all as s
from PyInquirer import prompt
from netifaces import interfaces
def main():
questions = [
dict(
type="checkbox",
name="interfaces",
message="Which of the following interfaces do you want to sniff?",
choices=[{"name": k} for k in interfaces()],
),
dict(type="input", name="timeout", message="How long do you want to sniff?"),
dict(
type="confirm", name="save", message="Do you want to save these to files?"
),
]
answers = prompt(questions)
results = s.sniff(iface=answers["interfaces"], timeout=int(answers["timeout"]))
if answers["save"]:
s.wrpcap("capture.pcap", results)
if __name__ == "__main__":
main()


from telnetlib import Telnet
from getpass import getpass
def main():
host = input('Please enter the host: ')#'3.236.125.153'
user = input('Please enter the username: ') #'justin'
password = getpass() #'P@$$w0rd!'
client = Telnet(host)
client.read_until(b'login: ')
client.write(user.encode() + b'\n')
if password:
client.read_until(b'Password: ')
client.write(password.encode() + b'\n')
client.write(b'ls -lah / \n')
client.write(b'uname -a \n')
client.write(b'exit \n')
print(client.read_all().decode())
if __name__ == '__main__':
main()


   