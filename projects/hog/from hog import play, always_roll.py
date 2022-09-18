 from hog import play, always_roll
 from dice import make_test_dice
 #
 # Ensure that say is properly updated within the body of play.
 def total(s0, s1):
     print(s0 + s1)
     return echo
 def echo(s0, s1):
     print(s0, s1)
     return total
 s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2, 5), goal=10, say=echo)