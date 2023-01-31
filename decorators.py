def abhi(fun):
    def xy(*args,**kwargs):
        # print(*args)
        # print(**kwargs)
        print("abhishek")
        fun(*args,**kwargs)
        print("abhishek2")
    return xy

# Decorators means the called function modify by the new function called abhi() function which is defined in the top of the function with the @ symbol
# It called the abhi function and pass the called function and the abhi function or the decorator function return the new function, the new returned function is called on the behalf of the info function or driver function 
@abhi
def info(a,b):
    print(f"Hello Good Morning a is {a} and the b is {b} ")

info('abhi','abhishek2')

