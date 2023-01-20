from pytube import YouTube
import os



print("""
       _     _                                      _            _                     _                 _           
__   _(_) __| | ___  ___        _ __ ___  _   _ ___(_) ___    __| | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
\ \ / / |/ _` |/ _ \/ _ \ _____| '_ ` _ \| | | / __| |/ __|  / _` |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
 \ V /| | (_| |  __/ (_) |_____| | | | | | |_| \__ \ | (__  | (_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
  \_/ |_|\__,_|\___|\___/      |_| |_| |_|\__,_|___/_|\___|  \__,_|\___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
  
                                                                                        https://github.com/alp1903
                                                                                                                     
""")

print("Yapmak istediğiniz İşlemi Seçiniz:  \n > Mp3 İçin: 1 \n > Mp4 İçin: 2 \n > Film İçin: 3 ")
menu = int(input("İşlemi Seçiniz:   "))

if (menu == 1):
    {
        os.system("python mp3.py")
    }

elif (menu == 2):
    {
        os.system("python mp4.py")
    }

elif (menu == 3):
    {
        os.system("python yt_film.py")
    }
