# jsasst (beta)
A little tool to automate some of the manual tasks of reviewing possibly malicious JavaScript files. It is intended to assist by making the script easier to read, i.e. after deobfuscation and beautification is done, as well as enable a quick overview of possible suspicious elements that may be contained within. ***NOTE:  This is a beta version, I am still testing and removing a few bugs.***
* The following tasks are automated *(based on your selected usage argument)*:  
  * Rename weird variable names to a name that you specify *(you provide the prefix and the tool will append an integer value to it)* 
  * Identify suspicious elements *(the tool uses the lookup list to accomplish this, i.e. the se_list.txt file that you can edit/update)* 
  * Identify URLs and files names within the script 
  * Identify misleading tuple structures in the script   

<h2>Arguments include:</h2>

Argument | Description
------------ | -------------
-f  | Specifies the file to be analysed
-t  | Directs the tool to identify any misleading tuple structures.
-e  | Directs the tool to identify if any of the elements that are listed in the se_list.txt file  are contained within the script.
-u  | Directs the tool to identify URLs and file names.
-s  | Directs the tool to display a summary of the above arguments (-t, -e, -u) in one page.
-v  | Directs the tool to update script variable names to one that is specified. See example in the table below.  (**NOTE:**  This must be used together with the -d argument stated below)
-d  | Specifies the file name to which the results of the above argument (-v) are dumped into. (**NOTE:**  Must be used together with the -v argument.  See example in the table below)  


<h2>Use any of the options below when processing the file:</h2>

Description | Example
------------ | -------------
Display help window | jsasst.py -h
Display misleading tuple structures | jsasst.py -f script.js -t  
Identify noteworthy elements  | jsasst.py -f script.js -e
Identify URLs and file names  | jsasst.py -f script.js -u
Summarises the above arguments (-t, -e, -u) in one page | jsasst.py -f script.js -s
Change variable names to one that you specify | jsasst.py -f script.js -d script_output.js -v param

**Additional:**  Output for each of the above examples can be piped to any file using the **>** sign in the terminal window

<h2>Setup</h2>

* Setup is as follows:
  * Copy jsasst.py to /usr/local/bin and make executable (chmod +x jsasst.py)
  * Copy se_list.txt to /usr/share/remnux (I am testing on a REMnux VM.  You can adjust this path in the code, simple find the comment that highlights this)
**Additional:** Review/update the se_list.txt file to enable the tool to identify the elements that you deem noteworthy

<h2>NOTE</h2>  
This is a beta version, I am still testing and removing a few bugs. Furthermore kindly note that I am not responsible for any damages to your code (if any) i.e. after running the tool.  Best to keep\make a backup of the script file prior to running this tool. 
<h3>Use at your own risk</h3> 

Thanks
