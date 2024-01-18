def isPalindrome(s):
    a = ''.join(char.lower() for char in s if char.isalpha() or char.isdigit())
    b = list(a)
    start, end = 0, len(b)-1

    while start < end:
        if b[start] == b[end]:
            start += 1
            end -= 1
        else:
            return False
    return True
            



s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))