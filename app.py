from pytube import YouTube

url = input("Digite o link: ")
_filename = input("Nome do arquivo: ")
formato = "'%s'.mp4" % _filename

print("baixando...")
YouTube(url).streams.first().download(filename=formato)
print("Download concluído!")


