'''docstring'''
import pickle
f=open("book_rent.dat","rb")
rec=pickle.load(f)
print(rec)
f.close()
