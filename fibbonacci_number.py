# write a function to calculate the fibbonacci number for n term:-
# 0,1,1,2,3,5,8,13,21,.......
# fibbonacci series:- addition of first two numbers.
# aisa function banana h jisme jo number input denge ussi number ka fibonacci number mil jaye.
# matlab agar 6 input karege to output 8 mil jayga.
#this program start with 1 series like (1,1,2,3,5,8,13).

def fibbonacci(n):
    """
    :param n:
    :return:(n-1) + (n-2)
    """
    if n == 0: # this for starting series by 1 like(1,1,2,3,5,8,..)
        return 0 # we can also start with 0 like(0,1,1,2,3,5,8..)
    elif n == 1: # for start with 0 we place n==1 and n==2 in if and elif place.
        return 1
    else:
     return fibbonacci(n-1) + fibbonacci(n-2)

inpnum = int(input("Enter the position of number which you want fibonacci number:\n"))
print("the fibonacci is",fibbonacci(inpnum))
