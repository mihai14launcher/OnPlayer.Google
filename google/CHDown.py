import tkinter as tk
from tkinter import messagebox, scrolledtext
import yt_dlp
import os
import re
import threading

def log_message(message):
    log_text.config(state=tk.NORMAL)
    log_text.insert(tk.END, message + '\n')
    log_text.config(state=tk.DISABLED)
    log_text.see(tk.END)

def download_video(url, format, output_path):
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]+bestvideo[ext=mp4]/best[ext=mp4]' if format == 'mp4' else 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }] if format == 'mp3' else [],
        'merge_output_format': 'mp4' if format == 'mp4' else None,
        'ffmpeg_location': 'C:\VOX\Extensions\OnPlayer\Required\FFMPEG\bin'  
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.add_progress_hook(progress_hook)
            ydl.download([url])
        messagebox.showinfo("Success", "Download completed successfully!")
    except yt_dlp.utils.DownloadError as e:
        log_message(f"Failed to download video: {e}")

def download_playlist(url, format, output_path):
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]+bestvideo[ext=mp4]/best[ext=mp4]' if format == 'mp4' else 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }] if format == 'mp3' else [],
        'merge_output_format': 'mp4' if format == 'mp4' else None,
        'ffmpeg_location': 'C:/ffmpeg/bin'  # Înlocuiește cu calea reală către ffmpeg
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.add_progress_hook(progress_hook)
            ydl.download([url])
        messagebox.showinfo("Success", "Download completed successfully!")
    except yt_dlp.utils.DownloadError as e:
        log_message(f"Failed to download playlist: {e}")

def is_playlist(url):
    return "playlist" in url or re.search(r"list=[\w-]+", url)

def start_download():
    url = url_entry.get().strip()
    format = format_var.get().lower()
    output_path = output_entry.get().strip()
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    download_thread = threading.Thread(target=download, args=(url, format, output_path))
    download_thread.start()

def download(url, format, output_path):
    if is_playlist(url):
        download_playlist(url, format, output_path)
    else:
        download_video(url, format, output_path)

def progress_hook(d):
    if d['status'] == 'downloading':
        log_message(f"Downloading: {d['_percent_str']} of {d['_total_bytes_str']} at {d['_speed_str']}")
    elif d['status'] == 'finished':
        log_message(f"Finished downloading: {d['filename']}")

def show_logs():
    if log_frame.winfo_viewable():
        log_frame.pack_forget()
    else:
        log_frame.pack(expand=True, fill='both', pady=10)

app = tk.Tk()
app.title("OnPlayer Downloader")

app.configure(bg="#2c3e50")

tk.Label(app, text="Enter YouTube video or playlist URL:", bg="#2c3e50", fg="white").pack(pady=5)
url_entry = tk.Entry(app, width=50)
url_entry.pack(pady=5)

tk.Label(app, text="Select format:", bg="#2c3e50", fg="white").pack(pady=5)
format_var = tk.StringVar(value="mp4")
tk.Radiobutton(app, text="MP4", variable=format_var, value="mp4", bg="#2c3e50", fg="white", selectcolor="#34495e").pack(pady=5)
tk.Radiobutton(app, text="MP3", variable=format_var, value="mp3", bg="#2c3e50", fg="white", selectcolor="#34495e").pack(pady=5)

tk.Label(app, text="Enter the folder path to save the file:", bg="#2c3e50", fg="white").pack(pady=5)
output_entry = tk.Entry(app, width=50)
output_entry.pack(pady=5)

tk.Button(app, text="Confirm Download", command=start_download, bg="#27ae60", fg="white").pack(pady=20)

tk.Button(app, text="Live Logs", command=show_logs, bg="#2980b9", fg="white").pack(pady=5)

log_frame = tk.Frame(app, bg="#2c3e50")
log_frame.pack(expand=True, fill='both', padx=10, pady=10)
log_frame.pack_forget()

log_text = scrolledtext.ScrolledText(log_frame, state='disabled', bg="#34495e", fg="white", wrap=tk.WORD)
log_text.pack(expand=True, fill='both')

app.mainloop()
