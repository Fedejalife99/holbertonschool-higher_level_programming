def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            continue
        if i % 3 == 0:
            print("Fizz", end = ' ')
            continue
        if i % 5 == 0:
            print("Buzz", end = ' ')
            continue
        print(i, end = ' ')