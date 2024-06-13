file_name = input("Enter file name ")
file = open(file_name)
for line in file :
    #### pritning lines 
    line = line.rstrip()
    print(line)

words = line.split()
print(words)