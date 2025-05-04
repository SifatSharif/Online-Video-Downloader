# Online-Video-Downloader
A simple yet powerful Python desktop application to download YouTube videos in high quality using a clean and intuitive Tkinter-based GUI. Just paste the video URL, choose your download location, and download any YouTube video in seconds.


# 🚀 Features

✅ Download videos from YouTube in the highest available resolution

📂 Select custom directory to save downloaded videos

🎞️ Automatically closes video file handlers after download using moviepy

🎨 User-friendly GUI built with Tkinter

🔔 Success notification when the download is complete

# 🛠️ Built With

Tkinter - GUI framework

pytubefix - YouTube video extraction

moviepy - Video file handling


# 🧠 How It Works

Paste a YouTube video URL into the input field.

Select a folder where you want to save the video.

Click "Download" – the video will be downloaded in its highest quality.

A success pop-up will notify you once the download is complete.

# Database Connection :

🔧 Step 1: Install MySQL Connector

🗃️ Step 2: Create MySQL Database and Table
You can run these in your MySQL console or GUI (like phpMyAdmin or MySQL Workbench):
data_base query :{ 
CREATE DATABASE video_downloader;

USE video_downloader;

CREATE TABLE users (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(100) NOT NULL
);

}

Need Xamp server always open