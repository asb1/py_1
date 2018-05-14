print """
Buat variabel seperti di bawah ini

data_tuple = (11,12,12,35)
data_list = ["agus","bayu","candra"]
data_obj = {
    "nama_orang_tua" : "Hasan"
    "umur" : 50
}


Buat outputdari kata di atas seperti contoh di bawah ini :
Nama Anak :
nama:agus
umur :13

data keluarga:
{
    "nama_orang_tua" : "Hasan",
    "umur":50,
    "anak" {
     "nama":"bayu"
     "umur": 12
    }
}




"""

#=============
data_tuple = (11,{'a':100},12,34,35)
data_list = ["agus","bayu","candra"]
data_obj = {
    "nama_orang_tua" : ["Hasan","Siti"],
    "umur" : 50
}

print "output: Nama anak : "
print "nama: {s}".format(s=data_list[0])
print "umur: {s}".format(s=data_tuple[1].get("a"))
print ""
print "data keluarga"
print " nama_orang_tua : {s}".format(s=data_obj.get("nama_orang_tua")[1])
print " anak: {s}, umur : {t}".format(s=data_list[1], t=data_tuple[0])
