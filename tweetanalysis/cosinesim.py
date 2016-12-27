import re
import math
from collections import Counter


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    word = re.compile(r'\w+')
    words = word.findall(text)
    return Counter(words)


def calculatescore(content_a, content_b):
    text1 = content_a
    text2 = content_b

    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)

    cosine_result = get_cosine(vector1, vector2)
    return cosine_result
dict={}
with open('D:\\education\\python\\twiiter.txt','r') as f:
    for line in f:
        key_value=line.split('\t')
        dict[key_value[0]]=key_value[1]
##################phase one clustering##########################
list_of_clusters=[]
keys_list = list(dict.keys())
keys_list.sort()
print("the number of tweets is ")
print(len(keys_list))
list_of_messages=[]
count=0
for i in range(0,len(keys_list)):

    if keys_list[i]!=0:
        print("****************************************************************************************")
        dict_of_cluster=[]
        dict_of_cluster.append(dict[keys_list[i]])
        print(dict[keys_list[i]])
        count=count+1
        for j in range(i+1,len(keys_list)):
            if  keys_list[j]!=0 and calculatescore(dict[keys_list[i]],dict[keys_list[j]])==1.0:
                #print(dict[keys_list[j]])
                dict_of_cluster.append(dict[keys_list[j]])
                keys_list[j]=0
                print(dict[keys_list[i]])
                count=count+1

        #dict_of_cluster_message={}
        #dict_of_cluster_message[dict[keys_list[i]]]=dict_of_cluster
        list_of_clusters.append(dict_of_cluster)

        list_of_messages.append(dict[keys_list[i]])
print ("the processed tweets is %d" %count)
print("after phase1 no of clusters formed is %d" %len(list_of_clusters))
print(list_of_clusters)
print(list_of_messages)
#################phase 2 clustering##############################################
def union_of_clusters(src, dest):
    dict=src
    for i in range(0,len(dest)):
        dict.append(dest[i])

    return dict
def union_of_messages(src,dest):
    list1=src.split(' ')
    list2=src.split(' ')
    final_list=list(set(list1)|set(list2))
    sentence=""
    for word in final_list:
        sentence += " " + word
    return sentence

list_of_messages2=[]
list_of_clusters2=[]
count=0
for i in range(0,len(list_of_messages)):
    if list_of_messages[i]!=[]:
        flag=0
        max=-2.0
        maxi=0
        for j in range(i+1,len(list_of_messages)):
            if list_of_messages[j]!=[]:
                score=calculatescore(list_of_messages[i],list_of_messages[j])
                if score>max and score>0.3:
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
for message in list_of_messages:
    print(message)
print(list_of_clusters)



