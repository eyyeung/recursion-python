import os

# Tower of hanoi - a set of disks from big to small, want to have them stacked in order in another pole other than the beginning pole 

class TowersOfHanoi:
    def __init__(self):
        self.stacks = [[3,2,1],[],[]]

    def play(self):
        self.display()

        while not self.won():
            print("What tower do you want to move from?")
            from_tower = int(input().strip())

            print("What tower do you want to move to?")
            to_tower = int(input().strip())

            if self.valid_move(from_tower,to_tower):
                self.move(from_tower, to_tower)
                self.display()
            else:
                self.display()
                print("Invalid move. Try again.")

        print("Congrats! You win!")
    
    def won(self):
        if len(self.stacks[0])==0 and (len(self.stacks[1])==0 or len(self.stacks[2])==0):
            return True
        else:
            return False
    
    def move(self,from_tower,to_tower):
        self.stacks[to_tower].append(self.stacks[from_tower].pop())

    def valid_move(self,from_tower,to_tower):
        if from_tower not in range(0,3) or to_tower not in range(0,3):
            return False
        elif len(self.stacks[from_tower])==0:
            return False
        elif len(self.stacks[to_tower])==0 or (self.stacks[from_tower][-1] < self.stacks[to_tower][-1]):
            return True

    def display(self):
        os.system('cls' if os.name=='nt' else 'clear')
        self.render()
    
    # imagine a tower laying on its side with its bottom on the left and the top on the right
    def render(self):
        print("Towers of Hanoi:",'\n')
        print("Imagine the towers are on its side with the bottom on the left and the top on the right",'\n')
        print("Tower 0: ", self.stacks[0],'\n')
        print("Tower 1: ", self.stacks[1],'\n')
        print("Tower 2: ", self.stacks[2],'\n')
        

hanoi = TowersOfHanoi()
hanoi.play()