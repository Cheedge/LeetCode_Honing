# Brute force
def solve(n: int)->None:
    for i in range(n):
        if i%3==0 and i%5==0:
            print(f"{i=}, FizzBuzz")
        elif i%3==0:
            print(f"{i=}, Fizz")
        elif i%5==0:
            print(f"{i=}, Buzz")



solve(100)