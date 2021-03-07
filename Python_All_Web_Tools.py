import os
import questionary
from colorama import Fore, Back, Style, init
init(autoreset=True)
print(Fore.GREEN + """

M""MMM""MMM""M          dP       M""""""""M                   dP       
M  MMM  MMM  M          88       Mmmm  mmmM                   88       
M  MMP  MMP  M .d8888b. 88d888b. MMMM  MMMM .d8888b. 88d888b. 88  .dP  
M  MM'  MM' .M 88ooood8 88'  `88 MMMM  MMMM 88'  `88 88'  `88 88888"   
M  `' . '' .MM 88.  ... 88.  .88 MMMM  MMMM 88.  .88 88    88 88  `8b. 
M    .d  .dMMM `88888P' 88Y8888' MMMM  MMMM `88888P8 dP    dP dP   `YP 
MMMMMMMMMMMMMM                   MMMMMMMMMM                       

""")
print(Style.RESET_ALL)
soru ="""        #####################
          #      WebTank      #
          #####################
          
          """
target = str(input("Hedef Adres :"))
answers = ["Nmap","SQLMap","WpScan","Uniscan" , "WafW00f"]
cikti = questionary.select(soru,choices=answers).ask()
if cikti == 'Nmap':
    print(Fore.BLUE + """
    ###############
    #   WebTank   #
    ###############
        
    """)
    print(Style.RESET_ALL)
    os.system("nmap -T4 -A -Pn -sV --script firewall-bypass" + target + "")
elif cikti == 'SQLMap':
    print(Fore.BLUE + """
       ###############
       #   WebTank   #
       ############### """)
    print(Style.RESET_ALL)
    os.system("sqlmap -u " + target + "--random-agent --hex --tamper=space2comment --dump-all --batch")
elif cikti == 'WpScan':
    print(Fore.BLUE + """
    ###############
    #   WebTank   #
    ###############

    """)
    print(Style.RESET_ALL)
    api_key = str(input("Wpscan Api Key :"))
    os.system("wpscan --url" + target +"--enumerate at , ap , u --api-token" + api_key +"")
elif cikti == 'Uniscan':
    print(Fore.BLUE + """
    ###############
    #   WebTank   #
    ###############

    """)
    print(Style.RESET_ALL)
    os.system("sudo uniscan -u" + target + "--qweds")
elif cikti == 'WafW00f':
    print(Fore.BLUE + """
    ###############
    #   WebTank   #
    ###############

    """)
    print(Style.RESET_ALL)
    os.system("sudo wafw00f " + target + "")
    
