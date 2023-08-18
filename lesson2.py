# -*- coding: utf-8 -*-
python_codes = {
    'int' : 'Integer - butun sonlarni ifodalaydi',
    'float' : 'sonlarni ifodalaydi',
    'len' : 'Berilgan elementning uzunligini aniqlaydi',
    'elif' : 'Shart operatorida 2 tadan ortiq tekshiruv bo`lganida bajariladi',
    'tuple' : 'Tuple - Ro`yxatdagi ma\'lumotlarni o`zgarmas tipga o`tkazadi',
    'list' : 'Berilgan ma\'lumotlarni ro`yxat ko\'rinishiga keltiradi',
    'range' : 'berilgan parametrlar bo`yicha raqamli qatorni hosil qilib beradi',
    'in' : 'for operatorida bog`lovchi vazifasini bajaradi, boshqa joylarda esa tekshiruv vazifasini bajaradi',
    'min' : 'Berilgan ro`yxatdagi eng kichik raqamni yoki matnni aniqlaydi',
    'sum' : 'Berilgan massivdagi sonlar yig`indisini qaytaradi'
}

kompyuterlar = { 
    "acer" : 7_500_000,
    "toshiba" : 5_500_000,
    "vp" : 3_500_000,
    "lenovo" : 9_500_000,
    "legion" : 7_500_000,
    "hp" : 5_500_000,
    "hp1" : 5_500_000,
    "hp2" : 5_500_000,
    "hp3" : 5_500_000,
    "hp4" : 5_500_000,
    "hp5" : 5_500_000,
}

countr = {
    'Uzbekistan': 'Tashkent',
    'Russia': 'Moscow',
    'Pakistan': 'Islamabad',
    'Armenia': 'Erevan'
}

restoran = {
    'shashlik': 50000,
    'mastava': 20200,
    'sho`rva': 45000,
    'choy': 5000,
    'lag`mon': 40000,
    'limon': 45000
}

m1 = input('1-taomni kiriting: ').lower()
m2 = input('2-taomni kiriting: ').lower()
m3 = input('3-taomni kiriting: ').lower()

if m1 in restoran: 
    print(f"{m1} - {restoran[m1]}")
else: 
    print(f"{m1} - Bizda bunday taom yo`q")

if m2 in restoran: 
    print(f"{m2} - {restoran[m2]}")
else: 
    print(f"{m2} - Bizda bunday taom yo`q")

if m3 in restoran: 
    print(f"{m3} - {restoran[m3]}")
else: 
    print(f"{m3} - Bizda bunday taom yo`q")