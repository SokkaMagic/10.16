# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Push() and Pop() - move TopOfStack yourself.

# Exercise 1
Stack = []
TopOfStack = -1
for x in range(10):
    Stack.append(-1)


def Push(DataToPush):
    global Stack, TopOfStack
    if TopOfStack == 9:
        return False
    TopOfStack = TopOfStack + 1
    Stack[TopOfStack] = DataToPush
    return True

def Pop():
    global Stack, TopOfStack
    if TopOfStack == -1:
        return -1
    DataToReturn = Stack[TopOfStack]
    TopOfStack = TopOfStack - 1
    return DataToReturn

def Peek():
    if TopOfStack == -1:
        return -1
    return Stack[TopOfStack]



def IsEmpty():
    return TopOfStack == -1

def Size():
    return TopOfStack + 1

def ReverseList(Numbers):
    lst = []
    finallst = []
    global Stack, TopOfStack

    for i in range(len(Numbers)):
        if TopOfStack == 9:
            print("Stack full")
            return False

        TopOfStack += 1
        Stack[TopOfStack] = Numbers[i]

    lst = Stack[:TopOfStack+1][::-1]

    for i in range(len(lst)):
        finallst.append(lst[i])

    TopOfStack = -1

    return finallst

# Exercise 3
def Balanced(Expression):
    # Write your code here
    pass
