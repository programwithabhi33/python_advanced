# filter is the built in python that takes two parameters and first is the function that contain condition and the second is the iterable object or list 

a = [2,3,4,5,6,7,8,9]

new_list = filter(lambda x:x<4,a)

print(list(new_list))