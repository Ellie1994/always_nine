#implementation of an exiting mathematical phenomenon: 
#1.take a number
#2.summ up its digits
#3.subtract this sum from the original number
#4.sum up the digits of the result ---> you will always get '9'

user = input("put in a number: ")

int_lst = [int(i) for i in user]

while len(int_lst) == 1:
    print("put in at least a two digit number")
    user = input("put in a number: ")
    int_lst = [int(i) for i in user]

if len(int_lst) > 1:
    summed = sum(int_lst)
    minus = int(user) - summed
    result = sum([int(i) for i in str(minus)])
    print(result)  
