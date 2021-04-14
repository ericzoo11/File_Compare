import os 
import filecmp as fc
import sys 

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
            pass
######
#Main
######

if __name__ == "__main__":

    root_dir1 = '/Users/ericzhu/Documents/My_Stuff/Resume_Stuff/'
    root_dir2 = '/Users/ericzhu/Desktop/Resume_Stuff/'
    #dog = fc.dircmp(root_dir1, root_dir2)
    #dir_diff(dog)
    #dir_iterate(root_dir1, root_dir2)
    dog = fc.dircmp(root_dir1, root_dir2, ignore=None, hide=None)
    
    sys.stdout = open('output_file.txt', 'w')
    dog.report_full_closure() 
    sys.stdout.close()

    #f = open("output_file", "w")
    #f.write(cat)
    #f.close
