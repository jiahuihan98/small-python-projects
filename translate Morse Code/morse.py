#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 16:42:07 2016
name: Jiahui Han
net ID: jh5226
Practice 1
"""

def create_dictionary(filename):
    in_file = open(filename , 'r')
    dict_morse = {}
    for line in in_file:
        line = line.strip()
        line_list = line.split('\t')
        key = line_list[0]
        value = line_list[1]
        dict_morse[key] = value
    
    in_file.close()
    return dict_morse
    
def create_morse(filename , text):
    text = text.upper()
    dict_morse = create_dictionary(filename)
    out_string = ''
    for char in text:
        if char == ' ':
            out_string += ' ' * 7
        else:
            morse = dict_morse[char]
            out_string = out_string + morse + (' ' * 3)
    return out_string
    
def create_text(filename , text):
    dict_morse = create_dictionary(filename)
    out_string = ''
    text_list = text.split(' ' * 7)
    for element in text_list:
        word_list = element.split(' ' * 3)
        for word in word_list:
            for key in dict_morse:
                if dict_morse[key] == word:
                    out_string += key
        out_string += ' '
    return out_string.lower()
    
      
    
def main():
    user_input_text = input('Please enter text:')
    morse_string = create_morse('Morse Code Chart.txt' , user_input_text)
    print(morse_string)
    user_input_morse = input('Please enter morse text:')
    text_string = create_text('Morse Code Chart.txt' , user_input_morse)
    print(text_string)
    
main()