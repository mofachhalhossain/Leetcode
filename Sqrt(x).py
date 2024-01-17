def mySqrt(x):
    left, right = 0, x

    while left <= right:
        mid = (left+right) // 2
        if mid * mid > x:
            right = mid - 1
        elif mid * mid < x:
            left = mid + 1
        else:
            return mid
        
    return right



x = 5
print(mySqrt(x))