def answer(n):
    count = 0
    n = int(n)
    while n != 1:
        if n&1 == 0 or n == 4:
            n = n >> 1
        elif ((n-1)>>1)&1 == 0  or n == 3:
            n -= 1
        else:
            n += 1
        count += 1

    return count

if __name__ == "__main__":
    print answer("4") == 2
    print answer("15") == 5
    print answer("13") == 5
    print answer("9") == 4
    print answer("2") == 1
    print answer("1") == 0

