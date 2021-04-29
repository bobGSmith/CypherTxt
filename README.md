# CYPHER TXT 
## Table of Contents
1. [About](#1)
2. [Disclaimer ](#2)
3. [IoC](#3)
4. [Quickstart](#4)


## About<a name = 1></a>
It's a variant on a Caesar cipher that uses a differnt shift size for each letter substitution, and the sequence of shift sizes used can only be determined if you have the password that was used to create them in the first place.

So, it uses a password to create seed for a pseudo-random number generator which it then uses to generate a list of numbers. It then does letter substitutions on the text and uses the random numbers to pick the shift size for the substitution (so a different shift is used for each letter). The same password must then be used to decrypt the text.

## Disclaimer <a name = 2></a>
I have no idea how secure this encryption method is as I made it up, so probably not very.. Having said that, I tried a few automatic cipher solvers and they havent had any luck with it. Not sure if there's an offical way to test thest things? 

If I had to guess, I think its a few security noteches above rot13 or Caesar cipher 

## IoC<a name = 3></a>
The encrypted text output seems to have a index of coincidence of around 0.8 which is close to what is seen in random text (english is about 1.7).

## Quickstart<a name = 4></a>
in terminal:

    python cypher.py "filepath/yourtextfile"

it will then prompt you for a password and ask you if you are encrypting or decrypting. 

It will then output a file in the same directory as the original file with "_encrypted" or "_decrypted" added on to the filename. 


