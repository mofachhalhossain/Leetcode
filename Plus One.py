def plusOne(digits):
    n = len(digits)
    digits[n - 1] += 1
    
    for i in range(n - 1, 0, -1):
        if digits[i] == 10:
            digits[i] = 0
            digits[i - 1] += 1
    
    if digits[0] == 10:
        digits[0] = 1
        digits.append(0)
    

    return digits


digits = [9]
print(plusOne(digits))