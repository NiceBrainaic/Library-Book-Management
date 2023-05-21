# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 23:17:37 2021

@author: sharr
"""
import pickle
f=open("book_details.dat", "wb")
data1=["Harry Potter", "Story Book", "J. K. Rowling", "1997", "9780050666319"]
data2=[ "Wimpy Kid", "Story Book","Jeff Kinney", "2007", "9567458325641"]
data3=["Charlie And The Chocolate Factory", "Story Book", "Roald Dahl", "1979", "97642583957641"]
data4=["Diary Of A Young Girl", "Autobiography", "Anne Frank", "1947", "9356871521486"]
data5=["Wings Of Fire", "Autobiography", "A.P.J Abdul Kalam", "1999", "935612034872"]
data6=["Captain America", "Comic", "Joe Simon", "1941", "9730256014829"]
data7=["Lord Of The Rings", "Novel", "J. R. R. Tolkien", "1954", "9785234682186"]
data8=["Song Of Solomon", "Novel", "Toni Morrison", "1977", "9730264852941"]
total=[data1, data2, data3, data4, data5, data6, data7, data8]
pickle.dump(total,f)

