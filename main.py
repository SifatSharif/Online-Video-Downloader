from tkinter import *
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip
from pytubefix import YouTube
from pytubefix.cli import on_progress

def download():
    video_path = url_entry.get()
    file_path = path_label.cget("text")
    mp4_path = YouTube(video_path,on_progress_callback=on_progress)
    print(mp4_path.title)
    ys= mp4_path.streams.get_highest_resolution()
    ys.download(file_path)
    video_clip = VideoFileClip(f"{file_path}/{mp4_path.title}.mp4")
    video_clip.close()
    messagebox.showinfo("Success", "Video downloaded successfully!")
    
     

def get_path():
    path = filedialog.askdirectory()
    if path:
        path_label.config(text=path)

# GUI Setup
root = Tk()
root.title("Video Downloader")
root.configure(bg="#2d083d")

canvas = Canvas(root, width=400, height=300, bg="#6A89A7", highlightthickness=0)
canvas.pack()

app_label = Label(root, text="Video Downloader", fg='#BDDDFC',bg="#384959", font=("Arial", 20))
canvas.create_window(200, 50, window=app_label)

url_label = Label(root, text="Enter Video URL:",fg="White",bg="#384959", font=("Arial", 12))
canvas.create_window(200, 80, window=url_label)

url_entry = Entry(root, width=50)
canvas.create_window(200, 100, window=url_entry)

path_label = Label(root, text="Select Path To Download")
canvas.create_window(200, 150, window=path_label)

path_button = Button(root, text="Select", command=get_path)
canvas.create_window(200, 170, window=path_button)

download_button = Button(root, text="Download", command=download)
canvas.create_window(200, 220, window=download_button)

root.mainloop()
