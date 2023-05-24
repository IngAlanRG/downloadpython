from pytube import YouTube

def descargar_video(url):
    try:
        # Crea una instancia de la clase YouTube con la URL del video
        video = YouTube(url)
        
        # Filtra los formatos disponibles y selecciona el formato MP4 con mayor resolución
        formato = video.streams.filter(file_extension='mp4').get_highest_resolution()
        title = video.title
        name = video.author
        # Descarga el video en el formato seleccionado
        formato.download()
        
        print("¡Descarga completada!")
        print(name ,title)
    except Exception as e:
        print("Error al descargar el video:", str(e))

# Aquí coloca la url del video de YouTube
url = "https://www.youtube.com/watch?v=GH4oTnyAFBk"
descargar_video(url)

#debes instalar python 
#debes de instalar > pip install pytube
#Para ejecútalo python Download.py
#con tabulador autocompleted el nombre 
#tabulador es la tecla de las dos flechas en inversa a la otra
