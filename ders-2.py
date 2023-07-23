# 2 şekilde tablo oluşturabiliriz.


# 1.yöntem : sql server a özel menüler üzerinden tablo oluşturma ,
# 2.yöntem : komut ile tablo oluşturma

# örnek olarak öğrenci veri tabanı oluşturacağız,

# tabloda şu sütunlar olacak . 
# 1- öğrenci no
# 2- Öğrenci adı
# 3- öğrenci soyadı
# 4- Öğrenci TC Kimlik No
# 5- Öğrenci Kayıt Tarihi
# 6- Erkekmi ? burası önemli. cinsiyet yazdığımızda 1 mi erkek 0 mi erkek olduğu bazen karışabilir. erkekmi sorusuna 0 yazarsak erken 0 yazarsak erkek değil olarak algılanmış olur.

# rows = satırlar
# columns = sütunlar


# tablo oluşturma : 

# Column name istediğimiz bir name verebiliriz ancak data type için aşağıdakilerden birtanesini seçmemiz gerekir.

# 1- Sayısal Veri Tipleri:

# INT: 32 bitlik bir işaretli tamsayı. Örneğin, -2,147,483,648 ile 2,147,483,647 arasındaki değerleri alır.
# BIGINT: 64 bitlik bir işaretli tamsayı. Çok büyük tamsayı değerleri için kullanılır.
# FLOAT(n): Ondalık sayıları saklamak için kullanılır. "n" parametresi, sayıların maksimum önceki basamak sayısını belirler.

# 2- Karakter Veri Tipleri:

# CHAR(n): Sabit uzunluktaki karakter dizileri için kullanılır. "n" parametresi, karakter dizisinin uzunluğunu belirtir.
# VARCHAR(n): Değişken uzunluktaki karakter dizileri için kullanılır. "n" parametresi, karakter dizisinin maksimum uzunluğunu belirtir.
# TEXT: Uzun metin verilerini saklamak için kullanılır.

# 3- Tarih ve Saat Veri Tipleri:

# DATE: Yıl, ay ve gün bilgisi içeren tarih verileri için kullanılır.
# TIME: Saat, dakika ve saniye bilgisi içeren saat verileri için kullanılır.
# DATETIME: Tarih ve saat bilgisi içeren veriler için kullanılır.

# 4- Mantıksal Veri Tipleri:

# BIT: True (1) veya False (0) değerlerini saklamak için kullanılır.
# BOOL: BIT veri tipine benzer şekilde, mantıksal verileri saklamak için kullanılır.

# 5- Para Veri Tipleri:

# MONEY: Sabit noktalı sayılar olarak para birimi değerlerini saklamak için kullanılır.
# SMALLMONEY: MONEY veri tipine benzer ancak daha küçük değerler için kullanılır.

# 6- Binary Veri Tipleri:

# BINARY(n): Sabit uzunluktaki binary verileri saklamak için kullanılır. "n" parametresi, verinin uzunluğunu belirtir.
# VARBINARY(n): Değişken uzunluktaki binary verileri saklamak için kullanılır. "n" parametresi, verinin maksimum uzunluğunu belirtir.

# 7- Diğer Veri Tipleri:

# XML: XML verilerini saklamak için kullanılır.
# UNIQUEIDENTIFIER: GUID (Global Unique Identifier) değerlerini saklamak için kullanılır.


# önemli : Allow Nulls - boş bırakılmasına izin ver anlamına gelir.

# önemli : database de türkçe karakter olmamalı.


