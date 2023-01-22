# map is a higher order function in python that take two arguments first is a function and the second is iterable object like a list or tuple

a = [2,3,4,5]

new_list = map(lambda x:x*x,a)

print(list(new_list))