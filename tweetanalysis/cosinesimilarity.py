from sklearn.feature_extraction.text import TfidfVectorizer
def calculatescore(documents):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
    from sklearn.metrics.pairwise import cosine_similarity
    result=cosine_similarity(tfidf_matrix, tfidf_matrix)
    return result



list_of_input=[]
with open('D:\\education\\python\\twiiter.txt','r') as f:
    for line in f:
        key_value=line.split('\t')
        list_of_input.append(key_value[1])
##################phase one clustering##########################
list_of_clusters=[]
print("the number of tweets is ")
print(len(list_of_input))
list_of_messages=[]
count=0
proxmitymatrix=calculatescore(list_of_input)
for i in range(0,len(list_of_input)):

    if proxmitymatrix[i][0]!=0:
        print("****************************************************************************************")
        dict_of_cluster=[]
        dict_of_cluster.append(list_of_input[i])
        print(list_of_input[i])
        count=count+1
        for j in range(i+1,len(list_of_input)):
            if  proxmitymatrix[j][0]!=0 and proxmitymatrix[i][j]>=1.0:
                #print(dict[keys_list[j]])
                dict_of_cluster.append(list_of_input[j])
                proxmitymatrix[j][0]=0
                print(list_of_input[j])
                count=count+1

        #dict_of_cluster_message={}
        #dict_of_cluster_message[dict[keys_list[i]]]=dict_of_cluster
        list_of_clusters.append(dict_of_cluster)

        list_of_messages.append(list_of_input[i])
print ("the processed tweets is %d" %count)
print("after phase1 no of clusters formed is %d" %len(list_of_clusters))
print(list_of_clusters)
print(list_of_messages)



