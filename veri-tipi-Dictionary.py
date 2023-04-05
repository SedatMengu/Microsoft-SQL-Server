# sözlüklerdeki key ler string veya integer olmak zorundadır.
# sözlüklerdeki value ler herhangi bir veri tipinde olabilirler.
# sözlüklerde index olmaz, yerine keys vardır.

kisi = { "isim" : "Ali",
        "soyisim" : "Şeker",
        "yaş" : 22,
        "hobiler" : ["Müzik Dinlemek" , "Resim Yapmak" , "Kitap Okumak"]
}

# dictionary de yazdırma işlemleri.
# index yerine keys ler kullanılır.
print(kisi)                         # / {'isim': 'Ali', 'soyisim': 'Şeker', 'yaş': 22, 'hobiler': ['Müzik Dinlemek', 'Resim Yapmak', 'Kitap Okumak']}
print(kisi["isim"])                 # / Ali
print(kisi["soyisim"])              # / Şeker
print(kisi["yaş"])                  # / 22
print(kisi["hobiler"])              # / ['Müzik Dinlemek', 'Resim Yapmak', 'Kitap Okumak']

# keys değiştirme

kisi ["isim"] = "Ahmet"
kisi ["soyisim"] = "Kara"
kisi ["yaş"] = 32
kisi ["hobiler"] = ["Golf Oynamak" , "Yüzmek" ,"Tenis Oynamak"]

print(kisi)                         # / {'isim': 'Ahmet', 'soyisim': 'Kara', 'yaş': 32, 'hobiler': ['Golf Oynamak', 'Yüzmek', 'Tenis Oynamak']}
print(kisi["isim"])                 # / Ahmet
print(kisi["soyisim"])              # / Kara
print(kisi["yaş"])                  # / 32
print(kisi["hobiler"])              # / ['Golf Oynamak', 'Yüzmek', 'Tenis Oynamak']

# aynı anda birden fazla value değiştirmek:

kisi.update({"isim" : "Tarkan" , "Soyisim" : "Beyaz"})
print(kisi["isim"])                 # / Tarkan
print(kisi["soyisim"])              # / Beyaz


# key eklemek:

kisi ["id"] = 12345
print(kisi)                         # / {'isim': 'Tarkan', 'soyisim': 'Kara', 'yaş': 32, 'hobiler': ['Golf Oynamak', 'Yüzmek', 'Tenis Oynamak'], 'Soyisim': 'Beyaz', 'id': 12345}

# key silme : 

del(kisi["isim"])
print(kisi)                         # / {'soyisim': 'Kara', 'yaş': 32, 'hobiler': ['Golf Oynamak', 'Yüzmek', 'Tenis Oynamak'], 'Soyisim': 'Beyaz', 'id': 12345}

# sadece key leri liste olarak almak istersek : 

print(kisi.keys())                  # / ['soyisim', 'yaş', 'hobiler', 'Soyisim', 'id']

# sadece value leri liste olarak almak istersek

print(kisi.values())                # / ['Kara', 32, ['Golf Oynamak', 'Yüzmek', 'Tenis Oynamak'], 'Beyaz', 12345]

# keey - value ikilisi olarak almak istersek

print(kisi.items())                 # / [('soyisim', 'Kara'), ('yaş', 32), ('hobiler', ['Golf Oynamak', 'Yüzmek', 'Tenis Oynamak']), ('Soyisim', 'Beyaz'), ('id', 12345)]

# olmayan bir key arattırıyorsak ve hata almamak istiyorsak : 

print(kisi.get("ikametgah" , "None"))      # / None

# get içerisinde 2.parametre ekrana bastırılan hata mesajıdır.