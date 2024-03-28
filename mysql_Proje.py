import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="FatihNida2001.",
  database ="mydatabase"
)


#mycursor = mydb.cursor()


# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"  #BİRDEN FAZLA VERİ EKLEDİĞİMİZDE BU ŞEKİL EKLERİZ
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
 

#sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"      #EKLEYECEĞİMİZ TABLO ADI BELİRTİRİZ NAME VE ADRESS COLONU BELİRTTİK VE 2 BİLGİ ALACAGINDAN 2 (%s, %s) DEĞER VERDİK


#val = ('Fatih','İstanbul Fdındıklı 18'),
#mycursor.execute(sql, val)

#mydb.commit()                                                      #Bu olmak zorunda yoksa değişiklik olmaz


#print(mycursor.lastrowid, " .kayıt eklendi.")                      #Tek veri ekledik en sonuncuyu belirtmek için  lastwrowid yazdık kaçıncı oldugunu gösterir.




# mycursor.execute('SELECT * FROM customers')                   #Bu şekilde tüm customers tblosunu erişip hepsini göstermiş oluruz.

# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)


# mycursor.execute('SELECT name,address  FROM customers')       #Burda sadece isim biligeri ve adresi almış oluruz ID almayız.
# myresult = mycursor.fetchall()                              #EĞER FETCHONE DİYİP SADECE SELECT *FROM customers dersek 1 veri verir.
# for x in myresult:
#     print(x)





# mycursor = mydb.cursor()

# sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"  #Where komutu ile adres bilgisi park lane 38 olan satırı seçme işlemi yaptık 

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)








# mycursor = mydb.cursor()

# sql = "SELECT * FROM customers WHERE address LIKE '%way%'" #Burada ise database de lıke ile içerisinde way geçen arama işlemi yaptık adress üzerinden dikkat et 

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)






# mycursor = mydb.cursor()

# sql = "SELECT * FROM customers WHERE address = %s" #Burda ise bir yer tutucuyla arama işlemi gerçekleştirdik.
# adr = ("Yellow Garden 2", )

# mycursor.execute(sql, adr)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)







# mycursor = mydb.cursor()

# sql = "SELECT * FROM customers ORDER BY name" #Bu order by sorgusu name göre alfabetik bir sıralama yapmaktadır .A dan başlar z ye kadar sıralı yapar 

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)






# mycursor = mydb.cursor()

# sql = "SELECT * FROM customers ORDER BY name DESC" #DESC  olması tersden sıralar alfabaye göre z en baştan gibi düşün 

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)




# mycursor = mydb.cursor()

# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"       #Adresi mountain 21 olan tüm kayıtları sile işlemi 
                                                                    #Where olmak zorunda hangisini sileceğini belirtir olmazsa tüm tabloyu siler dikkat et !!!
# mycursor.execute(sql)

# mydb.commit()                                             #Bu ekeleme güncelleme silme işlemlerinde herzaman olmak zorunda yoksa yaptıgımız işlem kayıtlı kalmaz 

# print(mycursor.rowcount, ".kayıt silinmiştir")









# mycursor = mydb.cursor()

# sql = "DELETE FROM customers WHERE address = %s" #Bu da yer tutucu ile yaptıgımız silme işlemi 
# adr = ("Yellow Garden 2", )

# mycursor.execute(sql, adr)

# mydb.commit()

# print(mycursor.rowcount, ". kayıt  silindi.")





# mycursor = mydb.cursor()

# sql = "DROP TABLE customers"    #Bu işlem Tablo silme işlemi gerçekleştirir.

# mycursor.execute(sql)








# mycursor = mydb.cursor()

# sql = "DROP TABLE IF EXISTS customers"  #Bu ifade ise hata almamak için varsa customers tablosunu sil demektir 

# mycursor.execute(sql)








# mycursor = mydb.cursor()

# sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"  #Bu bir güncelleme sorgusudur,walley 345 yazan yeri canyon 123 ile değiştir güncelle demektir.

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, ".kayıt güncellendi.")





# mycursor = mydb.cursor()

# sql = "UPDATE customers SET address = %s WHERE address = %s" #Bu şekilde de yer tutucuyla güncelleme yapabiliriz bu daha sağlıklı olanıdır.
# val = ("Valley 345", "Canyon 123")

# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record(s) affected")








# mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM customers LIMIT 5")  #Bu ifade müşteriler tablosundan ilk 5 kaydı seçin demektir.

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)







# mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2") #Bu ifade 2 offset demek ilk 3 kaydı alma 3 den sonrasını göster demektir.

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)




# mycursor = mydb.cursor()
# #mycursor.execute("CREATE TABLE users (name VARCHAR(255), address VARCHAR(255), fav INT)")  #Yeni bir tablo luşturduk


# sql = "INSERT INTO users (name, address,fav) VALUES (%s, %s,%s)" 
# val = [
#   ('Peter', 'Lowstreet 4', 101),
#   ('Amy', 'Apple st 652', 102),
#   ('Hannah', 'Mountain 21', 103),
#   ('Michael', 'Valley 345', 104),
#   ('Sandy', 'Ocean blvd 2', 105),
#   ('Betty', 'Green Grass 1', 106),
#   ('Richard', 'Sky st 331', 107),
#   ('Susan', 'One way 98', 108),                                           #  yENİ TABLOYA VERİ EKLEDİK 
#   ('Vicky', 'Yellow Garden 2', 109),
#   ('Ben', 'Park Lane 38', 110),
#   ('William', 'Central st 954', 111),
#   ('Chuck', 'Main Road 989', 112),
#   ('Viola', 'Sideway 1633', 113),
#   ('Lexis', 'fox 1633', 114)
# ]
# mycursor.executemany(sql, val)
# mydb.commit()







# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE products (name VARCHAR(255), id INT)")         #ürünler adında tablo oluşturduk.



#mydb.commit()










# mycursor = mydb.cursor()


# sql = "INSERT INTO products (name,id) VALUES (%s,%s)" 
# val = [
#   ('Çikolata', 5),
#   ('Elma', 10),                       #YENİ TABLOYA VERİ EKLEDİK 
#   ('Dondurma', 15)
# ]
# mycursor.executemany(sql, val)
# mydb.commit()









# mycursor = mydb.cursor()

# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   INNER JOIN products ON users.fav = products.id"          #Birleştirme işlemi 

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)




# SELECT ifadesi, veritabanından belirli sütunları seçmek için kullanılır. 
# users ve products tablolarından sütunlar seçilir. users.name AS user ifadesi, 
# users tablosundaki name sütununu kullanarak kullanıcı adlarını alır ve bu sütunu user 
# adında bir alias'a (takma ad) dönüştürür. Benzer şekilde, 
# products.name AS favorite ifadesi, products tablosundaki name sütununu kullanarak ürün 
# adlarını alır ve favorite adında bir alias'a dönüştürür.

# INNER JOIN ifadesi, iki tabloyu belirli bir koşula göre birleştirmek için kullanılır. 
# Bu durumda, users tablosundaki fav sütunu ile products tablosundaki id sütunu eşleştirilir. 
# Yani, her kullanıcının favori ürününün adını almak için kullanıcı adı ile ürün adı birleştirilir.

# mycursor.execute(sql) ifadesi, belirtilen SQL sorgusunu veritabanında çalıştırır.

# myresult = mycursor.fetchall() ifadesi, sorgunun veritabanından döndürdüğü tüm sonuçları alır.

# Son olarak, for x in myresult: döngüsü, her bir satır için sonuçları döngü içinde işler. 
# Bu durumda, her bir x satırında bir kullanıcı adı ve 
# bu kullanıcının favori ürünü adı bulunur ve ekrana yazdırılır.






