import random
from tkinter import *
from tkinter import messagebox

score = 0
run = True
root_h=700
root_w=600
# main loop
while run:
    root = Tk()
    root.geometry('700x600')
    root.title('HANG MAN')
    root.config(bg = '#E7FFFF')
    count = 0
    win_count = 0

    # choosing word
    index = random.randint(0,150)
    file = open('words.txt','r')
    l = file.readlines()
    selected_word = l[index].strip('\n')
    
    # creation of word dashes variables
    x = 250
    for i in range(0,len(selected_word)):
        x += 60
        exec('d{}=Label(root,text="_",bg="#E7FFFF",font=("arial",40))'.format(i))
        exec('d{}.place(x={},y={})'.format(i,x,350))
        
    
        
    # hangman images
    h123 = ['h1','h2','h3','h4','h5','h6','h7']
    for hangman in h123:
        exec('{}=PhotoImage(file="{}.png")'.format(hangman,hangman))
        
    #letters placement
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Create buttons for each alphabet
    botton_frame = Frame(root, bg='lightblue')
    botton_frame.pack(side=BOTTOM, fill=X)
    buttons = []
    for index, letter in enumerate(alphabets):
        button = Button(botton_frame,text=letter, command=lambda:check(letter,buttons[index]), width=2)
        row = index // 7  # Adjust the number of buttons per row
        column = index % 7  # Adjust the number of buttons per row
        button.grid(row=row, column=column, padx=5, pady=5)
        buttons.append(button)
    # button = [['b1','a',0,595],['b2','b',70,595],['b3','c',140,595],['b4','d',210,595],['b5','e',280,595],['b6','f',350,595],['b7','g',420,595],['b8','h',490,595],['b9','i',560,595],['b10','j',630,595],['b11','k',700,595],['b12','l',770,595],['b13','m',840,595],['b14','n',0,645],['b15','o',70,645],['b16','p',140,645],['b17','q',210,645],['b18','r',280,645],['b19','s',350,645],['b20','t',420,645],['b21','u',490,645],['b22','v',560,645],['b23','w',630,645],['b24','x',700,645],['b25','y',770,645],['b26','z',840,645]]

    '''for q1 in button:
        exec('{}=Button(root,bd=0,command=lambda:check("{}","{}"),bg="#E7FFFF",activebackground="#E7FFFF",font=10,image={})'.format(q1[0],q1[1],q1[0],q1[1]))
        exec('{}.place(x={},y={})'.format(q1[0],q1[2],q1[3]))'''
        
    #hangman placement
    picframe_x=300
    picframe_y=300
    x_center = (700 - picframe_x) // 2
    y_center = (600-picframe_y) // 2

    picframe = Frame(root, width=picframe_x, height=picframe_y, bg='lightblue')
    picframe.place(x=x_center, y=y_center)
    han = [['c1','h1'],['c2','h2'],['c3','h3'],['c4','h4'],['c5','h5'],['c6','h6'],['c7','h7']]
    for p1 in han:
        exec('{}=Label(picframe,bg="#E7FFFF",image={})'.format(p1[0],p1[1]))

    # placement of first hangman image
    c1.place(x = 200,y =100)
    
    # exit buton
    def close():
        global run
        answer = messagebox.askyesno('ALERT','YOU WANT TO EXIT THE GAME?')
        if answer == True:
            run = False
            root.destroy()
            
    
    ex = Button(root,bd = 0,text='EXIT',command = close,bg="#E7FFFF",activebackground = "#E7FFFF",font = 10)
    ex.place(x=10,y=10)
    s2 = 'SCORE:'+str(score)
    s1 = Label(root,text = s2,bg = "#E7FFFF",font = ("arial",25))
    s1.place(x = 10,y = 10)

    # button press check function
    def check(letter,button):
        global count,win_count,run,score
        #exec('{}.destroy()'.format(button))
        if letter in selected_word:
            for i in range(0,len(selected_word)):
                if selected_word[i] == letter:
                    win_count += 1
                    exec('d{}.config(text="{}")'.format(i,letter.upper()))
            if win_count == len(selected_word):
                score += 1
                answer = messagebox.askyesno('GAME OVER','YOU WON!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    root.destroy()   
                else:
                    run = False
                    root.destroy()
        else:
            count += 1
            exec('c{}.destroy()'.format(count))
            exec('c{}.place(x={},y={})'.format(count+1,300,-50))
            if count == 6:
                answer = messagebox.askyesno('GAME OVER','YOU LOST!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    score = 0
                    root.destroy()
                else:
                    run = False
                    root.destroy()         
    root.mainloop()
