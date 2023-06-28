def decimaltobinary(dec_num, array):
    i = 7
    while dec_num != 0:
        rem = dec_num % 2
        array[i] = rem
        dec_num = dec_num//2
        i -= 1


def binarytodecimal(array):
    deci = 0
    j=7
    for i in range(7):
        deci = deci + array[j] * pow(2, i)
        j -= 1
    return deci


def showbinary(array):
    for i in array:
        print(i, end="")
    print("\n")


def addbinary(number1, number2, result):
    c = 0
    for i in range(7, -1, -1):

        result[i] = (number1[i] ^ number2[i] ^ c)
        c = ((number1[i] & number2[i]) | (number1[i] & c) | (number2[i] & c))

    result[i] = c
    return c


def main():
    numb1 = [0, 0, 0, 0, 0, 0, 0, 0]
    numb2 = [0, 0, 0, 0, 0, 0, 0, 0]
    result = [0, 0, 0, 0, 0, 0, 0, 0]
    dec = int(input("enter the decimal: "))
    decimaltobinary(dec, numb1)
    dec2 = int(input("enter the decimal: "))
    decimaltobinary(dec2, numb2)
    showbinary(numb1)
    showbinary(numb2)
    add = addbinary(numb1, numb2, result)
    decimal = binarytodecimal(result)
    if add == 0:
        print("the eqivalent result is")
        showbinary(result)
        print("equivalent decimal")
        print(decimal)
    else:
        print("overload")
main()