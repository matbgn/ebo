import random

num_dict = random.sample(range(2, 13), 11)

horizontal_values = ""
for i in num_dict:
    horizontal_values += " " + str(i) if i != 10 else ""

print(horizontal_values)

num_dict = random.sample(range(2, 13), 11)

for i in num_dict:
    print(i) if i != 10 else ""
