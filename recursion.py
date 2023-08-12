x = 5;

def recurseX(x) :
    if(x == 0) : return;

    print(x);
    recurseX(x - 1);

def addTwoNumbers(x, y) :
    return x + y;

recurseX(x);
print(addTwoNumbers(5, 8));