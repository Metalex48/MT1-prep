'''
Control structures
'''

##### This program sorts the input in a list by asc or desc order.
scores = [51,54,66,89,91,70,45,71,90,68]
#order = int(input(f'\t--|Select your sorting order (1 or 2): '))
scores.sort()
#if order == 2:
#    scores = scores[-1::-1]
#print(f'\t--|You have chosen option {order}\n\t--|Sorted scores\n\t--|{scores}')



### For loops.
primes = [2,3,5,7,11]
for i, p in enumerate(primes):
    print (f'for i = {i}, p = {p}')

person = {'h':1.77 , 'w':74, 'name':'Alejandro', 'country':'Mexico'}
for x, y in person.items():
    print (f'(key, item) = ({x}, {y})')

### While loops.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0 
while i < len(a):
    print(a[i], end = '*** ')
    i += 1
print ()

i = 0
while i < 21:
    i += 1
    if i % 2 == 0:
        continue
    print(f'{i} ', end = ' ')
print()


# Generate a list that contains all positive integers less than 100 divisible by 6. 
import random 

my_list3 = []
i = 1
while i <= 100:
    if i%7 == 0:
        my_list3.append(i)
    i += 1
print (my_list3)



# Lab 4 exercises:

# Generate a list named lottery_numbers between 1 and 99. n\
# Rearrange the lottery_numbers list items in random order.
lottery_numbers = [x for x in range(1,100)]
random.shuffle(lottery_numbers)
print(lottery_numbers)

# Generate a list with the name lottery_draw of 6 randomly selected unique numbers n\
# from the list lottery_numbers list.
lottery_draw = random.sample(lottery_numbers,6)
print (lottery_draw)

# Sort the list lottery_draw in descending order.
lottery_draw.sort(reverse=True)
print (lottery_draw)
