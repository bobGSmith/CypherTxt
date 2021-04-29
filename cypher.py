# -*- coding: utf-8 -*-
"""
                        |========|
                        | CYPHER |
                        |========|
                            
                            
Created on Tue Apr 27 23:36:04 2021
@author: Bobby (Github: ovrhuman)
"""
import random
import sys 

filepath = sys.argv[1]
password = input("Enter password (cap sensitive)\n>> ")
en_or_decrypt = "select"
while en_or_decrypt.lower() not in ["e","d"]: 
    en_or_decrypt = input("Encrypt or decrypt? [e/d]\n>> ")
    if en_or_decrypt.lower() not in ["e","d"]: print("invalid input..")


with open(filepath) as infile: 
    test = infile.read()

chars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ 0123456789')
n_chars = len(chars)

seed = sum([chars.index(x) for x in password])
random.seed(seed)
cipher_key = [random.randint(0,200) for i in range(100)]

if en_or_decrypt.lower() == "d":
    chars = chars[-1::-1]

new_text = ""
for i in range(len(list(test))):
    if test[i] in chars:
        key = cipher_key[i % len(cipher_key)]
        new_text += (chars[((chars.index(test[i]))+key)%len(chars)])
    else:
        new_text += (test[i])

extension = ""
outfilepath = filepath[:filepath.rindex(".")]
if outfilepath != filepath:
    extension = filepath[filepath.rindex("."):]
if en_or_decrypt.lower() == "e":
    with open(outfilepath + "_Encrypted" + extension, "w") as outfile:
        outfile.write("".join(new_text))

elif en_or_decrypt.lower() == "d":
    with open(outfilepath + "_Decrypted" + extension, "w") as outfile:
        outfile.write("".join(new_text))    