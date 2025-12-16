"""
AL Transpiler
AST ni Python kodiga o'girish
"""

from typing import List
from .parser import (
    ASTNode, Dastur, Raqam, Satr, Mantiqiy, Hech, Identifikator,
    Tayinlash, BinarOperatsiya, UnarOperatsiya, Shart, UchunSikl,
    TokiSikl, FunksiyaDefinitsiya, FunksiyaChaqiruv, Qaytarish,
    SinfDefinitsiya, Atribut, IndeksOlish, Royxat, Lugat,
    Uzish, Davom, Otkazish, Import, ImportDan, HarakatTutish
)
from .tokens import KALIT_SOZLAR


class Transpiler:
    """AL kodini Python kodiga o'girish"""
    
    # O'zbekcha funksiya nomlari -> Python
    FUNKSIYA_TARJIMALARI = {
        # Asosiy
        'chop': 'print',
        'kiritish': 'input',
        'uzunlik': 'len',
        'turi': 'type',
        'oraliq': 'range',
        'royxat': 'list',
        'lugat': 'dict',
        'toplam': 'set',
        'satr': 'str',
        'butun': 'int',
        'haqiqiy': 'float',
        'mantiqiy': 'bool',
        
        # Matematik
        'abs': 'abs',
        'yaxlitlash': 'round',
        'min': 'min',
        'max': 'max',
        'sum': 'sum',
        'yigindi': 'sum',
        
        # Ro'yxat
        'saralash': 'sorted',
        'teskari': 'reversed',
        'sanash': 'enumerate',
        'filtrlash': 'filter',
        'xaritalash': 'map',
        'qisqartirish': 'reduce',
        'hammasi': 'all',
        'birortasi': 'any',
        'zip': 'zip',
        
        # Fayl
        'ochish': 'open',
        
        # Boshqa
        'id': 'id',
        'hash': 'hash',
        'dir': 'dir',
        'yordam': 'help',
        'exec': 'exec',
        'eval': 'eval',
    }
    
    # O'zbekcha metodlar -> Python
    METOD_TARJIMALARI = {
        # String metodlari
        'qoshish': 'append',
        'kengaytirish': 'extend',
        'olib_tashlash': 'remove',
        'chiqarib_olish': 'pop',
        'tozalash': 'clear',
        'nusxa': 'copy',
        'indeks': 'index',
        'sanash': 'count',
        'tartiblash': 'sort',
        'teskari_qilish': 'reverse',
        'birlashtirish': 'join',
        'ajratish': 'split',
        'almashtirish': 'replace',
        'katta_harf': 'upper',
        'kichik_harf': 'lower',
        'bosh_harf': 'capitalize',
        'sarlavha': 'title',
        'kesish': 'strip',
        'bilan_boshlanadi': 'startswith',
        'bilan_tugaydi': 'endswith',
        'topish': 'find',
        'formatlash': 'format',
        
        # Dict metodlari
        'kalitlar': 'keys',
        'qiymatlar': 'values',
        'juftliklar': 'items',
        'olish': 'get',
        'yangilash': 'update',
        
        # File metodlari
        'okish': 'read',
        'yozish': 'write',
        'yopish': 'close',
        'qatorlar': 'readlines',
    }
    
    def __init__(self, indent_size: int = 4):
        self.indent_size = indent_size
        self.indent_level = 0
    
    def _indent(self) -> str:
        """Joriy indent"""
        return ' ' * (self.indent_level * self.indent_size)
    
    def transpile(self, ast: Dastur) -> str:
        """ASTni Python kodiga o'girish"""
        # Import qismini qo'shish
        kod = "# -*- coding: utf-8 -*-\n"
        kod += "# AL (Algoritm Tili) dan Python ga transpile qilingan\n\n"
        
        # Amallarni transpile qilish
        for amal in ast.amallar:
            kod += self._node_transpile(amal) + '\n'
        
        return kod
    
    def _node_transpile(self, node: ASTNode) -> str:
        """Bitta nodeni transpile qilish"""
        if isinstance(node, Raqam):
            return str(node.qiymat)
        
        elif isinstance(node, Satr):
            # F-string tekshirish
            if node.qiymat.startswith('f"') or node.qiymat.startswith("f'"):
                return node.qiymat
            return repr(node.qiymat)
        
        elif isinstance(node, Mantiqiy):
            return 'True' if node.qiymat else 'False'
        
        elif isinstance(node, Hech):
            return 'None'
        
        elif isinstance(node, Identifikator):
            # ozini -> self
            if node.nom == 'ozini':
                return 'self'
            return node.nom
        
        elif isinstance(node, Tayinlash):
            nom = node.nom
            if nom == 'ozini':
                nom = 'self'
            qiymat = self._node_transpile(node.qiymat)
            return f"{self._indent()}{nom} {node.operator} {qiymat}"
        
        elif isinstance(node, BinarOperatsiya):
            chap = self._node_transpile(node.chap)
            ong = self._node_transpile(node.ong)
            return f"({chap} {node.operator} {ong})"
        
        elif isinstance(node, UnarOperatsiya):
            operand = self._node_transpile(node.operand)
            if node.operator == 'not':
                return f"(not {operand})"
            return f"({node.operator}{operand})"
        
        elif isinstance(node, Shart):
            return self._shart_transpile(node)
        
        elif isinstance(node, UchunSikl):
            return self._uchun_sikl_transpile(node)
        
        elif isinstance(node, TokiSikl):
            return self._toki_sikl_transpile(node)
        
        elif isinstance(node, FunksiyaDefinitsiya):
            return self._funksiya_transpile(node)
        
        elif isinstance(node, FunksiyaChaqiruv):
            return self._funksiya_chaqiruv_transpile(node)
        
        elif isinstance(node, Qaytarish):
            qiymat = self._node_transpile(node.qiymat) if node.qiymat else ''
            return f"{self._indent()}return {qiymat}".strip()
        
        elif isinstance(node, SinfDefinitsiya):
            return self._sinf_transpile(node)
        
        elif isinstance(node, Atribut):
            obyekt = self._node_transpile(node.obyekt)
            atribut = self.METOD_TARJIMALARI.get(node.atribut, node.atribut)
            return f"{obyekt}.{atribut}"
        
        elif isinstance(node, IndeksOlish):
            obyekt = self._node_transpile(node.obyekt)
            indeks = self._node_transpile(node.indeks)
            return f"{obyekt}[{indeks}]"
        
        elif isinstance(node, Royxat):
            elementlar = ', '.join(self._node_transpile(e) for e in node.elementlar)
            return f"[{elementlar}]"
        
        elif isinstance(node, Lugat):
            juftliklar = ', '.join(
                f"{self._node_transpile(k)}: {self._node_transpile(v)}" 
                for k, v in node.juftliklar
            )
            return f"{{{juftliklar}}}"
        
        elif isinstance(node, Uzish):
            return f"{self._indent()}break"
        
        elif isinstance(node, Davom):
            return f"{self._indent()}continue"
        
        elif isinstance(node, Otkazish):
            return f"{self._indent()}pass"
        
        elif isinstance(node, Import):
            if node.nom:
                return f"{self._indent()}import {node.modul} as {node.nom}"
            return f"{self._indent()}import {node.modul}"
        
        elif isinstance(node, ImportDan):
            nomlar = ', '.join(node.nomlar)
            return f"{self._indent()}from {node.modul} import {nomlar}"
        
        elif isinstance(node, HarakatTutish):
            return self._harakat_tutish_transpile(node)
        
        return str(node)
    
    def _shart_transpile(self, node: Shart) -> str:
        """if/elif/else transpile"""
        shart = self._node_transpile(node.shart)
        kod = f"{self._indent()}if {shart}:\n"
        
        self.indent_level += 1
        for amal in node.tanasi:
            kod += self._node_transpile(amal) + '\n'
        if not node.tanasi:
            kod += f"{self._indent()}pass\n"
        self.indent_level -= 1
        
        # elif
        for aks_shart, aks_tanasi in node.aks_holda:
            shart = self._node_transpile(aks_shart)
            kod += f"{self._indent()}elif {shart}:\n"
            
            self.indent_level += 1
            for amal in aks_tanasi:
                kod += self._node_transpile(amal) + '\n'
            if not aks_tanasi:
                kod += f"{self._indent()}pass\n"
            self.indent_level -= 1
        
        # else
        if node.boshqa:
            kod += f"{self._indent()}else:\n"
            
            self.indent_level += 1
            for amal in node.boshqa:
                kod += self._node_transpile(amal) + '\n'
            self.indent_level -= 1
        
        return kod.rstrip()
    
    def _uchun_sikl_transpile(self, node: UchunSikl) -> str:
        """for sikl transpile"""
        iterator = self._node_transpile(node.iterator)
        kod = f"{self._indent()}for {node.ozgaruvchi} in {iterator}:\n"
        
        self.indent_level += 1
        for amal in node.tanasi:
            kod += self._node_transpile(amal) + '\n'
        if not node.tanasi:
            kod += f"{self._indent()}pass\n"
        self.indent_level -= 1
        
        return kod.rstrip()
    
    def _toki_sikl_transpile(self, node: TokiSikl) -> str:
        """while sikl transpile"""
        shart = self._node_transpile(node.shart)
        kod = f"{self._indent()}while {shart}:\n"
        
        self.indent_level += 1
        for amal in node.tanasi:
            kod += self._node_transpile(amal) + '\n'
        if not node.tanasi:
            kod += f"{self._indent()}pass\n"
        self.indent_level -= 1
        
        return kod.rstrip()
    
    def _funksiya_transpile(self, node: FunksiyaDefinitsiya) -> str:
        """Funksiya transpile"""
        parametrlar = []
        for param in node.parametrlar:
            if param == 'ozini':
                param = 'self'
            if param in node.default_qiymatlar:
                default = self._node_transpile(node.default_qiymatlar[param])
                parametrlar.append(f"{param}={default}")
            else:
                parametrlar.append(param)
        
        params_str = ', '.join(parametrlar)
        kod = f"{self._indent()}def {node.nom}({params_str}):\n"
        
        self.indent_level += 1
        for amal in node.tanasi:
            kod += self._node_transpile(amal) + '\n'
        if not node.tanasi:
            kod += f"{self._indent()}pass\n"
        self.indent_level -= 1
        
        return kod.rstrip()
    
    def _funksiya_chaqiruv_transpile(self, node: FunksiyaChaqiruv) -> str:
        """Funksiya chaqiruvi transpile"""
        # Funksiya nomini tarjima qilish
        nom = node.nom
        
        # Metod chaqiruvi
        if '.' in nom:
            qismlar = nom.rsplit('.', 1)
            obyekt = qismlar[0]
            metod = qismlar[1]
            metod = self.METOD_TARJIMALARI.get(metod, metod)
            nom = f"{obyekt}.{metod}"
        else:
            nom = self.FUNKSIYA_TARJIMALARI.get(nom, nom)
        
        # Argumentlar
        args = [self._node_transpile(arg) for arg in node.argumentlar]
        
        # Kalit argumentlar
        for kalit, qiymat in node.kalit_argumentlar.items():
            args.append(f"{kalit}={self._node_transpile(qiymat)}")
        
        args_str = ', '.join(args)
        
        return f"{self._indent()}{nom}({args_str})".strip()
    
    def _sinf_transpile(self, node: SinfDefinitsiya) -> str:
        """Sinf transpile"""
        ota = f"({node.ota_sinf})" if node.ota_sinf else ""
        kod = f"{self._indent()}class {node.nom}{ota}:\n"
        
        self.indent_level += 1
        for amal in node.tanasi:
            kod += self._node_transpile(amal) + '\n'
        if not node.tanasi:
            kod += f"{self._indent()}pass\n"
        self.indent_level -= 1
        
        return kod.rstrip()
    
    def _harakat_tutish_transpile(self, node: HarakatTutish) -> str:
        """try/except/finally transpile"""
        kod = f"{self._indent()}try:\n"
        
        self.indent_level += 1
        for amal in node.harakat:
            kod += self._node_transpile(amal) + '\n'
        if not node.harakat:
            kod += f"{self._indent()}pass\n"
        self.indent_level -= 1
        
        for xato_turi, nom, tanasi in node.tutishlar:
            if xato_turi and nom:
                kod += f"{self._indent()}except {xato_turi} as {nom}:\n"
            elif xato_turi:
                kod += f"{self._indent()}except {xato_turi}:\n"
            else:
                kod += f"{self._indent()}except:\n"
            
            self.indent_level += 1
            for amal in tanasi:
                kod += self._node_transpile(amal) + '\n'
            if not tanasi:
                kod += f"{self._indent()}pass\n"
            self.indent_level -= 1
        
        if node.nihoyat:
            kod += f"{self._indent()}finally:\n"
            
            self.indent_level += 1
            for amal in node.nihoyat:
                kod += self._node_transpile(amal) + '\n'
            self.indent_level -= 1
        
        return kod.rstrip()
