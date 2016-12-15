#!/usr/bin/env python

import subprocess
import sys
import Tkinter

from Tkinter import *





def play(j):
    i = 0
    s = ent.get()
    t = w2.get()
    u = ""
    x = ''

     
    e = subprocess.check_output("cd "+s+"; exit 0", stderr=subprocess.STDOUT, shell=True)
    if t == 0:   
      p = subprocess.Popen(['mpg321', '-zB', '-o', 'pulse', '-a', 'hw:0,0', '-g', '50', s, '*'],  stdout= subprocess.PIPE, stderr= subprocess.STDOUT)

      ent.delete(0,END)
      ent.insert(150,s)   

    if t != 0:            
       t = str(w2.get())
       filtmp ="playlist-"+ t + ".txt"
       p = subprocess.Popen(['mpg321', '-zB', '-o', 'pulse', '-a', 'hw:0,0', '-@', filtmp],  stdout= subprocess.PIPE, stderr= subprocess.STDOUT)
       
       ent.delete(0,END)
       ent.insert(150,s)

        
    return

def stop():

    q = subprocess.Popen("killall mpg321", shell = True)


    return

def quit():
    q = subprocess.Popen("killall mpg321", shell = True)
    vindu.destroy(); vindu.quit()
    return

def makep():
    s = ent.get()
    t = str(w2.get())
    v = 0
    print('********************make playlist from folder   '+ s)
    if t != "0":
     filtmp ='playlist-'+ t + '.txt'

     try:
       v = subprocess.call("find " + s + "*.mp3   > "  + filtmp  , shell=True)
     except:
           print '**************ERROR 1***************'
     print(filtmp,v)

    return


vindu = Tk()
def playlist():
    menubar = Menu(vindu)
    pmenu =  Menu(menubar, tearoff=0)
    pmenu.add_command(label="Make playlist", command=makep)
    pmenu.add_command(label="Exit", command=vindu.quit) 
    menubar.add_cascade(label="Playlist", menu=pmenu)
    vindu.config(menu=menubar)




    return





lbl = Label(vindu, text="My Player is a GUI for mpg321 player")
lbl2 = Label(vindu, text="Playlists 1 to 22. Zero = none")
vindu.title('My Music Player')
vindu.geometry("700x500")

but = Button(vindu, text='Play', command= lambda: play(0))


but2 = Button(vindu, text='Stop', command= lambda : stop())
but3 = Button(vindu, text='Quit', command= lambda: quit())
but4 = Button(vindu, text='Playlist', command= lambda: playlist())
ent = Entry(vindu, text='<return>',width= 150)
w2 = Scale(vindu, from_=0, to=22, orient=HORIZONTAL)
txt = Text(vindu, height=7)
txt.insert(END,'Choose music directory in upper field by typing it. Default /home/pi/Music/.\nClick Stop to stop playing and Quit to quit. Stop before changing directory.\nMy Player play in shuffle mode including subdirs.\nYou have to install pulseaudio and pavucontrol packages in addtion to mpg321.\nThe GUI script is written in Python version 2.7.11.\nModify as needed. Maintained by                  kohauge@icloud.com\n')
ent.pack(pady=30, padx=100)
ent.insert(150,'/home/pi/Music/')
lbl.pack()
but2.pack(pady=10)
but3.pack(pady=30)
but.pack()
but4.pack()
w2.pack()
lbl2.pack()
txt.pack()

s ="/home/pi/Music/"
j = 0

print(s)



vindu.mainloop()




