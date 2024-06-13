'''
This code is to solve File I/O situations where we need to find the highest 
email sender. Topics used: lists, dictionaries, file io.
'''
# 1- find emails 2- which email shows up the most

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

email_counts = {}

#get lines
for line in handle :
    print(line)
    if not line.startswith("From ") :
        continue
    else :
        #create list of words, from lines starting with from 
        words = line.split()
        #get email
        email = words[1]
        
        #add email to dictionary
        if email not in email_counts :
            email_counts[email] = 1
        else:
                email_counts[email] += 1
                
 #find highest email count in email_counts dictionary
highest_emailer = None

for email, count in email_counts.items():
    if highest_emailer is None or count > highest_emailer[1]:
        highest_emailer = (email, count)

print(highest_emailer[0],highest_emailer[1])
