"""
AL (Algoritm Tili) - Spyder va boshqa IDE larda ishlatish uchun

Bu faylni import qiling va o'zbekcha funksiyalardan foydalaning!

Misol:
    from al_spyder import *
    
    chop("Salom Dunyo!")
    
    uchun i oraliq(5) ichida:
        chop(i)
"""

import sys
import os

# Loyiha yo'lini qo'shish
_AL_PATH = os.path.dirname(os.path.abspath(__file__))
if _AL_PATH not in sys.path:
    sys.path.insert(0, _AL_PATH)

# ============= ASOSIY FUNKSIYALAR =============
from kutubxona.asosiy import *
from kutubxona.matematika import *
from kutubxona.matn import *
from kutubxona.fayl import *
from kutubxona.vaqt import *

# ============= INTERPRETER =============
from al.interpreter import Interpreter as _Interpreter
from al.errors import ALXato

# Global interpreter
_interpreter = _Interpreter()


def al_bajarish(kod: str):
    """
    AL kodini bajarish
    
    Misol:
        al_bajarish('''
        x = 10
        uchun i oraliq(x) ichida:
            chop(i)
        ''')
    """
    return _interpreter.bajarish(kod)


def al_fayl(fayl_yoli: str):
    """
    AL faylini bajarish
    
    Misol:
        al_fayl("misollar/salom_dunyo.al")
    """
    return _interpreter.fayl_bajarish(fayl_yoli)


def pythonga(kod: str) -> str:
    """
    AL kodini Python kodiga aylantirish
    
    Misol:
        python_kod = pythonga("chop('Salom!')")
        print(python_kod)
    """
    return _interpreter.python_kodini_olish(kod)


# ============= KALIT SO'ZLAR (Python funksiyalari sifatida) =============

def agar(shart, togri_qiymat, notogri_qiymat=None):
    """Agar-boshqa ifoda"""
    return togri_qiymat if shart else notogri_qiymat


# ============= YORDAM =============

def yordam():
    """AL haqida yordam"""
    print("""
╔════════════════════════════════════════════════════════════════╗
║              AL (Algoritm Tili) - YORDAM                       ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  ASOSIY FUNKSIYALAR:                                           ║
║    chop(x)         - Ekranga chiqarish                         ║
║    kiritish(x)     - Foydalanuvchidan olish                    ║
║    uzunlik(x)      - Uzunlik                                   ║
║    turi(x)         - Tur                                       ║
║                                                                ║
║  MATEMATIKA:                                                   ║
║    ildiz(x)        - Kvadrat ildiz                             ║
║    daraja(x, n)    - Darajaga ko'tarish                        ║
║    sinus(x)        - Sinus                                     ║
║    tasodifiy()     - Tasodifiy son                             ║
║                                                                ║
║  MATN:                                                         ║
║    katta_harf(s)   - KATTA HARF                                ║
║    ajratish(s)     - Ajratish                                  ║
║    birlashtirish() - Birlashtirish                             ║
║                                                                ║
║  FAYL:                                                         ║
║    fayl_okish(f)   - Faylni o'qish                             ║
║    fayl_yozish()   - Faylga yozish                             ║
║    json_okish(f)   - JSON o'qish                               ║
║                                                                ║
║  VAQT:                                                         ║
║    hozir()         - Joriy vaqt                                ║
║    bugun()         - Bugungi sana                              ║
║    uxlash(n)       - N soniya kutish                           ║
║                                                                ║
║  AL KOD BAJARISH:                                              ║
║    al_bajarish(kod)  - AL kodini bajarish                      ║
║    al_fayl(fayl)     - AL faylini bajarish                     ║
║    pythonga(kod)     - Python ga aylantirish                   ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
    """)


# Boshlang'ich xabar
print("✅ AL (Algoritm Tili) yuklandi!")
print("💡 Yordam uchun: yordam()")
print("📝 Misol: chop('Salom Dunyo!')")
