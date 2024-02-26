### Signed binary/hexadecimal to decimal converter

def binary(s):
    s = list(s)
    s.pop(0)
    s.pop(0)
    count = 0
    inverse_s = s[::-1].copy()
    for i in range(len(s)):
        if inverse_s[i] == '1' or inverse_s[i] == '0':
            count += int(inverse_s[i])*2**i
        else:
            print("Invalid input")
            return
    print(count)
    return

def hexadecimal(s):
    hex2dec = {'0': 0,
               '1': 1,
               '2': 2,
               '3': 3,
               '4': 4,
               '5': 5,
               '6': 6,
               '7': 7,
               '8': 8,
               '9': 9,
               'A': 10, 'a': 10,
               'B': 11, 'b': 11,
               'C': 12, 'c': 12,
               'D': 13, 'd': 13,
               'E': 14, 'e': 14,
               'F': 15, 'f': 15
               }
    s = list(s)
    s.pop(0)
    s.pop(0)
    count = 0
    inverse_s = s[::-1].copy()
    for i in range(len(s)):
        if inverse_s[i] in hex2dec:
            count += hex2dec[inverse_s[i]]*16**i
        else:
            print("Invalid input")
            return
    print(count)
    return

if __name__ == "__main__":
    print("0b - binary")
    print("0x - hexadecimal")
    print("q - quit")
    s = input("Enter string: ")
    while(s != 'q'):
        if s[0:2] == '0b':
            binary(s)
        elif s[0:2] == '0x':
            hexadecimal(s)
        else:
            print("Invalid input")
        s = input("Enter string: ")