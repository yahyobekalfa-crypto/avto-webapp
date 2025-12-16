"""
AL Neyron Tarmoq
O'zbekcha neyron tarmoq implementatsiyasi
"""

import math
import random
from typing import List, Callable


def sigmoid(x: float) -> float:
    """Sigmoid aktivatsiya"""
    return 1 / (1 + math.exp(-max(-500, min(500, x))))


def sigmoid_hosilasi(x: float) -> float:
    """Sigmoid hosilasi"""
    return x * (1 - x)


def relu(x: float) -> float:
    """ReLU aktivatsiya"""
    return max(0, x)


def tanh(x: float) -> float:
    """Tanh aktivatsiya"""
    return math.tanh(x)


class Neyron:
    """Bitta neyron"""
    
    def __init__(self, kirishlar_soni: int):
        self.vaznlar = [random.uniform(-1, 1) for _ in range(kirishlar_soni)]
        self.bias = random.uniform(-1, 1)
        self.chiqish = 0.0
        self.delta = 0.0
    
    def oldinAga(self, kirishlar: List[float], aktivatsiya: Callable = sigmoid) -> float:
        """Oldinga tarqalish"""
        yigindi = sum(k * v for k, v in zip(kirishlar, self.vaznlar)) + self.bias
        self.chiqish = aktivatsiya(yigindi)
        return self.chiqish


class Qatlam:
    """Neyronlar qatlami"""
    
    def __init__(self, neyronlar_soni: int, kirishlar_soni: int):
        self.neyronlar = [Neyron(kirishlar_soni) for _ in range(neyronlar_soni)]
    
    def oldinAga(self, kirishlar: List[float], aktivatsiya: Callable = sigmoid) -> List[float]:
        """Qatlamdan o'tkazish"""
        return [n.oldinAga(kirishlar, aktivatsiya) for n in self.neyronlar]


class NeyronTarmog:
    """Ko'p qatlamli neyron tarmoq"""
    
    def __init__(self, tuzilma: List[int]):
        """
        tuzilma: [kirish, yashirin1, yashirin2, ..., chiqish]
        Masalan: [784, 128, 64, 10]
        """
        self.tuzilma = tuzilma
        self.qatlamlar: List[Qatlam] = []
        
        for i in range(1, len(tuzilma)):
            self.qatlamlar.append(Qatlam(tuzilma[i], tuzilma[i-1]))
    
    def bashorat(self, kirish: List[float]) -> List[float]:
        """Bashorat qilish"""
        joriy = kirish
        for qatlam in self.qatlamlar:
            joriy = qatlam.oldinAga(joriy)
        return joriy
    
    def orgatish(self, kirishlar: List[List[float]], maqsadlar: List[List[float]], 
                 epochlar: int = 1000, tezlik: float = 0.1):
        """Tarmoqni o'rgatish (backpropagation)"""
        for epoch in range(epochlar):
            umumiy_xato = 0.0
            
            for kirish, maqsad in zip(kirishlar, maqsadlar):
                # Oldinga
                chiqish = self.bashorat(kirish)
                
                # Xatoni hisoblash
                xato = sum((m - c) ** 2 for m, c in zip(maqsad, chiqish)) / len(maqsad)
                umumiy_xato += xato
                
                # Orqaga tarqalish
                self._orqaga_tarqalish(kirish, maqsad, tezlik)
            
            if epoch % 100 == 0:
                ortcha_xato = umumiy_xato / len(kirishlar)
                print(f"Epoch {epoch}: Xato = {ortcha_xato:.6f}")
    
    def _orqaga_tarqalish(self, kirish: List[float], maqsad: List[float], tezlik: float):
        """Orqaga tarqalish algoritmi"""
        # Oxirgi qatlamdan boshlash
        for i, neyron in enumerate(self.qatlamlar[-1].neyronlar):
            xato = maqsad[i] - neyron.chiqish
            neyron.delta = xato * sigmoid_hosilasi(neyron.chiqish)
        
        # Yashirin qatlamlar
        for q in range(len(self.qatlamlar) - 2, -1, -1):
            qatlam = self.qatlamlar[q]
            keyingi_qatlam = self.qatlamlar[q + 1]
            
            for i, neyron in enumerate(qatlam.neyronlar):
                xato = sum(k.vaznlar[i] * k.delta for k in keyingi_qatlam.neyronlar)
                neyron.delta = xato * sigmoid_hosilasi(neyron.chiqish)
        
        # Vaznlarni yangilash
        oldingi_chiqish = kirish
        for qatlam in self.qatlamlar:
            for neyron in qatlam.neyronlar:
                for j in range(len(neyron.vaznlar)):
                    neyron.vaznlar[j] += tezlik * neyron.delta * oldingi_chiqish[j]
                neyron.bias += tezlik * neyron.delta
            oldingi_chiqish = [n.chiqish for n in qatlam.neyronlar]
    
    def aniqlik(self, kirishlar: List[List[float]], maqsadlar: List[List[float]]) -> float:
        """Aniqlikni hisoblash"""
        togri = 0
        for kirish, maqsad in zip(kirishlar, maqsadlar):
            bashorat = self.bashorat(kirish)
            if bashorat.index(max(bashorat)) == maqsad.index(max(maqsad)):
                togri += 1
        return togri / len(kirishlar)


class Perseptron:
    """Oddiy perseptron"""
    
    def __init__(self, kirishlar_soni: int):
        self.vaznlar = [random.uniform(-1, 1) for _ in range(kirishlar_soni)]
        self.bias = random.uniform(-1, 1)
    
    def bashorat(self, kirish: List[float]) -> int:
        """Bashorat (0 yoki 1)"""
        yigindi = sum(k * v for k, v in zip(kirish, self.vaznlar)) + self.bias
        return 1 if yigindi >= 0 else 0
    
    def orgatish(self, kirishlar: List[List[float]], maqsadlar: List[int], 
                 epochlar: int = 100, tezlik: float = 0.1):
        """O'rgatish"""
        for _ in range(epochlar):
            for kirish, maqsad in zip(kirishlar, maqsadlar):
                bashorat = self.bashorat(kirish)
                xato = maqsad - bashorat
                
                for i in range(len(self.vaznlar)):
                    self.vaznlar[i] += tezlik * xato * kirish[i]
                self.bias += tezlik * xato


__all__ = ['NeyronTarmog', 'Neyron', 'Qatlam', 'Perseptron', 'sigmoid', 'relu', 'tanh']
