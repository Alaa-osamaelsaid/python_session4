from bitstring import BitArray

# example DDRA= 0b00110101
while True: #keep it working till the user enter the correct number
 try:
    direction= BitArray(input("please enter portA direction in binary, hint(0b11110000): "))
    if (len(direction)!= 8):
        raise ValueError("this number isn't 8 bits")
    break
 except ValueError:
    print("invalid port input,you must enter 8-bit binary number")


      