#1) smile face

#for loop

for num in range(1,11):
    print("\U0001f600" * num)


#while loop

times = 1
while times < 11:
    print("\U0001f600" * times)
    times += 1

#nested loop
for num in range(1,11):
    count = 1
    smileys =''
    while count < num:
        smileys += "\U0001f600"
        count += 1
    print(smileys)

# 2) sister game

msg = input("say something:")

while msg != "stop coping me " :
    print(msg)
    msg = input()
print('ok You won.')

# or
# while msg != "stop coping me":
#   msg = input (f"{msg}\n")
# print (" ugh you won")


# BREAK
# while True:
 command = input( "Type 'exit' to finish")
 if (command == "exit"):
     break


for x in range (1, 200):
    print(x)
    if x == 3:
        break

