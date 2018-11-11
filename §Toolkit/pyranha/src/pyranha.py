#!/usr/bin/python

# pyranha

# v1.0 - jlefanic
# 2016

# Usage :
# pycon run.dat
# output run.cat

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
import sys, re
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |

if __name__ == "__main__":

    # sys.argv is the list of command-line arguments
    # sys.argv[0] is the name of the program itself
    # sys.argv[1] will be the regex specfied at the command line
    
    # 'r' means read-only
    file_for_reading = open(sys.argv[1], 'r')
    text=""
    for line in file_for_reading :
        text=text+line
    file_for_reading.close()
    includes=re.findall("\x27([\S|\n]+)\x27",text,re.MULTILINE)
    print includes
        
    # 'w' is write -- will destroy the file if it already exists!
    file_for_writing = open(re.sub(r'\.dat',r'.cat',sys.argv[1]), 'w') 
    
    # for every line passed into the script
    file_for_reading = open(sys.argv[1], 'r')
    i=0
    k=0
    for line in file_for_reading :
        if re.search('^INCLUDE', line):
            sys.stdout.write(line)
            include=re.sub(r'\n',r'',includes[i])

            file_for_including = open(include, 'r')
            for include_line in file_for_including:
                        file_for_writing.write(include_line)
            file_for_including.close()  

            if re.search(r'\n',includes[i]):
                k=len(re.findall(r'\n',includes[i]))         
            i=i+1
            
        elif not re.search('^INCLUDE', line) and not re.search('^ENDDATA', line) and k<1:
            file_for_writing.write(line)          
        
        elif re.search('^ENDDATA', line):
            file_for_writing.write("ENDDATA\n")
            file_for_writing.write("$ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |\n")
            file_for_writing.write("$                                  .          ,---,                     |\n")
            file_for_writing.write("$       o                         . ._    _,-'    `--,                  |\n")
            file_for_writing.write("$   .       o                    .  ( `-,'            `\                |\n")
            file_for_writing.write("$              o                .   \            ,    o \               |\n")
            file_for_writing.write("$                 o           .      /   ,       ;       \              |\n")
            file_for_writing.write("$                    o      o       (_,-' \       `, _  \"\"/             |\n")
            file_for_writing.write("$                        o                 `-,___ =='__,-'              |\n")
            file_for_writing.write("$                                                ````                   |\n")  
            file_for_writing.write("$ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |\n\n")
          
        else :
            k=k-1
        
    file_for_writing.close()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
