"""
AL Vaqt Kutubxonasi
O'zbekcha vaqt funksiyalari
"""

import time as _time
import datetime as _datetime


# ============= JORIY VAQT =============

def hozir():
    """Joriy vaqtni olish (datetime)"""
    return _datetime.datetime.now()

def bugun():
    """Bugungi sanani olish (date)"""
    return _datetime.date.today()

def joriy_vaqt():
    """Joriy vaqtni olish (time)"""
    return _datetime.datetime.now().time()

def timestamp():
    """Unix timestamp"""
    return _time.time()

# ============= VAQT YARATISH =============

def sana(yil, oy, kun):
    """Sana yaratish"""
    return _datetime.date(yil, oy, kun)

def vaqt(soat=0, daqiqa=0, soniya=0):
    """Vaqt yaratish"""
    return _datetime.time(soat, daqiqa, soniya)

def sana_vaqt(yil, oy, kun, soat=0, daqiqa=0, soniya=0):
    """Sana va vaqt yaratish"""
    return _datetime.datetime(yil, oy, kun, soat, daqiqa, soniya)

# ============= VAQT QISMLARI =============

def yil(dt=None):
    """Yilni olish"""
    if dt is None:
        dt = hozir()
    return dt.year

def oy(dt=None):
    """Oyni olish"""
    if dt is None:
        dt = hozir()
    return dt.month

def kun(dt=None):
    """Kunni olish"""
    if dt is None:
        dt = hozir()
    return dt.day

def soat(dt=None):
    """Soatni olish"""
    if dt is None:
        dt = hozir()
    return dt.hour

def daqiqa(dt=None):
    """Daqiqani olish"""
    if dt is None:
        dt = hozir()
    return dt.minute

def soniya(dt=None):
    """Soniyani olish"""
    if dt is None:
        dt = hozir()
    return dt.second

def hafta_kuni(dt=None):
    """Hafta kunini olish (0=Dushanba, 6=Yakshanba)"""
    if dt is None:
        dt = hozir()
    return dt.weekday()

# ============= FORMATLASH =============

def vaqt_formatlash(dt, format_str="%Y-%m-%d %H:%M:%S"):
    """Vaqtni formatlash"""
    return dt.strftime(format_str)

def vaqt_okish(satr, format_str="%Y-%m-%d %H:%M:%S"):
    """Satrdan vaqt o'qish"""
    return _datetime.datetime.strptime(satr, format_str)

def ozbek_format(dt=None):
    """O'zbekcha format"""
    if dt is None:
        dt = hozir()
    kunlar = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", 
              "Juma", "Shanba", "Yakshanba"]
    oylar = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun",
             "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr"]
    
    return f"{kunlar[dt.weekday()]}, {dt.day} {oylar[dt.month-1]} {dt.year} yil, {dt.hour:02d}:{dt.minute:02d}"

# ============= VAQT FARQI =============

def farq(dt1, dt2):
    """Ikki vaqt orasidagi farq"""
    return dt1 - dt2

def kunlar_farqi(dt1, dt2):
    """Kunlar farqi"""
    delta = dt1 - dt2
    return abs(delta.days)

def soniyalar_farqi(dt1, dt2):
    """Soniyalar farqi"""
    delta = dt1 - dt2
    return abs(delta.total_seconds())

def kun_qoshish(dt, kunlar):
    """Kunga kun qo'shish"""
    return dt + _datetime.timedelta(days=kunlar)

def soat_qoshish(dt, soatlar):
    """Vaqtga soat qo'shish"""
    return dt + _datetime.timedelta(hours=soatlar)

# ============= KUTISH =============

def uxlash(soniyalar):
    """Soniya kutish (sleep)"""
    _time.sleep(soniyalar)

def ms_uxlash(millisoniyalar):
    """Millisoniya kutish"""
    _time.sleep(millisoniyalar / 1000)

# ============= VAQT O'LCHASH =============

class VaqtOlchagich:
    """Vaqtni o'lchash uchun klass"""
    
    def __init__(self):
        self.boshlash_vaqti = None
        self.tugash_vaqti = None
    
    def boshlash(self):
        """O'lchashni boshlash"""
        self.boshlash_vaqti = _time.perf_counter()
        return self
    
    def tugash(self):
        """O'lchashni tugatish"""
        self.tugash_vaqti = _time.perf_counter()
        return self.natija()
    
    def natija(self):
        """Natijani soniyalarda olish"""
        if self.boshlash_vaqti and self.tugash_vaqti:
            return self.tugash_vaqti - self.boshlash_vaqti
        return 0
    
    def __enter__(self):
        self.boshlash()
        return self
    
    def __exit__(self, *args):
        self.tugash()


__all__ = [
    'hozir', 'bugun', 'joriy_vaqt', 'timestamp', 'sana', 'vaqt', 'sana_vaqt',
    'yil', 'oy', 'kun', 'soat', 'daqiqa', 'soniya', 'hafta_kuni',
    'vaqt_formatlash', 'vaqt_okish', 'ozbek_format', 'farq', 'kunlar_farqi',
    'soniyalar_farqi', 'kun_qoshish', 'soat_qoshish', 'uxlash', 'ms_uxlash',
    'VaqtOlchagich'
]
