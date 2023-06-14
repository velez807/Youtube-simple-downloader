from tkinter import Tk, Label, Entry, Button, StringVar, Radiobutton
from pytube import YouTube
import tkinter.messagebox as mbox
from pytube.exceptions import AgeRestrictedError, VideoUnavailable, RegexMatchError, PytubeError

def descargar_audio(url):
    try:
        youtube_video = YouTube(url)
        audio = youtube_video.streams.get_audio_only()
        audio.download(output_path="audio")
        mbox.showinfo("Descarga completada", "La descarga de audio se ha completado.")
    except AgeRestrictedError:
        mbox.showwarning("Restricción de edad", "Este video tiene restricción de edad. Por favor, inicie sesión en YouTube para verificar su edad y vuelva a intentarlo.")
    except VideoUnavailable:
        mbox.showwarning("Video no disponible", "El video solicitado no está disponible en YouTube.")
    except RegexMatchError:
        mbox.showerror("Error", "La URL del video de YouTube no es válida.")
    except PytubeError:
        mbox.showerror("Error", "Ocurrió un error al descargar el audio. Por favor, verifique el enlace y su conexión a internet.")
    except Exception as e:
        mbox.showerror("Error", str(e))

def descargar_audio_y_video(url):
    try:
        youtube_video = YouTube(url)
        video = youtube_video.streams.get_highest_resolution()
        video.download(output_path="videos")
        mbox.showinfo("Descarga completada", "La descarga del video se ha completado.")
    except AgeRestrictedError:
        mbox.showwarning("Restricción de edad", "Este video tiene restricción de edad. Por favor, inicie sesión en YouTube para verificar su edad y vuelva a intentarlo.")
    except VideoUnavailable:
        mbox.showwarning("Video no disponible", "El video solicitado no está disponible en YouTube.")
    except RegexMatchError:
        mbox.showerror("Error", "La URL del video de YouTube no es válida.")
    except PytubeError:
        mbox.showerror("Error", "Ocurrió un error al descargar el audio. Por favor, verifique el enlace y su conexión a internet.")
    except Exception as e:
        mbox.showerror("Error", str(e))

def descargar():
    enlace = enlace_entry.get()
    if opcion_var.get() == "1":
        descargar_audio(enlace)
    elif opcion_var.get() == "2":
        descargar_audio_y_video(enlace)

# Configuración de la ventana principal
ventana = Tk()
ventana.title("Descargador de YouTube")
ventana.geometry("400x200")
ventana.resizable(False, False)
# ventana.config(bg="#292929")
# ventana.option_add("*foreground", "white")
# ventana.option_add("*background", "#292929")

# Etiqueta y campo de entrada de la URL
url_label = Label(ventana, text="URL del video de YouTube:")
url_label.pack()
enlace_entry = Entry(ventana, width=40)
enlace_entry.pack()

# Variable de control para la opción seleccionada
opcion_var = StringVar()

# Radio buttons para seleccionar la opción
# que la opcion de audio esté seleccionada de forma predeterminada
opcion_var.set("1")
opcion_audio = Radiobutton(ventana, text="Descargar solo audio", variable=opcion_var, value="1")
opcion_audio.pack()

opcion_audio_y_video = Radiobutton(ventana, text="Descargar audio y video", variable=opcion_var, value="2")
opcion_audio_y_video.pack()


# Botón de descarga
descargar_btn = Button(ventana, text="Descargar", command=descargar)
descargar_btn.pack()

# Ejecutar ventana principal
ventana.mainloop()
