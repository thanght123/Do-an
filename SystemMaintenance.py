# 6.1
# 6.2
import subprocess
import re
from termcolor import colored
from tqdm import tqdm
from time import sleep
class SystemFilePermissions:
    def __init__(self):
        # print([ m for m in dir(self) if not m.startswith('__')])
        # print(len(self))
        # print(dir(self))
        for i in tqdm(range(0, 100), desc ="System file permissions processing"):
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
    # def __init__(self):
    #     pass
    def PermissionEtcPasswd(self):
        print("[*] Ensure permissions on /etc/passwd are configured checking....")

        cmd = 'stat /etc/passwd'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
        # print("here")
        (output, err) = p.communicate()
        # print(output.decode('ascii'))
        # print(err)
        rules_pattern = r'Access: \(0644\/\-rw\-r\-\-r\-\-\)  Uid: \(    0\/    root\)   Gid: \(    0\/    root\)'
        search_pattern = re.findall(rules_pattern, output.decode("ascii"))
        # print(search_pattern)
        if len(search_pattern) > 0:
            print(colored("   [*] Ensure permissions on /etc/passwd are configured",'green'))
        else:
            print(colored("   [*] Ensure permissions on /etc/passwd are not configured",'yellow'))
            print(colored('''   [*] Recommendation:  chown root:root /etc/passwd && chmod 644 /etc/passwd''','green'))

    def PermissionEtcShadow(self):
        print("[*] Ensure permissions on /etc/shadow are configured checking....")

        cmd = 'stat /etc/shadow'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
        # print("here")
        (output, err) = p.communicate()
        # print(output.decode('ascii'))
        # print(err)
        rules_pattern = r'Access: \(0640\/\-rw\-r\-\-\-\-\-\)  Uid: \(    0\/    root\)   Gid: \(   42\/  shadow\)'
        search_pattern = re.findall(rules_pattern, output.decode("ascii"))
        # print(search_pattern)
        if len(search_pattern) > 0:
            print(colored("   [*] Ensure permissions on /etc/shadow are configured",'green'))
        else:
            print(colored("   [*] Ensure permissions on /etc/shadow are not configured",'yellow'))
            print(colored('''   [*] Recommendation: chown root:shadow /etc/shadow && chmod o-rwx,g-wx /etc/shadow''','green'))

    def PermissionEtcGroup(self):
        print("[*] Ensure permissions on /etc/group are configured checking....")

        cmd = 'stat /etc/group'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
        # print("here")
        (output, err) = p.communicate()
        # print(output.decode('ascii'))
        # print(err)
        rules_pattern = r'Access: \(0644\/\-rw\-r\-\-r\-\-\)  Uid: \(    0\/    root\)   Gid: \(    0\/    root\)'
        search_pattern = re.findall(rules_pattern, output.decode("ascii"))
        # print(search_pattern)
        if len(search_pattern) > 0:
            print(colored("   [*] Ensure permissions on /etc/group are configured",'green'))
        else:
            print(colored("   [*] Ensure permissions on /etc/group are not configured",'yellow'))
            print(colored('''   [*] Recommendation: chown root:root /etc/group && chmod 644 /etc/group''','green'))


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

class UserandGroupSettings:
    def __init__(self):
        pass