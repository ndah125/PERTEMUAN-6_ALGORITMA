#menghitung luan dan keliling lingkaran dengan jari-jari math
import math

#minta input jari-jari
jari_jari =float(input("masukkan jari_jari: "))

#hitung luas llingkaran
luas = (math.pi * jari_jari**2)

#hitung keliling lingkaran
keliling = 2* math.pi * jari_jari

#bulatan hasil bilangan
luas_bulat = round(luas,2)
keliling_bulat =round(keliling)


#tampilkan hasil
print("luas lingkaran(dibulatkan):",luas-bulat)
print("keliling lingkaran(dibulatkan):",keliling_bulat)
