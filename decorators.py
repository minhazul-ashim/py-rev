def outerFn(message) :
    print("Executed the outer function");
    
    def innerFn() :
        print("Executed the inner function");
        print(message); #It implements the closure property, because we can access the outer functions variables or arguments from the innter function.
    return innerFn;

# f = outerFn("Hello from Argument");
# f();

def decorator(originalFn) :
    print("Inside the Decorator Function");
    
    def wrapper(extraMsg) :
        print("Inside the wrapper function");
        return originalFn() + extraMsg;

    return wrapper;

@decorator
def authFn() : 
    return "This User is Authenticated";

# f = authFn(" Hello");
# print(f);

f = decorator(authFn)(" This is the extra message which is concatenated by the decorator function without affecting the original function");

# Output of line 26 is below
# Inside the Decorator Function
# Inside the wrapper function

print(f);

# Output of line 32 is below
# Inside the Decorator Function
# Inside the wrapper function
# This User is AuthenticatedExtra work done by the decorator function


# So what is happening here is, the decorator function takes in the original function as an argument. The original function here only returns string, and really small, but for complex applications the function can be really complex and tricky. So what the decorator function really solves us that it modifies the original function or results returned from the original function. It takes original function as a parameter, there is another wrapper function in the decorator function. This wrapper function does the extra work which is needed from the original function and returns the result to the wrapper function. And the original function returns the wrapper function value, so when the decorator function is called with the original function as its argument, it does certain job and stores the information within itself.