#! /usr/bin/python

import os
import stat

def walktree(current_folder= '.'):
    for file_name in os.listdir(current_folder):
	st = os.lstat(os.path.join(current_folder, file_name))
	if stat.S_ISDIR(st.st_mode):
	    walktree(os.path.join(current_folder, file_name))
	else:
	    if file_name=='gym.less':
		continue

	    name, extension = os.path.splitext(file_name)
	    if not extension == '.less':
		continue

	    print "@import \"%s\";" % (os.path.join(current_folder, file_name))

if __name__ == '__main__':
    walktree()
