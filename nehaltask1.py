Doc_1 = "new home sales top forecasts"
Doc_2 = "home sales rise in July"
Doc_3 = "increase in home sales in July"
Doc_4 = "July new home sales rise"

Docs =[Doc_1,Doc_2,Doc_3,Doc_4]
print(Docs)
#getting non repeated terms in the documents
unique_terms= set()
for doc in Docs:
    for term in doc.split():
        unique_terms.add(term)
# print(unique_terms)

#creating inverted index in the  a dictionary
inverted_index = {}
for i, doc in enumerate(Docs):
    for term in doc.split():
        if term in inverted_index:
            inverted_index[term].add(i)
        else: inverted_index[term] = {i}
# print(inverted_index)



#posting list for the term "home"
term_=input("Enter the word or the term:")
posting_list = inverted_index[term_]
print(posting_list)