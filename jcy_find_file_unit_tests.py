"""
This program was created to unit test jcy_find_file
If run in a new directory you must replace
'/Users/juliayoung/Documents/code_exam/' with the current working
directory location in the following files:
'standard_test3.txt'
'Match_standard.csv'
'Directories_checked_standard.txt'
'Directories_left_standard.txt'


This version requires python 3
Author: Julia Young
Last edit: October 1st, 2018
"""
# Import libraries
import os
import sys
import filecmp

def unit_test_one():
  """This function checks to see the correct response occurs while trying to run
  jcy_find_file.py with the wrong number of arguments"""
  os.system('python jcy_find_file.py > result_test1.txt')
  passtest = filecmp.cmp('standard_test1.txt', 'result_test1.txt')
  if passtest:
      print("Passed unit test one")
      os.system('rm result_test1.txt')
  else:
      print("Failed unit test one, exiting program.")
      sys.exit(1)
  return

def unit_test_two():
  """This function checks to see the correct response occurs while trying to run
  jcy_find_file.py with an incorrect directory_location"""
  os.system('python jcy_find_file.py not_a_dir ".txt" > result_test2.txt')
  passtest = filecmp.cmp('standard_test2.txt', 'result_test2.txt')
  if passtest:
      print("Passed unit test two")
      os.system('rm result_test2.txt')
  else:
      print("Failed unit test two, exiting program.")
      sys.exit(1)
  return

def unit_test_three():
  """This function checks to see the correct response occurs while running
  through some sample directories."""
  warning = """Warning!! If run in a new directory you must replace
  '/Users/juliayoung/Documents/code_exam/' with the current working
  directory location in the following files:
  'standard_test3.txt'
  'Match_standard.csv'
  'Directories_checked_standard.txt'
  'Directories_left_standard.txt'"""
  print(warning)

  #Create the test directories and files
  fill = """This is a file created for unit testing"""
  os.system('mkdir unit_test_temp')
  for ix in range(0,5):
    os.system('mkdir unit_test_temp/sub'+str(ix))
    fname = "unit_test_temp/sub"+str(ix)+"/testfile"+str(ix)+".txt"
    file = open(fname,"w")
    file.write(fill)
    file.close()

  #Generate files to check against standard
  cwd = os.getcwd()
  os.system('python jcy_find_file.py "'+cwd+'/unit_test_temp" ".txt" > result_test3.txt')

  passtest1 = filecmp.cmp('standard_test3.txt', 'result_test3.txt')
  passtest2 = filecmp.cmp('Match.csv','Match_standard.csv')
  passtest3 = filecmp.cmp('Directories_checked.txt','Directories_checked_standard.txt')
  passtest4 = filecmp.cmp('Directories_left.txt','Directories_left_standard.txt')
  if passtest1 and passtest2 and passtest3 and passtest4:
      print("Passed unit test three")
      os.system('rm result_test3.txt')

      #Clean up files and directories created for unit test
      for ix in range(0,5):
        fname = "unit_test_temp/sub"+str(ix)+"/testfile"+str(ix)+".txt"
        os.system('rm '+fname)
        os.system('rmdir unit_test_temp/sub'+str(ix))
      os.system('rmdir unit_test_temp')
      os.system('rm Match.csv')
      os.system('rm Directories_checked.txt')
      os.system('rm Directories_left.txt')

  else:
      print("Failed unit test three, exiting program.")
      sys.exit(1)
  return


def main():
    """This is the main function of the program that runs through
    the set of unit tests"""
    unit_test_one()
    unit_test_two()
    unit_test_three()
    print("End of tests")
    return

if __name__ == "__main__":
    if os.path.exists("Match.csv"):
        print ("Please rename or delete Match.csv, exiting program.")
        sys.exit(1)
    if os.path.exists("Directories_checked.txt"):
        print ("Please rename or delete Directories_checked.txt, exiting program.")
        sys.exit(1)
    if os.path.exists("Directories_left.txt"):
        print ("Please rename or delete Directories_left.txt, exiting program.")
        sys.exit(1)
    main()

#Define main function
