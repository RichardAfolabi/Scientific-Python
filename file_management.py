"""
File management
---------------
The goal of this exercise is to practice manipulating your file system:
creating folders and files, moving them around, and erasing them.

One piece of information to know about is that each python script contains its
own namespace. Such that, when in a script you define a = 1, a gets added to
the script namespace. But there are other variables that are added to that
namespace automatically: One example is __file__, which contains the filepath
to the current script.

1. Print the path to the current file/script and its containing folder.
"""
import os
pathx = os.getcwd()

print pathx

os.listdir(pathx)


#%%
"""
2. In the same directory as this exercise, create a new directory called
`analysis`.

Hints: Why it isn't enough to just run:
>>> os.mkdir("analysis")
Where would that folder be? Build its absolute path to create it. Also note
that if the folder already exists, mkdir will raise an error if the folder
doesn't get removed before being created again. To remove a folder, compare the
following functions: `shutil.rmtree` and `os.rmdir`.
"""

import shutil

path_build = os.path.abspath(pathx) + '\\analysis'
print path_build

def pathfinder(mypath):
	''' Create a new folder if not existing. Delete and recreate if existing'''
	try:
		if os.path.exists(mypath):
			existpth = raw_input("Path already exists. Delete and recreate? YES(Y) / No(N): ")
			if str(existpth).capitalize() == 'Y':
				shutil.rmtree(mypath)
				print("Path '\%s' removed " %os.path.basename(mypath))
				os.mkdir(mypath)
				print("\n Path '\%s' recreated!" %os.path.basename(mypath))
			else:
				print("\n\n Path '\%s' untouched!" %os.path.basename(mypath))
		else:
			print("\n\n Path does not exist. Path '\%s' will be created." %os.path.basename(mypath))
			os.mkdir(mypath)
	except Exception as excpt:
		print ('Oopps... %s ' %excpt)
	
pathfinder(path_build)

#%%
"""
3. Create, wherever you are, a set of files with the names and content
described in the dictionary `contents` provided to you. Then, move all these
files into the `analysis` folder. For this, the `copy` function of the module
`shutil` will be useful.

"""
contents = {
    'data.csv': 'Date,High,Low,Close\n'
                '4-Apr-2014,124,105,111\n'
                '5-Apr-2014,132,125,130\n'
                '6-Apr-2014,112,95,95\n'
                '7-Apr-2014,124,105,110\n',
    'script1.py': 'def bar(x):\n'
              '        print x\n',
    'script2.py': 'def foo(x):\n'
              '        print x*x\n',
    'readme.txt': 'This folder contains the data files scrapped off the web\n'
                  'from financial websites in csv formar as well as python\n'
                  'scripts for analyzing them.\n',
}

curr_path = os.path.dirname(path_build)


# Since 'contents' is a dictionary, we grab the keys, insert them into open statement in a loop.
# Within the loop, we write the value of each key in the dictionary into the newly created file.

try:
	for key in contents.keys():
		with open(key,'w') as fptr:
			fptr.write(contents[key])
			print("\n file '%s' created and populated." %key)
except Exception as excpt:
	print("scratching head... I'm confused!")


#Required: Move all the newly created files into the 'analysis folder'. Since we have created a robust 
# function for 'analysis', we just call it. Using for loop, we move the files and delete them from cwd. 

pathfinder(path_build)

for key in contents.keys():
	shutil.copy(key,path_build)
	os.remove(key)
	print("\n File move for '%s' completed!" %key)
	

#%%

"""

4. Print the absolute path of all the Python `.py` files in this `analysis` directory.

"""

pycount = []
def python_hunter(xpath):
	""" Takes a path and return absolute dir of all Python files in the directory """
	
	for xfile in os.listdir(xpath):
		if os.path.splitext(xfile)[1] == '.py':
			pycount.append(os.path.abspath(xfile))
	
	print(pycount)
	print("\n -- %d Python files found -- "% len(pycount))


python_hunter(path_build)



