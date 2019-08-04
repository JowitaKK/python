# def raise_to_power(base_num, pow_num):
#     result = 1     # store results of the math
#     for index in range(pow_num):
#         result = result * base_num
#     return result
#
# print(raise_to_power(2, 3))


#==========grid=================
#accessing nasted elements

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]


print(number_grid[0][0])   #1
print(number_grid[2][1])   #8 remember about index

#or
for row in number_grid:
    for col in row:
        print(col)     # print column in row
