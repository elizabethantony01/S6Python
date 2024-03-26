import turtle as t

def draw_star(n,c):
    t.pencolor(c)
 
    for j in range(n):
        for i in range(5):
            t.forward(20)
            t.right(144)
        t.penup()
        t.forward(20)
        t.pendown()

    
    t.done()
n=int(input("Enter the number of stars you want to draw:"))
c=input("Enter the colour of stars:")
draw_star(n,c)
