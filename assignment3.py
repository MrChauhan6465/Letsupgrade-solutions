#*agr used inside the python function


def sum(*n):
    res = 0
    for i in n:
        res = res+i
    print("addion is ",res)
sum(90,80)



def spam(**inp):
    for key,value in inp.items():
        print("{} is {}".format(key,value))
spam(firstname="Vijaykumar",lastname = "Chauhan")