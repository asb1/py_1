#perulangan
list_nama = ["Indra", "Asep", "Ujang", "Firman"]
list_alamat = ["Jl. Panjang", "Jl. Pejuang", "Jl. Abdul Muis", "Jl. Sudirman"]
list_umur = ["12", "13", "10", "25"]
#print "Buat data dengan output ber bentuk object"
#print """
#Buat struktur data dalam file seperti contoh dibawah ini
#Nama: Indra
#Alamat: Jl. Pejuang
#Umur: 10
#
#----------------
#
#Nama: Indra
#Alamat: Jl. Pejuang
#Umur: 10
#
#
#----------------
#
#Nama: Indra
#Alamat: Jl. Pejuang
#Umur: 10
#
#"""
for item in list_nama:
    pass
    for item2 in list_alamat:
        pass
        for item3 in list_umur:
            pass
    list_nama2 ={
        'nama':item,
        'alamat':item2,
        'umur':int(item3)
    }
    print list_nama2

list_data=[]
for item in range(0,4):
    data = {
        "nama":list_nama[item],
        "alamat":list_alamat[item],
        "umur":list_umur[item]
    }
    list_data.append(data)
for item in list_data:
    print item



# Contoh menulis file
new_file = open("file.txt","wb+")
for item in list_data:
    data = """
    Nama:{n}
    Alamat:{a}
    Umur:{u}
    ---------------------
    """.format(n=item.get('nama'),a=item.get('alamat'),u=item.get('umur'))
    new_file.writelines(data)

new_file.close()

print "Menggunakan ==count=="
count = 0
while (count < 4):
    print "Nama :{f}".format(f=list_nama[count])
    print "Alamat :{f}".format(f=list_alamat[count])
    print "Umur :{f}".format(f=list_umur[count])
    print '--------------------------------'
    count = count +1

print '------Menggunakan for---------------'
for item in list_nama:
    pass
    for item2 in list_alamat:
        pass
        for item3 in list_umur:
            pass
    print "nama= ",item
    print "alamat=",item2
    print "umur=",item3
    print "---------------xxx----------------"


list_nama = ["Asep Indrayana", "Asep Subagja", "Muh Husen", "M Ali", "Dadang", "Moh Nuh", "Ali Hasan"]
#print """
#Buat data list baru dengan kelompok:
#1. Awalan nama 'M'
#2. Awalan nama 'A'
#3. Awalan nama 'Asep'
#4. Awalan nama "Muh"
#"""

item = [item for item in list_nama if item[0]=="M"]
print "1. Awalan nama 'M' :", item
item = [item for item in list_nama if item[0]=="A"]
print "2. Awalan nama 'A' :", item
item = [item for item in list_nama if item[0]=="A" and item [1]=="s"]
print "3. Awalan nama 'Asep' :", item
item = [item for item in list_nama if item[:4]=="Asep"]
print "3. Awalan nama 'Asep' :", item
item = [item for item in list_nama if item[0]=="M" and item [1]=="u"]
print "4. Awalan nama 'Muh' :", item
item = [item for item in list_nama if item[:3]=="Muh"]
print  "4. Awalan nama 'Muh' :", item
