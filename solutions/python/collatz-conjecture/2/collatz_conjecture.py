def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    steps_of_collatz_conjecture = 0

    while number != 1:
        if number % 2 == 0:
            number //= 2
            if steps_of_collatz_conjecture == 0:
                steps_of_collatz_conjecture = 1
            else:
                steps_of_collatz_conjecture += 1
        else:
            number = number * 3 + 1
            if steps_of_collatz_conjecture == 0:
                steps_of_collatz_conjecture = 1
            else:
                steps_of_collatz_conjecture += 1

    return steps_of_collatz_conjecture
        