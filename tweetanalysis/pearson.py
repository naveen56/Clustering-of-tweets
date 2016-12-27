import re, math
import numpy
from collections import Counter

WORD = re.compile(r'\w+')


def calculatescore(text1,text2):
    vec1=text_to_vector(text1)
    vec2=text_to_vector(text2)
    intersection = set(vec1.keys()) | set(vec2.keys())
    list1=[]
    list2=[]
    for x in intersection:
        if x in vec1:
            list1.append(vec1[x])
        else:
            list1.append(0)
        if x in vec2:
            list2.append(vec2[x])
        else:
            list2.append(0)
    print(list1)
    print(list2)

    value=(numpy.corrcoef(list1, list2)[0, 1])


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)
calculatescore("hai ra maya","maya hai ra")