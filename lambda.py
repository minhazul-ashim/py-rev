def addThreeNum(x, y, z) : 
    return x + y + z;

result1 = addThreeNum(5, 5, 5);
result2 = lambda x, y, z : x + y + z;

print(result1);
print(result2(5,5,5));

# Both of these functions return the same thing. That means Lambda function is just like a syntactic sugar for Python just like Arrow functions are for Javascript