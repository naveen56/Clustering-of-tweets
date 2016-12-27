def calculatescore(string1,string2):

    intersect=list(set(string1)&set(string2))
    union=list(set(string1)|set(string2))

    jc=len(intersect)/len(union)
    print(jc)
    return jc


dict={}
with open('D:\\education\\python\\twiiter.txt','r') as f:
    for line in f:
        key_value=line.split('\t')
        dict[key_value[0]]=key_value[1].split(' ')
##################calculating proximity matrix##########################

keys_list = list(dict.keys())
list_of_score=[]
for i in range(0,len(dict)):
    individual_list=[]
    for j in range(i+1,len(dict)):
        individual_list.append(calculatescore(dict[keys_list[i]],dict[keys_list[j]]))
    list_of_score.append(individual_list)

print(list_of_score)





