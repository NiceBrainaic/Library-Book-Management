import pickle
f=open("book_data.dat","wb")
rec={'Story Book': ['Harry Potter', 'Wimpy Kid', 'Charlie And The Chocolate Factory'], 'Autobiography': ['The Diary Of A Young Girl', 'Wings Of Fire'], 'Comic': ["Captain America"], 'Novel': ['The Lord Of the Rings', 'Song Of Solomon']}
pickle.dump(rec,f)
f.close()
