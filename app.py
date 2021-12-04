from pytube import YouTube

url = input("Digite o link: ")
_filename = input("Nome do arquivo: ")
mp3 = "'%s'.mp3" % _filename

print("baixando...")
YouTube(url).streams.first().download(filename=mp3)
print("Download concluído!")


