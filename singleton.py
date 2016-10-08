
def singleton(cls):
    instances = {}
    def getinstances():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstances

class MusicPlayer:

    def __init__(self, list):
        self.music_list = list

    def playmusic(self):
        for music in self.music_list:
            print(music)

print (type(MusicPlayer))
MusicPlayer = singleton(MusicPlayer)
print(type (MusicPlayer))