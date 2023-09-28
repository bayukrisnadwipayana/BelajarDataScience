#!usr/bin/python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#buat data sembarang dalam hal ini dibuat data penjualan barang yaitu harga dan permintaan barang
kuantitas=np.array([7,7,6,5,4,4,3,3,2,1])
harga=np.array([10,12,15,20,25,25,35,40,40,45])

#buat dataframe dengan pandas dari data yang kita buat sembarang
df=pd.DataFrame({'kuantitas':kuantitas,'harga':harga})


#membuat kolom baru kuantitas pangkat 2 dan mengkuadratkan nilai pada kolom kuantitas
df['kuadrat kuantitas']=[x**2 for x in kuantitas]

#membuat kolom baru harga pangkat 2 dan mengkuadratkan nilai pada kolom harga
df['kuadrat harga']=[cost**2 for cost in harga]

#mengalikan hasil kolom kuantitas dan harga
df['kuantitas x harga']=df.kuantitas*df.harga

#menjumlahkan masing masing kolom

#menjumlahkan kolom kuantitas dan simpan pada variabel Q_total
Q_total=sum(kuantitas)

#menjumlahkan kolom harga dan simpan pada variabel P_total
P_total=sum(harga)

#menjumlahkan kolom kuadrat kuantitas dan simpan pada variabel Q2_total
Q2_total=sum(df['kuadrat kuantitas'])

#menjumlahkan kolom kuadrat harga dan simpan pada variabel P2_total
P2_total=sum(df['kuadrat harga'])

#menjumlahkan kolom kuantitas x harga dan simpan pada variabel QxP
QxP=sum(df['kuantitas x harga'])

#cetak data frame
print(df)

#save data dalam bentuk csv
df.to_csv("PermintaanBarang.csv")

'''
masukan rumus regresi linier mencari konstanta
c=((sy.sx^2)-(sx.sxy))/n.sx^2-(sx)^2
'''
konstanta=((P_total*Q2_total)-(Q_total*QxP))/((len(df)*Q2_total)-(Q_total**2))
print("konstanta adalah: ",konstanta)

'''
masukan rumus regresi linier mencari koefisien regresi
m=((n.sxy)-(sx.sy))/n.sx^2-(sx)^2
'''

gradien=((len(df)*QxP)-(Q_total*P_total))/((len(df)*Q2_total)-(Q_total**2))
print("gradien adalah: ",gradien)


model=(gradien*kuantitas)+konstanta
absis=np.arange(0,9,1)

def Prediksi_Harga(kuantitas,gradien=gradien,konstanta=konstanta):
	harga=(kuantitas*gradien)+konstanta
	return harga

print("harga barang adalah: ",int(Prediksi_Harga(5)))

#menciptakan persamaan garis lurus
ordinat=Prediksi_Harga(absis)

#buat visualisasi data
plt.title("Regresi Linier")
plt.plot(absis,ordinat,'r')
plt.scatter(kuantitas,harga)
plt.xlabel("Kuantitas")
plt.ylabel("Harga")
plt.show()
