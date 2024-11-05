#!/usr/bin/env python3
# Author ID: Jerrico Gomez - 131382228

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    file = open(file_name, "r")
    file_read = file.read()
    file.close()
    return file_read

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line character
    file = open(file_name, "r")
    file_lines_list = [line.strip() for line in file.readlines()]
    file.close()
    return file_lines_list

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    file = open(file_name, "a")
    file.write(string_of_lines)
    file.close()

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    file = open(file_name, "w")
    for line in list_of_lines:
        file.write(line+"\n")
    file.close()

def copy_file_add_line_numbers(filepath1, filepath2):
    linecount = 1
    file1 = open(filepath1, "r")
    file1_read = file1.readlines()
    file2 = open(filepath2, "w")
    for line in file1_read:
        file2.write(f"{linecount}:{line}")
        linecount +=1
    file1.close()
    file2.close()
    
    


if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
