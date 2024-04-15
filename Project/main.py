# Project Name -> YouTube Video Downloader
# Team Members -> Anmol Kumar Gupta, Aryan Saini, Aakash Saini

import tkinter
from pytube import YouTube
import customtkinter

# My Download Function
def startdownload():
    try:
        youtube_link = link.get()
        youtube_obj = YouTube(youtube_link,on_progress_callback=on_progress)
        video = youtube_obj.streams.get_highest_resolution()
        title.configure(text=youtube_obj.title, text_color='white')
        finish_label.configure(text="")
        video.download()
        finish_label.configure(text="Downloaded")
        
    except:
        finish_label.configure(text="Youtube link is invalid", text_color="red")

def on_progress(stream, chunk,  bytes_reamaining):

    total_size = stream.filesize
    bytes_reamaining = total_size-bytes_reamaining
    percentage_of_compeletion = bytes_reamaining / total_size *100
    per = str(int(percentage_of_compeletion))
    progress_perc.configure(text=per+'%')
    progress_perc.update()

    # update progress bar
    progress_bar.set(float(percentage_of_compeletion)/100)


# System Color Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

# App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Video Downloader")

# My UI Elements
title = customtkinter.CTkLabel(app, text="Enter youtube link here")
title.pack(padx=10, pady=10)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=360, height=45, textvariable=url_var)
link.pack()

# Finished Downloading
finish_label = customtkinter.CTkLabel(app, text='')
finish_label.pack()

# Progress bar
progress_perc = customtkinter.CTkLabel(app, text="0%")
progress_perc.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

# Download Button
download_button = customtkinter.CTkButton(app, text="Download", command=startdownload)
download_button.pack(padx=10, pady=10)

# Run App
app.mainloop()