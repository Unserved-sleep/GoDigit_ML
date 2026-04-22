class Track:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        minutes, seconds = map(int, duration.split(":"))
        self.duration = minutes * 60 + seconds

    def formatted_duration(self):
        return f"{self.duration // 60}:{self.duration % 60:02d}"

    def __str__(self):
        return self.title + " by " + self.artist + "[" + str(self.formatted_duration()) + "]"


def formatted_duration(duration):
    return f"{duration // 60}:{duration % 60:02}"


class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = []

    def add(self, track):
        self.tracks.append(track)
    def remove(self, track):
        self.tracks.remove(track)
    def total_duration(self):
        total = sum( x.duration for x in self.tracks )
        return formatted_duration(total)
    def longest_track(self):
        return max(self.tracks, key= lambda x: x.duration)
    def shortest_track(self):
        return min(self.tracks, key= lambda x: x.duration)
    def average_track(self):
        total = sum( x.duration for x in self.tracks )
        avg = total/len(self.tracks)
        return formatted_duration(avg)

    def tracks_under(self, seconds):
        return [x.title for x in self.tracks if x.duration < seconds]

    def summary(self):
        return f"{self.name} | {len(self.tracks)} tracks | {self.total_duration()} seconds"


tracks = [
  Track("Blinding Lights", "The Weekend",     "3:20"),
  Track("Levitating",      "Dua Lipa",       "3:23"),
  Track("Stay",            "Kid LAROI",      "2:21"),
  Track("Peaches",         "Justin Bieber",  "3:18"),
  Track("Good 4 U",        "Olivia Rodrigo", "2:58"),
]

playlist = Playlist("Evening Vibes")
for t in tracks:
    playlist.add(t)

print(f"str(tracks[0]): {str(tracks[0])}")
print(f"tracks[0].seconds: {tracks[0].duration}")
print(f"Total Duration: {playlist.total_duration()}")
print(f"Longest: {playlist.longest_track()}")
print(f"Shortest: {playlist.shortest_track()}")
print(f"Average: {playlist.average_track()}")
print(f"Tracks under 200s: {playlist.tracks_under(200)}")
print(playlist.summary())


