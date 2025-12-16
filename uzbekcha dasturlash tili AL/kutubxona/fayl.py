"""
AL Fayl Kutubxonasi
O'zbekcha fayl operatsiyalari
"""

import os
import shutil
import json


# ============= FAYL OCHISH/YOPISH =============

def fayl_ochish(yol, rejim="r", kodlash="utf-8"):
    """Faylni ochish
    Rejimlar: 'r' - o'qish, 'w' - yozish, 'a' - qo'shish
    """
    return open(yol, rejim, encoding=kodlash)

def fayl_yopish(fayl):
    """Faylni yopish"""
    fayl.close()

# ============= O'QISH/YOZISH =============

def fayl_okish(yol, kodlash="utf-8"):
    """Faylni butunlay o'qish"""
    with open(yol, 'r', encoding=kodlash) as f:
        return f.read()

def fayl_yozish(yol, mazmun, kodlash="utf-8"):
    """Faylga yozish"""
    with open(yol, 'w', encoding=kodlash) as f:
        f.write(mazmun)

def fayl_qoshish(yol, mazmun, kodlash="utf-8"):
    """Faylga qo'shish"""
    with open(yol, 'a', encoding=kodlash) as f:
        f.write(mazmun)

def qatorlar_okish(yol, kodlash="utf-8"):
    """Faylni qatorlar ro'yxati sifatida o'qish"""
    with open(yol, 'r', encoding=kodlash) as f:
        return f.readlines()

def qatorlar_yozish(yol, qatorlar, kodlash="utf-8"):
    """Qatorlar ro'yxatini yozish"""
    with open(yol, 'w', encoding=kodlash) as f:
        f.writelines(qatorlar)

# ============= JSON =============

def json_okish(yol):
    """JSON faylni o'qish"""
    with open(yol, 'r', encoding='utf-8') as f:
        return json.load(f)

def json_yozish(yol, malumot, chiroyli=True):
    """JSON faylga yozish"""
    with open(yol, 'w', encoding='utf-8') as f:
        if chiroyli:
            json.dump(malumot, f, ensure_ascii=False, indent=2)
        else:
            json.dump(malumot, f, ensure_ascii=False)

def json_satrga(malumot, chiroyli=True):
    """Ma'lumotni JSON satrga o'girish"""
    if chiroyli:
        return json.dumps(malumot, ensure_ascii=False, indent=2)
    return json.dumps(malumot, ensure_ascii=False)

def json_dan(satr):
    """JSON satrdan ma'lumot olish"""
    return json.loads(satr)

# ============= FAYL/PAPKA OPERATSIYALARI =============

def mavjud_mi(yol):
    """Fayl yoki papka mavjudligini tekshirish"""
    return os.path.exists(yol)

def fayl_mi(yol):
    """Bu faylmi?"""
    return os.path.isfile(yol)

def papka_mi(yol):
    """Bu papkami?"""
    return os.path.isdir(yol)

def papka_yaratish(yol):
    """Papka yaratish"""
    os.makedirs(yol, exist_ok=True)

def ochirib_tashlash(yol):
    """Fayl yoki papkani o'chirish"""
    if os.path.isfile(yol):
        os.remove(yol)
    elif os.path.isdir(yol):
        shutil.rmtree(yol)

def nomini_ozgartirish(eski_yol, yangi_yol):
    """Fayl/papka nomini o'zgartirish"""
    os.rename(eski_yol, yangi_yol)

def nusxa_olish(manba, manzil):
    """Faylni nusxalash"""
    shutil.copy2(manba, manzil)

def kochirish(manba, manzil):
    """Faylni ko'chirish"""
    shutil.move(manba, manzil)

# ============= YO'L FUNKSIYALARI =============

def papkadagilar(yol):
    """Papkadagi fayllar ro'yxati"""
    return os.listdir(yol)

def yol_birlashtirish(*qismlar):
    """Yo'l qismlarini birlashtirish"""
    return os.path.join(*qismlar)

def fayl_nomi(yol):
    """Yo'ldan fayl nomini olish"""
    return os.path.basename(yol)

def papka_yoli(yol):
    """Yo'ldan papka yo'lini olish"""
    return os.path.dirname(yol)

def kengaytma(yol):
    """Fayl kengaytmasini olish"""
    return os.path.splitext(yol)[1]

def joriy_papka():
    """Joriy ish papkasi"""
    return os.getcwd()

def papkani_ozgartirish(yol):
    """Joriy papkani o'zgartirish"""
    os.chdir(yol)

def mutlaq_yol(yol):
    """Mutlaq yo'lni olish"""
    return os.path.abspath(yol)

# ============= FAYL MA'LUMOTLARI =============

def fayl_hajmi(yol):
    """Fayl hajmi (baytlarda)"""
    return os.path.getsize(yol)

def fayl_vaqti(yol):
    """Faylning oxirgi o'zgartirilgan vaqti"""
    import datetime
    timestamp = os.path.getmtime(yol)
    return datetime.datetime.fromtimestamp(timestamp)


__all__ = [
    'fayl_ochish', 'fayl_yopish', 'fayl_okish', 'fayl_yozish', 'fayl_qoshish',
    'qatorlar_okish', 'qatorlar_yozish', 'json_okish', 'json_yozish',
    'json_satrga', 'json_dan', 'mavjud_mi', 'fayl_mi', 'papka_mi',
    'papka_yaratish', 'ochirib_tashlash', 'nomini_ozgartirish', 'nusxa_olish',
    'kochirish', 'papkadagilar', 'yol_birlashtirish', 'fayl_nomi', 'papka_yoli',
    'kengaytma', 'joriy_papka', 'papkani_ozgartirish', 'mutlaq_yol',
    'fayl_hajmi', 'fayl_vaqti'
]
