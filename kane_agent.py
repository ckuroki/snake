import time
from pynput.keyboard import Key, Controller

# globals
keyboard = Controller()
xfruit = 10
yfruit = 10
xhead = 8
yhead = 5 

# Base class for Behavior Tree nodes
class Node:
    def run(self):
        raise NotImplementedError("This method should be overridden.")

# Composite nodes
class Selector(Node):
    """Runs each child until one succeeds."""
    def __init__(self, children):
        self.children = children

    def run(self):
        for child in self.children:
            if child.run():
                return True
        return False

class Sequence(Node):
    """Runs each child until one fails."""
    def __init__(self, children):
        self.children = children

    def run(self):
        for child in self.children:
            if not child.run():
                return False
        return True

# Leaf nodes
class ActionNode(Node):
    """Executes an action."""
    def __init__(self, action):
        self.action = action

    def run(self):
        return self.action()

class ConditionNode(Node):
    """Checks a condition."""
    def __init__(self, condition):
        self.condition = condition

    def run(self):
        return self.condition()

# conditions
def fruit_to_the_right():
    if xfruit > xhead:
        return True
    return False

def fruit_to_the_left():
    if xfruit < xhead:
        return True
    return False

def fruit_equal():
    if xfruit == xhead:
        return True
    return False

# actions
def move_right():
    print("Move to the right")
    return True

def move_left():
    print("Move to the left")
    return True

def not_move():
    print("not moving")
    return True

# Building the Behavior Tree
def build_behavior_tree():
    # Leaf nodes
    condition_fruit_to_the_right = ConditionNode(fruit_to_the_right)
    condition_fruit_to_the_left = ConditionNode(fruit_to_the_left)
    condition_fruit_equal = ConditionNode(fruit_equal)

    action_right = ActionNode(move_right)
    action_left = ActionNode(move_left)
    action_not_move= ActionNode(not_move)

    # Subtrees
    right_sequence = Sequence([condition_fruit_to_the_right, action_right])
    left_sequence = Sequence([condition_fruit_to_the_left, action_left])
    not_move_sequence = Sequence([condition_fruit_equal, action_not_move])

    root_selector = Selector([right_sequence,left_sequence,not_move_sequence])

    return root_selector

# Agent initialization

# Build the tree
behavior_tree = build_behavior_tree()

# Sleep for 5 seconds before start
time.sleep(5) 
print('Start!')
# Start the game by pressing x
keyboard.press('x')
time.sleep(0.2)
keyboard.release('x')

# Open state file used to read game state
fstate = open('state.out', 'rb')

while True: 
    # run the tree
    behavior_tree.run()
    

    time.sleep(0.5)  # sleep for 500ms


    # move down
    # keyboard.press(Key.down)
    # print('Down')
    # time.sleep(0.2)
    # keyboard.release(Key.down)

    #keyboard.press(Key.right)
    #print('Right')
    #time.sleep(0.2)
    #keyboard.release(Key.right)

