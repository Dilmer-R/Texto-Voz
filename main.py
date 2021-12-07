from gtts import gTTS
texto = input("Ingrese el texto a convertir: ")
txt = gTTS(texto, lang="es-us")
txt.save("texto.mp3")