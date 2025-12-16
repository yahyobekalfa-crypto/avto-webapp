"""
AL Token Turlari va Kalit So'zlar
O'zbekcha kalit so'zlarni Python ga map qilish
"""

from enum import Enum, auto
from typing import Dict

class TokenTuri(Enum):
    """Token turlari"""
    # Literals
    RAQAM = auto()          # Raqam (int, float)
    SATR = auto()           # Satr (string)
    MANTIQIY = auto()       # Mantiqiy (bool)
    HECH = auto()           # None
    
    # Identifikator
    IDENTIFIKATOR = auto()  # O'zgaruvchi nomi
    KALIT_SOZ = auto()      # Kalit so'z
    
    # Operatorlar
    QOSHISH = auto()        # +
    AYIRISH = auto()        # -
    KOPAYTIRISH = auto()    # *
    BOLISH = auto()         # /
    QOLDIQ = auto()         # %
    DARAJA = auto()         # **
    BUTUN_BOLISH = auto()   # //
    
    # Taqqoslash
    TENG = auto()           # ==
    TENG_EMAS = auto()      # !=
    KICHIK = auto()         # <
    KATTA = auto()          # >
    KICHIK_TENG = auto()    # <=
    KATTA_TENG = auto()     # >=
    
    # Tayinlash
    TAYINLASH = auto()      # =
    QOSHIB_TAYINLASH = auto()   # +=
    AYIRIB_TAYINLASH = auto()   # -=
    KOPAYT_TAYINLASH = auto()   # *=
    BOLIB_TAYINLASH = auto()    # /=
    
    # Qavslar
    OCHIQ_QAVS = auto()     # (
    YOPIQ_QAVS = auto()     # )
    OCHIQ_KVADRAT = auto()  # [
    YOPIQ_KVADRAT = auto()  # ]
    OCHIQ_FIGURALI = auto() # {
    YOPIQ_FIGURALI = auto() # }
    
    # Belgilar
    VERGUL = auto()         # ,
    NUQTA = auto()          # .
    IKKI_NUQTA = auto()     # :
    NUQTA_VERGUL = auto()   # ;
    STRELKA = auto()        # ->
    DOG = auto()            # @
    
    # Maxsus
    YANGI_QATOR = auto()    # \n
    INDENT = auto()         # Indent (bo'shliq)
    DEDENT = auto()         # Dedent
    FAYL_OXIRI = auto()     # EOF
    IZOH = auto()           # Comment (#)


# O'zbekcha kalit so'zlar -> Python
KALIT_SOZLAR: Dict[str, str] = {
    # Shartlar
    'agar': 'if',
    'aks_holda': 'elif',
    'boshqa': 'else',
    
    # Sikllar
    'uchun': 'for',
    'toki': 'while',
    'ichida': 'in',
    
    # Funksiya va Sinf
    'funksiya': 'def',
    'sinf': 'class',
    'qaytarish': 'return',
    'ozini': 'self',
    
    # Mantiqiy operatorlar
    'va': 'and',
    'yoki': 'or',
    'emas': 'not',
    
    # Mantiqiy qiymatlar
    'togri': 'True',
    'notogri': 'False',
    'hech': 'None',
    
    # Boshqaruv
    'uzish': 'break',
    'davom': 'continue',
    'otkazish': 'pass',
    
    # Xatolar
    'harakat': 'try',
    'tutish': 'except',
    'nihoyat': 'finally',
    'chiqarish': 'raise',
    
    # Import
    'import': 'import',
    'dan': 'from',
    'sifatida': 'as',
    
    # Async
    'asinxron': 'async',
    'kutish': 'await',
    
    # Boshqalar
    'global': 'global',
    'mahalliy': 'nonlocal',
    'lambda': 'lambda',
    'bilan': 'with',
    'tasdiqlash': 'assert',
    'ochirib': 'del',
    'chiqish': 'yield',
}

# Python kalit so'zlar -> O'zbekcha (teskari)
PYTHON_KALIT_SOZLAR: Dict[str, str] = {v: k for k, v in KALIT_SOZLAR.items()}

# MaxSus belgilar
OPERATORLAR = {
    '+': TokenTuri.QOSHISH,
    '-': TokenTuri.AYIRISH,
    '*': TokenTuri.KOPAYTIRISH,
    '/': TokenTuri.BOLISH,
    '%': TokenTuri.QOLDIQ,
    '**': TokenTuri.DARAJA,
    '//': TokenTuri.BUTUN_BOLISH,
    '==': TokenTuri.TENG,
    '!=': TokenTuri.TENG_EMAS,
    '<': TokenTuri.KICHIK,
    '>': TokenTuri.KATTA,
    '<=': TokenTuri.KICHIK_TENG,
    '>=': TokenTuri.KATTA_TENG,
    '=': TokenTuri.TAYINLASH,
    '+=': TokenTuri.QOSHIB_TAYINLASH,
    '-=': TokenTuri.AYIRIB_TAYINLASH,
    '*=': TokenTuri.KOPAYT_TAYINLASH,
    '/=': TokenTuri.BOLIB_TAYINLASH,
}

QAVSLAR = {
    '(': TokenTuri.OCHIQ_QAVS,
    ')': TokenTuri.YOPIQ_QAVS,
    '[': TokenTuri.OCHIQ_KVADRAT,
    ']': TokenTuri.YOPIQ_KVADRAT,
    '{': TokenTuri.OCHIQ_FIGURALI,
    '}': TokenTuri.YOPIQ_FIGURALI,
}

BELGILAR = {
    ',': TokenTuri.VERGUL,
    '.': TokenTuri.NUQTA,
    ':': TokenTuri.IKKI_NUQTA,
    ';': TokenTuri.NUQTA_VERGUL,
    '->': TokenTuri.STRELKA,
    '@': TokenTuri.DOG,
}


class Token:
    """Token sinfi"""
    
    def __init__(self, turi: TokenTuri, qiymat: str, qator: int = 0, ustun: int = 0):
        self.turi = turi
        self.qiymat = qiymat
        self.qator = qator
        self.ustun = ustun
    
    def __repr__(self):
        return f"Token({self.turi.name}, '{self.qiymat}', qator={self.qator})"
    
    def __eq__(self, other):
        if isinstance(other, Token):
            return self.turi == other.turi and self.qiymat == other.qiymat
        return False
