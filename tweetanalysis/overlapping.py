"""
 @desc:calculate the overlapping similarity between two strings
 @:param:string1:first string, string2 second string
 @:return:float value ,which is similarity of two i/p strings

"""
def calculatescore(string1,string2):
    list1=string1.split(' ')
    list2 = string2.split(' ')
    intersect=list(set(list1)&set(list2))

    len1=len(set(list1))
    len2=len(set(list2))

    if(len1<len2):

        jc=len(intersect)/len1

    else:
        jc=len(intersect)/len2

    return jc

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
    list1=src.split(' ')
    list2=dest.split(' ')
    final_list=list(set(list1)|set(list2))
    sentence=""
    for word in final_list:
        sentence += " " + word
    return sentence

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
"""
for message in list_of_messages:
    print(message)
print(list_of_clusters)
"""
for i in range(0,len(list_of_clusters)):
     list_of_tweets_in_cluster=list_of_clusters[i]
     print("***************************************************************************************")
     for j in range(0,len(list_of_tweets_in_cluster)):
         print(list_of_tweets_in_cluster[j])
     print("Bag_of_messages:%s" %list_of_messages[i])



