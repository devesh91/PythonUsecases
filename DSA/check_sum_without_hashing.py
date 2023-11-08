x =[2,6,5,8,11]
y= list(enumerate(x))
x.sort()

sum = 14

def grab_left(x, index):
    return x[index+1::]

def grab_right(x, index1,index):

    return x[index1:index:]

def check_sum(x):
    print(x)
    for index,value in enumerate(x):

        if value + x[-1]  == sum:
            print(index,-1)
            return (value,x[-1])
        elif value + x[-1] <sum:
            new_list= grab_left(x, index)
            return check_sum(new_list)
        else:
            new_list=grab_right(x, index,len(x)-1)
            return check_sum(new_list)




values=check_sum(x)
print(values)
answer=[]
for i in y:
    print(i)
    if i[1] ==values[0]:
        answer.append(i[0])
    elif i[1] == values[1]:
        answer.append(i[0])
print(answer)