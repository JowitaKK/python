friends = ["Jov", "Antos", "Olek"]

print(friends[-1])
"Jov" in friends


# access all values
# ==============for loop============

colors = ["red", "black", "orange", True, 8.6]

for color in colors:
    print(color)

numbers= [3, 5, 7, 12]

for num in numbers:
    print(num)

# ============ while loop============

colors = ["red", "black", "orange"]
index = 0
while index < len(colors):
    print(colors[index])
    index += 1

#=======================================


sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

result = ''
for s in sounds:
    result += s.upper()

#====================list method =================

                                # adding

        # append - add an idet to the end of the list IT TAKES JUST ONE ARGUMENT!!!!!!

first_list = [2, 2, 3, 4]
first_list.append(5)
print(first_list)

=====================extend======================
        # add to the end of the list all values passed to extend  TO ADD MORE ARGUMENTS !!!!!!

second_list = [3, 3, 4, 4]

second_list.extend ([1, 1, 1,])
print(second_list)


========================insert=====================

        # insert an item at a given position

first_list = [1, 3, 2]
first_list.insert(2, "hi")
print(first_list)  # 1, 2, 3, "hi"

first_list.insert(-1, "end")
print(first_list) # 1,3, end, 2




                                        # clear

#=======================pop========================

            # remove the item at the given position in the list,
            # if index no specified, removes & return last item in the list
first_list = [3, 6, 4, 5]
first_list.pop()   #5
first_list.pop(1)  # removes 6

#=======================remove====================

            # remove the first item from list with given value
            # throws a ValueError if the item is not found

first_list = [1, 2, 3, 4, 4, 4]
first_list.remove(2)   # 1, 3, 4, 4, 4
first_list.remove(4)   # 1, 2, 3, 4, 4  first at given value
















