# from dice import make_fair_dice, make_test_dice
# from hog import take_turn, roll_dice
# def roll_dice(num_rolls, dice):
#     """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
#     the outcomes unless any of the outcomes is 1. In that case, return 1.

#     num_rolls:  The number of dice rolls that will be made.
#     dice:       A function that simulates a single dice roll outcome.
#     """
#     # These assert statements ensure that num_rolls is a positive integer.
#     assert type(num_rolls) == int, 'num_rolls must be an integer.'
#     assert num_rolls > 0, 'Must roll at least once.'
#     # BEGIN PROBLEM 1
#     "*** YOUR CODE HERE ***"
#     n = 1
#     total = 0
#     pigout = 0
#     while n<=num_rolls:
#         temp = dice()
#         total, n = total + temp ,n+1
#         if temp ==1:
#             pigout = pigout + 1
#     if pigout > 0:
#         return 1
#     else:
#         return total
        
# print(roll_dice(2,make_test_dice(4,5,1))) 
# from hog import play, always_roll
# from dice import make_test_dice
#  #
#  # Ensure that say is properly updated within the body of play.
# def total(s0, s1):
#      print(s0 + s1)
#      return echo
# def echo(s0, s1):
#      print(s0, s1)
#      return total
# s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2, 5), goal=10, say=echo)
ss= [1,5]
print(ss[1])