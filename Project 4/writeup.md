Project 4
==========
# Team Members:
- Grigory Polunin
- Luke Villaluz
- Saiyushi Kumar
- Luke Trusheim

# Expected Data Structures
Since a coverage tester gives details about the level to which the written coding of an application has been tested, 
some data structures we would be likely to use if we were implementing a coverage tester are: dictionaries, hash tables, 
arrays, linked lists, and binary trees. These data structures offer efficiency in storing various types of information, 
such as source code and coverage reports. They also facilitate the tracking and analysis of coverage information during 
execution, allowing for the identification of untested code segments and ensuring comprehensive testing. The diverse 
range of data structures utilized in a coverage tester contributes to its intricate implementation. Each data structure 
serves specific purposes, such as improving efficiency and accuracy, as well as facilitating the storage and management 
of data. In conclusion, the successful implementation of a coverage tester likely relies on the use of a combination of 
different data structures to fulfill its requirements.

# Initial Code Examination
The folder contains a useful README file that provides information about coverage.py. The projects in the folder vary in 
length, ranging from around 50 to 600 lines.
Our initial examination focused on the test_numbits.py file in the tests folder. It appeared to contain several tests 
for numbits functions. Next, we reviewed the test_goldtest.py file, which had strategically placed comments that greatly 
aided our understanding of the functions. This file comprised coverage test cases for the "contains" functions in 
goldentest.py.
Moving on to the coverage subdirectory, we analyzed the files annotate.py, data.py, numbits.py, multiproc.py, and 
disposition.py. Annotate.py’s purpose is to generate annotated source files. On the other hand, data.py contained 
utility functions for working with coverage data in coverage.py. Numnits.py housed functions for manipulating packed 
binary representations called numbits, and it was relatively easy to comprehend.
Multiproc.py had helpful comments, but the code itself provided better insights into the file's purpose. Lastly, 
disposition.py defines simple value objects for tracking file handling within a larger coverage system. In this case, 
the code proved more valuable than the comments for understanding its content.
In summary, the comments in these files are beneficial for comprehending their purpose and functions. However, 
ultimately, the code itself is more valuable in gaining a complete understanding of their contents.

# Detailed Code Examination
For the detailed code examination I have chosen to use the summary.py file in the coverage subdirectory. This file 
appears to be a good candidate as it is lengthy in code and has many different functions within it. The main data 
structures used for this file are dictionaries, lists and strings. The dictionaries in the case of this file are used 
for storage of strings such as the project name and author. The lists in this case are used for the coverage dictionary 
at each point such as packages, package data, entry points, and extra require. Strings are also obviously used all over 
the place in the if statements, the dictionary, and also for the sources. From what it looks like the setup_args is a 
dictionary with the indexes, coverage, package, package data, entry points, extra require, and ext errors. Ext errors 
seems to contain a couple of instances of some class called errors which has the attributes compileerror, 
distuilsexecerror, and distutilsplatformerror. There is also a data definition for a class called buildfailed which has 
a init which takes in a cause and stores it in the self.cause. There is also another class called ve_build_ext which has 
run function and a build extension function which takes in itself and ext. At the end of the function there are a couple 
if statements which rely on a boolean titled compile_extension which is set to true before the if statements. The last 
if statement in the file contains a whole bunch of stuff I have no clue about but what I can say is that there is a lot 
of nested data and attributes for each thing stored within the setup_args.update dictionary. At the end of the file it 
has a def main function to actually invoke the setup of the file so all the code can run. Overall the code was written 
very neatly with many comments.

# Summary
The code is generally readable, with meaningful variable names and consistent formatting. However, some 
lines are quite long, which can make it harder to read and understand the code.
Function clarity: Most functions have clear names and do a single specific task, making it easier to understand their 
purpose.
Much of the code I looked at includes comments at the beginning of the file with licensing information and a 
link to the project's GitHub repository. There are also some comments above certain functions, explaining their purpose. 
However, more comments could be added within the code to provide further explanation of complex logic or algorithms.
Maintaining or updating this code could be challenging for someone not familiar with the coverage.py 
library. Several of the files interact with each other in complicated ways, so without a good understanding of the 
library's internals, making changes or fixing bugs could be difficult.
This code is much more advanced than the code I write. There are lots of aspects of the code 
that I don’t understand or recognize. 
