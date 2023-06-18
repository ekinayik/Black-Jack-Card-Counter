from tkinter import *
from tkinter import messagebox
#Backend
deeckcount=1
cardcount=52
counter=0
test=True
# Cardname | Point | Number of Cards | Possibility
cards=[
    [0,2,2,deeckcount*4,4/52],       #0
    [1,3,3,deeckcount*4,4/52],       #1
    [2,4,4,deeckcount*4,4/52],       #2
    [3,5,5,deeckcount*4,4/52],       #3
    [4,6,6,deeckcount*4,4/52],       #4
    [5,7,7,deeckcount*4,4/52],       #5
    [6,8,8,deeckcount*4,4/52],       #6
    [7,9,9,deeckcount*4,4/52],       #7
    [8,10,10,deeckcount*4,4/52],     #8
    [9,'J',10,deeckcount*4,4/52],    #9
    [10,'Q',10,deeckcount*4,4/52],    #10
    [11,'K',10,deeckcount*4,4/52],    #11
    [12,'A',11,deeckcount*4,4/52]     #12
    ]
def Hit(row):
    global cardcount
    cardcount=cardcount-1
    CardCount(row)
    Dec(row)
    print('Card Counter : ' + str(counter))
    updatetexts()
def Stand():
    return
def Dec(row):
    global cards
    i=0
    cards[row][3]=cards[row][3]-1
    while(i<13):
        cards[i][4]=cards[i][3]/((deeckcount-1)*52+cardcount)
        i=i+1
#Done
def updatetexts():
    probtext2.config(text = str(cards[0][1]) + '     |     %' + str(cards[0][4]*100))
    probtext3.config(text = str(cards[1][1]) + '     |     %' + str(cards[1][4]*100))
    probtext4.config(text = str(cards[2][1]) + '     |     %' + str(cards[2][4]*100))
    probtext5.config(text = str(cards[3][1]) + '     |     %' + str(cards[3][4]*100))
    probtext6.config(text = str(cards[4][1]) + '     |     %' + str(cards[4][4]*100))
    probtext7.config(text = str(cards[5][1]) + '     |     %' + str(cards[5][4]*100))
    probtext8.config(text = str(cards[6][1]) + '     |     %' + str(cards[6][4]*100))
    probtext9.config(text = str(cards[7][1]) + '     |     %' + str(cards[7][4]*100))
    probtext10.config(text = str(cards[8][1]) + '     |     %' + str(cards[8][4]*100))
    probtextJ.config(text = str(cards[9][1]) + '     |     %' + str(cards[9][4]*100))
    probtextQ.config(text = str(cards[10][1]) + '     |     %' + str(cards[10][4]*100))
    probtextK.config(text = str(cards[11][1]) + '     |     %' + str(cards[11][4]*100))
    probtextA.config(text = str(cards[12][1]) + '     |     %' + str(cards[12][4]*100))
def Reset():
    global counter
    counter=0
    global cards
    cards=[
        [0,2,2,deeckcount*4,4/52],       #0
        [1,3,3,deeckcount*4,4/52],       #1
        [2,4,4,deeckcount*4,4/52],       #2
        [3,5,5,deeckcount*4,4/52],       #3
        [4,6,6,deeckcount*4,4/52],       #4
        [5,7,7,deeckcount*4,4/52],       #5
        [6,8,8,deeckcount*4,4/52],       #6
        [7,9,9,deeckcount*4,4/52],       #7
        [8,10,10,deeckcount*4,4/52],     #8
        [9,'J',10,deeckcount*4,4/52],    #9
        [10,'Q',10,deeckcount*4,4/52],    #10
        [11,'K',10,deeckcount*4,4/52],    #11
        [12,'A',11,deeckcount*4,4/52]     #12
        ]
#Working on
def CardCount(row):
    global counter
    if(row<5):
        counter=counter+1
    elif(row>7):
        counter=counter-1
def HardTotals(tot):
    if(tot>=17):
        return
    elif(tot==16):
        return
    elif(tot==15):
        return
    elif(tot==14):
        return
    elif(tot==13):
        return
    elif(tot==12):
        return
    elif(tot==11):
        return
    elif(tot==10):
        return
    elif(tot==9):
        return
    elif(tot<=8):
        return
def SoftTotals(tot):
    if(tot==20):
        return
    elif(tot==19):
        return
    elif(tot==18):
        return
    elif(tot==17):
        return
    elif(tot==16):
        return
    elif(tot==15):
        return
    elif(tot==14):
        return
    elif(tot==13):
        return
def ProbOfAllCards():
    global cards
    for row in cards:
        print(str(row[1]) + '     |     %' + str(row[4]*100))
def ProbCalc():
    global cards
    totprob=0
    for row in cards:
        if(row[2]>=10):
            totprob+=row[4]*100
    print('Lose Prob is: '+str(totprob))
def HitProbCalc():
    global cards
    totalprob=0
    for row in cards:
        if(row[3]>=6 and row[2]!='A'):
            totalprob+=row[4]*100
    print('Lose Prob is:' + str(totalprob))

#Interface
master = Tk()
master.geometry("800x800")
fonttype=('Times',20,'bold')
frame=Frame(master)
frame.place(relx=0.1,rely=0.05)
textframe=Frame(master)
textframe.place(relx=0.02,rely=0.3)
#Card Buttons
card2=Button(frame,text=cards[0][1],font=fonttype,command= lambda:Hit(cards[0][0]))
card2.grid(row=0,column=0,padx=15,pady=15)
card3=Button(frame,text=cards[1][1],font=fonttype,command= lambda:Hit(cards[1][0]))
card3.grid(row=0,column=1,padx=15,pady=15)
card4=Button(frame,text=cards[2][1],font=fonttype,command= lambda:Hit(cards[2][0]))
card4.grid(row=0,column=2,padx=15,pady=15)
card5=Button(frame,text=cards[3][1],font=fonttype,command= lambda:Hit(cards[3][0]))
card5.grid(row=0,column=3,padx=15,pady=15)
card6=Button(frame,text=cards[4][1],font=fonttype,command= lambda:Hit(cards[4][0]))
card6.grid(row=0,column=4,padx=15,pady=15)
card7=Button(frame,text=cards[5][1],font=fonttype,command= lambda:Hit(cards[5][0]))
card7.grid(row=0,column=5,padx=15,pady=15)
card8=Button(frame,text=cards[6][1],font=fonttype,command= lambda:Hit(cards[6][0]))
card8.grid(row=0,column=6,padx=15,pady=15)
card9=Button(frame,text=cards[7][1],font=fonttype,command= lambda:Hit(cards[7][0]))
card9.grid(row=1,column=0,padx=15,pady=15)
card10=Button(frame,text=cards[8][1],font=fonttype,command= lambda:Hit(cards[8][0]))
card10.grid(row=1,column=1,padx=15,pady=15)
cardJ=Button(frame,text=cards[9][1],font=fonttype,command= lambda:Hit(cards[9][0]))
cardJ.grid(row=1,column=2,padx=15,pady=15)
cardQ=Button(frame,text=cards[10][1],font=fonttype,command= lambda:Hit(cards[10][0]))
cardQ.grid(row=1,column=3,padx=15,pady=15)
cardK=Button(frame,text=cards[11][1],font=fonttype,command= lambda:Hit(cards[11][0]))
cardK.grid(row=1,column=4,padx=15,pady=15)
cardA=Button(frame,text=cards[12][1],font=fonttype,command= lambda:Hit(cards[12][0]))
cardA.grid(row=1,column=5,padx=15,pady=15)
# Create text widget and specify size. 
# Create label
probtext = Label(textframe, text = "Probability Of Next Card")
probtext.config(font =("Courier", 14))
probtext.grid()
probtext2 = Label(textframe, text = str(cards[0][1]) + '     |     %' + str(cards[0][4]*100))
probtext2.config(font =("Courier", 14))
probtext2.grid()
probtext3 = Label(textframe, text = str(cards[1][1]) + '     |     %' + str(cards[1][4]*100))
probtext3.config(font =("Courier", 14))
probtext3.grid()
probtext4 = Label(textframe, text = str(cards[2][1]) + '     |     %' + str(cards[2][4]*100))
probtext4.config(font =("Courier", 14))
probtext4.grid()
probtext5 = Label(textframe, text = str(cards[3][1]) + '     |     %' + str(cards[3][4]*100))
probtext5.config(font =("Courier", 14))
probtext5.grid()
probtext6 = Label(textframe, text = str(cards[4][1]) + '     |     %' + str(cards[4][4]*100))
probtext6.config(font =("Courier", 14))
probtext6.grid()
probtext7 = Label(textframe, text = str(cards[5][1]) + '     |     %' + str(cards[5][4]*100))
probtext7.config(font =("Courier", 14))
probtext7.grid()
probtext8 = Label(textframe, text = str(cards[6][1]) + '     |     %' + str(cards[6][4]*100))
probtext8.config(font =("Courier", 14))
probtext8.grid()
probtext9 = Label(textframe, text = str(cards[7][1]) + '     |     %' + str(cards[7][4]*100))
probtext9.config(font =("Courier", 14))
probtext9.grid()
probtext10 = Label(textframe, text = str(cards[8][1]) + '     |     %' + str(cards[8][4]*100))
probtext10.config(font =("Courier", 14))
probtext10.grid()
probtextJ = Label(textframe, text = str(cards[9][1]) + '     |     %' + str(cards[9][4]*100))
probtextJ.config(font =("Courier", 14))
probtextJ.grid()
probtextQ = Label(textframe, text = str(cards[10][1]) + '     |     %' + str(cards[10][4]*100))
probtextQ.config(font =("Courier", 14))
probtextQ.grid()
probtextK= Label(textframe, text = str(cards[11][1]) + '     |     %' + str(cards[11][4]*100))
probtextK.config(font =("Courier", 14))
probtextK.grid()
probtextA = Label(textframe, text = str(cards[12][1]) + '     |     %' + str(cards[12][4]*100))
probtextA.config(font =("Courier", 14))
probtextA.grid()
master.mainloop()
