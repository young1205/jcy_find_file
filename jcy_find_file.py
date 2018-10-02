"""
This program was created to find files containing a substring
This version requires python 3
Author: Julia Young
Last edit: October 1st, 2018

Usage reguires two arguments.
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
"""
# Import libraries
import os,fnmatch
import sys
import pandas as pd

#Search Parameters
allowed_directory_count = 30

def locate(location, substring):
  """This function gerenrates a list of subdirectories and matches
       to the specified substring"""
  directories = [f.path for f in os.scandir(location) if f.is_dir() ]
  files = [f for f in os.listdir(location) if substring in f]
  return directories, files

def main(base, substring):
    """This is the main function of the program, to be called
       if the correct arguments are given"""

    print("Entering main function, checking in:"+base+" for:"+substring)

    #Create pandas object to hold output matches and directories checked
    col_names =  ['Directory', 'Matches']
    match_df  = pd.DataFrame(columns = col_names)

    # Initialize directory count and list
    directories_checked_count  = 0
    directories_checked = []

    #Check the base directory
    current_dir = base
    new_directories, files = locate(current_dir,substring)
    directories_checked.append(current_dir)
    directories_checked_count  += 1
    num_files = len(files)
    if num_files > 0:
        match_df = match_df.append({'Directory':current_dir,
                                    'Matches':files},
                                    ignore_index=True)

    # Run through the subdirectories of the base
    print(new_directories[0])
    while (directories_checked_count  <  allowed_directory_count) & (len(new_directories) > 0):
      current_dir = (new_directories[0])
      new_directories = new_directories[1:]
      print("Currently checking: "+current_dir)
      next_directories_deep, files = locate(current_dir,substring)
      new_directories += next_directories_deep
      directories_checked.append(current_dir)
      directories_checked_count  += 1
      num_files = len(files)
      if num_files > 0:
        match_df = match_df.append({'Directory':current_dir,
                                    'Matches':files},
                                    ignore_index=True)

    print('Checked '+str(directories_checked_count)+' directories')
    print("End of search")
    #print(directories_checked)

    # Create file outputs
    match_df.to_csv('Match.csv',sep='|',index=False)
    with open('Directories_checked.txt','w') as f:
        for item in directories_checked:
            f.write("%s\n" % item)
    with open('Directories_left.txt','w') as f:
        for item in new_directories:
            f.write("%s\n" % item)
    return

if __name__ == "__main__":
    if len(sys.argv) == 3:
        if os.path.isdir(sys.argv[1]) == False:
            print (sys.argv[1],"--Not a valid directory, exiting program.")
            sys.exit(1)
        if os.path.exists("Match.csv"):
            print ("Please rename or delete Match.csv, exiting program.")
            sys.exit(1)
        if os.path.exists("Directories_checked.txt"):
            print ("Please rename or delete Directories_checked.txt, exiting program.")
            sys.exit(1)
        if os.path.exists("Directories_left.txt"):
            print ("Please rename or delete Directories_left.txt, exiting program.")
            sys.exit(1)
        main(sys.argv[1],sys.argv[2])
    else:
        error_string = """To use this program type:
                          python jcy_find_file.py directory_location substring

                          Where directory_location is the base location to
                          begin your search. Substring is the string in the
                          files you are looking for.(Examples '.txt', 'main') """
        print(error_string)

