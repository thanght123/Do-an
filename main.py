## File systemconfig
# pip install termcolor
# 1.1.1
# 1.5
# 3.1
# 3.3
# 3.4
# 3.5
# 5.1
# 5.2
# 5.4
# 6.1
# 6.2
import subprocess
 
# p = subprocess.Popen("pwd", stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
 
# (output, err) = p.communicate()

# ## Wait for date to terminate. Get return returncode ##
# # p_status = p.wait()
# print("Command output : ", output.decode('ascii'))
# print("Command exit status/return code : ", p_status)

# class NetworkConfiguration:
#     class NetworkParameters:
#         def NetworkParameters():
#             cmd = 'sysctl net.ipv4.ip_forward'
#             p = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
            
#             (output, err) = p.communicate()
#             print(output.decode('ascii'))
#             return True
from AccessConfiguration import *
# from InitialSetup import *
from NetworkConfiguration import *
from SystemMaintenance import *
# a = FileSystemConfiguration.NetworkParameters()


def banner():
    '''
    '''

def parse_args():
    import argparse
    parser = argparse.ArgumentParser(prog="python3 main.py")
    parser.add_argument('--network',required=False,type=bool,default=False)
    parser.add_argument('--system',required=False,type=bool,default=False)
    parser.add_argument('--access',required=False,type=bool,default=False)
    parser.add_argument('--install',required=False,type=bool,default=True)


    # parser.add_argument('-u','--url',required=True,type=str,default=None)
    # parser.add_argument('--proxy',required=False,type=str,default=None, help="Proxy URL, support HTTP proxies (Example: http://127.0.0.1:8080)")
    # parser.add_argument('--ping',required=False,type=str,default=None,dest="IP",help="Ping to ip address")
    # parser.add_argument('--shell',required=False,type=str,default=None,help="Your aspx shell address (Example: http://127.0.0.1/shell.aspx)")
    return parser.parse_args()

def main():
    
    # from tqdm import tqdm
    # from time import sleep
    # for i in tqdm(range(0, 100), desc ="Text You Want"):
    #     pass
    #     # sleep(.1)
    args = parse_args()
    network = args.network
    access = args.access
    system = args.system
    # if install == True:
    #     pass
    # print(network)
    if network == True:
        TCPWrapper()
        NetworkParameters()
    #     # print("here")
    #     NetworkParameters.IPForwarding()
    #     NetworkParameters.PacketRedirectSending()
    #     TCPWrapper.WrapperInstall()
    #     TCPWrapper.HostDeny()
    #     TCPWrapper.PermissionHostAllow()
    #     TCPWrapper.PermissionHostDeny()
    if access == True:
        ConfigureCron()
    #     ConfigureCron.CronDaemon()
    #     ConfigureCron.PermissionCrontab()
        
    if system == True:
        SystemFilePermissions()
        # pass
        # print("Here")
        # for i in tqdm(range(0, 100), desc ="Text You Want"):
        #     sleep(.1)
        #     SystemFilePermissions.PermissionEtcPasswd()
        #     SystemFilePermissions.PermissionEtcShadow()
    # print(network)
    # ip = args.IP
# print(a)
main()