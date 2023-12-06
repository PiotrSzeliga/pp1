
class Song():
    def __init__(self,artist,track_title,album,album_year):
        self.artist = artist
        self.track_title = track_title
        self.album = album
        self.album_year = album_year
    def __str__(self):
        return f"Artist: {self.artist}\nTitle: {self.track_title}\nAlbum: {self.album}\nRok: {self.album_year}\n"


song1 = Song("Ed Sheeran","Hearts Don't Break Around Here","Divide","2017")
song2 = Song("Queen","Seven Seas of Rhye","Queen"," 1973")

print(song1)
print(song2)

