from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os

class MusicPlayer:

    def __init__(self, window):
        window.geometry('320x100'); window.title('Musio Player'); window.resizable(0,0)
        Load = Button(window, text = 'Load',  width = 10, font = ('Times', 10), command = self.load)
        Play = Button(window, text = 'Play',  width = 10,font = ('Times', 10), command = self.play)
        Pause = Button(window,text = 'Pause',  width = 10, font = ('Times', 10), command = self.pause)
        Stop = Button(window ,text = 'Stop',  width = 10, font = ('Times', 10), command = self.stop)
        Load.place(x=0,y=20);Play.place(x=110,y=20);Pause.place(x=220,y=20);Stop.place(x=110,y=60)
        
        self.music_file = []
        self.playing_state = False
        self.auto_load()
        print(self.music_file)
        # self.play()


    def auto_load(self):
        files = []
        os.chdir(r'G:\Jupiter-Project\bobi assistant\assets\music') 
        songs = os.listdir()
        for s in songs:
            self.music_file.append(s)
        
        if self.music_file:
            self.play()


    def load(self):
        self.music_file = list(filedialog.askopenfilenames())


    def play(self):
        if self.music_file:
            for music in self.music_file:
                mixer.init()
                mixer.music.load(music)
                mixer.music.play()
                while mixer.music.get_busy() == True:
                    continue


    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False


    def stop(self):
        mixer.music.stop()



root = Tk()
app = MusicPlayer(root)
root.mainloop()