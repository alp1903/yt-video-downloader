from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download('/srv/dev-disk-by-uuid-D260B0F160B0DD83/nassy/Movies')
    except:
        print("bir hata oluştu.")
    print("İndirme başarıyla tamamlandı!!")


link = input("YouTube film URL'sini girin: ")
Download(link)

secenek = int(input("Devam Etmek İster Misiniz?"))

while secenek == 1:
    def Download(link):
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
            youtubeObject.download('/srv/dev-disk-by-uuid-D260B0F160B0DD83/nassy/Movies')
        except:
            print("bir hata oluştu.")
        print("İndirme başarıyla tamamlandı!!")


    link = input("YouTube film URL'sini girin: ")
    Download(link)

    secenek = int(input("Devam Etmek İster Misiniz?"))
