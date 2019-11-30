def sum_two_numbers(a, b):
    return a + b            # return result to the function caller

print(sum_two_numbers(5, 10))  # assign result of function execution to variable 'c'


def fib(n):
    """This is documentation string for function. It'll be available by fib.__doc__()
    Return a list containing the Fibonacci series up to n."""
    result = []
    a = 0
    b = 1
    while a < n:
        result.append(a)
        # var = b
        result.append(b)
        # result.append(a)
    return result

print(fib(5))