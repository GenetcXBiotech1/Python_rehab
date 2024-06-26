### Functions are tools that are used to perform a specific task
## Display hyped statement
print("I can't wait to write my own functions!!!")

## Created function that adds 2 to int input and returns sum to where
### the f() is called
def f(x):
    ## Adds 2 to the input
    result = x+2
    ## Returns the sum to where the f() is called
    return result
## Display the output f() using different inputs
print(f(1))
print(f(2))
print(f(10))

## Creates a function called f()
## That takes one argument
def f(x):
    ## Indent anytime you create a function
    ## Adds 2 to the input int value
    result = x + 2
    ## Returns the result value to where the function f() is called
    return result

## New function g(y), takes one argument
def g(y):
    ## Multiplies the input by 5 and returns the value to 
    ## where the function is called.
    return y*5

# Display the output g function with int argument 10
print(g(10))

## New function h(a,b), takes two arguments,
def h(a, b):
    ## Summs the inputs
    result = a + b
    ## Returns the summ to where the h() function is called
    return result

## Display the different outputs to h() function
print(h(1, 2))
print(h(5, 7))

## New function test() that takes 1 argument
def test(x):
    ## The input is multplied by 2 and product is returned to where
    ## The function is called
    return x+2

## Display the output of the test() function
print(test(1))

## New fuction h(), takes 1 argument
def h(z):
    ## Multiplies the input by itself and returns the product
    ## To where the function h() is called
    return z*z

## Display the output of the h() function
print(h(10))

## New function add_together, takes 2 arguments
def add_together(a, b):
    ## Summs the two arguments and returns the sum to where the
    ## add_together() function is called
    return a + b

## Display the output of the add_together function
print(add_together(3, 4))

## New function times_three, takes one argument
def times_three(number):
    ## Multiplies the input by 3 and stores the product in result variable
    result = number * 3
    ## Returns the product to where the times_three function is called
    return result

## Display output of the times_three() function
print(times_three(8))

## New function add, takes 1 parameter
def add(number):
    ## Summs the input with 40 and stores the sum value in result variable
    result = number + 40
    ## Returns the summ to where the add() function is called
    return result

## Display output for the add() function
print(add(15))

## New function forty_two() that takes 0 arguments
def forty_two():
    ## Returns the int value 42 to where the function forty_two is called
    return 42
    

# Display the output of the forty_two() function
print(forty_two())

## New function send_123(), takes 0 arguments
def send_123():
    ## Return the int value 123 to where the function
    ## send_123() is called
    return 123
    
## Display the output of the send_123() function
print(send_123())

## New function f(), takes 0 arguments
def f():
    ## Return the int value 123 to where the f() is called
    return 123
    ## This line of code will "not" be read since the return kewyword
    ## Is before it
    ## After python reads the return keyword it exits the function
    print("never reached")

## Store the value of the f() function in the y variable
y = f()
## Display the output of the y variable
print(y)