import tkinter as tk
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os
import pygame

pygame.mixer.init()

root = tk.Tk()
root.title("Language Translator")
root.config(background="#2C3E50")
root.geometry("1500x1200")

translator = Translator()

def lang_translater():
    from_lannguage = from_lang.get()
    to_language = to_lang.get()
    text = entry1.get("1.0", "end-1c")
    translated_text = translator.translate(text, src=from_lannguage, dest=to_language).text
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, translated_text)
    result_text.config(state=tk.DISABLED)

def play_audio(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove(file_path)

def volume():
    try:
        speak_text1 = entry1.get("1.0", "end-1c")
        tts = gTTS(text=speak_text1, lang=from_lang.get())
        tts.save("speak.mp3")
        play_audio("speak.mp3")
    except:
        error_label = tk.Label(root, text="Language can't be pronounced.", fg="white", bg="#E74C3C", font=("Arial", 12, "italic"))
        error_label.place(x=600, y=750)
        root.after(4000, error_label.destroy)

def volume2():
    try:
        speak_text2 = result_text.get("1.0", "end-1c")
        tts = gTTS(text=speak_text2, lang=to_lang.get())
        tts.save("speak1.mp3")
        play_audio("speak1.mp3")
    except:
        error_label = tk.Label(root, text="Language can't be pronounced.", fg="white", bg="#E74C3C", font=("Arial", 12, "italic"))
        error_label.place(x=700, y=750)
        root.after(4000, error_label.destroy)

def swap_lang():
    L1 = from_lang.get()
    L2 = to_lang.get()
    from_lang.set(L2)
    to_lang.set(L1)

label1 = tk.Label(root, text="Language Translator", fg="#ECF0F1", bg="#2C3E50", font=("Arial", 50, "bold"))
label1.pack(pady=1)

label2 = tk.Label(root, text="From Language:", fg="#ECF0F1", bg="#2C3E50", font=("Arial", 20, "bold"))
label2.place(x=150, y=200)

label3 = tk.Label(root, text="To Language:", fg="#ECF0F1", bg="#2C3E50", font=("Arial", 20, "bold"))
label3.place(x=1000, y=200)

entry1 = tk.Text(root, width=50, height=10, font=("Arial", 14))
entry1.place(x=150, y=350)

result_text = tk.Text(root, width=50, height=10, font=("Arial", 14), bg="#ECF0F1")
result_text.place(x=900, y=350)
result_text.config(state=tk.DISABLED)

from_lang = tk.StringVar()
from_lang.set("en")
from_lang_menu = tk.OptionMenu(root, from_lang, *LANGUAGES)
from_lang_menu.config(font=("Arial", 12))
from_lang_menu.place(x=400, y=200, width=200, height=40)

to_lang = tk.StringVar()
to_lang.set("hi")
to_lang_menu = tk.OptionMenu(root, to_lang, *LANGUAGES)
to_lang_menu.config(font=("Arial", 12))
to_lang_menu.place(x=1200, y=200, width=200, height=40)

button1 = tk.Button(root, text="Translate", command=lang_translater, fg="white", bg="#2980B9", font=("Arial", 16, "bold"))
button1.place(x=750, y=450, width=120, height=50)

volume_button = tk.Button(root, text="🔊", command=volume, fg="white", bg="#1ABC9C", font=("Arial", 20))
volume_button.place(x=655, y=575, width=50, height=50)

volume_button2 = tk.Button(root, text="🔊", command=volume2, fg="white", bg="#1ABC9C", font=("Arial", 20))
volume_button2.place(x=1407, y=575, width=50, height=50)

volume_button = tk.Button(root, text="🔁", command=swap_lang, fg="white", bg="#1ABC9C", font=("Arial", 20))
volume_button.place(x=780, y=180, width=70, height=60)

label4 = tk.Label(root, text="RAHUL  SAINI  ", fg="black", bg="#2C3E50", font=("Arial", 20, "italic"))
label4.place(x=1300, y=800)


root.mainloop()
