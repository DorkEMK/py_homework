#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

def word_replace(stem, flex, new_stem, text):
    ''' 
    Replaces stem to newstem, saves flexes.
    '''
    pattern = r'\b%s%s\b'
    repl = r'%s\1'
    text = re.sub(pattern % (stem, flex), repl % (new_stem), text)
    stem = stem.capitalize()
    new_stem = new_stem.capitalize()
    text = re.sub(pattern % (stem, flex), repl % (new_stem), text)
    stem = stem.upper()
    flex = flex.upper()
    new_stem  = new_stem.upper()
    text = re.sub(pattern % (stem, flex), repl % (new_stem), text)
    return(text)

# язык > шашлык
infile = open('HW_04_лингвистика.txt', 'r')
outfile = open('HW_04_шашлыковедение.txt', 'w')

clean_text = infile.read().replace(chr(769), '') # delete stress
outfile.write(word_replace('язык', '(а|у|ом|е|и|ов|ам|ами|ах|)', 'шашлык', clean_text))

infile.close()
outfile.close()

# Финляндия > Малайзия
infile = open('HW_04_Финляндия.txt', 'r')
outfile = open('HW_04_Малайзия.txt', 'w')

clean_text = infile.read().replace(chr(769), '')
outfile.write(word_replace('финлянди', '(я|и|ю|ей)', 'малайзи', clean_text))

infile.close()
outfile.close()

# философия > астрология
infile = open('HW_04_философия.txt', 'r')
outfile = open('HW_04_астрология.txt', 'w')

clean_text = infile.read().replace(chr(769), '')
outfile.write(word_replace('философи', '(я|и|ю|ей|й|ям|ями|ях)', 'астрологи', clean_text))

infile.close()
outfile.close()
