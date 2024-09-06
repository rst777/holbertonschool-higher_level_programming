#!/usr/bin/python3
def remove_char_at(str, n):

    nouvelle_chaine = ""
    for i in range(len(str)):
        if i != n:
            nouvelle_chaine += str[i]
    return nouvelle_chaine
