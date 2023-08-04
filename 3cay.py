import random
from tkinter import *
from tkinter.ttk import *

card_index=['2','3','4','5','6','7','8','9','A']
card_suit=['\u2660', '\u2663', '\u2665','\u2666' ]

#create Card
def showdeck():
    global deck
    deck=[]
    for i in list(card_index):
        for j in list(card_suit):
            deck.append(i+j)
    print(deck)

#shuff
def shuffle():
    global shuffledeck
    for x in range(len(deck)):
        card1=deck[x]
        r=random.randint(0, len(deck)-1)
        card2=deck[r]
        deck[x]=card2
        deck[r]=card1
    shuffledeck=deck
    for card in deck:
        print(card, end =' ')

#window
window = Tk()
window.geometry('500x500')
window.title("3caygame")
#welcome label
label_welcome=Label(window, text='Một cây làm chẳng nên non\n 3 cây chụm lại nên hòn núi cao').grid(column=0, row=0)
#nhap so nguoi choi
label_numberplayer=Label(window, text='Nhập số người chơi: ').grid(column=0, row=1)
numberplayer= Combobox(window, width= 3)
numberplayer['values']= [0,1,2,3,4,5,6,7,8,9,10]
numberplayer.current(0)
numberplayer.grid(column=1, row = 1)

#table label
label_table=Label(window, text='TABLE').grid(column=0, row=7)
def table():
    global player_number
    player_number= int(numberplayer.get())
    for x in range(0,10):
        TXTshowplayer=Label(window,text='                   ').grid(column=0, row=8+x)
    for x in range(0, player_number):
        TXTshowplayer=Label(window,text='Player '+str(x+1)).grid(column=0, row=8+x)

button_showplayer=Button(window, text="Show player", command=table).grid(column=2, row=1)
#show deck
button_showdeck=Button(window, text="Check deck", command=showdeck).grid(column=0, row=3)
#shuffle deck
button_shuffle=Button(window, text="Shuffle this deck!!!", command=shuffle).grid(column=1, row=3)
#deal card
def deal():
    global tablecard
    tablecard=[]
    card1=[]
    card2=[]
    card3=[]
    playerhand=['card1','card2','card3']
    for playerindex in range (0, player_number):
        card1.append(shuffledeck[playerindex])
    for playerindex in range (player_number, player_number*2):
        card2.append(shuffledeck[playerindex])
    for playerindex in range (player_number*2, player_number*3):
        card3.append(shuffledeck[playerindex])
    for playerindex in range (0,player_number):
        playerhand[0]=card1[playerindex]
        playerhand[1]=card2[playerindex]
        playerhand[2]=card3[playerindex]
        tablecard.append(playerhand)
        playerhand=['card1','card2','card3']
    #print(tablecard)
    for playerindex in range(0,10):
        TXTshowhand=Label(window,text='                   ').grid(column=1, row=8+playerindex)
    for playerindex in range(0, player_number):
        TXTshowhand=Label(window,text=str(tablecard[playerindex])).grid(column=1, row=8+playerindex)
    print(tablecard)
button_deal=Button(window, text="Deal card", command=deal).grid(column=2, row=3)

def tinhdiem():
    rank=[]
    playerpoint=[]  
    top=Toplevel(window)
    top.geometry("250x250")
    top.title('Kết quả đê!!!')
    #count point
    for i in range (0,player_number):
        rank.append(i+1)
        count=0
        for j in range(0,3):
            if str(tablecard[i][j])[0] == 'A':
                count+=1
            else:
                count+=int(str(tablecard[i][j])[0])
        if 10<count<=20:
            count=count-10
        if count > 20:
            count=count-20
        playerpoint.append(count)
    print(rank)
    print(playerpoint)
    for x in range (0,player_number-1):
        minindex=x
        for y in range (x+1,player_number):
            if playerpoint[x]>playerpoint[y]:
                minindex=y
                tg=playerpoint[y]
                playerpoint[y]=playerpoint[x]
                playerpoint[x]=tg
                tgrank=rank[y]
                rank[y]=rank[x]
                rank[x]=tgrank
            else:
                if playerpoint[x]==playerpoint[y]: #tire breaker
                    suitlist1= [card_suit.index((tablecard[x][0])[1]),card_suit.index((tablecard[x][1])[1]),card_suit.index((tablecard[x][2])[1])]
                    suitlist2= [card_suit.index((tablecard[y][0])[1]),card_suit.index((tablecard[y][1])[1]),card_suit.index((tablecard[y][2])[1])]
                    print(suitlist1)
                    print(suitlist2)
                    maxsuit1= max(suitlist1)
                    maxsuit2= max(suitlist2)
                    print(maxsuit1)
                    print(maxsuit2)
                    if maxsuit1>maxsuit2:   #so sánh chất trong bài
                        minindex=y
                        tg=playerpoint[y]
                        playerpoint[y]=playerpoint[x]
                        playerpoint[x]=tg
                        tgrank=rank[y]
                        rank[y]=rank[x]
                        rank[x]=tgrank               
                    else:
                        if maxsuit1==maxsuit2: #nếu cùng có suit
                        #Kiểm tra index lớn nhất của suit trong hand
                            ordermaxsuit1=[]
                            ordermaxsuit2=[]
                            indexsuitlist1=[]
                            indexsuitlist2=[]
                            for z in range (0,3):
                                if maxsuit1 == card_suit.index((tablecard[x][z])[1]):
                                    ordermaxsuit1.append(z)
                                if maxsuit2 == card_suit.index((tablecard[y][z])[1]):
                                    ordermaxsuit2.append(z)
                            for t1 in range (0,len(ordermaxsuit1)):
                                indexsuitlist1.append(tablecard[x][ordermaxsuit1[t1]][0])
                            for t2 in range (0,len(ordermaxsuit2)):
                                indexsuitlist2.append(tablecard[x][ordermaxsuit1[t2]][0])
                            maxindexsuit1=max(indexsuitlist1)
                            maxindexsuit2=max(indexsuitlist2)
                            #So sánh index của suit của 2 hand
                            if maxindexsuit1>maxindexsuit2:
                                minindex=y
                                tg=playerpoint[y]
                                playerpoint[y]=playerpoint[x]
                                playerpoint[x]=tg
                                tgrank=rank[y]
                                rank[y]=rank[x]
                                rank[x]=tgrank
    print("kiểm tra điểm và rank")
    print(playerpoint)
    print(rank)
    playerpoint.reverse()
    rank.reverse()
    print("kiểm tra rank đảo ngược")
    print(rank)
    print(playerpoint)
    #print on Tkinter popup
    for playerindex in range(0,player_number):
        lbltop=Label(top, text=str("top "+str(playerindex+1))).grid(column=0,row=playerindex)
        TXTshowplayer=Label(top,text="Player "+str(rank[playerindex])).grid(column=2, row=playerindex)
        TXTshowhand=Label(top,text=str(tablecard[int(rank[playerindex])-1])).grid(column=4, row=playerindex)
        TXTshowpoint=Label(top,text=str(playerpoint[playerindex])).grid(column=6, row=playerindex)
    top.mainloop()

button_count=Button(window, text="Result", command=tinhdiem).grid(column=2, row=18)
window.mainloop()