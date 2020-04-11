from tkinter import *
from newspaper import Article
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import numpy as np
import warnings

#Ignore Warning messages
warnings.filterwarnings('ignore')
#nltk.download('punkt') # run only one time
#nltk.download('wordnet')
#Getting article url
article = Article('https://telegra.ph/AI-project-crm-04-10')
article.download()
article.parse()
article.nlp
var1=article.text
"""
#printing variable
#print(var1)
"""

#tokenization
text=var1
sent_tokens=nltk.sent_tokenize(text) #converting the text into list of sentences 
#printing list of sentences
#print(sent_tokens)

#creating a dictionary(key:value)pair for removing punctuations
remove_punct_dict = dict( (ord(punct),None)for punct in string.punctuation)

#print punctuations 
#print(string.punctuation)

#print dictionary
#print(remove_punct_dict)

#Create a function to return list of lemmatized lowercase wordes without punctuations
def normalize(text):
  return nltk.word_tokenize(text.lower().translate(remove_punct_dict))
#printing tokenisation text  
#print(normalize(text))

#keyword matching
#Greetings input
greetings_inputs=["hey","hello","hi","sup","greetings","start","wassup","on"]
#Greetings responses from bot to user
greetings_response=["hello dear!","hey!","hey there! welcome!","hey,How r u","hey there!","hello","hey dude!wassup?"]

#Function to return random greeting response to users input
def greetings(sentence):
  #if users input is a greeting,then return a randomly chosen greetings response
  for word in sentence.split():
    if word.lower() in greetings_inputs:
      return random.choice(greetings_response)


#Genrate response
def response(user_response):
   #user_input as user input query variable
  user_response=user_response.lower() #making response lower case
  #print user queries
  #print(user_response)
  #chat bots reply for empty string
  botty_response=''
  #Append the users response ro the sentence list
  sent_tokens.append(user_response)
  #Print the sentence list after appending the users response
  #print(sent_tokens)
  #Creating a TfidfVectrorizer object
  TfidfVec=TfidfVectorizer(tokenizer=normalize,stop_words='english')
  #Convert text to a matrix of TF-IDf(Term frequency ,inverse document frequency) features
  tfidf=TfidfVec.fit_transform(sent_tokens)
  ##print TFIDf features
  #print(tfidf)
  #Get the measure of similarity(how much query and reponse is matching)
  vals=cosine_similarity(tfidf[-1], tfidf)
  #printing similarity scores
 #print(vals)
  #get the index of most similar text for a reply to user by botty
  idx=vals.argsort()[0][-2]
  #Reduce the dimensionality of vals(making it as one list)
  flat=vals.flatten()
  #sorting the list in ascending order
  flat.sort()
  #Get the most similar score to users response
  score=flat[-2]
  #printing similarity score
  #print(score)

   #If the varibale 'score' is 0 then similar response does not exist
  if(score==0):
    botty_response=botty_response+"Sorry for the Inconvenience,I dont understand that"
  else:
    botty_response=botty_response+sent_tokens[idx]
  #print chatbot response
  #print(botty_response)
  #Removing the user response from sentence token list
  sent_tokens.remove(user_response)
  return botty_response
#-------------GUI---------------
main = Tk()
main.geometry("600x500")

main.title("CRM Help Desk")


def Ask():
    user_response = field.get()
    Ans_from_bot = response(user_response)
    msgs.insert(END,"You :"+ user_response)
    msgs.insert(END,"Bot :"+Ans_from_bot)
    field.delete(0,END)
    msgs.yview(END)

frame = Frame(main)
frame.pack()
sc= Scrollbar(frame)
sc.pack(side = RIGHT,fill = Y)

msgs = Listbox(frame,width=80,height=20,yscrollcomman = sc.set)
msgs.pack(side = LEFT,fill = BOTH, pady = 10)

#creating text field
field = Entry(main,font =("Verdana",20))
field.pack(fill = X,pady =10)

#Creating send button 
btn = Button(main,text = "Ask Your Query", font = ("Verdana",20),command = Ask)
btn.pack()

#making auto click of send btn
def auto_click(event):
    btn.invoke()

#bind in the main window with keys
#key code of Enter
main.bind('<Return>', auto_click) 

#main.mainloop()
