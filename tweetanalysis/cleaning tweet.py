import json
import re
import string
from nltk.corpus import stopwords
import nltk
##with open('D:/Python_Packages/AzharJudgementDay.json','r') as f:
##    line = f.readline()
##    tweet = json.loads(line)
##    print(tweet)
##    print(json.dumps(tweet, indent=4))
##
infp = open('D:\\education\\python\\twiiter.json','r')
#str = fobj.readline()
# cur_pos = fobj.tell()
# created_time = str.split('{"created_at":"')[1].split('+0000')[0]
# ID = str.split('","id":')[1].split(',"id_str":"')[0]
# tweet = str.split('","text":"')[1].split('","source":"')[0]

lines = infp.readlines()
def preprocessing(tweet_text):
    tweet_text = tweet_text.replace("\n"," ").replace("\r"," ")
    tweet_text = tweet_text.replace('RT',"")
    tweet_text = tweet_text.lower()
    tweet_text = re.sub('((www\.[\s]+)|(https://[^\s]+)|(http.*[^\x00-\x7f]+[^\s]*))',"",tweet_text)
    tweet_text = re.sub('@[^\s]+','',tweet_text)
    tweet_text = re.sub('[\s]+', ' ', tweet_text)
    tweet_text = re.sub('#([^\s]+)', r'\1', tweet_text)
    tweet_text = re.sub('([^\x00-\x7f]+)',"",tweet_text)
    tweet_text = ("".join(pun for pun in tweet_text if pun not in string.punctuation)).strip()
    tweet_text = ' '.join([word for word in tweet_text.split() if word not in stopwords.words("english")])
    return tweet_text
def remove_adjectives(pre_processed_tweet_text):
    tweet_token = nltk.word_tokenize(pre_processed_tweet_text)
    tagged = nltk.pos_tag(tweet_token)
    adj_rem =''
    for i in range(0,len(tagged)):
        tup = tagged[i]
        if tup[1] not in ('JJ','JJR','JJS'):
            adj_rem +=' '+tup[0]
    tweet_text_adj = adj_rem.strip()
    return tweet_text_adj


for i in range(0,len(lines)):
    if lines[i] not in ('\n','\r\n') :
        jtweet = json.loads(lines[i])
        #created_time = jtweet["created_at"]
        if "id" in jtweet:
            tweet_id = jtweet["id"]
            tweet_text = jtweet["text"]
            processed_tweet_text = preprocessing(tweet_text)
            #processed_tweet_text = remove_adjectives(pre_processed_tweet_text)
            #if processed_tweet_text:
            outfp = open('D:\\education\\python\\twiiter.txt','a', encoding="utf-8")
            outfp.write(str(tweet_id)+"\t")
                #outfp.write(created_time+"\t")
            outfp.write(processed_tweet_text+"\n")
    else:
        continue

infp.close()
outfp.close()



