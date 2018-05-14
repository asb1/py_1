"""
    Hello world
"""

a="Hello world"
print a

a  = "Hello Agus"
#Mengambil kata Hello
agus = a.split(" ")
print "isi variabel 'a' adalah {s}".format(s=a)
print "contoh kode agus = a.split(\" \"), maka akan muncul "
print "Hasil {s}".format(s=agus)
#
print "Mengambil huruf awal dan akhir"
print " Huruf pertama {r} dan akhir {s} ".format(r=agus[0][0], s=agus[1][3])


remove_space = a.replace(" ", "")
print "Menghtung jumlah huruf , dan jumlah huruf 'a'"
print "Jumlah huruf = {r}, jumlah huruf 'a' = {s}".format(r=len(a), s=len(remove_space))

print "ambil salah satu kata dalam text dalam text menggunakan teknik slice"
print "kata pertama = {r} kata kedua = {s}".format(r=a[0:5], s=a[6:10])
