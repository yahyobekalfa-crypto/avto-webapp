"""
AL Matematika Kutubxonasi
O'zbekcha matematik funksiyalar
"""

import math
import random as _random

# ============= KONSTANTALAR =============

PI = math.pi
E = math.e
CHEKSIZLIK = float('inf')
MANFIY_CHEKSIZLIK = float('-inf')

# ============= ASOSIY MATEMATIK =============

def mutlaq(son):
    """Mutlaq qiymat (abs)"""
    return abs(son)

def yaxlitlash(son, xonalar=0):
    """Yaxlitlash (round)"""
    return round(son, xonalar)

def daraja(asos, korsatkich):
    """Darajaga ko'tarish (pow)"""
    return pow(asos, korsatkich)

def ildiz(son):
    """Kvadrat ildiz (sqrt)"""
    return math.sqrt(son)

def kub_ildiz(son):
    """Kub ildiz (cbrt)"""
    return son ** (1/3)

def n_ildiz(son, n):
    """N-chi ildiz"""
    return son ** (1/n)

# ============= TRIGONOMETRIYA =============

def sinus(burchak):
    """Sinus (sin) - radianlarda"""
    return math.sin(burchak)

def kosinus(burchak):
    """Kosinus (cos) - radianlarda"""
    return math.cos(burchak)

def tangens(burchak):
    """Tangens (tan) - radianlarda"""
    return math.tan(burchak)

def arksinus(qiymat):
    """Arksinus (asin)"""
    return math.asin(qiymat)

def arkkosinus(qiymat):
    """Arkkosinus (acos)"""
    return math.acos(qiymat)

def arktangens(qiymat):
    """Arktangens (atan)"""
    return math.atan(qiymat)

def radianga(gradus):
    """Gradusdan radianga o'girish"""
    return math.radians(gradus)

def gradusga(radian):
    """Radiandan gradusga o'girish"""
    return math.degrees(radian)

# ============= LOGARIFMLAR =============

def logarifm(son, asos=math.e):
    """Logarifm"""
    return math.log(son, asos)

def log10(son):
    """10 asosli logarifm"""
    return math.log10(son)

def log2(son):
    """2 asosli logarifm"""
    return math.log2(son)

def eksponent(son):
    """e^x"""
    return math.exp(son)

# ============= YAXLITLASH =============

def ship(son):
    """Yuqoriga yaxlitlash (ceil)"""
    return math.ceil(son)

def pol(son):
    """Pastga yaxlitlash (floor)"""
    return math.floor(son)

def kesish(son):
    """Kasr qismini kesish (trunc)"""
    return math.trunc(son)

# ============= FAKTORIAL VA KOMBINATORIKA =============

def faktorial(n):
    """Faktorial (n!)"""
    return math.factorial(n)

def kombinatsiya(n, k):
    """Kombinatsiya C(n, k)"""
    return math.comb(n, k)

def permutatsiya(n, k):
    """Permutatsiya P(n, k)"""
    return math.perm(n, k)

def ekub(a, b):
    """Eng katta umumiy bo'luvchi (GCD)"""
    return math.gcd(a, b)

def ekuk(a, b):
    """Eng kichik umumiy karrali (LCM)"""
    return math.lcm(a, b)

# ============= TASODIFIY SONLAR =============

def tasodifiy():
    """0 dan 1 gacha tasodifiy son"""
    return _random.random()

def tasodifiy_butun(boshlash, tugash):
    """Oraliqda tasodifiy butun son"""
    return _random.randint(boshlash, tugash)

def tasodifiy_haqiqiy(boshlash, tugash):
    """Oraliqda tasodifiy haqiqiy son"""
    return _random.uniform(boshlash, tugash)

def tasodifiy_tanlash(royxat):
    """Ro'yxatdan tasodifiy element tanlash"""
    return _random.choice(royxat)

def aralashtirish(royxat):
    """Ro'yxatni aralashtirish"""
    _random.shuffle(royxat)
    return royxat

# ============= MAXSUS FUNKSIYALAR =============

def ishorat(son):
    """Sonning ishorati (-1, 0, 1)"""
    if son > 0:
        return 1
    elif son < 0:
        return -1
    return 0

def juft_mi(son):
    """Son juftmi?"""
    return son % 2 == 0

def toq_mi(son):
    """Son toqmi?"""
    return son % 2 != 0

def tub_mi(son):
    """Son tubmi (prime)?"""
    if son < 2:
        return False
    for i in range(2, int(ildiz(son)) + 1):
        if son % i == 0:
            return False
    return True

def fibonacci(n):
    """N-chi Fibonacci soni"""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Eksport
__all__ = [
    'PI', 'E', 'CHEKSIZLIK', 'MANFIY_CHEKSIZLIK',
    'mutlaq', 'yaxlitlash', 'daraja', 'ildiz', 'kub_ildiz', 'n_ildiz',
    'sinus', 'kosinus', 'tangens', 'arksinus', 'arkkosinus', 'arktangens',
    'radianga', 'gradusga', 'logarifm', 'log10', 'log2', 'eksponent',
    'ship', 'pol', 'kesish', 'faktorial', 'kombinatsiya', 'permutatsiya',
    'ekub', 'ekuk', 'tasodifiy', 'tasodifiy_butun', 'tasodifiy_haqiqiy',
    'tasodifiy_tanlash', 'aralashtirish', 'ishorat', 'juft_mi', 'toq_mi',
    'tub_mi', 'fibonacci'
]
