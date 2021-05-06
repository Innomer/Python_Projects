import sys, os
import pyperclip
import pyshorteners
from tkinter import *

from pyshorteners.exceptions import ShorteningErrorException, BadURLException


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


window = Tk()
window.geometry("500x300")
window.resizable(False, False)
window.title("URL Shortener")
window.configure(bg="#4B8BBE")
url = StringVar()
url_add = StringVar()


def urlshortener():
    try:
        urladdress = url.get()
        url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
        url_add.set(url_short)
    except ShorteningErrorException:
        url_add.set("Enter A Valid URL(with https://)!")


def copyurl():
    url_short = url_add.get()
    pyperclip.copy(url_short)


Label(window, text="My URL Shortener", font=("Helvetica", "25"), bg="#4B8BBE").pack(pady=20)
Entry(window, textvariable=url).pack(pady=15, ipadx=30)
Button(window, text="Generate Shortened URL", command=urlshortener).pack(pady=7)
Entry(window, textvariable=url_add).pack(pady=15, ipadx=30)
Button(window, text="Copy URL", command=copyurl).pack(pady=7)
resource_path('main.py')
window.mainloop()
