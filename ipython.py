import pickle
f=open("book_details.dat", "rb")
rec=pickle.load(f)
print(rec)
