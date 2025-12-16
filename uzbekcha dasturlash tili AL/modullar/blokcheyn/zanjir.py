"""
AL Blockchain (Blokzanjir)
O'zbekcha blockchain implementatsiyasi
"""

import hashlib
import json
import time
from typing import List, Dict, Any


class Blok:
    """Blok sinfi"""
    
    def __init__(self, indeks: int, tranzaksiyalar: List[Dict], oldingi_hash: str, vaqt: float = None):
        self.indeks = indeks
        self.tranzaksiyalar = tranzaksiyalar
        self.oldingi_hash = oldingi_hash
        self.vaqt = vaqt or time.time()
        self.nonce = 0
        self.hash = self.hash_hisoblash()
    
    def hash_hisoblash(self) -> str:
        """Blok hashini hisoblash"""
        blok_satr = json.dumps({
            'indeks': self.indeks,
            'tranzaksiyalar': self.tranzaksiyalar,
            'oldingi_hash': self.oldingi_hash,
            'vaqt': self.vaqt,
            'nonce': self.nonce
        }, sort_keys=True)
        return hashlib.sha256(blok_satr.encode()).hexdigest()
    
    def qazish(self, qiyinlik: int = 4):
        """Blokni qazish (mining)"""
        maqsad = '0' * qiyinlik
        while not self.hash.startswith(maqsad):
            self.nonce += 1
            self.hash = self.hash_hisoblash()
        return self.hash
    
    def lugat(self) -> Dict:
        """Blokni lug'at sifatida olish"""
        return {
            'indeks': self.indeks,
            'tranzaksiyalar': self.tranzaksiyalar,
            'oldingi_hash': self.oldingi_hash,
            'vaqt': self.vaqt,
            'nonce': self.nonce,
            'hash': self.hash
        }


class BlokZanjir:
    """Blockchain sinfi"""
    
    def __init__(self, qiyinlik: int = 4):
        self.zanjir: List[Blok] = []
        self.kutilayotgan_tranzaksiyalar: List[Dict] = []
        self.qiyinlik = qiyinlik
        self.qazish_mukofoti = 10
        
        # Genesis blok
        self._genesis_blok_yaratish()
    
    def _genesis_blok_yaratish(self):
        """Birinchi blokni yaratish"""
        genesis = Blok(0, [], "0")
        genesis.qazish(self.qiyinlik)
        self.zanjir.append(genesis)
    
    def oxirgi_blok(self) -> Blok:
        """Oxirgi blokni olish"""
        return self.zanjir[-1]
    
    def tranzaksiya_qoshish(self, yuboruvchi: str, qabul_qiluvchi: str, miqdor: float) -> Dict:
        """Yangi tranzaksiya qo'shish"""
        tranzaksiya = {
            'yuboruvchi': yuboruvchi,
            'qabul_qiluvchi': qabul_qiluvchi,
            'miqdor': miqdor,
            'vaqt': time.time()
        }
        self.kutilayotgan_tranzaksiyalar.append(tranzaksiya)
        return tranzaksiya
    
    def blok_qazish(self, qazuvchi_manzil: str) -> Blok:
        """Yangi blok qazish"""
        # Qazuvchiga mukofot
        self.tranzaksiya_qoshish("TIZIM", qazuvchi_manzil, self.qazish_mukofoti)
        
        yangi_blok = Blok(
            indeks=len(self.zanjir),
            tranzaksiyalar=self.kutilayotgan_tranzaksiyalar,
            oldingi_hash=self.oxirgi_blok().hash
        )
        
        print(f"⛏️ Blok qazilmoqda... (qiyinlik: {self.qiyinlik})")
        yangi_blok.qazish(self.qiyinlik)
        print(f"✅ Blok qazildi! Hash: {yangi_blok.hash[:16]}...")
        
        self.zanjir.append(yangi_blok)
        self.kutilayotgan_tranzaksiyalar = []
        
        return yangi_blok
    
    def zanjir_togri_mi(self) -> bool:
        """Zanjir to'g'riligini tekshirish"""
        for i in range(1, len(self.zanjir)):
            joriy = self.zanjir[i]
            oldingi = self.zanjir[i - 1]
            
            # Hash tekshirish
            if joriy.hash != joriy.hash_hisoblash():
                return False
            
            # Oldingi blok bilan bog'lanish
            if joriy.oldingi_hash != oldingi.hash:
                return False
        
        return True
    
    def balans(self, manzil: str) -> float:
        """Manzil balansini hisoblash"""
        balans = 0.0
        
        for blok in self.zanjir:
            for tx in blok.tranzaksiyalar:
                if tx['yuboruvchi'] == manzil:
                    balans -= tx['miqdor']
                if tx['qabul_qiluvchi'] == manzil:
                    balans += tx['miqdor']
        
        return balans
    
    def zanjir_malumoti(self) -> Dict:
        """Zanjir haqida ma'lumot"""
        return {
            'bloklar_soni': len(self.zanjir),
            'qiyinlik': self.qiyinlik,
            'kutilayotgan_tranzaksiyalar': len(self.kutilayotgan_tranzaksiyalar),
            'oxirgi_blok_hash': self.oxirgi_blok().hash,
            'togri': self.zanjir_togri_mi()
        }
    
    def eksport(self) -> List[Dict]:
        """Zanjirni eksport qilish"""
        return [blok.lugat() for blok in self.zanjir]
    
    def __len__(self):
        return len(self.zanjir)
    
    def __str__(self):
        return f"BlokZanjir({len(self.zanjir)} blok)"


__all__ = ['Blok', 'BlokZanjir']
