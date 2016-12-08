import turtle

def koch(order, length, t):
    if order == 1:
        for i in [60, -120, 60]:
            t.forward(length/3)
            t.left(i)
        t.forward(length/3)

    else:
        for i in [60,-120,60]:
            koch(order-1, length/3, t)
            t.left(i)
        koch(order-1, length/3, t)

bess = turtle.Turtle()
tess = turtle.Turtle()
tess.penup()
tess.goto(-300, -300)
tess.pendown()
wn = turtle.Screen()

koch(1, 100, bess)
koch(3, 300, bess)
koch(5, 900, tess)


wn.mainloop()