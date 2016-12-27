import re, math
from collections import Counter

WORD = re.compile(r'\w+')


"""
 @desc:calculate the cosine similarity between two strings
 @:param:string1:first string, string2 second string
 @:return:float value ,which is similarity of two i/p strings

"""
def calculatescore(text1, text2):
     vec1 = text_to_vector(text1)
     vec2 = text_to_vector(text2)
     print(vec1)
     print(vec2)
     for x in vec1.keys():
         vec1[x]=vec1[x]/len(text1)
     for x in vec2.keys():
         vec2[x]=vec2[x]/len(text2)

     print(vec1)
     print(vec2)




"""
 @desc:calculate frequency of words in tweet
 @:param:text ,it is a string(tweet)
 @:return:Counter type ,it contains frequency of words(eg:[is:2])

"""
def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)
calculatescore("hai ra naveen hai","hai ra")
