''' This code is a probability calculator. The class 'Hat' contains a certain number of balls of different colours. The
    purpose of this is to calculate the probability of selecting a ball or certain number of balls of a particular colour.'''

import copy
import random
class Hat:
    def __init__(self,**kwargs):
        # **kwargs used to collect key-worded, variable length dictionary
        # Keyword is required because we need ball colour and the corresponding number of balls of that colour
        self.argument = kwargs
        self.contents = []

        for x in self.argument:
            # Append the item multiple times to the list
            for _ in range(self.argument[x]):
                (self.contents).append(x)

    # stores all balls in a python list
    def conts(self):
        return list(self.contents)

    # method in the Hat class I will use to take out balls from the ball collection in the hat
    def draw(self,balls):
        self.balls = balls
        self.removed = []

        # Create a copy of the original list
        hat_copy = (self.contents).copy()

        # Shuffle the copy
        random.shuffle(hat_copy)
        # Remove the required number of items from the shuffled list
        for _ in range(self.balls):
            (self.removed).append(hat_copy.pop())
        self.contents = hat_copy
        return self.removed

''' This if the function to carry out the probability experiment.
    hat - Contains the Hat in which the balls are contained
    expected_balls - the balls you want to pick from the hat
    num_balls_drawn - number of balls you want to draw
    num_experiments - the number of times you want to pick the expected_balls out of the num_balls_drawn'''
def experiment(hat,expected_balls, num_balls_drawn,num_experiments):

    selected_count = 0

    ball_count = []

    for x,y in expected_balls.items():
        # create a list containing the necessary copies of the ball colours
        ball_count.extend([x] * y)
        # Now, the ball_count list contains the balls we c]want to remove

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat.conts())  # Create a deep copy to avoid modifying the original hat

        # Use random.choices to select items with replacement
        selected_items = random.choices(hat_copy, k=num_balls_drawn)

        # to check if the selected_items contains the balls we want to pick in ball_count
        if set(ball_count).issubset(selected_items):
            selected_count += 1

    return selected_count / num_experiments



hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 1,
                    "red": 2},
    num_balls_drawn=4,
    num_experiments=3000)

'''This gives the probability of selecting 2 blue balls and 1 red ball out of 4 balls from the Hat 300 times.'''
print("Probability:", probability)
