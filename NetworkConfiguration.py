# 3.1
# 3.3
# 3.4
# 3.5
import subprocess
import re
from termcolor import colored
from tqdm import tqdm
from time import sleep

class NetworkParameters:
    def __init__(self):
        # print([ m for m in dir(self) if not m.startswith('__')])
        # print(len(self))
        # print(dir(self))
        for i in tqdm(range(0, 100), desc ="Network Parameters processing"):
            sleep(.03)
            

        for method in [ m for m in dir(self) if not m.startswith('__')]:
            # print(method)
            eval("self."+method+"()")
            sleep(1)

            # print(method)
        # self.PermissionHostDeny()
        # sleep(.5)
        # TCPWrapper.PermissionHostAllow()
    #     pass
    def __len__(self):
        return len([ m for m in dir(self) if not m.startswith('__')])
    def IPForwarding(self):
        print("[*] IP Forwarding checking....")
        cmd = 'grep "net\.ipv4\.ip_forward" /etc/sysctl.conf /etc/sysctl.d/* && grep "net\.ipv6\.conf\.all\.forwarding" /etc/sysctl.conf /etc/sysctl.d/*'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
        # print("here")
        (output, err) = p.communicate()
        # print(output.decode('utf-8'))
        rules_pattern = r"(net\.ipv4\.ip_forward=[0,1])|(net\.ipv6\.conf\.all\.forwarding=[0,1])"
        search_pattern = re.findall(rules_pattern, output.decode("ascii"))
        # tmp = list(set(search_pattern))
        # print(list(set(search_pattern)))
        current = [re.sub(r"['\(\),\[\] ]",'',str(x)) for x in list(set(search_pattern))]
        # configs = [sorted(x.split('=')) for x in current]
        # print(current)
        # configs[0]['net.ipv4.ip_forward']
        for config in current:
            result = config.split('=')
            # print(config[1])
            if result[1] == '1':
                print(colored("   [*] IP forwarding is enabled: "+config, 'yellow'))
                print(colored('''   [*] Recommendation: '''+result[0]+"=0",'green'))
            else:
                print(colored("Ensure IP forwarding is disabled", 'green'))
            
            
            # print(config)
        # tmp_1 = 
        # print(current)
        # print(type(str(tmp[0])))
        
        # print(str(list(set(search_pattern))[0]))
        
        # x = str(list(set(search_pattern))[1])
        # tmp = re.sub(r"'\(\)","",x)
        # print(tmp[0])
        # print(x.split("="))
        # print(list(set(search_pattern)))
        # a = [x if (str(x) != "'')" ) else None for x in search_pattern]

        # search_pattern = list(set(search_pattern))
        # print(search_pattern)
        # print(list(set(search_pattern)))
        # a = [x if (str(x) != "'')" ) else None for x in search_pattern]
        # print(a)
        # x = list(set(search_pattern))
        # x = x.replace(r"(|)","")
        # print(x)
        # print(list(x)[0])
        # print(output.decode('ascii'))
        return True
    def PacketRedirectSending(self):
        print("[*] Packet redirect sending checking....")

        cmd = 'grep "net\.ipv4\.conf\.all\.send_redirects" /etc/sysctl.conf /etc/sysctl.d/* && grep "net\.ipv4\.conf\.default\.send_redirects" /etc/sysctl.conf /etc/sysctl.d/*'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
        # print("here")
        (output, err) = p.communicate()
        # print(output)
        # print(output.decode('utf-8'))
        rules_pattern = r"(net\.ipv4\.conf\.all\.send_redirects = [0,1])|(net\.ipv4\.conf\.default\.send_redirects = [0,1])"
        search_pattern = re.findall(rules_pattern, output.decode("ascii"))

        # # tmp = list(set(search_pattern))
        # print(list(set(search_pattern)))
        current = [re.sub(r"['\(\),\[\]] ",'',str(x)) for x in list(set(search_pattern))]
        # # configs = [sorted(x.split('=')) for x in current]
        # # print(current)
        # # configs[0]['net.ipv4.ip_forward']
        for config in current:
            # print(config)
            result = config.split(' = ')
            # print(result[1])
            if result[1] == '1':
                print(colored("     [*] Packet redirect sending is enabled: "+config, 'yellow'))
                print(colored('''   [*] Recommendation: '''+result[0]+"=0",'green'))
            else:
                print(colored("   [*] Ensure packet redirect sending is disabled", 'green'))
        # pass


class TCPWrapper:
    def __init__(self):
        # print([ m for m in dir(self) if not m.startswith('__')])
        # print(len(self))
        # print(dir(self))
        for i in tqdm(range(0, 100), desc ="TCP Wrapper processing"):
            sleep(.03)
            

        for method in [ m for m in dir(self) if not m.startswith('__')]:
            # print(method)
            eval("self."+method+"()")
            sleep(1)

            # print(method)
        # self.PermissionHostDeny()
        # sleep(.5)
        # TCPWrapper.PermissionHostAllow()
    #     pass
    def __len__(self):
        return len([ m for m in dir(self) if not m.startswith('__')])
    def WrapperInstall(self):
        print("[*] TCP Wrappers is installed checking....")

        cmd = 'dpkg -s tcpd'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
        # print("here")
        (output, err) = p.communicate()
        # print(output)
        # print(err)
        rules_pattern = r"package 'tcpd' is not installed"
        search_pattern = re.findall(rules_pattern, err.decode("ascii"))
        if len(search_pattern) > 0:
            print(colored("   [*] TCP Wrappers is not installed",'yellow'))
            print(colored('''   [*] Recommendation: apt-get install tcpd''','green'))
        else:
            print(colored("   [*] TCP Wrappers is installed",'green'))
    def HostDeny(self):
        print("[*] Host deny configured checking....")

        cmd = 'cat /etc/hosts.deny'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
        # print("here")
        (output, err) = p.communicate()
        # print(output.decode('ascii'))
        # print(err)
        rules_pattern = r"ALL:ALL"
        search_pattern = re.findall(rules_pattern, output.decode("ascii"))
        # print(search_pattern)
        if len(search_pattern) == 0:
            print(colored("   [*] Ensure /etc/hosts.deny is not configured",'yellow'))
            print(colored('''   [*] Recommendation: echo "ALL: ALL" >> /etc/hosts.deny''','green'))
        else:
            print(colored("   [*] Ensure /etc/hosts.deny is configured",'green'))

    def PermissionHostAllow(self):
        print("[*] Host allow configured checking....")

        cmd = 'stat /etc/hosts.deny'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
        # print("here")
        (output, err) = p.communicate()
        # print(output.decode('ascii'))
        # print(err)
        rules_pattern = r'Access: \(0644\/\-rw\-r\-\-r\-\-\)  Uid: \(    0\/    root\)   Gid: \(    0\/    root\)'
        search_pattern = re.findall(rules_pattern, output.decode("ascii"))
        # print(search_pattern)
        if len(search_pattern) > 0:
            print(colored("   [*] Ensure permissions on /etc/hosts.allow are configured ",'yellow'))
        else:
            print(colored("   [*] Ensure /etc/hosts.deny is configured",'green'))
            print(colored('''   [*] Recommendation: chown root:root /etc/hosts.allow && chmod 644 /etc/hosts.allow''','green'))
    def PermissionHostDeny(self):
        print("[*] Host deny configured checking....")

        cmd = 'stat /etc/hosts.allow'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
        # print("here")
        (output, err) = p.communicate()
        # print(output.decode('ascii'))
        # print(err)
        rules_pattern = r'Access: \(0644\/\-rw\-r\-\-r\-\-\)  Uid: \(    0\/    root\)   Gid: \(    0\/    root\)'
        search_pattern = re.findall(rules_pattern, output.decode("ascii"))
        # print(search_pattern)
        if len(search_pattern) > 0:
            print(colored("   [*] Ensure permissions on /etc/hosts.deny are configured ",'green'))
        else:
            print(colored("   [*] Ensure /etc/hosts.deny are not configured",'yellow'))
            print(colored('''   [*] Recommendation: chown root:root /etc/hosts.deny && chmod 644 /etc/hosts.deny''','green'))

    # def run():
        
class UncommonNetworkProtocols:
    def __init__(self):
        pass
    # def DCCP():

class FirewallConfiguration:
    def __init__(self):
        pass