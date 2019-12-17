#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        length = len(sentence)
        first = sentence[0]
    else:
        lenght = len(sentence)
        first = None
    return (length, first)
