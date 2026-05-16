"""
Sonora Tilton
IS 303-A03

Playlist Analyzer
- This program analyzes a playlist and provides insights on the total playtime,
filters by genre, finds the longest song, and counts over a certain duration.

Input:
- User name
- Playlist name
- A list of songs represented as dictionaries with keys "title", "duration", and "genre"

Processes:
- Create a dicitonary to store playlist info
- Calculate total playtime via accumulation
- Filter songs by genre- print only pop songs by name
- Find longest song (max length)
- Keep a count of songs over a certain duration

output:
- print a personalized statement to the user and playlist by name including the total
duration, longest song, and number of pop songs
"""
username = input("What is your username? ")
playlist_name = input("What is your playlist called? ")

songs = []

add_song = "yes"
while add_song == "yes":
    song_title = input("What is the name of the song? ").title()
    song_duration = int(input("How long (in minutes) is the song rounded to the minute? "))
    song_genre = input("What genre of music is the song? ").title()
    songs.append({"title": song_title, "duration": song_duration, "genre": song_genre})
    add_song = input("Would you like to add another song? yes/no ").lower()

#accumulator
total_duration = 0
#count
long_songs = 0
for song in songs:
    total_duration += song["duration"]
    if song["duration"] >= 5:
        long_songs += 1

#max length
longest_song = songs[0]
for song in songs:
    if song["duration"] > longest_song["duration"]:
        longest_song = song

#filter only show pop
pop_songs = []
for song in songs:
    if song["genre"] == "Pop":
        pop_songs.append(song["title"])

#personalized statement
print(f"Hello, {username}! Your playlist, '{playlist_name}' is {total_duration} minutes long.\n Your included pop songs are {pop_songs}\n and your longest song is {longest_song["title"]} at {longest_song["duration"]} minutes long. You have {long_songs} long songs.")