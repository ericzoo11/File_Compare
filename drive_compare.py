import os 
import filecmp as fc
import sys 
import re

def parse_report():
    re = [] #list for report
    lines = []# list for lines with "Only in"

    f = open('output_file.txt', 'r')
    rep = f.readlines()
    f.close()
    
    #add only lines that have differences
    for line in rep:
        if "Only in" in line:
            lines.append(line)

    return lines

def org_list(listA):
    main_list = {}
    
    for item in listA:
        
        temp = item.split()
        a = temp[2] #holds the path of the files
        b = re.findall(r"'(.*?)'", item, re.DOTALL) #list of diff files
        
        #add path as key and diff files as values in dictionary
        main_list[a] = b

    return main_list

######
#Main
######

if __name__ == "__main__":

    root_dir1 = '/Users/ericzhu/Documents/My_Stuff/Resume_Stuff/'
    root_dir2 = '/Users/ericzhu/Desktop/Resume_Stuff/'

    dog = fc.dircmp(root_dir1, root_dir2, ignore=None, hide=None)
    
    default_stdout = sys.stdout #saving current stdout to var
    file_handle = open('output_file.txt', 'w')

    #output report to file 
    try:
        sys.stdout = file_handle
        dog.report_full_closure() 
        sys.stdout.close()
    finally:
        #revert to default stdout
        sys.stdout = default_stdout
    print("\n\n\n")
    
    # data is now in dictionary ready to go to extract and print
    data_ready = org_list(parse_report()) 
    

''' First go at script functions
def dir_diff(dir_obj):
    
    # grab left and right directories with the help of the built in function 
    l_list = dir_obj.left_list
    r_list = dir_obj.right_list
    
    #run lists through hidden_remove
    list1 = hidden_remove(r_list)
    list2 = hidden_remove(l_list)   

    diff_files = compare_list(list1, list2)

    print("files missing in one of the directories:")
    for i in diff_files:
        print(i)
    
######################################################  
#function to remove hidden files from my list of names
def hidden_remove(list1):
    temp = list1 # keeping the list local 
    list2 = [] # temp list to hold the new updated list without the hidden files

    # remove hidden files and .Dstore from list
    for i in (temp):
        if "._" in i or ".D" in i:
            pass
        else:
            list2.append(i)
    
    # return fresh list that is ready to be used to compare with other directory
    return list2

########################################################################
# function to compare two list and print what is missing from each other
def compare_list(a, b):

    # list comprehension to find provide a list of all the file names in the union of the list
    c = [x for x in a+b if x not in a or x not in b]

    #return list of different files found
    return c


def dir_iterate(dir1, dir2):
    for subdir, dirs, files in os.walk(dir1):
        print(subdir)
        for file in files:
            pass'''