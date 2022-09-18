def summation(n, term ,k):
    if n == 0:
        return 0
    else :
        return term(k) + summation(n - 1 , term, k)

from hog import roll_dice

exi_time = 800
def excepted_score_of_n_rolls(k):
    return summation(exi_time, roll_dice, k)/exi_time

i = 1
while i <=  10:
    temp = excepted_score_of_n_rolls(i)
    print(temp)
    i = i + 1 

E_roll = [4,6 ,7,8,8,8,8,8,7,6]