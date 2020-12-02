import os
print(""" 

Merhabalar. Python İle Toplu Web Araçlarına Hoşgeldin.
Bu Program Web Araçlarını Kullanarak Toplu Bir Şekilde Taramana Yardımcı Olur.
Coded By arda6
Programı Kullanarak Tüm Sorumluluğu Üzerine Almış Olursun!!!

""")
print("Gerekli Yüklemeler Yapılacak. Şimdilik Linux İçin İdeal Durumda. Eğer Y (Yes) Tuşuna Basarsan Yüklemeler Yapılacak")
installer = int(input(|Y|es / |N|o:)) 
if installer = 'Y';
    os.system('sudo apt-get install figlet')
    os.system('clear')
    os.system('apt-get install nikto')
    os.system('Kali Linux İçin İndirmeler Bu Kadar.')
else installer = 'N';
    print('Çıkarılıyorunuz....')
print("""

Seçenekler ;
    
    1) Wordpress Scan
    2) Normal Web Scan 
    3) Port Scan 
    4) Sql Injection Scan
    5) Xss Injection Scan 
    6) Csrf Injection Scan
    7) Code Injection Scan
    
""")

hedef = str(input('Target Site :'))
secim = print("Which Scan Types :")
if secim = '1';
wordpress = print("""
    
    Wordpress Scan ;

    1) Normal Scan and Users Finder:
    2) Themes Finder:
    
""")
if wordpress = '1';
    os.system("wpscan --url" " " + hedef + )
else wordpress = '2';
    os.system("wpscan --url" " " + hedef + " " " enumerate u ")

else secim = '2';
    print("""

    1) Uniscan Scan
    2) Nikto Scan

""")
if normal = '1';
    os.system("uniscan -u" + hedef + "-qweds")
else normal = '2';
    os.system("nikto -h " + hedef + )

else secim = '3';
    port = print ("""
    
    1) Nmap Version Scan
    2) Nmap OS Scani
    
    
    """)
if port = '1';
    os.system("nmap -sV " + hedef + " ")
if port = '2';
    os.system("sudo nmap -sV -O " + hedef + )
else secim = '4';
    sql = print("""
    
    1) Sqlmap Sql Test
    2) Sqlmap Sql Attack
    
    """) 
if sql = '1';
    os.system("sqlmap -u " " " + hedef + " " "--batch")
else sql = '2';
    os.system("sqlmap -u " " " + hedef + " " "--batch")
else secim = '5';
    os.system("nikto -h " + hedef +  )
else secim = '6';
    os.system("uniscan -u" + hedef +)
else secim = '7';
    os.system("uniscan -u " + hedef +)
    
