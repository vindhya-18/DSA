def countdown(n):
    if n == 0:
        print("LAUNCH!")
    else:
        print(n)
        countdown(n - 1)

n = int(input("Enter countdown starting number: "))
countdown(n)
