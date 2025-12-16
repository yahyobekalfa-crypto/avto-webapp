"""
AL Hamyon (Wallet)
Kripto hamyon funksiyalari
"""

import hashlib
import secrets
import json
from typing import Dict, Tuple


class Hamyon:
    """Kripto hamyoni"""
    
    def __init__(self, nom: str = None):
        self.maxfiy_kalit, self.ochiq_kalit = self._kalitlar_yaratish()
        self.nom = nom or f"Hamyon-{self.manzil[:8]}"
    
    def _kalitlar_yaratish(self) -> Tuple[str, str]:
        """Kalit juftligini yaratish"""
        maxfiy = secrets.token_hex(32)
        ochiq = hashlib.sha256(maxfiy.encode()).hexdigest()
        return maxfiy, ochiq
    
    @property
    def manzil(self) -> str:
        """Hamyon manzili"""
        return "0x" + self.ochiq_kalit[:40]
    
    def imzolash(self, xabar: str) -> str:
        """Xabarni imzolash"""
        imzo_data = self.maxfiy_kalit + xabar
        return hashlib.sha256(imzo_data.encode()).hexdigest()
    
    def eksport(self, parol: str = None) -> Dict:
        """Hamyonni eksport qilish"""
        data = {
            'nom': self.nom,
            'manzil': self.manzil,
            'ochiq_kalit': self.ochiq_kalit
        }
        if parol:
            # Oddiy shifrlash (real loyihada kuchliroq shifrlash kerak)
            shifrlangan = hashlib.sha256((self.maxfiy_kalit + parol).encode()).hexdigest()
            data['shifrlangan_kalit'] = shifrlangan
        else:
            data['maxfiy_kalit'] = self.maxfiy_kalit
        return data
    
    def saqlash(self, fayl_yoli: str, parol: str = None):
        """Hamyonni faylga saqlash"""
        with open(fayl_yoli, 'w') as f:
            json.dump(self.eksport(parol), f, indent=2)
    
    @classmethod
    def yuklash(cls, fayl_yoli: str) -> 'Hamyon':
        """Hamyonni fayldan yuklash"""
        with open(fayl_yoli, 'r') as f:
            data = json.load(f)
        
        hamyon = cls(data.get('nom'))
        if 'maxfiy_kalit' in data:
            hamyon.maxfiy_kalit = data['maxfiy_kalit']
            hamyon.ochiq_kalit = data['ochiq_kalit']
        return hamyon
    
    def __str__(self):
        return f"Hamyon({self.nom}, {self.manzil})"


def tasodifiy_manzil() -> str:
    """Tasodifiy manzil yaratish"""
    return "0x" + secrets.token_hex(20)


def hash_yaratish(matn: str) -> str:
    """SHA-256 hash yaratish"""
    return hashlib.sha256(matn.encode()).hexdigest()


def imzo_tekshirish(ochiq_kalit: str, xabar: str, imzo: str) -> bool:
    """Imzoni tekshirish (soddalashtirilgan)"""
    # Real implementatsiyada asimmetrik kriptografiya ishlatiladi
    kutilgan = hashlib.sha256((ochiq_kalit + xabar).encode()).hexdigest()
    return kutilgan == imzo


__all__ = ['Hamyon', 'tasodifiy_manzil', 'hash_yaratish', 'imzo_tekshirish']
