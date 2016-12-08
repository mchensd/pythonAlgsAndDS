import turtle

def draw_triangle(length, t, color):  # draws a triangle, assumes that turtle is in the direction we want and returns the turtle in the same direction
    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.right(120)
    t.forward(length)
    t.right(120)
    t.forward(length)
    t.right(120)
    t.end_fill()




def sierpinski(turtle, order, length, color):
    colors = ['red', 'green', 'yellow']
    if order == 0:  # base case: draw a triangle. We assume that the turtle is in the direction we want.
        draw_triangle(length, turtle, color)
    else:
        draw_triangle(length, turtle, colors[order%3])  # draw the outline of the biggest order

        # Each of the sierpinski calls draws a sierpinski triangle of order(order-1) at 3 locations
        sierpinski(turtle, order-1, length/2, 'blue')
        turtle.forward(length/2)
        sierpinski(turtle, order-1, length/2, 'blue')
        turtle.right(60)
        turtle.forward(length/2)
        turtle.right(60)
        sierpinski(turtle, order-1, length/2, 'blue')
        turtle.forward(length/2)
        turtle.right(120)
        turtle.forward(length)
        turtle.right(120)



t = turtle.Turtle()
wn = turtle.Screen()
t.left(60)
sierpinski(t, 5, 400, 'blue')

wn.mainloop()