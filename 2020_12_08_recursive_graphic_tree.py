import turtle

def tree(branch_len, t, pen_size):
    if branch_len > 5:
        if branch_len < 15:
            t.color("brown")
        else:
            t.color("green")
        
        t.pensize(pen_size)        
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t, pen_size-0.5)
        t.left(40)
        tree(branch_len - 10,t, pen_size-0.5)
        t.right(20)
        t.backward(branch_len)

def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t, 4)
    my_win.exitonclick()
main()

