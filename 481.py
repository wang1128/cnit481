__author__ = 'penghao'
from numpy import *
import csv
import difflib
f = open("questions.csv")
csv_f = csv.reader(f)
question_list =[]
category_list = []
for row in csv_f:
    question_list.append(row[0])
    category_list.append(row[1])

def similar(seq1, seq2):
    return difflib.SequenceMatcher(a=seq1.lower(), b=seq2.lower()).ratio()

def recommendation(question,category):
    new_question_list=[]
    rec_list=[]
    reversed_list=[]
    for idx,cag in enumerate(category_list):
        if category in cag:

            new_question_list.append(question_list[idx])
    for element in new_question_list:
        if similar(question,element)>0.5:
            rec_list.append((element,similar(question,element)))

    if rec_list.__len__()==0:
        print ("Sorry, there is no similar questions T-T")

    return rec_list

def question():
    que = raw_input('Write your question: ')
    cag = raw_input('Category: ')
    recommendation(que,cag)
    list = recommendation("Does obseity relate to race?","Race")
    reversed_list = sorted(list, key=lambda list: list[1], reverse=True)
    print("The top 2 recommendations are :")
    print(reversed_list[0][0])
    print(reversed_list[1][0])
#print(list)
#list2=sorted(list, key=lambda list: list[1], reverse=True)
#print(list2)
#que = raw_input('Write your question: ')

#cag = raw_input('Category: ')
#recommendation(que,cag)
