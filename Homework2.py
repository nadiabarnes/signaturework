import random
import sys
from math import sqrt, ceil
from collections import defaultdict
import search
from search import Node
class ToggleIt(search.Problem):
    """
    A class to represent a ToggleIt problem. Key parameters to init are:
     SIZE: the number of rows and columns in the grid.
     STATE: we represent a state as a string of size**2 characters
      where each character is a 0 or a 1.  The first character
      holds the value of the upper left cell of the grid, the second
      character the cell to its right, etc.
     INITIAL: an arbitrary start state.
     GOAL: a state with all bits equal to 0
    """

    def __init__(self, size=3, initial=None, goal=None, current=None):
        self.size = size
        self.goal = goal or ''.join('0' for _ in range(size**2))
        self.initial = initial if initial else ''.join(random.choice(['0','1']) for _ in range(size**2))
        self.current = self.initial #variable I added for visualizing testing
        pass
    
    def showBoard(self):
        """This prints the current state of the board in a grid format
        Adjusts based on the size of the board"""
        res = ""
        counter = 0
        for i in range(self.size*self.size): #for every number in the current state
            res = res + str(self.current[counter]) + " " #apend the num to the string
            counter = counter+1
            if counter % self.size ==0: # test if it's the end of the line
                res = res + "\n"
        return res

    def __repr__(self):
        """ Returns a string representing the class """
        #Changed this as instructed during office hours
        return "ToggleIt({},{},{})".format(self.size,self.initial,self.goal)

    def goal_test(self, state):
        """ Returns true if state is a goal state.
        does the current state match the goal state? """
        if self.goal == state: #simple true/false test
            return True
        else: return False

    def h(self, node):
        """ Estimate of cost of shortest path from node to a goal """
        # No need to change this, we won't instaniate the base ToggleIt directly
        return 1
    
    def actions(self, state):
        """ generates legal actions for state."""
        #an "action" is a integer within the range of the board which is a node that can be changed.
        #so a 3x3 board has 9 potential actions, each action being an index you can select to change
        temp = 0
        res=[]
        for char in state:
            res.append(temp) #make a list where each index in the list is an action
            temp = temp + 1
        return res

    def result(self, state, action):
        """ Returns the successor of state after doing action """
        stateLis = [i for i in state] #turn the state into a list for usability
        if action < len(state) and action >= 0: #if the action is valid
            #change the value of actual square
            stateLis[action] = self.switch(stateLis[action])
            #the four if statements below test if the selected action/index is on the edge of the board
            #test for the edges, if not on that edge then switch it's neighbor
            if action >= self.size:
                #not top edge
                stateLis[action-self.size] = self.switch(stateLis[action-self.size])
            if action < (self.size*self.size)-self.size:
                #not bottom edge
                stateLis[action+self.size] = self.switch(stateLis[action+self.size])
            if action % self.size != 0:
                #not left edge
                stateLis[action-1] = self.switch(stateLis[action-1])
            if action % self.size != (self.size-1):
                #not right edge
                stateLis[action+1] = self.switch(stateLis[action+1])
        resStr = "" #turn the list back into a string to return
        for i in stateLis:
            resStr += i
        self.current = resStr #update self.current for testing
        return resStr        

    def path_cost(self, c, state1, action, state2):
        """ Cost of path from start node to state1 assuming cost c to
        get to state1 and doing action to get to state2 """
        #cost of 1 always, so just add 1 to c
        return c + 1

    def switch(self, num=str):
        #helper method we made to turn 1s into 0s and 0s into 1s
        if int(num) == 0:
            return "1"
        else: return "0"


class ToggleIt_optimal(ToggleIt):
    name = "optimal"
    def h(self, node=Node):
        """ Returns an admissable estimate of cost of shortest path
        from node to a goal """
        currOnes = node.state.count("1") #count the 1s on the current board
        movePotential = 5.0 #one action could erase 5 1s
        if self.size < 4:
            movePotential = self.size + 1 #if the board is smaller, that potential decreases
        return ceil(currOnes/movePotential) #divide the 1s by the move potential


class ToggleIt_suboptimal(ToggleIt):
    name = "Sub-optimal"
    def h(self, node=Node):
        """ a suboptimal, non-admissable estimate of cost of
        shortest path from node to a goal """
        currOnes = node.state.count("1") #count the 1s on the board
        return currOnes #thats the suboptimal heuristic

#testing section
#--------------------
    
# testBoard = ToggleIt_optimal(2)
# print(testBoard.showBoard())
# print("inital repr:")
# print(testBoard.initial)
# print("goal_test(initial):")
# print(testBoard.goal_test(testBoard.initial))
# print("actions(initial)")
# print(testBoard.actions(testBoard.initial))
# print("result(initial, index)")
# testBoard.result(testBoard.initial, 3)
# print(testBoard.showBoard())
# print("h(initial)")
# print(testBoard.h(Node(testBoard.initial)))
