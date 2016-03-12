import os

suffix = 'pptx'
new_name_prefix = 'CSE140L Lecture '
for file in os.listdir('.'):
    if file[len(file) - len(suffix) : len(file)] == suffix:
        old_name = file[:len(file) - len(suffix) - 1]
        day = old_name[-1]
        new_name = new_name_prefix + day + '.' + suffix
        os.rename(file, new_name)
