# MusicPlayer - A Simple Music Player Application

# Dictionary to store music tracks
music_library = {}

# Function to add a music track to the library
def add_track(track_name, artist, duration):
    music_library[track_name] = {'artist': artist, 'duration': duration}

# Function to list all music tracks in the library
def list_tracks():
    if not music_library:
        print("The music library is empty.")
    else:
        print("Music Library:")
        for track_name, track_info in music_library.items():
            print(f"Track: {track_name}")
            print(f"Artist: {track_info['artist']}")
            print(f"Duration: {track_info['duration']} minutes")
            print()

# Function to play a music track
def play_track(track_name):
    if track_name in music_library:
        print(f"Now playing '{track_name}' by {music_library[track_name]['artist']}. Enjoy the music!")
    else:
        print(f"'{track_name}' is not found in the music library.")

# Main function
def main():
    while True:
        print("\n--- MusicPlayer ---")
        print("1. Add a Music Track")
        print("2. List Music Tracks")
        print("3. Play a Music Track")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "4":
            print("Goodbye!")
            break

        if choice == "1":
            track_name = input("Enter the track name: ")
            artist = input("Enter the artist name: ")
            duration = input("Enter the duration (in minutes): ")
            add_track(track_name, artist, duration)
            print(f"'{track_name}' has been added to the music library.")
        elif choice == "2":
            list_tracks()
        elif choice == "3":
            track_name = input("Enter the track name you want to play: ")
            play_track(track_name)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
