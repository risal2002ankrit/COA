def DecimalToBinary(decimal):
    if decimal >= 1:
        DecimalToBinary(decimal // 2)
    global value
    value = decimal% 2
    print(value, end='')


def binaryToDecimal(binary):
    decimal, i = 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    print(decimal)


if __name__ == '__main__':
    dec_val = 20

    DecimalToBinary(dec_val)
    print(value, end='')
    binaryToDecimal(10100)


