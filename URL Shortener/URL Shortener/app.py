import tkinter
import pyshorteners
from PIL import Image, ImageTk


root = tkinter.Tk()
root.title('URL Shortener')
root.geometry('500x300')
root.overrideredirect(True) #Sistem başlık çubuğu gizleme

#Başlık çubuğu oluşturma 

def start_move(event):
    root.x = event.x
    root.y = event.y

def stop_move(event):
    root.x = None
    root.y = None

def do_move(event):
    x = root.winfo_pointerx() - root.x
    y = root.winfo_pointery() - root.y
    root.geometry(f'+{x}+{y}')

def close_app():
    root.destroy()


title_bar = tkinter.Frame(root, bg="#2F4F3E", relief="raised", bd=0, height=30)
title_bar.pack(fill=tkinter.X)

title_label = tkinter.Label(title_bar, text="URL Shortener", bg="#2F4F3E", fg="white")
title_label.pack(side=tkinter.LEFT, padx=10)

close_button = tkinter.Button(title_bar, text="✕", command=close_app, bg="#e74c3c", fg="white", bd=0)
close_button.pack(side=tkinter.RIGHT, padx=5)

# Sürükleme olayları
title_bar.bind("<ButtonPress-1>", start_move)
title_bar.bind("<ButtonRelease-1>", stop_move)
title_bar.bind("<B1-Motion>", do_move)

#Arka plan resmi
frame_image = Image.open('URL Shortener/Turkic_border.png') 
frame_image = frame_image.resize((500, 300), Image.Resampling.LANCZOS)
frame_photo = ImageTk.PhotoImage(frame_image)


canvas = tkinter.Canvas(root, width=500, height=300)
canvas.create_image(0, 0, image=frame_photo, anchor="nw")
canvas.pack()


def clear_focus(event=None):
    root.focus()

root.bind("<Escape>", clear_focus)
canvas.bind("<Button-1>", clear_focus)


#URL kısaltma fonksiyonu
def shorten(): 
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_entry.get())
    print(shorturl_entry.insert(0, short_url))



longurl_label = tkinter.Label(root, text='Enter Long URL', bg="#2F4F3E", fg="white")
longurl_entry = tkinter.Entry(root)
shorturl_label = tkinter.Label(root, text='Output Shortened URL', bg="#2F4F3E", fg="white")
shorturl_entry = tkinter.Entry(root)
shorten_button = tkinter.Button(root, text='Shorten URL', command=shorten , bg="#2F4F3E" , fg="white")



longurl_label.pack()
longurl_entry.pack()
shorturl_label.pack()
shorturl_entry.pack()
shorten_button.pack()



canvas.create_window(250, 80, window=longurl_label)
canvas.create_window(250, 110, window=longurl_entry)
canvas.create_window(250, 140, window=shorturl_label)
canvas.create_window(250, 170, window=shorturl_entry)
canvas.create_window(250, 210, window=shorten_button)


root.mainloop()



