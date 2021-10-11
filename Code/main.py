import tkinter as tkp
import pygame
import os
from tkinter.filedialog import askdirectory

#window
player = tkp.Tk()
player.title("موزیک")
player.geometry("500x500")

#pygame init
pygame.init()
pygame.mixer.init()

playlist=tkp.Listbox()

def Play():
    pygame.mixer.music.load(playlist.get(tkp.ACTIVE))
    var.set(playlist.get(tkp.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(volume.get())

def Stop():
    pygame.mixer.music.stop()

def Pause():
    pygame.mixer.music.pause()

def UnPause():
    pygame.mixer.music.unpause()

def ChangeVolume(a):
    a=volume.get()
    pygame.mixer.music.set_volume(a)

def Load():
    directory=askdirectory()
    os.chdir(directory)
    musiclist=os.listdir(directory)
    for item in musiclist:
        if item.endswith(".mp3"):
          i=0
          playlist.insert(i,item)
          i=i+1


#btn
btnplay=tkp.Button(player,width=5,height=3,text="پخش",command=Play)
btnstop=tkp.Button(player,width=5,height=3,text="توقف",command=Stop)
btnpause=tkp.Button(player,width=5,height=3,text="مکث",command=Pause)
btnunpause=tkp.Button(player,width=5,height=3,text="ادامه پخش",command=UnPause)
btnload=tkp.Button(player,width=5,height=3,text="انتخاب پوشه",command=Load)

#volume
volume=tkp.Scale(player,from_=0,to_=1,resolution=0.1,orient=tkp.HORIZONTAL,command=ChangeVolume)

#music name
var = tkp.StringVar()
musictitle=tkp.Label(player,textvariable=var)

#place
btnload.pack(fill="x")
playlist.pack()
volume.pack(fill="x")
musictitle.pack()
btnplay.pack(fill="x")
btnpause.pack(fill="x")
btnunpause.pack(fill="x")
btnstop.pack(fill="x")

player.mainloop()