#!/usr/bin/env python3

import random

parts_of_speech = {
        'noun': None,
        'verb': None,
        'adj': None,
        'adv_manner': None,
        'adv_degree': None,
        'imperative_adv': None,
        }

def list_of_words(pos):
    filename = 'HW03_' + pos + '.tsv'
    with open(filename,'r', encoding = 'utf-8') as f:
        words = [l.strip() for l in f.readlines()]
    return(words)

def rand_word(pos):
    return random.choice(parts_of_speech[pos])

def declarative():
    sentence = rand_word('adj').title() + ' ' + rand_word('noun') + ' ' +\
                rand_word('adv_manner') + ' '+ rand_word('verb')+ 's '+\
                rand_word('adj') + ' ' + rand_word('noun') + '.'
    return sentence

def imperative():
    sentence = rand_word('imperative_adv').title() + ' ' + rand_word('verb') +\
                ' ' + 'the' + ' ' + rand_word('adj') + ' ' +  rand_word('noun') +\
                ' ' + rand_word('adv_manner') + '.'
    return sentence

def interrogative():
    sentence = 'Does the ' + rand_word('adj') + ' ' + rand_word('noun') +\
                ' ' + rand_word('verb') + ' ' + rand_word('adj') + ' ' + rand_word('noun') +\
                ' ' + rand_word('adv_manner') + '?'
    return sentence

def a_noun(word):
    w = rand_word(word)
    article = 'an' if w[0] in 'euioa' else 'a'
    return article + ' ' + w

def exclamatory():
    sentence = 'What ' + a_noun('adj') + ' ' + rand_word('noun') + '!'
    return sentence

def conditional():
    sentence = 'If ' + rand_word('adj') + ' ' + rand_word('noun') +\
                ' ' + rand_word('verb') + 's ' + rand_word('adj') + ' ' + rand_word('noun') +\
                ', the ' +  rand_word('adj') + ' ' + rand_word('noun') + ' will ' +\
                rand_word('adv_degree') + ' ' + rand_word('verb') + ' the ' + rand_word('noun') + '.'
    return sentence

def main():
    # заполняем данные из tsv
    for p in parts_of_speech.keys():
        parts_of_speech[p] = list_of_words(p)
    sentences = [declarative, imperative, interrogative, exclamatory, conditional]
    with open('random_text.txt', 'w') as f:
        for i in range(5):
            print(random.choice(sentences)(), file=f)

if __name__ == '__main__':
    main()

    

