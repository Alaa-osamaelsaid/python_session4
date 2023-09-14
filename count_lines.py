
#file name (file must be in the same count_lines path)
file_path = 'file.txt'
#function to read and count number of lines in the file above
def read_and_count_lines(file_path):
    with open(file_path,'r') as f: # or f = open(file_path, "r")
        return sum(1 for i in f ) # equal to  for i in f return i+1
        

number_of_lines = read_and_count_lines(file_path)
print(f"The number of lines in {file_path} is {number_of_lines} lines")

#method 2 
#with open(file_path,"r") as file:
    #lines_number = file.readlines()
    #print(len(lines_number))