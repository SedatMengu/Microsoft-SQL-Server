#daha önce oluşturduğumuz tabloyu bu sefer de komutlar yardımı ile oluşturacağız. (Query)

# 1- Select Sorgusu ( Veri Sorgulama)
# 2- insert into sorgusu ( veri ekleme)
# 3- update sorgusu (veri güncelleme)
# 4- delete from sorgusu ( veri silme)
# 5- join sorgusu ( tabloları birleştirme)
# 6- group by sorgusu ( gruplama)
# 7- order by sorgusu ( sıralama)
# 8- where sorgusu ( filtreleme)
# 9- like sorgusu (yerine koyma)
# 10- distinct sorgusu ( tekilleştirme)
# 11- between sorgusu ()
# 12- in sorgusu
# 13- not in sorgusu
# 14- null sorgusu
# 15- not null sorgusu
# 16- count sorgusu
# 17- sum sorgusu
# 18- avg sorgusu
# 19- max ve min sorgusu
# 20- having sorgusu
# 21- case sorgusu
# 22- subquery sorgusu


# 01- creat table / tablo oluşturma
# 02- drop table / tablo silme
# 03- alter table / tablo güncelleme
# 04- truncate table / tablo içeriğini temizleme
# 05- rename table / tablo adını değiştirme
# 06- crate index / bir veya birden fazla sütuna index eklemeye
# 07- drop index / var olan indexi silme


# select

# truncate
# comment
# rename

# insert
# update
# delete
# merge

# grant
# revoke

# transaction
# commit
# rollback
# sacepoint

# QUERY üzerinden tablo oluşturma ,

# CREATE TABLE Ogrenci2(                                      / Ogrenci2 adında bir tablo oluşturdu.
#     OgrenciNo int NOT NULL , 
#     OgrenciAdi varchar(30) NOT NULL , 
#     OgrenciSoyadi carchar(30) NOT NULL ,
#     TCKimlikNo char(11) NOT NULL ,
#     KayitTarihi date NOT NULL,
#     ErkekMi bit NOT NULL,
# ) 

# DROP TABLE Ogrenci2                                         / Ogrenci2 adındaki tabloyu komple sildi.

# ALTER TABLE Ogrenci2 ADD DogumTarihi date                   / Ogrenci2 adındaki tabloya DogumTarihi kolonunu date data tipinde ekledi,

# ALTER TABLE Ogrenci2 ALTER COLUMN DogumTarihi date NOT NULL; / Ogrenci2 adındaki tabloda DogumTarihi kolonunu güncelledi.