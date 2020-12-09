import turtle

def tree(branch_len, t):
    if branch_len > 5:
        if branch_len > 50:
            t.pensize(7)
        elif branch_len > 20:
            t.pensize(2)
        elif branch_len > 10:    
            t.pensize(1)
            # t.color("yellow")
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t)
        t.left(40)
        tree(branch_len - 10,t)
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
    tree(75, t)
    my_win.exitonclick()
main()

