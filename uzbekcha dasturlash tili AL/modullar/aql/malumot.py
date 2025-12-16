"""
AL Ma'lumot Ishlov Berish
O'zbekcha data processing
"""

from typing import List, Dict, Any, Callable
import math
import random


# ============= MA'LUMOT TUZILMALARI =============

class MalumotToplami:
    """Ma'lumotlar to'plami (Dataset)"""
    
    def __init__(self, malumotlar: List[Any] = None):
        self.malumotlar = malumotlar or []
    
    def qoshish(self, element):
        """Element qo'shish"""
        self.malumotlar.append(element)
    
    def uzunlik(self) -> int:
        return len(self.malumotlar)
    
    def bolish(self, nisbat: float = 0.8) -> tuple:
        """Train/test ga bo'lish"""
        aralashtirish = self.malumotlar.copy()
        random.shuffle(aralashtirish)
        chegara = int(len(aralashtirish) * nisbat)
        return aralashtirish[:chegara], aralashtirish[chegara:]
    
    def normalizatsiya(self, ustun: int = None) -> 'MalumotToplami':
        """Ma'lumotlarni normalizatsiya qilish"""
        if not self.malumotlar:
            return self
        
        if ustun is not None and isinstance(self.malumotlar[0], (list, tuple)):
            qiymatlar = [m[ustun] for m in self.malumotlar]
            min_q, max_q = min(qiymatlar), max(qiymatlar)
            farq = max_q - min_q if max_q != min_q else 1
            
            yangi = []
            for m in self.malumotlar:
                m = list(m)
                m[ustun] = (m[ustun] - min_q) / farq
                yangi.append(m)
            return MalumotToplami(yangi)
        
        return self
    
    def __iter__(self):
        return iter(self.malumotlar)
    
    def __len__(self):
        return len(self.malumotlar)
    
    def __getitem__(self, indeks):
        return self.malumotlar[indeks]


# ============= STATISTIKA =============

def ortacha(sonlar: List[float]) -> float:
    """O'rtacha qiymat"""
    return sum(sonlar) / len(sonlar) if sonlar else 0


def median(sonlar: List[float]) -> float:
    """Median"""
    saralangan = sorted(sonlar)
    n = len(saralangan)
    if n == 0:
        return 0
    if n % 2 == 0:
        return (saralangan[n//2 - 1] + saralangan[n//2]) / 2
    return saralangan[n//2]


def moda(sonlar: List[float]) -> float:
    """Moda (eng ko'p uchraydigan)"""
    sanoq = {}
    for s in sonlar:
        sanoq[s] = sanoq.get(s, 0) + 1
    return max(sanoq, key=sanoq.get)


def dispersiya(sonlar: List[float]) -> float:
    """Dispersiya"""
    ort = ortacha(sonlar)
    return sum((x - ort) ** 2 for x in sonlar) / len(sonlar)


def standart_chetlanish(sonlar: List[float]) -> float:
    """Standart chetlanish"""
    return math.sqrt(dispersiya(sonlar))


def kovariatsiya(x: List[float], y: List[float]) -> float:
    """Kovariatsiya"""
    ort_x, ort_y = ortacha(x), ortacha(y)
    return sum((xi - ort_x) * (yi - ort_y) for xi, yi in zip(x, y)) / len(x)


def korrelyatsiya(x: List[float], y: List[float]) -> float:
    """Pearson korrelyatsiya koeffitsiyenti"""
    std_x, std_y = standart_chetlanish(x), standart_chetlanish(y)
    if std_x == 0 or std_y == 0:
        return 0
    return kovariatsiya(x, y) / (std_x * std_y)


# ============= MASOFA FUNKSIYALARI =============

def evklid_masofasi(a: List[float], b: List[float]) -> float:
    """Evklid masofasi"""
    return math.sqrt(sum((ai - bi) ** 2 for ai, bi in zip(a, b)))


def manhattan_masofasi(a: List[float], b: List[float]) -> float:
    """Manhattan masofasi"""
    return sum(abs(ai - bi) for ai, bi in zip(a, b))


def kosinus_oxshashligi(a: List[float], b: List[float]) -> float:
    """Kosinus o'xshashligi"""
    nuqta = sum(ai * bi for ai, bi in zip(a, b))
    norma_a = math.sqrt(sum(ai ** 2 for ai in a))
    norma_b = math.sqrt(sum(bi ** 2 for bi in b))
    if norma_a == 0 or norma_b == 0:
        return 0
    return nuqta / (norma_a * norma_b)


# ============= ENCODING =============

def birlik_kodlash(kategoriyalar: List[Any]) -> Dict[Any, List[int]]:
    """One-hot encoding"""
    unikal = list(set(kategoriyalar))
    kodlar = {}
    for i, kat in enumerate(unikal):
        kod = [0] * len(unikal)
        kod[i] = 1
        kodlar[kat] = kod
    return kodlar


def yorliq_kodlash(kategoriyalar: List[Any]) -> Dict[Any, int]:
    """Label encoding"""
    unikal = list(set(kategoriyalar))
    return {kat: i for i, kat in enumerate(unikal)}


# ============= XUSUSIYATLAR =============

def min_max_normalizatsiya(sonlar: List[float]) -> List[float]:
    """Min-Max normalizatsiya (0-1 oralig'iga)"""
    min_q, max_q = min(sonlar), max(sonlar)
    farq = max_q - min_q if max_q != min_q else 1
    return [(x - min_q) / farq for x in sonlar]


def z_normalizatsiya(sonlar: List[float]) -> List[float]:
    """Z-score normalizatsiya"""
    ort = ortacha(sonlar)
    std = standart_chetlanish(sonlar)
    if std == 0:
        return [0] * len(sonlar)
    return [(x - ort) / std for x in sonlar]


__all__ = [
    'MalumotToplami', 'ortacha', 'median', 'moda', 'dispersiya',
    'standart_chetlanish', 'kovariatsiya', 'korrelyatsiya',
    'evklid_masofasi', 'manhattan_masofasi', 'kosinus_oxshashligi',
    'birlik_kodlash', 'yorliq_kodlash', 'min_max_normalizatsiya', 'z_normalizatsiya'
]
