import MySQLdb
#open database connection
db = MySQLdb.connect("localhost","root","root","training")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print "Database version : %s " % data
db.close()
