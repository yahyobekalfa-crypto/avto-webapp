"""
AL Matn Kutubxonasi
O'zbekcha string funksiyalari
"""

import re


# ============= ASOSIY OPERATSIYALAR =============

def katta_harf(matn):
    """Katta harfga o'girish"""
    return matn.upper()

def kichik_harf(matn):
    """Kichik harfga o'girish"""
    return matn.lower()

def bosh_harf(matn):
    """Birinchi harfni katta qilish"""
    return matn.capitalize()

def sarlavha(matn):
    """Har so'z boshini katta qilish"""
    return matn.title()

def teskari(matn):
    """Matnni teskari qilish"""
    return matn[::-1]

# ============= QO'SHISH/AJRATISH =============

def birlashtirish(ajratuvchi, royxat):
    """Ro'yxatni satrga birlashtirish"""
    return ajratuvchi.join(royxat)

def ajratish(matn, ajratuvchi=" "):
    """Satrni ajratish"""
    return matn.split(ajratuvchi)

def qatorlarga(matn):
    """Qatorlarga ajratish"""
    return matn.splitlines()

# ============= KESISH =============

def kesish(matn):
    """Ikki tomondan bo'shliqlarni olib tashlash"""
    return matn.strip()

def chap_kesish(matn):
    """Chap tomondan kesish"""
    return matn.lstrip()

def ong_kesish(matn):
    """O'ng tomondan kesish"""
    return matn.rstrip()

# ============= ALMASHTIRISH =============

def almashtirish(matn, eski, yangi):
    """Matnda almashtirish"""
    return matn.replace(eski, yangi)

def birinchi_almashtirish(matn, eski, yangi):
    """Faqat birinchi uchrashadigan joyni almashtirish"""
    return matn.replace(eski, yangi, 1)

# ============= QIDIRISH =============

def topish(matn, qidiruv, boshi=0):
    """Qidiruv matnini topish (indeks, -1 topilmasa)"""
    return matn.find(qidiruv, boshi)

def oxirisini_topish(matn, qidiruv):
    """Oxirisidan qidirish"""
    return matn.rfind(qidiruv)

def sanash(matn, qidiruv):
    """Necha marta uchrayotganini sanash"""
    return matn.count(qidiruv)

def bor_mi(matn, qidiruv):
    """Matn ichida bormi?"""
    return qidiruv in matn

def bilan_boshlanadi(matn, prefix):
    """Shu bilan boshlanadimi?"""
    return matn.startswith(prefix)

def bilan_tugaydi(matn, suffix):
    """Shu bilan tugaydimi?"""
    return matn.endswith(suffix)

# ============= TEKSHIRISH =============

def raqam_mi(matn):
    """Faqat raqamlardan iboratmi?"""
    return matn.isdigit()

def harf_mi(matn):
    """Faqat harflardan iboratmi?"""
    return matn.isalpha()

def harfraqam_mi(matn):
    """Harf va raqamlardan iboratmi?"""
    return matn.isalnum()

def boshliq_mi(matn):
    """Faqat bo'shliqlardan iboratmi?"""
    return matn.isspace()

def bush_mi(matn):
    """Bo'shmi?"""
    return len(matn) == 0

# ============= FORMATLASH =============

def formatlash(shablon, *args, **kwargs):
    """Matnni formatlash"""
    return shablon.format(*args, **kwargs)

def f_satr(shablon, **ozgaruvchilar):
    """F-string o'xshash formatlash"""
    return shablon.format_map(ozgaruvchilar)

def chap_toldirish(matn, uzunlik, belgi=" "):
    """Chapga to'ldirish"""
    return matn.rjust(uzunlik, belgi)

def ong_toldirish(matn, uzunlik, belgi=" "):
    """O'ngga to'ldirish"""
    return matn.ljust(uzunlik, belgi)

def markazlashtirish(matn, uzunlik, belgi=" "):
    """Markazlashtirish"""
    return matn.center(uzunlik, belgi)

def nol_toldirish(matn, uzunlik):
    """Nol bilan to'ldirish"""
    return matn.zfill(uzunlik)

# ============= REGEX =============

def regex_topish(shablon, matn):
    """Regex bilan topish"""
    match = re.search(shablon, matn)
    return match.group() if match else None

def regex_hammasi(shablon, matn):
    """Regex bilan hammasini topish"""
    return re.findall(shablon, matn)

def regex_almashtirish(shablon, almashtirish, matn):
    """Regex bilan almashtirish"""
    return re.sub(shablon, almashtirish, matn)

def regex_ajratish(shablon, matn):
    """Regex bilan ajratish"""
    return re.split(shablon, matn)


__all__ = [
    'katta_harf', 'kichik_harf', 'bosh_harf', 'sarlavha', 'teskari',
    'birlashtirish', 'ajratish', 'qatorlarga', 'kesish', 'chap_kesish',
    'ong_kesish', 'almashtirish', 'birinchi_almashtirish', 'topish',
    'oxirisini_topish', 'sanash', 'bor_mi', 'bilan_boshlanadi', 'bilan_tugaydi',
    'raqam_mi', 'harf_mi', 'harfraqam_mi', 'boshliq_mi', 'bush_mi',
    'formatlash', 'f_satr', 'chap_toldirish', 'ong_toldirish',
    'markazlashtirish', 'nol_toldirish', 'regex_topish', 'regex_hammasi',
    'regex_almashtirish', 'regex_ajratish'
]
