def dec_to_bin(x):
    return int(bin(x)[2:])

def isPali(number, binary = False):
    if binary:
        digits = str(dec_to_bin(number))
    else:
        digits = str(number)
    for i in range(0,len(digits)-1):
        if digits[i] != digits[-i - 1]:
            return False
    return True

answer = 0

for x in range(1,1000001):
    if isPali(x) and isPali(x, True):
        answer += x

print(answer)
