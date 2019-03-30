# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:53:27 2019

@author: YASH SAINI
"""

filename = "mac.txt"

text =(open(filename).read()).lower()
U_char = sorted(list(set(text)))

chr_int={}
int_chr={}

index=0
for i in U_char:
    chr_int[i]=index
    int_chr[index]=i
    index+=1
    
X = []
Y = []

for i in range(0, len(text) - 50):
    sequence = text[i:i + 50]
    label =text[i + 50]
    X.append([chr_int[char] for char in sequence])
    Y.append(int_chr[label])