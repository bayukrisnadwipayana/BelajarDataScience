#!/usr/bin/python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

x=np.array([7,6,6,1,2,2])
y=np.array([6,6,5,3,4,2])
c=np.array(['bad','bad','bad','good','good','good'])

x_baru=3
y_baru=5
k=3

def JarakBaruX(x,x_baru):
	return x_baru-x

def JarakBaruY(y,y_baru):
	return y_baru-y

df=pd.DataFrame({'x':x,'y':y,'c':c})

#hitung jarak euclidean
df['jarak x']=JarakBaruX(df['x'],x_baru)
df['jarak y']=JarakBaruY(df['y'],y_baru)
df['kuadrat jarak x']=df['jarak x']**2
df['kuadrat jarak y']=df['jarak y']**2
df['total jarak']=(df['kuadrat jarak x']+df['kuadrat jarak y'])**0.5

#nilai sebelum di sorting
print("data sebelum disorting")
print(df)
print("\n")
#cetak nilai sorting
print("data setelah disorting")
print(df.sort_values(['total jarak']))
print("\n")
#sorting nilai ascending dan nilai terkecil
print(f"klasifikasi {x_baru},{y_baru} termasuk dalam",df.sort_values(['total jarak']).iloc[0])

#plot data
plt.scatter(x,y)
plt.show()