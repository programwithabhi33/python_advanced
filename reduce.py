from functools import reduce

# print(reduce)

a = [1,2,3,4]

new_list = reduce(lambda x,y:x+y,a)
print(new_list)