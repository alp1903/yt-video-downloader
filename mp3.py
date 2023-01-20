from pytube import YouTube
import os

yt = YouTube(
	str(input("İndirmek istediğiniz videonun URL'sini girin:    ")))

video = yt.streams.filter(only_audio=True).first()

out_file = video.download()

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

print(yt.title + "Başarılı!!")

secenek = int(input("Devam Etmek İster Misiniz? (Evet = 1 Hayır = 0)    "))

while secenek == 1:
	yt = YouTube(
		str(input("İndirmek istediğiniz videonun URL'sini girin:    ")))

	video = yt.streams.filter(only_audio=True).first()

	out_file = video.download()

	base, ext = os.path.splitext(out_file)
	new_file = base + '.mp3'
	os.rename(out_file, new_file)

	print(yt.title + "Başarılı!!")

	secenek = int(input("Devam Etmek İster Misiniz? (Evet = 1 Hayır = 0)    "))