from tkinter import *
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip
from pytubefix import YouTube
from pytubefix.cli import on_progress
import mysql.connector

# ============== MySQL Config ==============
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_NAME = "video_downloader"

# ============== MySQL Connection ==============
def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

# ============== Video Downloader ==============
def open_main_app():
    def download():
        video_path = url_entry.get()
        file_path = path_label.cget("text")
        try:
            mp4_path = YouTube(video_path, on_progress_callback=on_progress)
            print(mp4_path.title)
            ys = mp4_path.streams.get_highest_resolution()
            ys.download(file_path)
            video_clip = VideoFileClip(f"{file_path}/{mp4_path.title}.mp4")
            video_clip.close()
            messagebox.showinfo("Success", "Video downloaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download: {e}")
        
    def get_path():
        path = filedialog.askdirectory()
        if path:
            path_label.config(text=path)

    root = Tk()
    root.title("Video Downloader")
    root.configure(bg="#2d083d")

    canvas = Canvas(root, width=400, height=300, bg="#6A89A7", highlightthickness=0)
    canvas.pack()

    app_label = Label(root, text="Video Downloader", fg='#BDDDFC', bg="#384959", font=("Arial", 20))
    canvas.create_window(200, 50, window=app_label)

    url_label = Label(root, text="Enter Video URL:", fg="White", bg="#384959", font=("Arial", 12))
    canvas.create_window(200, 80, window=url_label)

    url_entry = Entry(root, width=50)
    canvas.create_window(200, 100, window=url_entry)

    global path_label
    path_label = Label(root, text="Select Path To Download")
    canvas.create_window(200, 150, window=path_label)

    path_button = Button(root, text="Select", command=get_path)
    canvas.create_window(200, 170, window=path_button)

    download_button = Button(root, text="Download", command=download)
    canvas.create_window(200, 220, window=download_button)

    root.mainloop()

# ============== Login/Register ==============
def run_login_window():
    login_window = Tk()
    login_window.title("Login / Register")
    login_window.geometry("400x400")
    

    def register_user():
        username = reg_user.get()
        password = reg_pass.get()
        if username == "" or password == "":
            messagebox.showwarning("Input Error", "Username and Password cannot be empty")
            return
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            messagebox.showinfo("Success", "User registered successfully!")
        except mysql.connector.IntegrityError:
            messagebox.showerror("Error", "Username already exists!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            conn.close()

    def login_user():
        username = login_user_entry.get()
        password = login_pass_entry.get()
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
            result = cursor.fetchone()
            conn.close()
            if result:
                login_window.destroy()
                open_main_app()
            else:
                messagebox.showerror("Error", "Invalid credentials")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    Label(login_window, text="Login", font=("Arial", 16)).pack(pady=10)

    Label(login_window, text="Username").pack()
    login_user_entry = Entry(login_window)
    login_user_entry.pack()

    Label(login_window, text="Password").pack()
    login_pass_entry = Entry(login_window, show="*")
    login_pass_entry.pack()

    Button(login_window, text="Login", command=login_user).pack(pady=10)

    Label(login_window, text="Register New User", font=("Arial", 12)).pack(pady=10)

    reg_user = Entry(login_window)
    reg_user.pack()
    reg_pass = Entry(login_window, show="*")
    reg_pass.pack()

    Button(login_window, text="Register", command=register_user).pack(pady=5)

    login_window.mainloop()

# ============== Start App ==============
if __name__ == "__main__":
    run_login_window()
