# jcy_find_file.py
A program that finds the location of a substring in file names under a subdirectory

This program was created to find files containing a substring </br>
This version requires python 3 </br>
Author: Julia Young </br>
Last edit: October 1st, 2018 </br>

Usage reguires two arguments.
Example: python jcy_find_file.py '/Users/juliayoung/Documents/' '.txt' </br>

If a valid directory is set, outputs are as follows: </br>
Match.csv, deliminator = '|' </br>
Directories_checked.txt </br>
Directories_left.txt </br>

If no files are found that match the argument, Match.csv will not have any
entries.

To limit the search the following parameters are set: </br>
allowed_directory_count (This means if there are more than the allowed number
    of subdirectories left to check, end the search.)

## Unit testing
To run the unit tests after editing the code to make sure the program is still working use: 
python jcy_find_file_unit_tests.py

The following files must be downloaded to the test directory as well: </br>
standard_test1.txt </br>
standard_test2.txt </br>

(If unit testing in a new directory, the following files must be downloaded and in the files 
you must replace '/Users/juliayoung/Documents/code_exam/' with the current working directory.) </br>
standard_test3.txt </br>
Directories_checked_standard.txt </br>
Directories_left_standard.txt </br>
Match_standard.csv </br>

