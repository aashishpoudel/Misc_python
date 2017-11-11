from os import listdir, getcwd, rename
from os.path import isfile, join
import os
import sys


current_word = sys.argv[1]
new_word = sys.argv[2]

my_cwd = getcwd()
#listdir includes both files and directories
onlyfiles = [f for f in listdir(my_cwd) if isfile(join(my_cwd, f))]


for file in onlyfiles:
    print(str(file))
    if current_word in file:
        old_filename = file
        part1, part2 = old_filename.split(current_word)
        new_filename = part1 + new_word + part2
        print("renaming file " + str(old_filename) + " to " + str(new_filename))
        os.rename(old_filename, new_filename)
        print("Now the list of files are:")
        print(os.listdir(my_cwd))
