import re

total_sum = 0 
pattern = r'[0-9]+'

with open("/Users/diegopons/Documents/Coding/Chat-GPT-Learning/Python/Regular Expressions/textbook.txt", "r") as file:
    for line in file:
        line.strip()
        all_nums = re.findall(pattern, line)
        for i in all_nums:
            total_sum += int(i)

#total = sum(all_nums)
#print(total)
print(total_sum)
        
