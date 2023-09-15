#################################################################
# this is version 1.0 of beepnotes
# code is bulky, repetitive and disorganized
# mainly was an initial "trial" for working with beeply
#################################################################
# this version was FORSAKEN after v 2.0 was made
#################################################################


import sys
from beeply import notes
import winsound  # for special notes, undefined in beeply #

helpStr="\n a demonstration of several melodies using 'beeply' module"
helpStr+="\n\n command:\t beepnotes [# of item to play]\n\n"
helpStr+=" items:"

a = sys.argv

def main():
    if len(a)<2 or a[1]=="?" or a[1]=="help":
        print(helpStr)
        for i in range(0,len(lst)):
            print("\t\t",i+1,".  ",lst[i][0])
    else:
        if not isIntInRange(a[1]):
            print("INPUT ERROR!")
            exit()
        item = int(a[1])
        # choose item #
        print(lst[item-1][0])
        lst[item-1][1]()


####################################################
    
def isIntInRange(value):
    try:
        return int(value)>0 and int(value)<=len(lst)
    except ValueError:
        return False

####################################################

# 1
def mary():
    # write notes for melody #
    line1 = ['E','D','C','D','E','E','E']
    line2 = ['D','D','D','E','E','E']
    line3 = line1
    line4 = ['E','D','D','E','D','C']
    melody = [line1,line2,line3,line4]
    # init beeply object #
    play = notes.beeps(500)
    # play it #
    for line in melody:
        for note in line:
            play.hear(note)
        notes.sleep(0.5)
        

# 2
def twinkle():
    # notes for melody # * denotes long note #
    line1 = ["G","G","D","D","E","E","D*","C","C","B","B","A","A","G*"] 
    line2 = ["D","D","C","C","B","B","A*","D","D","C","C","B","B","A*"]
    line3 = ["G","G","D","D","E","E","D*","C","C","B","B","A","A","G*"]
    melody = [line1,line2,line3]
    # init beeply objects #
    short = notes.beeps(400)
    # play it #
    for line in melody:
        for note in line:
            if len(note)>1:
                short.hear(note[0],1000)
            else:
                short.hear(note)
        notes.sleep(0.5)
    
# 3    
def baby():
    # notes, * denotes a long note #
    line1 = ["E","G","E_","D_*","C_","E","G","C_","B*","F","G","F_","E_*","D_","D_","C_","A","G*"]
    line2 = ["E","G","E_","D_*","C_","E","G","C_","B*","A","G","C_","F_","E_*","C_","D_","A","B","C_*"]
    melody =[line1,line2]
    # init short and long beeply objects "
    short = notes.beeps(750)
    long = notes.beeps(2000)
    # play it #
    for line in melody:
        for note in line:
            if len(note)==1: # if short & NOT high-scale
                short.hear(note)
            elif len(note)==2 and note[1]=='_': # if short & high-scale
                short.hear(note)
            elif len(note)==2 and note[1]=='*': # if long & NOT high-scale
                long.hear(note[0])
            else: # if long & high-scale
                long.hear(note[:2])
        notes.sleep(1.25)

# 4
def birthday():
    # notes # ~ denotes middle length, * denotes long notes #
    line1 = ["C","C","D~","C~","F~","E*"]
    line2 = ["C","C","D~","C~","G~","F*"]
    line3 = ["C","C","C~","A~","F~","E~","D~"]
    line4 = ["b","b","A~","F~","G~","F*"]
    melody = [line1,line2,line3,line4]
    b = (notes.beeps.B + notes.beeps.C) // 2 # special note b
    # init short, middle and long beeply objects #
    short = notes.beeps(400)
    middle = notes.beeps(800)
    long = notes.beeps(1200)
    # play it #
    for line in melody:
        for note in line:
            if len(note)==1:  # short
                if note.lower() == note: # special (using winsound directly)
                    winsound.Beep(b,400)
                else:
                    short.hear(note)
            elif len(note)==2:  # middle or long
                if note[1]=='~': # middle
                    middle.hear(note[0])
                else: # long
                    long.hear(note[0])
        notes.sleep(0.5)

# 5
def happy():
    # notes # ~ denotes very long (3xShort) #
    line1 = ["G","G","C_","C_","C_","C_","C_","C_","B","C_","D_~"]
    line2 = ["G","G","D_","D_","D_","D_","D_","D_","C_","D_","E_~"]
    line3 = ["E_","E_","F_","F_","F_","F_","A","A","F_","F_","E_",
              "E_","E_","D_","C_","C_","E_","E_","D_","D_","D_","C_","B","B","A","B","C_~"]
    melody = [line1,line2,line3]
    # init short and very-long beeply objects #
    short = notes.beeps(400)
    vlong = notes.beeps(1200)
    # play it #
    for line in melody:
        for note in line:
            if len(note)==1:        # short and NOT high-scale
                short.hear(note)
            elif len(note)==2:
                if note[1]=='_':    # short and high-scale
                    short.hear(note)
                else:               # long and NOT high-scale
                    vlong.hear(note[0])
            else:                   # long and high-scale
                vlong.hear(note[:2])
        notes.sleep(0.5)


# 6
def christmas():
    # notes # ~ denotes very long (3xShort) #
    line1=["G","C_","C_","D_","C_","B","A","A","A","D_","D_","E_","D_",
           "C_","B","G","G","E_","E_","F_","E_","D_","C_","A","G","G","A","D_","B","C_~"]
    line2=["G","C_","C_","C_","B~","B","C_","B","A","G~"]
    line3=["D_","E_","D_","C_","G_","G","G","G","A","D_","B","C_~"]
    line4=line1
    melody = [line1,line2,line3,line4]
    # init short and very-long beeply objects #
    short = notes.beeps(400)
    vlong = notes.beeps(1200)
    # play it #
    for line in melody:
        for note in line:
            if len(note)==1:        # short and NOT high-scale
                short.hear(note)
            elif len(note)==2:
                if note[1]=='_':    # short and high-scale
                    short.hear(note)
                else:               # long and NOT high-scale
                    vlong.hear(note[0])
            else:                   # long and high-scale
                vlong.hear(note[:2])
        notes.sleep(0.5)



# 7
def joy():
    # notes # < denotes very short #
    line1=["E_","E_","F_","G_","G_","F_","E_","D_","C_","C_","D_","E_","E_","D_<","D_"]
    line2=["E_","E_","F_","G_","G_","F_","E_","D_","C_","C_","E_","E_","D_","C_<","C_"]
    line3=["D_","D_","E_","C_","D_","E_<","F_<","E_","C_","D_","E_<","F_<","E_","D_","C_","D_","G"]
    line4=["E_","E_","F_","G_","G_","F_","E_","D_","C_","C_","D_","E_","D_","C_<","C_"]
    melody = [line1,line2,line3,line4]
    # init normal and very short beeply objects #
    normal = notes.beeps(750)
    vshort = notes.beeps(250)
    # play it #
    for line in melody:
        for note in line:
            if len(note)==1:    # normal and NOT high-scale
                normal.hear(note)
            elif len(note)==2:
                if note[1]=='_':    # normal and HIGH-scale
                    normal.hear(note)
                else:           # very short and NOT high-scale
                    vshort.hear(note[0])
            else:   # very short and HIGH-scale
                vshort.hear(note[:2])
        notes.sleep(0.5)


# 8
def grace():
    # notes # as tuples, notes in 0, and tempo/duration in 1 #
    # 1 - short , 2 - normal , 3 - long , 4 - very long #
    line1=[("G",2),("C_",3),("E_",1),("C_",1),("E_",3),("D_",2),("C_",3),("A",2),("G",3)]
    line2=[("G",2),("C_",3),("E_",1),("C_",1),("E_",3),("D_",2),("G_",4)]
    line3=[("E_",2),("G_",3),("E_",1),("C_",1),("E_",3),("D_",2),("C_",3),("A",2),("G",3)]
    line4=[("G",2),("C_",3),("E_",1),("C_",1),("E_",3),("D_",2),("C_",4)]
    melody = [line1,line2,line3,line4]
    # init beeply object for all durations #
    short =  notes.beeps(250)
    normal = notes.beeps(500)
    long = notes.beeps(1000)
    vlong = notes.beeps(1500)
    # play it #
    for line in melody:
        for note in line:
            t = note[1] # duration  1,2,3,4
            n = note[0] #  the note to play
            if t==1:
                short.hear(n)
            elif t==2:
                normal.hear(n)
            elif t==3:
                long.hear(n)
            elif t==4:
                vlong.hear(n)
        notes.sleep(0.5)

# 9
def auld_lang_syne():
    # notes # as tuples: notes at 0 ; tempo/duration at 1 #
    #  1 - short ,  2 - normal , 3 - longer , 4 - longest (end of line) #
    line1=[("G",2),("C_",3),("B",1),("C_",2),("E_",2),("D_",3),("C#",2),("D_",2),("E_",2),("C_",2),("C_",1),("E_",2),("G_",2),("A_",4)]
    line2=[("A_",2),("G_",3),("E_",1),("E_",2),("C_",2),("D_",3),("C#",2),("D_",2),("E_",1),("D_",1),("C_",2),("A",1),("A",2),("G",2),("C_",4)]
    line3=[("A_",2),("G_",3),("E_",1),("E_",2),("C_",2),("D_",3),("C#",1),("D_",2),("A_",2),("G_",3),("E_",1),("E_",2),("G_",2),("A_",4)]
    line4=[("A_",2),("G_",3),("E_",1),("E_",2),("C_",2),("D_",3),("C#",1),("D_",2),("E_",1),("D_",1),("C_",3),("A",1),("A",2),("G",2),("C_",4)]
    melody = [line1,line2,line3,line4]
    c_sharp  = (notes.beeps.C_ + notes.beeps.D_) // 2 # special note C# (C-sharp) # between C_ & D_
    durations = [250,500,1000,1500]
    # init beeply object  #
    play = notes.beeps()
    # play it #
    for line in melody:
        for note in line:
            n = note[0] # note
            t = note[1] # duration
            if n=="C#":  # special note , play using winsound
                winsound.Beep(c_sharp,durations[t-1])
            else: # any other note, using beeply object
                play.hear(n,durations[t-1])
        notes.sleep(0.5)
        
# 10
def imperial():
    # notes # as tuples # same assumptions as previous method #
    melody=[
        [("E",3),("E",3),("E",3),("C",2),("G",1),("E",3),("C",2),("G",1),("E",4)],
        [("B",3),("B",3),("B",3),("C_",2),("G",1),("D#",3), ("C",2),("G",1),("E",4)],
        [("E_",3),("E",2),("E",1),("E_",3),("D#_",2),("D_",1),("C#_",1),("C_",1),("C#_",2)],
        [("F",1),("A#",3),("A",2),("G#",1),("G",1),("F#",1),("G",2)],
        [("C",1),("D#",3),("C",2),("E",1),("G",3),("E",2),("G",1),("B",4)],
        [("E_",3),("E",2),("E",1),("E_",3),("D#_",2),("D_",1),("C#_",1),("C_",1),("C#_",2)],
        [("F",1),("A#",3),("A",2),("G#",1),("G",1),("F#",1),("G",2)],
        [("C",1),("D#",3),("C",2),("G",1),("E",3),("C",2),("G",1),("E",4)]
            ]
    durations = [250,500,750,1000]
    # init beeply object
    play = notes.beeps()
    # play it #
    for line in melody:
        for note in line:
            n = note[0]
            t = note[1]
            if isSharp(n):
                playSharp(n,durations[t-1])
            else:
                play.hear(n,durations[t-1])
        notes.sleep(0.5)

################# some helper methods ##############

def isSharp(note):
    return "#" in note

def playSharp(note,duration):
    t = notes.beeps
    sharp_notes = {"C#": (t.C+t.D)//2,
                   "D#": (t.D+t.E)//2,
                   "F#": (t.F+t.G)//2,
                   "G#": (t.G+t.A)//2,
                   "A#": (t.A+t.B)//2,
                   "C#_":(t.C_+t.D_)//2,
                   "D#_":(t.D_+t.E_)//2,
                   "F#_":(t.F_+t.G_)//2,
                   "G#_":(t.G_+t.A_)//2,
                   "A#_":(t.A_+t.B_)//2}
    winsound.Beep(sharp_notes[note],duration)

                   
####################################################

## main list which maps items to their functions ##
        
lst = [
       ["Mary Had A Little Lamb",mary],                   # 1
       ["Twinkle Twinkle Little Star",twinkle],           # 2
       ["Rock-a-Bye Baby",baby],                          # 3
       ["Happy Birthday to You",birthday],                # 4
       ["If You're Happy and You Know It",happy],         # 5
       ["We Wish You A Merry Christmas",christmas],       # 6
       ["Ode to Joy",joy],                                # 7
       ["Amazing Grace",grace],                           # 8
       ["Auld Lang Syne (New Year's Eve)",auld_lang_syne],# 9
       ["Imperial March",imperial]                        #10
       ]

####################################################

if __name__=="__main__": 
    main()


