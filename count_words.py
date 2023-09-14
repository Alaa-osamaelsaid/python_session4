
file_name = 'file.txt'

with open(file_name,'r') as file:
    no_of_words= file.read()

print(len(no_of_words.split()))
#split( is used to count words)
#without split it counts number of letters