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

def showp():
    s = ent.get()
    t = str(w2.get())
    v = 1
    showcontent =''
    fil  =''
    slutt = int(s)
    antlinjer = 0
    txt.delete(0,END)
    txt.insert(END,'****show playlist number  '+ t +'  '+ s + ' first lines ****')
    if t != "0":
     filtmp ='playlist-'+ t + '.txt'

     try:
       fil = open(filtmp,'r')

       while slutt  !=  antlinjer:
         showcontent = fil.readline()
         
         lengde = fil.tell()
         antlinjer  = antlinjer + 1
         if  showcontent != '':

           txt.insert(END, showcontent + '    ' + str(antlinjer) +' lines read ' + str(lengde)+ ' bytes ')
           
       close(fil)
     except:
           txt.insert(END,'************* COMPLETED **************')


    
    return

def mergep():
    s = ent.get()
    t = str(w2.get())
    v = 1
    content =''
    fil  =''
    merge = int(s)
    
    txt.insert(END,'********** merge playlist number  '+ t +'  '+ s + ' = playlist-'+ t +'.txt **********')
    if t != "0":
     filtmp ='playlist-'+ t + '.txt'
     filtmp2 ='playlist-'+ s + '.txt'
     try:
       fil = open(filtmp,'a')
       fil2 = open(filtmp2, 'r')
       content = fil2.read()    
       fil.write(content)
       close(fil2)
       close(fil)
     except:
           txt.insert(END,'************** COMPLETED ***************')

    return


def clrvindu():
    s = ent.get()
    t = str(w2.get())
    txt.delete(0,END)
    return


vindu = Tk()
def playlist():
    menubar = Menu(vindu)
    pmenu =  Menu(menubar, tearoff=0)
    pmenu.add_command(label="Make playlist from full path given in the upper field. Remember / at the end ", command=makep)
    pmenu.add_command(label="Show playlist as selected on switch and num of lines given in the upper field", command=showp)
    pmenu.add_command(label="Merge playlist as selected on switch with num of playlist given in the upper field", command=mergep)
    pmenu.add_command(label="Clear text area.", command=clrvindu)
    pmenu.add_command(label="Exit", command=vindu.quit) 
    menubar.add_cascade(label="Playlist", menu=pmenu)
    vindu.config(menu=menubar)




    return





lbl = Label(vindu, text="My Player is a GUI for mpg321 player")
lbl2 = Label(vindu, text="Playlists 1 to 22. Zero = none")
vindu.title('My Music Player')
vindu.geometry("700x500")
sbar = Scrollbar(vindu)
sbar.pack( side  = RIGHT , fill = Y )
but = Button(vindu, text='Play', command= lambda: play(0))


but2 = Button(vindu, text='Stop', command= lambda : stop())
but3 = Button(vindu, text='Quit', command= lambda: quit())
but4 = Button(vindu, text='Playlist', command= lambda: playlist())
ent = Entry(vindu, text='<return>',width= 150)
w2 = Scale(vindu, from_=0, to=22, orient=HORIZONTAL)
txt = Listbox(vindu, width=50, height=5, yscrollcommand = sbar.set)
txt.insert(END,'Choose music directory in upper field by typing it.') 
txt.insert(END,'Default dir is /home/pi/Music/.')
txt.insert(END,'Click Stop to stop playing and Quit to quit the GUI.')
txt.insert(END,'Stop before changing directory.')
txt.insert(END,'My Player play in shuffle mode including subdirs.')
txt.insert(END,'You have to install pulseaudio and pavucontrol')
txt.insert(END,'packages in addtion to mpg321.')
txt.insert(END,'The GUI script is written in Python version 2.7.11.')
txt.insert(END,'Modify as needed. Maintained by  kohauge24@gmail.com')
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
#txt.pack( fill = BOTH)
sbar.config(command = txt.yview)
s ="/home/pi/Music/"
j = 0

print(s)



vindu.mainloop()




