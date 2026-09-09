def is_armstrong_number(number):
    list_number = []

    str_number = str(number)

    sum_numbers = 0
    
    for digit in str_number:
        num = int(digit) ** len(str_number)
        list_number.append(num)

    for num in list_number:
        if sum_numbers == 0:
            sum_numbers = num
        else:
            sum_numbers += num
        
    return sum_numbers == number