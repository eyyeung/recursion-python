# from https://www.cs.cmu.edu/~cburch/survey/recurse/hanoiimpl.html

def move(disk, source, dest, spare):
    if disk>=1:
        move(disk-1,source,spare,dest)
        printMove(source,dest)
        move(disk-1,spare,dest,source)

def printMove(fp,tp):
    print("moving disk from",fp,"to",tp)

#move(3,"A","B","C")

"""
moving disk from A to B
moving disk from A to C
moving disk from B to C
moving disk from A to B
moving disk from C to A
moving disk from C to B
moving disk from A to B
"""