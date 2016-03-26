import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
from _ctypes import Array
from matplotlib import style
import pandas as pd
from pandas import DataFrame, read_csv
from docutils.nodes import inline

names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]

BabyDataSet = list(zip(names,births))

df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])


import os
path_s = 'C:\\Beths_PySandbox'
df.to_csv(os.path.join(path_s, 'births1880.csv'), index=False, header=False)

Location = r'C:\\Beths_PySandbox\births1880.csv'

df=pd.read_csv(Location, names=['Names','Births'])

df['Births'].plot()
MaxValue = df['Births'].max()
MaxName = df['Names'][df['Births']==df['Births'].max()].values
Text = str(MaxValue)+ "-" + MaxName

plt.annotate(Text, xy=(1, MaxValue), xytext=(8,0), xycoords=('axes fraction', 'data'), textcoords='offset points')

print("The most popular name")
df[df['Births']== df['Births'].max()]

plt.show()








""""a = np.arange(15).reshape(3,5)

print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
print(type(a))"""


#a = np.arange( 10, 30, 5)
#print(a)

#a = np.linspace( 0, 2, 9)
#print(a)

#a = np.arange(6) #1d Array
#b = np.arange(12).reshape(4, 3)
#c = np.arange(24).reshape(2, 3, 4)
#print(c)

#Consine and Sine plot
""""X = np.linspace( -np.pi, np.pi, 256, endpoint=True)
S = np.sin(X)
C = np.cos(X)
plt.figure(figsize=(10,6), dpi=80)
plt.xlim(X.min()*1.1, X.max()*1.1)
plt.ylim(C.min()*1.1, C.max()*1.1)
plt.plot(X,S, color="red", linewidth=2.5, linestyle="-")
plt.plot(X,C, color="blue",linewidth=2.5, linestyle="-")
plt.show()"""


# Playing with Tuples    
"""def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))
        
    t.sort(reverse=True)
    return t 


words = ('Beth', 'Kevin', 'Mitchell')
sort_by_length(words)    

f = sort_by_length(words)
print(f)"""

#Histogram
"""mu, sigma = 5, 0.5
v = np.random.normal(mu, sigma, 10000)
plt.hist(v, bins=50, normed=1)
plt.show()"""

#Matplotlib
 
"""style.use('ggplot')

x,y = np.loadtxt('data.csv', unpack=True, delimiter = ',')


plt.plot(x,y)
 
#plt.plot(x,y,'g', label='line one', linewidth=5)
 
plt.title('Beth\'s Line Chart') 
plt.ylabel('Y axis')
plt.xlabel('X axis')
#plt.legend() 
plt.show()"""

    

