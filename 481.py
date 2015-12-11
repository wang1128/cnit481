__author__ = 'penghao'
from numpy import *
import csv
import difflib
f = open("question.csv")
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
    for idx,cag in enumerate(category_list):
        if category in cag:

            new_question_list.append(question_list[idx])
    for element in new_question_list:
        if similar(question,element)>0.5:
            print(element)
            print(similar(question,element))


#print(category_list.index("Diet"))
recommendation("Does obseity relate to race?","Race")


que = raw_input('Wirte your question: ')

cag = raw_input('Category: ')
recommendation(que,cag)
