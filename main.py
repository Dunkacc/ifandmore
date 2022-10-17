rec_file = open("sillyRec.txt",'r')
all_lines = rec_file.readlines()
line_number = 1
for line in all_lines:
    if line_number % 2 == 1:
        print(line)
    line_number = line_number +1