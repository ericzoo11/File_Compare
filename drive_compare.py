import filecmp as fc

# global variables
##################
dir1 = '/Users/ericzhu/Documents/My_Stuff/Resume_Stuff/2018'
dir2 = '/Volumes/500_T5_SDD/My_Stuff/Resume_Stuff/2018'

dog = fc.dircmp(dir1, dir2)

def diff_files(dir_obj):
    
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

######
#Main
######

diff_files(dog)


l;ksd;lksdl;fk