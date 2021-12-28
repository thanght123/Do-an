import subprocess
import re
from termcolor import colored
from tqdm import tqdm
from time import sleep
class ConfigureCron:
    def __init__(self):
        # print([ m for m in dir(self) if not m.startswith('__')])
        # print(len(self))
        # print(dir(self))
        for i in tqdm(range(0, 100), desc ="Configure Cron processing"):
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
    def CronDaemon(self):
        print("[*] Cron daemon checking....")

        cmd = 'systemctl is-enabled cron'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
        # print("here")
        (output, err) = p.communicate()
        # print(output.decode('ascii'))
        # print(err.decode('ascii'))
        # rules_pattern = r''
        # search_pattern = re.findall(rules_pattern, output.decode("ascii"))
        # print(search_pattern)
        if str(output.decode("ascii")) == 'enabled\n':
            print(colored("   [*] Ensure cron daemon is enabled",'green'))
        else:
            print(colored("   [*] Cron daemon is not enabled",'yellow'))
            print(colored('''   [*] Recommendation:  systemctl enable cron''','green'))
    def PermissionCrontab(self):
        print("[*] Cron daemon checking....")

        cmd = 'stat /etc/crontab'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
        # print("here")
        (output, err) = p.communicate()
        # print(output.decode('ascii'))
        # print(err.decode('ascii'))
        rules_pattern = r'Access: \(0644\/\-rw\-r\-\-r\-\-\)  Uid: \(    0\/    root\)   Gid: \(    0\/    root\)'
        search_pattern = re.findall(rules_pattern, output.decode("ascii"))
        # print(search_pattern)
        if len(search_pattern) > 0:
            print(colored("   [*] Ensure permissions on /etc/crontab are configured",'green'))
        else:
            print(colored("   [*] Ensure permissions on /etc/crontab are not configured",'yellow'))
            print(colored('''   [*] Recommendation: chown root:root /etc/crontab && chmod og-rwx /etc/crontab''','green'))
class SSHServerConfiguration:
    def __init__(self):
        pass

class UserAccountsandEnvironment:
    def __init__(self):
        pass