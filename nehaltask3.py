from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import PorterStemmer

snowb = SnowballStemmer(language='english')
ports = PorterStemmer()

text=input(" Inter Your Text : ")
print("1: word tokenize 2: sent tokenize 3: o text 4: stem 4.1: SnowballStemmer 4.2: PorterStemmer")
choice=input("Choose Your Num :")

if choice=="1":
    print(word_tokenize(text))
elif choice == "2":
    print(sent_tokenize(text))
elif choice =="3":
    print(text)
elif choice =="4.1":
    print(snowb.stem(text))
elif choice =="4.2":
    print(ports.stem(text))

else:
    print("wrong choice")







