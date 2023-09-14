import sys
# Get the command line arguments

args = sys.argv
value= input(args).split(' ')
# Print the command line arguments
print(f"list of arguments: {str(value)}")
#count number of arguments
print(f"number of arguments: {len(value)}")
