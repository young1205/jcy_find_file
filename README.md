# jcy_find_file.py
A program that finds the location of a substring in file names under a subdirectory

This program was created to find files containing a substring
This version requires python 3
Author: Julia Young
Last edit: October 1st, 2018

Usage reguires two arguments. /n
Example: python jcy_find_file.py '/Users/juliayoung/Documents/' '.txt'

If a valid directory is set, outputs are as follows:
Match.csv, deliminator = '|'
Directories_checked.txt
Directories_left.txt

If no files are found that match the argument, Match.csv will not have any
entries.

To limit the search the following parameters are set:
allowed_directory_count (This means if there are more than the allowed number
    of subdirectories left to check, end the search.)

## Unit testing
To run the unit tests after editing the code to make sure the program is still working use 
jcy_find_file_unit_tests.py
