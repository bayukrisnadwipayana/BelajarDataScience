#!usr/bin/python

#import module yang diperlukan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
persamaan gas ideal berdasarkan temperatur dan tekanan gas
T~P
'''

#buat array data suhu dan tekanan berdasarkan hasil penelitian
suhu=np.array([0,5,10,12,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,35,40,45,50,55,60,65,70,80,90,92,94,96,98,100,102,104,106,108,110])
tekanan=np.array([4.58,6.54,9.21,10.52,11.99,13.63,14.53,15.48,16.84,17.54,18.65,19.83,21.07,22.38,23.76,25.21,26.74,28.35,30.04,31.82,42.2,55.3,71.9,97.5,118.0,149.4,187.5,233.7,355.1,525.8,567.0,610.9,657.6,707.3,760.0,815.9,875.1,937.9,1004.6,1074.6])

#buat dataframe dari dua data
df=pd.DataFrame({'Suhu':suhu,'Tekanan':tekanan})

#buat tabel bantu kuadrat suhu dan kuadratkan kolom suhu dan jumlahkan total kuadrat suhu
df["kuadrat_suhu"]=[x**2 for x in suhu]
totalkuadratsuhu=sum(df["kuadrat_suhu"])

#buat tabel bantu suhu x tekanan dan jumlah suhu x tekanan
df['suhu x tekanan']=df.Suhu*df.Tekanan
jumlah_suhuxtekanan=sum(df['suhu x tekanan'])

#buat tabel bantu kuadrat suhu x tekanan dan jumlah kuadrat suhu x tekanan
df['kuadrat suhu x tekanan']=df['kuadrat_suhu']*df.Tekanan
jumlah_kuadratsuhuxtekanan=sum(df['kuadrat suhu x tekanan'])

#pangkat 3 suhu
df['pangkat tiga suhu']=[x**3 for x in suhu]
totalpangkat3suhu=sum(df['pangkat tiga suhu'])

#pangkat 4 suhu
df['pangkat empat suhu']=[x**4 for x in suhu]
totalpangkat4suhu=sum(df['pangkat empat suhu'])

#jumlah suhu
jumlah_suhu=sum(df.Suhu)

#jumlah tekanan
jumlah_tekanan=sum(df.Tekanan)

#hitung banyak data
banyak_data=len(df)

#cetak dataframe
print(df)

#koefisien regresi kuadrat
koefisien=np.polyfit(suhu,tekanan,2)
polinomial=np.poly1d(koefisien)
print(koefisien)
print(polinomial)

#buat matriks tiga dimensi dari dataframe
model1=np.array([[banyak_data,jumlah_suhu,totalkuadratsuhu],[jumlah_suhu,totalkuadratsuhu,totalpangkat3suhu],[totalkuadratsuhu,totalpangkat3suhu,totalpangkat4suhu]])
model2=np.array([jumlah_tekanan,jumlah_suhuxtekanan,jumlah_kuadratsuhuxtekanan])
modelakhir=np.linalg.solve(model1,model2)
# print("koefisien regresi linier a,b,c adalah: ",modelakhir)
# print(modelakhir[2])
# print(modelakhir[1])
# print(modelakhir[0])

#visualisasi model berdasarkan sebaran data pada dataframe
model_absis=np.arange(0,115,1)
model_ordinat=88.13076448480557-(6.9290936191660295*model_absis)+(0.13761243001124693*(model_absis**2))
model_ordinat_150=88.13076448480557-(6.9290936191660295*150)+(0.13761243001124693*(150**2))

def PrediksiTekanan(suhu,a=modelakhir[0],x1=modelakhir[1],x2=modelakhir[2]):
	tekanan=a-(suhu*x1)+(x2*suhu*suhu)
	return tekanan

print("Tekanan Pada Suhu 150 adalah: ",PrediksiTekanan(150))
print("Tekanan Pada Suhu model_ordinat_150: ",model_ordinat_150)
	
#tentukan tekanan apabila suhu mencapai 150 derajat celcius
plt.scatter(suhu,tekanan)
plt.xlabel("Suhu")
plt.ylabel("Tekanan")

plt.plot(model_absis,model_ordinat)
plt.show()

