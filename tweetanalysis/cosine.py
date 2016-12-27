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
     #print(vec1)
     #print(vec2)
     intersection = set(vec1.keys()) | set(vec2.keys())
     #print(intersection)
     numerator = sum([vec1[x] * vec2[x] for x in intersection])
     #print(numerator)
     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = round(math.sqrt(sum1) * math.sqrt(sum2),4)
     #print(denominator)
     if not denominator:
        return 0.0
     else:
        #print(text2)
        val=float(numerator / denominator)
        #print(val)
        return float(numerator / denominator)


"""
 @desc:calculate frequency of words in tweet
 @:param:text ,it is a string(tweet)
 @:return:Counter type ,it contains frequency of words(eg:[is:2])

"""
def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)
print(calculatescore("hai naveen ","hai naveen"))
print(calculatescore("hai naveen how are you","hai naveenkalyan"))
print(calculatescore("hai naveenkalyan","hai naveen how are you"))
print(calculatescore("hai ","hai naveen "))

#dictionary of input ,tweetid as key & tweet as value
dict={}
with open('D:\\education\\python\\twiiter.txt','r') as f:
    for line in f:
        key_value=line.split('\t')
        dict[key_value[0]]=key_value[1] #storing tweets in dictionary
##################phase one clustering##########################
#list_of_clusters is list of cluster formed
list_of_clusters=[]
#list_of_messages is bag of words of tweets in cluster
list_of_messages=[]
keys_list = list(dict.keys())
keys_list.sort()
print("the number of tweets is ")
print(len(keys_list))

#param:count is to store the count of processed tweets
count=0
for i in range(0,len(keys_list)):
    #if tweet is not added into any cluster
    if keys_list[i]!=0:

        dict_of_cluster=[]
        dict_of_cluster.append(dict[keys_list[i]])

        count=count+1
        for j in range(i+1,len(keys_list)):
            if  keys_list[j]!=0 and calculatescore(dict[keys_list[i]],dict[keys_list[j]])==1.0:

                dict_of_cluster.append(dict[keys_list[j]])
                keys_list[j]=0

                count=count+1

        list_of_clusters.append(dict_of_cluster)

        list_of_messages.append(dict[keys_list[i]])
print ("the processed tweets is %d" %count)
print("after phase1 no of clusters formed is %d" %len(list_of_clusters))
print(list_of_clusters)
print(list_of_messages)
#################phase 2 clustering##############################################
""""
@desc:all the tweets in two cluster forms into one cluster
@parm:src,dest:list of tweets in one cluster
@:return:return the union of two cluster
"""
def union_of_clusters(src, dest):
    dict=src
    for i in range(0,len(dest)):
        dict.append(dest[i])

    return dict
""""
@desc:bag_of_words of two clusters are grouped
@parm:src,dest:tweet
@:return:union of two bag_of_words
"""

def union_of_messages(src,dest):
    return src+dest

count=0
while count!=len(list_of_clusters): #untill another cluster cant form with more tweets
    count=0
    list_of_messages2=[]
    list_of_clusters2=[]


    for i in range(0,len(list_of_messages)):
        if list_of_messages[i]!=[]:
            flag=0
            max=-2.0
            maxi=0
            for j in range(i+1,len(list_of_messages)):
                if list_of_messages[j]!=[]:
                    score=calculatescore(list_of_messages[i],list_of_messages[j])
                    if score>max and score>0.5:
                        max=score
                        flag=1
                        maxi=j
            if flag==1:
                count=count+2
                list_of_messages2.append(union_of_messages(list_of_messages[maxi],list_of_messages[i]))
                list_of_clusters2.append(union_of_clusters(list_of_clusters[maxi],list_of_clusters[i]))
                list_of_messages[maxi]=[]
                list_of_clusters[maxi]=[]

            if flag==0:
                count=count+1
                list_of_messages2.append(list_of_messages[i])
                list_of_clusters2.append(list_of_clusters[i])

    print("no of clusters processed in phase 2 is %d" %count)

    list_of_messages=list_of_messages2
    list_of_clusters=list_of_clusters2
    del list_of_messages2
    del list_of_clusters2
    print("no of clusters formed after phase 2 is %d" %len(list_of_messages))
for i in range(0,len(list_of_clusters)):
     list_of_tweets_in_cluster=list_of_clusters[i]
     print("***************************************************************************************")
     for j in range(0,len(list_of_tweets_in_cluster)):
         print(list_of_tweets_in_cluster[j])
     print("Bag_of_messages:%s" %list_of_messages[i])





