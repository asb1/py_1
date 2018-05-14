print "Buat huruf 'b' menjadi 6"
a= ("b")*6
print "output = {s}".format (s=a)

print ""
print "Buat beberapa variable berisi string dan integer , lalu buat print dalam satu kalimat"
b = "Bagus"
c = "Citra"
d = b + c
e = 123
f = 456
g = e + f
print "output = {s}".format (s=d)
print "output = {s}".format (s=g)

print "Buat sebuah paragraf yang berisikan soal matematika dengan memanfaatkan variable yang sudah dibuat"
h = """
{s} mempunyai {t} kelereng;
{u} mempunyai {v} kelereng
Jumlah kelereng semuanya = {w} kelereng
""".format (s=b, t=e, u=c, v=f, w=g)

print h
