#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i >= 0:
        if(i == 0):
            print('Happy New Year!')
        else:
            print(i)
        i -= 1
    pass

def square_integers(int_list):
    # code goes here!
    return [i ** 2 for i in int_list]
    # print(int_list)
    pass
# square_integers([1, 2, 3, 4, 5])

def fizzbuzz():
    # code goes here!
    i = 1
    while i <= 100:
        if(i % 3 == 0 and i % 5 == 0):
            print('FizzBuzz')
        elif(i % 3 == 0):
            print('Fizz')
        elif(i % 5 == 0):
            print('Buzz')
        else:
            print(i)
        i += 1
    pass

fizzbuzz()

# i = 0
# while i < 5:
#     print('Looping')
#     i += 1

# for i in range(10):
#     print('Looping')
#     print(f'i is: {i}')

# player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]

# inch_heights = list()
# for height in player_heights:
#     inch_height = height * 7920
#     inch_heights.append(inch_height)

# inch_heights = [height * 7920 for height in player_heights]

# print(inch_heights)