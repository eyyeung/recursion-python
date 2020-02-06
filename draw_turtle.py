import turtle
from random import randint

# 100 is a good value for the lineLen
def drawSquareSpiral (myTurtle, lineLen=100):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSquareSpiral(myTurtle, lineLen-5)

# 70 is a good value for the branchLen with the setting as is
def drawBranch(myTurtle,branchLen=70):
    if branchLen > 5:
        # As the branchLen gets smaller, the pen size gets smaller
        myTurtle.pensize(branchLen/10)
        myTurtle.forward(branchLen)
        # to introduce some randomness and asymmetry, use randint to control the angle
        angle = randint(20,40)
        myTurtle.right(angle)
        drawBranch(myTurtle,branchLen-15)
        myTurtle.left(2*angle)
        drawBranch(myTurtle,branchLen-15)
        myTurtle.right(angle)
        myTurtle.backward(branchLen)

# Call this to draw the tree
def drawTree(myTurtle,branchLen=70):
    # These steps are to orient the turtle to draw the tree correctly to be rightside up
    myTurtle.left(90)
    myTurtle.up()
    myTurtle.backward(100)
    myTurtle.down()
    myTurtle.color("brown")
    drawBranch(myTurtle,branchLen)


def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    # can drawTree or drawSquareSpiral
    drawTree(myTurtle,70)
    myWin.exitonclick()

main()