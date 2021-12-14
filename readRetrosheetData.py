
file = open('2021BAL.EVA')
line_count = 0
for line in file:
    if line != "\n":
        line_count += 1
file.close()
print(line_count)