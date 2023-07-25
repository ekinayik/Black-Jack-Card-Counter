from tkinter import *
from tkinter import messagebox
#Backend
lastoperation=0
deckcount=6
cardcount=52
counter=0
halvescount=0
test=True
# Cardname | Point | Number of Cards | Possibility
cards=[
    [0,2,2,deckcount*4,4/52],       #0
    [1,3,3,deckcount*4,4/52],       #1
    [2,4,4,deckcount*4,4/52],       #2
    [3,5,5,deckcount*4,4/52],       #3
    [4,6,6,deckcount*4,4/52],       #4
    [5,7,7,deckcount*4,4/52],       #5
    [6,8,8,deckcount*4,4/52],       #6
    [7,9,9,deckcount*4,4/52],       #7
    [8,10,10,deckcount*4,4/52],     #8
    [9,'J',10,deckcount*4,4/52],    #9
    [10,'Q',10,deckcount*4,4/52],    #10
    [11,'K',10,deckcount*4,4/52],    #11
    [12,'A',11,deckcount*4,4/52]     #12
    ]
def Hit(row):
    CardCount(row)
    HalvesCount(row)
    Dec(row)
    print('Card Counter : ' + str(counter))
    updatetexts()
def Stand():
    return
def Dec(row):
    global cards    
    global cardcount
    if(cards[row][3]!=0):
        cardcount=cardcount-1
        i=0
        cards[row][3]=cards[row][3]-1
        while(i<13):
            cards[i][4]=cards[i][3]/((deckcount-1)*52+cardcount)
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
    cardcountertext.config(text='Card Counter : ' + str(counter))
    if(deckcount==0):
        truecardcountertext.config(text='True Counter : ' + str(counter))
        halvescardcountertext.config(text='Halves Counter : ' + str(halvescount))
    else:
        truecardcountertext.config(text='True Counter : ' + str(counter/deckcount))
        halvescardcountertext.config(text='Halves Counter : ' + str(halvescount/deckcount))
    proboften.config(text='Prob Of Ten = '+ str((cards[8][4]+cards[9][4]+cards[10][4]+cards[11][4])*100))
def Reset():
    global counter
    counter=0
    global deckcount
    deckcount=6
    global cardcount
    cardcount=52
    global halvescount
    halvescount=0
    global cards
    cards=[
        [0,2,2,deckcount*4,4/52],       #0
        [1,3,3,deckcount*4,4/52],       #1
        [2,4,4,deckcount*4,4/52],       #2
        [3,5,5,deckcount*4,4/52],       #3
        [4,6,6,deckcount*4,4/52],       #4
        [5,7,7,deckcount*4,4/52],       #5
        [6,8,8,deckcount*4,4/52],       #6
        [7,9,9,deckcount*4,4/52],       #7
        [8,10,10,deckcount*4,4/52],     #8
        [9,'J',10,deckcount*4,4/52],    #9
        [10,'Q',10,deckcount*4,4/52],    #10
        [11,'K',10,deckcount*4,4/52],    #11
        [12,'A',11,deckcount*4,4/52]     #12
        ]
    updatetexts()
def CardCount(row):
    global counter
    if(cards[row][3]!=0):
        if(row<5):
            counter=counter+1
        elif(row>7):
            counter=counter-1
def HalvesCount(row):
    global halvescount
    if(cards[row][3]!=0):
        if(row==0 or halvescount==5):
            halvescount=halvescount+0.5
        elif(row==1 or row ==2 or row ==4):
            halvescount=halvescount+1
        elif(row==3):
            halvescount=halvescount+1.5
        elif(row==7):
            halvescount=halvescount-0.5
        elif(row>7):
            halvescount=halvescount-1
#working on
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
framecardsbt=Frame(master)
framecardsbt.place(relx=0.1,rely=0.05)
probofcardsframe=Frame(master)
probofcardsframe.place(relx=0.02,rely=0.3)
framecardcounter=Frame(master)
framecardcounter.place(relx=0.5,rely=0.3)
resetbt=Button(text='Reset',font=fonttype,command=lambda:Reset())
resetbt.grid()
resetbt.place(relx=0.8,rely=0.8)
#Card Buttons
card2=Button(framecardsbt,text=cards[0][1],font=fonttype,command= lambda:Hit(cards[0][0]))
card2.grid(row=0,column=0,padx=15,pady=15)
card3=Button(framecardsbt,text=cards[1][1],font=fonttype,command= lambda:Hit(cards[1][0]))
card3.grid(row=0,column=1,padx=15,pady=15)
card4=Button(framecardsbt,text=cards[2][1],font=fonttype,command= lambda:Hit(cards[2][0]))
card4.grid(row=0,column=2,padx=15,pady=15)
card5=Button(framecardsbt,text=cards[3][1],font=fonttype,command= lambda:Hit(cards[3][0]))
card5.grid(row=0,column=3,padx=15,pady=15)
card6=Button(framecardsbt,text=cards[4][1],font=fonttype,command= lambda:Hit(cards[4][0]))
card6.grid(row=0,column=4,padx=15,pady=15)
card7=Button(framecardsbt,text=cards[5][1],font=fonttype,command= lambda:Hit(cards[5][0]))
card7.grid(row=0,column=5,padx=15,pady=15)
card8=Button(framecardsbt,text=cards[6][1],font=fonttype,command= lambda:Hit(cards[6][0]))
card8.grid(row=0,column=6,padx=15,pady=15)
card9=Button(framecardsbt,text=cards[7][1],font=fonttype,command= lambda:Hit(cards[7][0]))
card9.grid(row=1,column=0,padx=15,pady=15)
card10=Button(framecardsbt,text=cards[8][1],font=fonttype,command= lambda:Hit(cards[8][0]))
card10.grid(row=1,column=1,padx=15,pady=15)
cardJ=Button(framecardsbt,text=cards[9][1],font=fonttype,command= lambda:Hit(cards[9][0]))
cardJ.grid(row=1,column=2,padx=15,pady=15)
cardQ=Button(framecardsbt,text=cards[10][1],font=fonttype,command= lambda:Hit(cards[10][0]))
cardQ.grid(row=1,column=3,padx=15,pady=15)
cardK=Button(framecardsbt,text=cards[11][1],font=fonttype,command= lambda:Hit(cards[11][0]))
cardK.grid(row=1,column=4,padx=15,pady=15)
cardA=Button(framecardsbt,text=cards[12][1],font=fonttype,command= lambda:Hit(cards[12][0]))
cardA.grid(row=1,column=5,padx=15,pady=15)
# Create text widget and specify size. 
# Create label
cardcountertext=Label(framecardcounter,text='Card Counter : ' + str(counter))
cardcountertext.config(font=("Courier",14))
cardcountertext.grid()
truecardcountertext=Label(framecardcounter,text='True Count : ' + str(counter/deckcount))
truecardcountertext.config(font=("Courier",14))
truecardcountertext.grid()
halvescardcountertext=Label(framecardcounter,text='Halves Count : ' + str(halvescount/deckcount))
halvescardcountertext.config(font=("Courier",14))
halvescardcountertext.grid()
proboften=Label(framecardcounter,text='Prob Of Ten = '+ str((cards[8][4]+cards[9][4]+cards[10][4]+cards[11][4])*100))
proboften.config(font=("Courier",14))
proboften.grid()
probtext = Label(probofcardsframe, text = "Probability Of Next Card")
probtext.config(font =("Courier", 14))
probtext.grid()
probtext2 = Label(probofcardsframe, text = str(cards[0][1]) + '     |     %' + str(cards[0][4]*100))
probtext2.config(font =("Courier", 14))
probtext2.grid()
probtext3 = Label(probofcardsframe, text = str(cards[1][1]) + '     |     %' + str(cards[1][4]*100))
probtext3.config(font =("Courier", 14))
probtext3.grid()
probtext4 = Label(probofcardsframe, text = str(cards[2][1]) + '     |     %' + str(cards[2][4]*100))
probtext4.config(font =("Courier", 14))
probtext4.grid()
probtext5 = Label(probofcardsframe, text = str(cards[3][1]) + '     |     %' + str(cards[3][4]*100))
probtext5.config(font =("Courier", 14))
probtext5.grid()
probtext6 = Label(probofcardsframe, text = str(cards[4][1]) + '     |     %' + str(cards[4][4]*100))
probtext6.config(font =("Courier", 14))
probtext6.grid()
probtext7 = Label(probofcardsframe, text = str(cards[5][1]) + '     |     %' + str(cards[5][4]*100))
probtext7.config(font =("Courier", 14))
probtext7.grid()
probtext8 = Label(probofcardsframe, text = str(cards[6][1]) + '     |     %' + str(cards[6][4]*100))
probtext8.config(font =("Courier", 14))
probtext8.grid()
probtext9 = Label(probofcardsframe, text = str(cards[7][1]) + '     |     %' + str(cards[7][4]*100))
probtext9.config(font =("Courier", 14))
probtext9.grid()
probtext10 = Label(probofcardsframe, text = str(cards[8][1]) + '     |     %' + str(cards[8][4]*100))
probtext10.config(font =("Courier", 14))
probtext10.grid()
probtextJ = Label(probofcardsframe, text = str(cards[9][1]) + '     |     %' + str(cards[9][4]*100))
probtextJ.config(font =("Courier", 14))
probtextJ.grid()
probtextQ = Label(probofcardsframe, text = str(cards[10][1]) + '     |     %' + str(cards[10][4]*100))
probtextQ.config(font =("Courier", 14))
probtextQ.grid()
probtextK= Label(probofcardsframe, text = str(cards[11][1]) + '     |     %' + str(cards[11][4]*100))
probtextK.config(font =("Courier", 14))
probtextK.grid()
probtextA = Label(probofcardsframe, text = str(cards[12][1]) + '     |     %' + str(cards[12][4]*100))
probtextA.config(font =("Courier", 14))
probtextA.grid()
master.mainloop()