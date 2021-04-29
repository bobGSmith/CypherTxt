# -*- coding: utf-8 -*-
"""
                        |===================|
                        | CYPHER - function |
                        |===================|
                            
                            
Created on Tue Apr 27 23:36:04 2021
@author: Bobby (Github: ovrhuman)
"""
import random



def cypher(text, password = "password",en_or_decrypt = "e" ):
    '''en_or_decrypt = e or d. '''
    chars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ 0123456789')
    n_chars = len(chars)
    
    seed = sum([chars.index(x) for x in password])
    random.seed(seed)
    cipher_key = [random.randint(0,200) for i in range(100)]
    
    if en_or_decrypt.lower() == "d":
        chars = chars[-1::-1]
    
    new_text = ""
    for i in range(len(list(text))):
        if text[i] in chars:
            key = cipher_key[i % len(cipher_key)]
            new_text += (chars[((chars.index(text[i]))+key)%len(chars)])
        else:
            new_text += (text[i])
    return new_text 
