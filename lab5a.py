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
    


if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
