class Track():

    def __init__(self, number, name_track, time):
        self.number = number
        self.name_track = name_track
        self.time = time

    def __str__(self):
        return f"  Track{self.number} {self.name_track} - {self.time}"

  
class Album():
    
    def __init__(self, name_album, name_group):
            self.name_album = name_album
            self.name_group = name_group
            self.list_track =[]

    def __str__(self):
        print(f"Album: {self.name_album}\nGroup: {self.name_group}\nTracks:")
        self.get_tracks()
        self.get_duration()
        return  f""
   
    
    def add_track(self, name_track, time):
         number =len(self.list_track)+1
         track = Track(number, name_track, time)
         self.list_track.append(track)

    def get_tracks(self):
        for item in self.list_track:
            print(item)

    def get_duration(self):
        minutes = seconds = 0
        for item in self.list_track:
            timeTotal = item.time.split(":")
            minutes += int(timeTotal[0])
            seconds += int(timeTotal[1])
     
        minutes = minutes + seconds//60
        seconds = seconds % 60 
        print(f"Total duration of album: {minutes}min {seconds}sec")

                
my_album = Album("Nevermind", "Nirvana" )
my_album.add_track("Polly","2:57")
my_album.add_track("On a Plain","3:16")
my_album.add_track("Stay Away","3:29")

my_album_2 = Album("Strange Days", "The Doors" )
my_album_2.add_track("Strange Days","5:33")
my_album_2.add_track("Unhappy Girl","3:03")
my_album_2.add_track("Love Me Two Times","0:59")

my_album.get_tracks()
my_album.get_duration()
print('')

print(my_album)
print(my_album_2)

