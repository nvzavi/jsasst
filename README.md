# jsasst (beta)
A little tool to automate some of the manual tasks of reviewing obfuscated JavaScript files. It is intended to assist by making the script easier to read, i.e. after deobfuscation and beautification, as well as enable a quick overview of possible suspicious elements that may be contained within. ***NOTE:  This is a beta version, I am still testing and removing a few bugs.***
* The following tasks are automated *(based on your selected usage argument)*:  
  * Rename weird variable names to a name that you specify *(you provide the prefix and the tool will append an integer value to it)* 
  * Identify suspicious elements *(the tool uses the lookup list to accomplish this, i.e. se_list.txt, that you can define)* 
  * Identify URLs and files names within the script 
  * Identify misleading tuple structures in the script   

Use any of the options below when processing the file:

Description | Example
------------ | -------------
Display help window | jsasst.py -h
Display misleading tuple structures | jsasst.py -f script.js -t
Identify noteworthy elements  | jsasst.py -f script.js -e
Identify URLs and file names  | jsasst.py -f script.js -u
Display a summary of the above arguments in one page | jsasst.py -f script.js -s
Change variable names to one that you specify | jsasst.py -f script.js -d script_output.js -v param

**Additional:**  Output for the above can be piped to any file using the **>** sign in the terminal window

<h2>NOTE</h2>  
This is a beta version, I am still testing and removing a few bugs and hence kindly note that I am not responsible for any damages to your code (if any). 
<h3>Use at your own risk</h3> 
