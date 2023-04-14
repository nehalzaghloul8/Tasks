from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

text=input(" Inter Your Text : ")
print("1: word tokenize 2: sent tokenize 3: o text")
choice=input("Choose Your Num : ")
if choice=="1":
    print(word_tokenize(text))
elif choice == "2":
    print(sent_tokenize(text))
elif choice =="3":
    print(text)
    
else:
    print("wrong choice ")







