# Recursion
## Description
Some basic recursion functions implemented in Python, including drawing a spiral and a fractal tree using Python's turtle module. Includes a hanoi tower solver. For fun, a Towers of Hanoi game implemented in python is also included for you to play yourself.
## Content
* basic_recursion.py : include functiosn implemented using recursion
    * recursionSum(nums) : adding numbers in the nums list using recursion
    * recursionToBase(integer,base) : converting the positive integer to base up to 16
    * recursionReverse(for_str) : reverse the for_str (forward string)
    * testPalindrome(phase): test whether a word or a phase is a palindrome. Will remove all punctuations and spaces automatically
    * power(base, exp) : find the power of bsae to the exp using recursion
    * lucas_number(n) : print the n-th number of the lucas sequence
* draw_turtle.py
    * drawSquareSpiral(myTurtle, lineLen=100) : draws a square spiral using turtle module and recursion
    * drawTree(myTurtle, BrachLen=70) : draws a fractal tree using turtle module and recursion
* play_hanoi.py : contains a game of hanoi implemented in Python
    * TowersOfHanoi().play() : will start the game
* automatic_hanoi.py : gives the proper steps of moving the disk to solve the tower of Hanoi
    * move(disk, source, dest, spare) : disk is the number of disks to start with, give a name to source, dest and spare

## Testing
* basic_recursion.py
```python
# testing recursionSum
print(recursionSum([1,3,5,7,9])) # should get 25

# testing recursionToBase
print(recursionToBase(188,16)) # should get BC
print(recursionToBase(18,16.2)) # should raise ValueErorr, base 1 to 16, integers only
print(recursionToBase(1.2,16)) # should raise ValueError, value should be positive integer only

#testing recursionReverse
print(recursionReverse("abcde")) #should get edcba
print(recursionReverse("Hello World"))  # should get dlroW olleH

# testing removePunct
clean_phase = removePunct("Reviled did I live, said I, as evil I did deliver.")
print(clean_phase) # should get : revileddidilivesaidiasevilididdeliver

#testing testPalindrome
print(testPalindrome("kay")) # should get False
print(testPalindrome("Live not on evil")) # should get True
print(testPalindrome("Go hang a salami; I’m a lasagna hog.")) # should get True
print(testPalindrome("Reviled did I live, said I, as evil I did deliver")) # should get True

#testing our own power function
print(power(4,3)) # should be 64
print(power(2,0)) # should be 1
print(power(-2,2))  # should be 4

# testing lucas_number
print(lucas_number(9)) #should be 76
```
## To Run Program
* draw_turtle.py
```python
def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    # drawTree or drawSquareSpiral
    drawTree(myTurtle,70)
    myWin.exitonclick()
main()
# A screen will show up and automatically draw the tree or the spiral
```

* play_hanoi.py
```python
hanoi = TowersOfHanoi()
hanoi.play()
"""
Starting screen:

Towers of Hanoi: 

Imagine the towers are on its side with the bottom on the left and the top on the right

Tower 0:  [3, 2, 1]

Tower 1:  []

Tower 2:  []

What tower do you want to move from?

# input 0, 1, or 2
"""
```

* automatic_hanoi.py
```python
move(3,"A","B","C")

"""
Output:

moving disk from A to B
moving disk from A to C
moving disk from B to C
moving disk from A to B
moving disk from C to A
moving disk from C to B
moving disk from A to B
"""
```