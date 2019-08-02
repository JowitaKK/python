# for loop

# for x in range (1,10):
#     print(x)
#     print(x*x)

for letter in "coffee":  # for in - const, letter- any varriable name
    print(letter)

for num in range (10,20,2):  # its exclusive does not print 20
    print(num)

for num in range(0,100,5):
    print(num)

#=========Exercises=================

# 1) print odds number in range 10 20 (is explusive remember has to be 21)
x = 0
for n in range(10,21):
    if n % 2 !=0:
        x += n

# 2) cleaning your room

times = input ("How many time do I have to tell You ?")
times = int(times)

for time in range(times):
    print(f"time {time+1}: Clean up Your room") # +1 to not to print 0

# 3) loop through numbers 1-20 (with 20) /4, 12 print (is unlucky) for even numbers = even , for odds = odd

for num in range(1,21):
    if num == 4 or num ==13:
        print(f"{num} is unlucky")
    elif num % 2 == 0:                     # for odd    num % 2 == 1:
        print("f{num} is even")
    else:
        print("f{num} is odd")







# while loops

#1)
msg = input ("what was the secret password?")
while msg != "banana ": # which should be true
    print("Wrong")
    msg = input("what is the secret password?")
print("Correct")


#2) print range(1,11)
num = 1
while num < 11:
    print(num)
    num += 1  # print and stop loop     // to do even num += 2






