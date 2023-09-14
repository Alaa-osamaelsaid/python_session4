#mylist = ["alaa","ahmed","osama"]

#fill your data in the runtime
mylist= input("please fill up you list with comma in between the words: \n")
answer= mylist.split(",")
print(answer) #used to print the list

# create new text file in the same working   
with open('test.txt','w') as file:
     #file.write("".join(mylist)) #to write list with space between words
      file.write(str(mylist))

#show the content of the text file
read_content= open('test.txt')
print(read_content.read())

