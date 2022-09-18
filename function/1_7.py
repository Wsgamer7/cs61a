# # from this import d


# # def is_even(n):
# #     if n == 0:
# #         return True
# #     else:
# #         return is_odd(n-1)

# # def is_odd(n):
# #     if n == 0:
# #         return False
# #     else:
# #         return is_even(n-1)

# # print(is_odd(4))
# def alice_turn(n):
#     if n ==0 :
#         print("bob win!")
#     else:
#         return bob_turn(n-1)

# def bob_turn(n):
#     if n == 0:
#         print("alice win!")
#     elif n%2 ==0 :
#         return alice_turn(n-2)
#     else :
#         return alice_turn(n-1)

# alice_turn(18)
def count_patition(n,m):
    if n == 0:
        return 1
    elif n < 0 :
        return 0
    elif m==0:
        return 0
    else:
        return count_patition(n-m, m) + count_patition(n, m-1)

print(count_patition(100,4))