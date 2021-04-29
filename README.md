# CYPHER TXT 
## Table of Contents
1. [About](#1)
2. [Disclaimer ](#2)
3. [IoC](#3)
4. [Quickstart](#4)


## About<a name = 1></a>
This uses a password to create seed for a pseudo-random number generator which it then uses to perform letter substitutions using a character list and some modular arithmetic. 

The same password must then be used to decrypt the text.

## Disclaimer <a name = 2></a>
I have no idea how secure this encryption method is as I made it up, so probably not very.. 

## IoC<a name = 3></a>
The encrypted text output by cypher.py seems to have a index of coincidence of around 0.8 (english is about 1.7)

## Quickstart<a name = 4></a>
in terminal:
    python cypher.py "filepath/yourtextfile"

it will then prompt you for a password and ask you if you are encrypting or decrypting. 

It will then output a file in the same directory as the original file with "_encrypted" or "_decrypted" added on to the filename. 


