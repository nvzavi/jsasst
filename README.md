# jsasst
This tool is intended to assist in reviewing JavaScript files.   **Still testing and removing a few bugs.**

Use any of the options below when processing the file:

Usage | Example
------------ | -------------
Display help window | jsasst.py -h
Display misleading tuple structures | jsasst.py -f script.js -t
Identify noteworthy elements (lookup data found in se_list.txt)  | jsasst.py -f script.js -e
Identify URLs and file names  | jsasst.py -f script.js -u
Display a summary of the above arguments in one page | jsasst.py -f script.js -s
Change variable names to one that you specify | jsasst.py -f script.js -d script_output.js -v param

**NOTE:**  Output for the above can be piped to any file using the > sign in the terminal window
