import random
from tkinter import *
from tkinter import messagebox

score = 0
run = True

# main loop
while run:
    root = Tk()
    #root.geometry('500x500')
    root.title('HANG MAN')
    root.config(bg = '#E7FFFF')
    count = 0
    win_count = 0 
    
 # choosing word
    file = open('words.txt','r')
    l = file.readlines()
    selected_word = random.choice(l)
    
    # creation of word dashes variables
    x = 250
    for i in range(0,len(selected_word)):
        x += 60
        exec('d{}=Label(root,text="_",bg="#E7FFFF",font=("arial",40))'.format(i))
        exec('d{}.place(x={},y={})'.format(i,x,450))
        
    #letters icon
    for i in range(ord('A'), ord('Z')+1):
        letter = chr(i)
        #button = tk.Button(root, text=letter, command=lambda l=letter: button_click(l))
        exec('button_{}= Button(root,bd=0,text=letter,command=lambda:check("button_{}","{}"),bg="#E7FFFF",activebackground="#E7FFFF",font=10)'.format(chr(i),chr(i),chr(i),chr(i),))
        exec('button_{}.pack()'.format(chr(i)))
    

        
    '''al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for let in al:
        exec('{}=PhotoImage(file="{}.png")'.format(let,let))'''
    
     #letters placement
    '''
    for q1 in button:
        exec('{}=Button(root,bd=0,command=lambda:check("{}","{}"),bg="#E7FFFF",activebackground="#E7FFFF",font=10,image={})'.format(q1[0],q1[1],q1[0],q1[1]))
        exec('{}.place(x={},y={})'.format(q1[0],q1[2],q1[3]))'''
        
        
    # hangman images
    h123 = ['h1','h2','h3','h4','h5','h6','h7']
    for hangman in h123:
        exec('{}=PhotoImage(file="{}.png")'.format(hangman,hangman))
        
   
    #hangman placement
    han = [['c1','h1'],['c2','h2'],['c3','h3'],['c4','h4'],['c5','h5'],['c6','h6'],['c7','h7']]
    for p1 in han:
        exec('{}=Label(root,bg="#E7FFFF",image={})'.format(p1[0],p1[1]))

    # placement of first hangman image
    c1.place(x = 300,y =- 50)
    
    # exit buton
    def close():
        global run
        answer = messagebox.askyesno('ALERT','YOU WANT TO EXIT THE GAME?')
        if answer == True:
            run = False
            root.destroy()
            
    e1 = PhotoImage(file = 'exit.png')
    ex = Button(root,bd = 0,command = close,bg="#E7FFFF",activebackground = "#E7FFFF",font = 10,image = e1)
    ex.place(x=770,y=10)
    s2 = 'SCORE:'+str(score)
    s1 = Label(root,text = s2,bg = "#E7FFFF",font = ("arial",25))
    s1.place(x = 10,y = 10)

    # button press check function
    def check(letter,button):
        global count,win_count,run,score
        exec('{}.destroy()'.format(button))
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

