#!/usr/bin/env python
# coding: utf-8

#this script sets a variable for line_no (the line number in the text file, starting with 0 due to being a list) 
#because line is used as a string and using len(file_lines)
#is kind of long winded

line_no = 0

#this just reads the file and throws all the lines into a list, it's done with proper encoding to avoid weirdness
#like mismatched string lengths

with open("rawdata.txt", mode = 'r', encoding = 'utf-8') as source_file:
    file_lines = source_file.readlines()

#just a loop that iterates over every single line of the file
    
for line in file_lines:
    
    #if there's already a ';', then it just writes the line as is and adds 1 to line_no to move to the next line
    
    if file_lines[line_no][-2] == ';':
        with open("appended_data.txt", mode = 'a+', encoding = 'utf-8') as target_file:
            target_file.write(line)
        line_no += 1
    
    #the only other case is that there's no ';', then it has to split the line at the "\n" to avoid
    #putting the ";" in a new line and then add ";\n" to the split line to keep putting words
    #in new lines, then it adds 1 to line_no to move to the next line
    
    else:
        with open("appended_data.txt", mode = 'a+', encoding = 'utf-8') as target_file:
            target_file.write(line.split("\n")[0] + ';\n')
        line_no += 1

