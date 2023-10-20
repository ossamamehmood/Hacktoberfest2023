import tkinter as tk
import pygame

# Initialize pygame
pygame.init()

# Create the main window
root = tk.Tk()
root.title("Simple Media Player")

# Create a function to play an audio file
def play_audio():
    file_path = entry.get()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Create a label and entry widget for file path
label = tk.Label(root, text="Enter file path:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Create a button to play the audio
play_button = tk.Button(root, text="Play", command=play_audio)
play_button.pack()

# Create a function to stop playback
def stop_audio():
    pygame.mixer.music.stop()

# Create a button to stop the audio
stop_button = tk.Button(root, text="Stop", command=stop_audio)
stop_button.pack()

# Start the main loop
root.mainloop()

