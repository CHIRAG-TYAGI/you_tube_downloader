import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from downloader_working import download_video
import os

class YouTubeDownloaderUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")
        self.root.geometry("600x400")
        self.root.resizable(True, True)
        
        # Create main frame
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # URL Entry
        ttk.Label(self.main_frame, text="Enter YouTube URL:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.url_var = tk.StringVar()
        self.url_entry = ttk.Entry(self.main_frame, textvariable=self.url_var, width=50)
        self.url_entry.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Output Directory
        ttk.Label(self.main_frame, text="Output Directory:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.output_path_var = tk.StringVar(value=os.path.join(os.getcwd(), "downloads"))
        self.output_entry = ttk.Entry(self.main_frame, textvariable=self.output_path_var, width=40)
        self.output_entry.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=5)
        
        # Browse Button
        self.browse_btn = ttk.Button(self.main_frame, text="Browse", command=self.browse_directory)
        self.browse_btn.grid(row=3, column=1, padx=5, pady=5)
        
        # Download Button
        self.download_btn = ttk.Button(self.main_frame, text="Download", command=self.start_download)
        self.download_btn.grid(row=4, column=0, columnspan=2, pady=20)
        
        # Progress
        self.progress_var = tk.StringVar(value="")
        self.progress_label = ttk.Label(self.main_frame, textvariable=self.progress_var)
        self.progress_label.grid(row=5, column=0, columnspan=2, pady=5)
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)

    def browse_directory(self):
        directory = filedialog.askdirectory(initialdir=self.output_path_var.get())
        if directory:
            self.output_path_var.set(directory)

    def start_download(self):
        url = self.url_var.get().strip()
        output_path = self.output_path_var.get().strip()
        
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL")
            return
            
        self.progress_var.set("Downloading... Please wait.")
        self.download_btn.state(['disabled'])
        self.root.update()
        
        try:
            success = download_video(url, output_path)
            if success:
                messagebox.showinfo("Success", "Video downloaded successfully!")
                self.url_var.set("")  # Clear the URL field
            else:
                messagebox.showerror("Error", "Failed to download the video")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            self.progress_var.set("")
            self.download_btn.state(['!disabled'])

def main():
    root = tk.Tk()
    app = YouTubeDownloaderUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
