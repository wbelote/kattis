import sys


def secs(t):
    t = t.split(":")
    return int(t[0]) * 60 + int(t[1])


def mins(t):
    if t % 60 >= 10:
        return f"{t // 60}:{t % 60}"
    return f"{t // 60}:0{t % 60}"


class Song:
    def __init__(self, line):
        self.title = line[0].replace("_", " ")
        self.time = secs(line[1])
        self.album = line[2].replace("_", " ")
        self.genre = line[3].replace("_", " ")
        self.track = int(line[4])

    def __str__(self):
        return f" {self.track}. {self.title} {mins(self.time)}"


class Album:
    def __init__(self, song):
        self.title = song.album
        self.songs = [song]
        self.time = song.time

    def __str__(self):
        self.songs.sort(key=lambda x: x.track)
        out = f"{self.title}: {len(self.songs)}, {mins(self.time)}"
        for s in self.songs:
            out += f"\n{s}"
        return out


def main():
    line = sys.stdin.readline().split()
    albums = {}
    songs = 0
    while line[0] != "-1":
        song = Song(line)
        songs += 1
        if song.album not in albums:
            albums[song.album] = Album(song)
        else:
            albums[song.album].songs.append(song)
            albums[song.album].time += song.time
        line = sys.stdin.readline().split()

    albums = list(albums.values())
    albums.sort(key=lambda x: x.title)
    time = sum([a.time for a in albums])
    print(f"{songs} MP3 files, {mins(time)} of time\n")
    for a in albums:
        print(a)


main()
