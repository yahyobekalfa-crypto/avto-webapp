"""
AL Asosiy Kutubxona
O'zbekcha asosiy funksiyalar
"""

# ============= KIRISH/CHIQISH =============

def chop(*qiymatlar, ajratuvchi=" ", oxiri="\n"):
    """Ekranga chiqarish (print)"""
    print(*qiymatlar, sep=ajratuvchi, end=oxiri)

def kiritish(xabar=""):
    """Foydalanuvchidan kiritish olish (input)"""
    return input(xabar)

# ============= TUR FUNKSIYALARI =============

def uzunlik(obyekt):
    """Uzunlikni qaytarish (len)"""
    return len(obyekt)

def turi(obyekt):
    """Turni qaytarish (type)"""
    return type(obyekt)

def satr(qiymat):
    """Satrga o'girish (str)"""
    return str(qiymat)

def butun(qiymat):
    """Butun songa o'girish (int)"""
    return int(qiymat)

def haqiqiy(qiymat):
    """Haqiqiy songa o'girish (float)"""
    return float(qiymat)

def mantiqiy(qiymat):
    """Mantiqiy qiymatga o'girish (bool)"""
    return bool(qiymat)

# ============= KOLLEKSIYALAR =============

def royxat(iterator=None):
    """Ro'yxat yaratish (list)"""
    if iterator is None:
        return []
    return list(iterator)

def lugat(**kwargs):
    """Lug'at yaratish (dict)"""
    return dict(**kwargs)

def toplam(iterator=None):
    """To'plam yaratish (set)"""
    if iterator is None:
        return set()
    return set(iterator)

def kortej(iterator=None):
    """Kortej yaratish (tuple)"""
    if iterator is None:
        return ()
    return tuple(iterator)

# ============= ITERATOR FUNKSIYALARI =============

def oraliq(*args):
    """Oraliq yaratish (range)"""
    return range(*args)

def sanash(iterator, boshlash=0):
    """Sanash bilan iteratsiya (enumerate)"""
    return enumerate(iterator, start=boshlash)

def zip_qilish(*iteratorlar):
    """Iteratorlarni birlashtirish (zip)"""
    return zip(*iteratorlar)

def xaritalash(funksiya, iterator):
    """Funksiyani qo'llash (map)"""
    return map(funksiya, iterator)

def filtrlash(funksiya, iterator):
    """Filtrlash (filter)"""
    return filter(funksiya, iterator)

def saralash(iterator, kalit=None, teskari=False):
    """Saralash (sorted)"""
    return sorted(iterator, key=kalit, reverse=teskari)

def teskari(iterator):
    """Teskari qilish (reversed)"""
    return reversed(iterator)

# ============= AGREGAT FUNKSIYALAR =============

def yigindi(iterator):
    """Yig'indini hisoblash (sum)"""
    return sum(iterator)

def eng_katta(*args):
    """Eng katta qiymat (max)"""
    if len(args) == 1:
        return max(args[0])
    return max(args)

def eng_kichik(*args):
    """Eng kichik qiymat (min)"""
    if len(args) == 1:
        return min(args[0])
    return min(args)

def hammasi(iterator):
    """Hammasi True mi? (all)"""
    return all(iterator)

def birortasi(iterator):
    """Birortasi True mi? (any)"""
    return any(iterator)

# ============= TEKSHIRISH FUNKSIYALARI =============

def bor_mi(element, kolleksiya):
    """Element mavjudligini tekshirish"""
    return element in kolleksiya

def bosh_mi(kolleksiya):
    """Kolleksiya bo'shligini tekshirish"""
    return len(kolleksiya) == 0

def son_mi(qiymat):
    """Qiymat sonmi?"""
    return isinstance(qiymat, (int, float))

def satr_mi(qiymat):
    """Qiymat satrmi?"""
    return isinstance(qiymat, str)

def royxat_mi(qiymat):
    """Qiymat ro'yxatmi?"""
    return isinstance(qiymat, list)

def lugat_mi(qiymat):
    """Qiymat lug'atmi?"""
    return isinstance(qiymat, dict)

# ============= YORDAMCHI FUNKSIYALAR =============

def identifikator(obyekt):
    """Obyekt ID sini olish (id)"""
    return id(obyekt)

def hash_qiymat(obyekt):
    """Hash qiymatini olish (hash)"""
    return hash(obyekt)

def buyruqlar(obyekt):
    """Obyekt atributlarini olish (dir)"""
    return dir(obyekt)

def repr_satr(obyekt):
    """Repr satrini olish (repr)"""
    return repr(obyekt)

def ascii_kod(belgi):
    """Belgi ASCII kodi (ord)"""
    return ord(belgi)

def belgiga(kod):
    """ASCII koddan belgi (chr)"""
    return chr(kod)

# Eksport
__all__ = [
    'chop', 'kiritish', 'uzunlik', 'turi', 'satr', 'butun', 'haqiqiy', 'mantiqiy',
    'royxat', 'lugat', 'toplam', 'kortej', 'oraliq', 'sanash', 'zip_qilish',
    'xaritalash', 'filtrlash', 'saralash', 'teskari', 'yigindi', 'eng_katta',
    'eng_kichik', 'hammasi', 'birortasi', 'bor_mi', 'bosh_mi', 'son_mi',
    'satr_mi', 'royxat_mi', 'lugat_mi', 'identifikator', 'hash_qiymat',
    'buyruqlar', 'repr_satr', 'ascii_kod', 'belgiga'
]
