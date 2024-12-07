import tkinter as tk
from tkinter import filedialog, messagebox
import pygame
import os
from PIL import ImageTk, Image

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x150")

        # Initialize pygame mixer
        # Նստացնում ենք փայգեյմ գրադարանը 
        pygame.mixer.init()

        # Create buttons
        # Ստեղծում ենք կոճակները
        
        root.configure(bg='black')
        self.song_label = tk.Label(root, text="No song playing", font=('Helvetica', 25), bg="black", fg="white")
        self.song_label.pack(pady=7)
        self.image = ImageTk.PhotoImage(Image.open('images.jpg'))
        tk.Label(root, image=self.image, bg="black").pack()
        self.load_button = tk.Button(root, text="Load Music", command=self.load_music,width="20",fg="white",bg="red")
        self.load_button.pack(pady=7)

        self.play_button = tk.Button(root, text="Play", command=self.play_music,width="20",fg="white",bg="blue")
        self.play_button.pack(pady=7)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_music,width="20",fg="black",bg="yellow")
        self.pause_button.pack(pady=7)

        self.unpause_button = tk.Button(root, text="Unpause", command=self.unpause_music,width="20",fg="white",bg="red")
        self.unpause_button.pack(pady=7)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music,width="20",fg="white",bg="blue")
        self.stop_button.pack(pady=7)



        self.music_file = None

    def load_music(self):
        self.music_file = filedialog.askopenfilename(title="Select a Music File",filetypes=(("MP3 files", "*.mp3"),("WAV files", "*.wav"),("All files", "*.*")))
        if self.music_file:
            self.song_label.config(text=f"Music Loaded {os.path.basename(self.music_file)}")

    def play_music(self):
        if self.music_file and os.path.exists(self.music_file):
            pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.play()
            print(f"Playing: {os.path.basename(self.music_file)}")
            self.song_label.config(text=f"Music Loaded {os.path.basename(self.music_file)}")
        else:
            messagebox.showwarning("Warning", "Please load a music file first!")

    def pause_music(self):
        pygame.mixer.music.pause()
        print("Music Paused.")
        self.song_label.config(text=f"Music Paused.")

    def unpause_music(self):
        pygame.mixer.music.unpause()
        print("Music Unpaused.")
        self.song_label.config(text=f"Music Loaded {os.path.basename(self.music_file)}")

    def stop_music(self):
        pygame.mixer.music.stop()
        print("Music Stoped.")
        self.song_label.config(text=f"Music Stoped.")
        

if __name__ == "__main__":
    root = tk.Tk()
    player = MusicPlayer(root)
    root.mainloop()