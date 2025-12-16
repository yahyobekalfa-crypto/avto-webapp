"""
AL Parser (Tahlilchi)
Tokenlarni AST ga o'girish
"""

from typing import List, Any, Optional
from .tokens import Token, TokenTuri, KALIT_SOZLAR
from .errors import SintaksisXatosi


class ASTNode:
    """Asosiy AST tugun sinfi"""
    pass


class Dastur(ASTNode):
    """Butun dastur"""
    def __init__(self, amallar: List[ASTNode]):
        self.amallar = amallar


class Raqam(ASTNode):
    """Raqam literali"""
    def __init__(self, qiymat: str):
        self.qiymat = float(qiymat) if '.' in qiymat else int(qiymat)


class Satr(ASTNode):
    """Satr literali"""
    def __init__(self, qiymat: str):
        self.qiymat = qiymat


class Mantiqiy(ASTNode):
    """Mantiqiy literal"""
    def __init__(self, qiymat: bool):
        self.qiymat = qiymat


class Hech(ASTNode):
    """None literal"""
    pass


class Identifikator(ASTNode):
    """O'zgaruvchi nomi"""
    def __init__(self, nom: str):
        self.nom = nom


class Tayinlash(ASTNode):
    """Tayinlash amali"""
    def __init__(self, nom: str, qiymat: ASTNode, operator: str = "="):
        self.nom = nom
        self.qiymat = qiymat
        self.operator = operator


class BinarOperatsiya(ASTNode):
    """Ikkilik amal"""
    def __init__(self, chap: ASTNode, operator: str, ong: ASTNode):
        self.chap = chap
        self.operator = operator
        self.ong = ong


class UnarOperatsiya(ASTNode):
    """Birlik amal"""
    def __init__(self, operator: str, operand: ASTNode):
        self.operator = operator
        self.operand = operand


class Shart(ASTNode):
    """if/elif/else"""
    def __init__(self, shart: ASTNode, tanasi: List[ASTNode], 
                 aks_holda: List[tuple] = None, boshqa: List[ASTNode] = None):
        self.shart = shart
        self.tanasi = tanasi
        self.aks_holda = aks_holda or []  # [(shart, tanasi), ...]
        self.boshqa = boshqa or []


class UchunSikl(ASTNode):
    """for sikli"""
    def __init__(self, ozgaruvchi: str, iterator: ASTNode, tanasi: List[ASTNode]):
        self.ozgaruvchi = ozgaruvchi
        self.iterator = iterator
        self.tanasi = tanasi


class TokiSikl(ASTNode):
    """while sikli"""
    def __init__(self, shart: ASTNode, tanasi: List[ASTNode]):
        self.shart = shart
        self.tanasi = tanasi


class FunksiyaDefinitsiya(ASTNode):
    """Funksiya definitsiyasi"""
    def __init__(self, nom: str, parametrlar: List[str], tanasi: List[ASTNode], 
                 default_qiymatlar: dict = None):
        self.nom = nom
        self.parametrlar = parametrlar
        self.tanasi = tanasi
        self.default_qiymatlar = default_qiymatlar or {}


class FunksiyaChaqiruv(ASTNode):
    """Funksiya chaqiruvi"""
    def __init__(self, nom: str, argumentlar: List[ASTNode], kalit_argumentlar: dict = None):
        self.nom = nom
        self.argumentlar = argumentlar
        self.kalit_argumentlar = kalit_argumentlar or {}


class Qaytarish(ASTNode):
    """return"""
    def __init__(self, qiymat: ASTNode = None):
        self.qiymat = qiymat


class SinfDefinitsiya(ASTNode):
    """Sinf definitsiyasi"""
    def __init__(self, nom: str, ota_sinf: str, tanasi: List[ASTNode]):
        self.nom = nom
        self.ota_sinf = ota_sinf
        self.tanasi = tanasi


class Atribut(ASTNode):
    """Obyekt atributi (obj.attr)"""
    def __init__(self, obyekt: ASTNode, atribut: str):
        self.obyekt = obyekt
        self.atribut = atribut


class IndeksOlish(ASTNode):
    """Indeks olish (list[i])"""
    def __init__(self, obyekt: ASTNode, indeks: ASTNode):
        self.obyekt = obyekt
        self.indeks = indeks


class Royxat(ASTNode):
    """Ro'yxat literali"""
    def __init__(self, elementlar: List[ASTNode]):
        self.elementlar = elementlar


class Lugat(ASTNode):
    """Lug'at literali"""
    def __init__(self, juftliklar: List[tuple]):
        self.juftliklar = juftliklar


class Uzish(ASTNode):
    """break"""
    pass


class Davom(ASTNode):
    """continue"""
    pass


class Otkazish(ASTNode):
    """pass"""
    pass


class Import(ASTNode):
    """import"""
    def __init__(self, modul: str, nom: str = None):
        self.modul = modul
        self.nom = nom


class ImportDan(ASTNode):
    """from ... import ..."""
    def __init__(self, modul: str, nomlar: List[str]):
        self.modul = modul
        self.nomlar = nomlar


class HarakatTutish(ASTNode):
    """try/except/finally"""
    def __init__(self, harakat: List[ASTNode], tutishlar: List[tuple], 
                 nihoyat: List[ASTNode] = None):
        self.harakat = harakat
        self.tutishlar = tutishlar  # [(xato_turi, nom, tanasi), ...]
        self.nihoyat = nihoyat


class Parser:
    """AL dasturlash tili uchun parser"""
    
    def __init__(self, tokenlar: List[Token]):
        self.tokenlar = tokenlar
        self.pozitsiya = 0
        self.joriy_token = self.tokenlar[0] if tokenlar else None
    
    def _keyingi(self):
        """Keyingi tokenga o'tish"""
        self.pozitsiya += 1
        if self.pozitsiya < len(self.tokenlar):
            self.joriy_token = self.tokenlar[self.pozitsiya]
        else:
            self.joriy_token = None
    
    def _oldinga_qara(self, qadamlar: int = 1) -> Optional[Token]:
        """Oldindagi tokenni ko'rish"""
        pos = self.pozitsiya + qadamlar
        if pos < len(self.tokenlar):
            return self.tokenlar[pos]
        return None
    
    def _kutish(self, turi: TokenTuri, qiymat: str = None) -> Token:
        """Ma'lum turdagi tokenni kutish"""
        if self.joriy_token is None:
            raise SintaksisXatosi(f"Kutilmagan fayl oxiri")
        
        if self.joriy_token.turi != turi:
            raise SintaksisXatosi(
                f"Kutilgan: {turi.name}, topildi: {self.joriy_token.turi.name}",
                self.joriy_token.qator, self.joriy_token.ustun
            )
        
        if qiymat and self.joriy_token.qiymat != qiymat:
            raise SintaksisXatosi(
                f"Kutilgan: '{qiymat}', topildi: '{self.joriy_token.qiymat}'",
                self.joriy_token.qator, self.joriy_token.ustun
            )
        
        token = self.joriy_token
        self._keyingi()
        return token
    
    def _yangi_qatorlarni_otkazish(self):
        """Yangi qatorlarni o'tkazib yuborish"""
        while self.joriy_token and self.joriy_token.turi == TokenTuri.YANGI_QATOR:
            self._keyingi()
    
    def parse(self) -> Dastur:
        """Tokenlarni parse qilish"""
        amallar = []
        
        while self.joriy_token and self.joriy_token.turi != TokenTuri.FAYL_OXIRI:
            self._yangi_qatorlarni_otkazish()
            
            if self.joriy_token and self.joriy_token.turi != TokenTuri.FAYL_OXIRI:
                amal = self._amal_parse()
                if amal:
                    amallar.append(amal)
        
        return Dastur(amallar)
    
    def _amal_parse(self) -> ASTNode:
        """Bitta amalni parse qilish"""
        if self.joriy_token is None:
            return None
        
        # Kalit so'zlarni tekshirish
        if self.joriy_token.turi == TokenTuri.KALIT_SOZ:
            qiymat = self.joriy_token.qiymat
            
            if qiymat == 'agar':
                return self._shart_parse()
            elif qiymat == 'uchun':
                return self._uchun_sikl_parse()
            elif qiymat == 'toki':
                return self._toki_sikl_parse()
            elif qiymat == 'funksiya':
                return self._funksiya_parse()
            elif qiymat == 'sinf':
                return self._sinf_parse()
            elif qiymat == 'qaytarish':
                return self._qaytarish_parse()
            elif qiymat == 'uzish':
                self._keyingi()
                return Uzish()
            elif qiymat == 'davom':
                self._keyingi()
                return Davom()
            elif qiymat == 'otkazish':
                self._keyingi()
                return Otkazish()
            elif qiymat == 'import':
                return self._import_parse()
            elif qiymat == 'dan':
                return self._import_dan_parse()
            elif qiymat == 'harakat':
                return self._harakat_tutish_parse()
        
        # Ifodani parse qilish
        return self._ifoda_parse()
    
    def _shart_parse(self) -> Shart:
        """if/elif/else parse qilish"""
        self._kutish(TokenTuri.KALIT_SOZ, 'agar')
        shart = self._ifoda_parse()
        self._kutish(TokenTuri.IKKI_NUQTA)
        
        tanasi = self._blok_parse()
        
        aks_holda = []
        boshqa = None
        
        self._yangi_qatorlarni_otkazish()
        
        # elif
        while (self.joriy_token and 
               self.joriy_token.turi == TokenTuri.KALIT_SOZ and 
               self.joriy_token.qiymat == 'aks_holda'):
            self._keyingi()
            aks_shart = self._ifoda_parse()
            self._kutish(TokenTuri.IKKI_NUQTA)
            aks_tanasi = self._blok_parse()
            aks_holda.append((aks_shart, aks_tanasi))
            self._yangi_qatorlarni_otkazish()
        
        # else
        if (self.joriy_token and 
            self.joriy_token.turi == TokenTuri.KALIT_SOZ and 
            self.joriy_token.qiymat == 'boshqa'):
            self._keyingi()
            self._kutish(TokenTuri.IKKI_NUQTA)
            boshqa = self._blok_parse()
        
        return Shart(shart, tanasi, aks_holda, boshqa)
    
    def _uchun_sikl_parse(self) -> UchunSikl:
        """for sikl parse qilish"""
        self._kutish(TokenTuri.KALIT_SOZ, 'uchun')
        ozgaruvchi_token = self._kutish(TokenTuri.IDENTIFIKATOR)
        ozgaruvchi = ozgaruvchi_token.qiymat
        
        self._kutish(TokenTuri.KALIT_SOZ, 'ichida')
        iterator = self._ifoda_parse()
        self._kutish(TokenTuri.IKKI_NUQTA)
        
        tanasi = self._blok_parse()
        
        return UchunSikl(ozgaruvchi, iterator, tanasi)
    
    def _toki_sikl_parse(self) -> TokiSikl:
        """while sikl parse qilish"""
        self._kutish(TokenTuri.KALIT_SOZ, 'toki')
        shart = self._ifoda_parse()
        self._kutish(TokenTuri.IKKI_NUQTA)
        
        tanasi = self._blok_parse()
        
        return TokiSikl(shart, tanasi)
    
    def _funksiya_parse(self) -> FunksiyaDefinitsiya:
        """Funksiya definitsiyasini parse qilish"""
        self._kutish(TokenTuri.KALIT_SOZ, 'funksiya')
        nom_token = self._kutish(TokenTuri.IDENTIFIKATOR)
        nom = nom_token.qiymat
        
        self._kutish(TokenTuri.OCHIQ_QAVS)
        
        parametrlar = []
        default_qiymatlar = {}
        
        while self.joriy_token and self.joriy_token.turi != TokenTuri.YOPIQ_QAVS:
            param_token = self._kutish(TokenTuri.IDENTIFIKATOR)
            param = param_token.qiymat
            parametrlar.append(param)
            
            # Default qiymat
            if self.joriy_token and self.joriy_token.turi == TokenTuri.TAYINLASH:
                self._keyingi()
                default_qiymatlar[param] = self._ifoda_parse()
            
            if self.joriy_token and self.joriy_token.turi == TokenTuri.VERGUL:
                self._keyingi()
        
        self._kutish(TokenTuri.YOPIQ_QAVS)
        self._kutish(TokenTuri.IKKI_NUQTA)
        
        tanasi = self._blok_parse()
        
        return FunksiyaDefinitsiya(nom, parametrlar, tanasi, default_qiymatlar)
    
    def _sinf_parse(self) -> SinfDefinitsiya:
        """Sinf definitsiyasini parse qilish"""
        self._kutish(TokenTuri.KALIT_SOZ, 'sinf')
        nom_token = self._kutish(TokenTuri.IDENTIFIKATOR)
        nom = nom_token.qiymat
        
        ota_sinf = None
        if self.joriy_token and self.joriy_token.turi == TokenTuri.OCHIQ_QAVS:
            self._keyingi()
            if self.joriy_token and self.joriy_token.turi == TokenTuri.IDENTIFIKATOR:
                ota_sinf = self.joriy_token.qiymat
                self._keyingi()
            self._kutish(TokenTuri.YOPIQ_QAVS)
        
        self._kutish(TokenTuri.IKKI_NUQTA)
        
        tanasi = self._blok_parse()
        
        return SinfDefinitsiya(nom, ota_sinf, tanasi)
    
    def _qaytarish_parse(self) -> Qaytarish:
        """return parse qilish"""
        self._kutish(TokenTuri.KALIT_SOZ, 'qaytarish')
        
        qiymat = None
        if self.joriy_token and self.joriy_token.turi not in [TokenTuri.YANGI_QATOR, TokenTuri.FAYL_OXIRI]:
            qiymat = self._ifoda_parse()
        
        return Qaytarish(qiymat)
    
    def _import_parse(self) -> Import:
        """import parse qilish"""
        self._kutish(TokenTuri.KALIT_SOZ, 'import')
        modul_token = self._kutish(TokenTuri.IDENTIFIKATOR)
        modul = modul_token.qiymat
        
        nom = None
        if self.joriy_token and self.joriy_token.qiymat == 'sifatida':
            self._keyingi()
            nom_token = self._kutish(TokenTuri.IDENTIFIKATOR)
            nom = nom_token.qiymat
        
        return Import(modul, nom)
    
    def _import_dan_parse(self) -> ImportDan:
        """from ... import ... parse qilish"""
        self._kutish(TokenTuri.KALIT_SOZ, 'dan')
        modul_token = self._kutish(TokenTuri.IDENTIFIKATOR)
        modul = modul_token.qiymat
        
        self._kutish(TokenTuri.KALIT_SOZ, 'import')
        
        nomlar = []
        nom_token = self._kutish(TokenTuri.IDENTIFIKATOR)
        nomlar.append(nom_token.qiymat)
        
        while self.joriy_token and self.joriy_token.turi == TokenTuri.VERGUL:
            self._keyingi()
            nom_token = self._kutish(TokenTuri.IDENTIFIKATOR)
            nomlar.append(nom_token.qiymat)
        
        return ImportDan(modul, nomlar)
    
    def _harakat_tutish_parse(self) -> HarakatTutish:
        """try/except/finally parse qilish"""
        self._kutish(TokenTuri.KALIT_SOZ, 'harakat')
        self._kutish(TokenTuri.IKKI_NUQTA)
        
        harakat = self._blok_parse()
        
        tutishlar = []
        self._yangi_qatorlarni_otkazish()
        
        while (self.joriy_token and 
               self.joriy_token.turi == TokenTuri.KALIT_SOZ and 
               self.joriy_token.qiymat == 'tutish'):
            self._keyingi()
            
            xato_turi = None
            nom = None
            
            if self.joriy_token and self.joriy_token.turi == TokenTuri.IDENTIFIKATOR:
                xato_turi = self.joriy_token.qiymat
                self._keyingi()
                
                if self.joriy_token and self.joriy_token.qiymat == 'sifatida':
                    self._keyingi()
                    nom = self.joriy_token.qiymat
                    self._keyingi()
            
            self._kutish(TokenTuri.IKKI_NUQTA)
            tanasi = self._blok_parse()
            tutishlar.append((xato_turi, nom, tanasi))
            self._yangi_qatorlarni_otkazish()
        
        nihoyat = None
        if (self.joriy_token and 
            self.joriy_token.turi == TokenTuri.KALIT_SOZ and 
            self.joriy_token.qiymat == 'nihoyat'):
            self._keyingi()
            self._kutish(TokenTuri.IKKI_NUQTA)
            nihoyat = self._blok_parse()
        
        return HarakatTutish(harakat, tutishlar, nihoyat)
    
    def _blok_parse(self) -> List[ASTNode]:
        """Blokni parse qilish (indentatsiya bilan)"""
        self._yangi_qatorlarni_otkazish()
        
        amallar = []
        
        if self.joriy_token and self.joriy_token.turi == TokenTuri.INDENT:
            self._keyingi()
            
            while self.joriy_token and self.joriy_token.turi != TokenTuri.DEDENT:
                self._yangi_qatorlarni_otkazish()
                if self.joriy_token and self.joriy_token.turi != TokenTuri.DEDENT:
                    amal = self._amal_parse()
                    if amal:
                        amallar.append(amal)
            
            if self.joriy_token and self.joriy_token.turi == TokenTuri.DEDENT:
                self._keyingi()
        
        return amallar
    
    def _ifoda_parse(self) -> ASTNode:
        """Ifodani parse qilish"""
        return self._tayinlash_parse()
    
    def _tayinlash_parse(self) -> ASTNode:
        """Tayinlashni parse qilish"""
        chap = self._mantiqiy_yoki_parse()
        
        if self.joriy_token and self.joriy_token.turi in [
            TokenTuri.TAYINLASH, TokenTuri.QOSHIB_TAYINLASH,
            TokenTuri.AYIRIB_TAYINLASH, TokenTuri.KOPAYT_TAYINLASH,
            TokenTuri.BOLIB_TAYINLASH
        ]:
            operator = self.joriy_token.qiymat
            self._keyingi()
            qiymat = self._ifoda_parse()
            
            if isinstance(chap, Identifikator):
                return Tayinlash(chap.nom, qiymat, operator)
            elif isinstance(chap, Atribut):
                return Tayinlash(f"{self._ast_to_str(chap.obyekt)}.{chap.atribut}", qiymat, operator)
        
        return chap
    
    def _mantiqiy_yoki_parse(self) -> ASTNode:
        """or parse qilish"""
        chap = self._mantiqiy_va_parse()
        
        while (self.joriy_token and 
               self.joriy_token.turi == TokenTuri.KALIT_SOZ and 
               self.joriy_token.qiymat == 'yoki'):
            self._keyingi()
            ong = self._mantiqiy_va_parse()
            chap = BinarOperatsiya(chap, 'or', ong)
        
        return chap
    
    def _mantiqiy_va_parse(self) -> ASTNode:
        """and parse qilish"""
        chap = self._mantiqiy_emas_parse()
        
        while (self.joriy_token and 
               self.joriy_token.turi == TokenTuri.KALIT_SOZ and 
               self.joriy_token.qiymat == 'va'):
            self._keyingi()
            ong = self._mantiqiy_emas_parse()
            chap = BinarOperatsiya(chap, 'and', ong)
        
        return chap
    
    def _mantiqiy_emas_parse(self) -> ASTNode:
        """not parse qilish"""
        if (self.joriy_token and 
            self.joriy_token.turi == TokenTuri.KALIT_SOZ and 
            self.joriy_token.qiymat == 'emas'):
            self._keyingi()
            operand = self._mantiqiy_emas_parse()
            return UnarOperatsiya('not', operand)
        
        return self._taqqoslash_parse()
    
    def _taqqoslash_parse(self) -> ASTNode:
        """Taqqoslash operatorlarini parse qilish"""
        chap = self._qoshish_ayirish_parse()
        
        taqqoslash_operatorlar = [
            TokenTuri.TENG, TokenTuri.TENG_EMAS, TokenTuri.KICHIK,
            TokenTuri.KATTA, TokenTuri.KICHIK_TENG, TokenTuri.KATTA_TENG
        ]
        
        while self.joriy_token and self.joriy_token.turi in taqqoslash_operatorlar:
            operator = self.joriy_token.qiymat
            self._keyingi()
            ong = self._qoshish_ayirish_parse()
            chap = BinarOperatsiya(chap, operator, ong)
        
        # 'ichida' operatori
        if (self.joriy_token and 
            self.joriy_token.turi == TokenTuri.KALIT_SOZ and 
            self.joriy_token.qiymat == 'ichida'):
            self._keyingi()
            ong = self._qoshish_ayirish_parse()
            chap = BinarOperatsiya(chap, 'in', ong)
        
        return chap
    
    def _qoshish_ayirish_parse(self) -> ASTNode:
        """+ va - operatorlarini parse qilish"""
        chap = self._kopaytirish_bolish_parse()
        
        while self.joriy_token and self.joriy_token.turi in [TokenTuri.QOSHISH, TokenTuri.AYIRISH]:
            operator = self.joriy_token.qiymat
            self._keyingi()
            ong = self._kopaytirish_bolish_parse()
            chap = BinarOperatsiya(chap, operator, ong)
        
        return chap
    
    def _kopaytirish_bolish_parse(self) -> ASTNode:
        """*, /, //, % operatorlarini parse qilish"""
        chap = self._daraja_parse()
        
        while self.joriy_token and self.joriy_token.turi in [
            TokenTuri.KOPAYTIRISH, TokenTuri.BOLISH, 
            TokenTuri.BUTUN_BOLISH, TokenTuri.QOLDIQ
        ]:
            operator = self.joriy_token.qiymat
            self._keyingi()
            ong = self._daraja_parse()
            chap = BinarOperatsiya(chap, operator, ong)
        
        return chap
    
    def _daraja_parse(self) -> ASTNode:
        """** operatorini parse qilish"""
        chap = self._unar_parse()
        
        if self.joriy_token and self.joriy_token.turi == TokenTuri.DARAJA:
            self._keyingi()
            ong = self._daraja_parse()  # O'ngga bog'langan
            chap = BinarOperatsiya(chap, '**', ong)
        
        return chap
    
    def _unar_parse(self) -> ASTNode:
        """Unar operatorlarni parse qilish"""
        if self.joriy_token and self.joriy_token.turi in [TokenTuri.QOSHISH, TokenTuri.AYIRISH]:
            operator = self.joriy_token.qiymat
            self._keyingi()
            operand = self._unar_parse()
            return UnarOperatsiya(operator, operand)
        
        return self._postfiks_parse()
    
    def _postfiks_parse(self) -> ASTNode:
        """Postfiks operatorlarni parse qilish (., [], ())"""
        chap = self._atom_parse()
        
        while self.joriy_token:
            if self.joriy_token.turi == TokenTuri.NUQTA:
                self._keyingi()
                atribut = self._kutish(TokenTuri.IDENTIFIKATOR)
                chap = Atribut(chap, atribut.qiymat)
            
            elif self.joriy_token.turi == TokenTuri.OCHIQ_KVADRAT:
                self._keyingi()
                indeks = self._ifoda_parse()
                self._kutish(TokenTuri.YOPIQ_KVADRAT)
                chap = IndeksOlish(chap, indeks)
            
            elif self.joriy_token.turi == TokenTuri.OCHIQ_QAVS:
                self._keyingi()
                argumentlar, kalit_argumentlar = self._argumentlar_parse()
                self._kutish(TokenTuri.YOPIQ_QAVS)
                
                if isinstance(chap, Identifikator):
                    chap = FunksiyaChaqiruv(chap.nom, argumentlar, kalit_argumentlar)
                elif isinstance(chap, Atribut):
                    chap = FunksiyaChaqiruv(
                        f"{self._ast_to_str(chap.obyekt)}.{chap.atribut}", 
                        argumentlar, kalit_argumentlar
                    )
            else:
                break
        
        return chap
    
    def _argumentlar_parse(self) -> tuple:
        """Funksiya argumentlarini parse qilish"""
        argumentlar = []
        kalit_argumentlar = {}
        
        while self.joriy_token and self.joriy_token.turi != TokenTuri.YOPIQ_QAVS:
            # Kalit argument tekshirish
            if (self.joriy_token.turi == TokenTuri.IDENTIFIKATOR and 
                self._oldinga_qara() and 
                self._oldinga_qara().turi == TokenTuri.TAYINLASH):
                kalit = self.joriy_token.qiymat
                self._keyingi()
                self._keyingi()  # = ni o'tkazish
                qiymat = self._ifoda_parse()
                kalit_argumentlar[kalit] = qiymat
            else:
                argumentlar.append(self._ifoda_parse())
            
            if self.joriy_token and self.joriy_token.turi == TokenTuri.VERGUL:
                self._keyingi()
        
        return argumentlar, kalit_argumentlar
    
    def _atom_parse(self) -> ASTNode:
        """Atom (eng oddiy ifoda) parse qilish"""
        token = self.joriy_token
        
        if token is None:
            raise SintaksisXatosi("Kutilmagan fayl oxiri")
        
        # Raqam
        if token.turi == TokenTuri.RAQAM:
            self._keyingi()
            return Raqam(token.qiymat)
        
        # Satr
        if token.turi == TokenTuri.SATR:
            self._keyingi()
            return Satr(token.qiymat)
        
        # Mantiqiy
        if token.turi == TokenTuri.MANTIQIY:
            self._keyingi()
            return Mantiqiy(token.qiymat == 'True')
        
        # None
        if token.turi == TokenTuri.HECH:
            self._keyingi()
            return Hech()
        
        # Identifikator
        if token.turi == TokenTuri.IDENTIFIKATOR:
            self._keyingi()
            return Identifikator(token.qiymat)
        
        # Qavsli ifoda
        if token.turi == TokenTuri.OCHIQ_QAVS:
            self._keyingi()
            ifoda = self._ifoda_parse()
            self._kutish(TokenTuri.YOPIQ_QAVS)
            return ifoda
        
        # Ro'yxat
        if token.turi == TokenTuri.OCHIQ_KVADRAT:
            return self._royxat_parse()
        
        # Lug'at
        if token.turi == TokenTuri.OCHIQ_FIGURALI:
            return self._lugat_parse()
        
        raise SintaksisXatosi(
            f"Kutilmagan token: {token.qiymat}",
            token.qator, token.ustun
        )
    
    def _royxat_parse(self) -> Royxat:
        """Ro'yxatni parse qilish"""
        self._kutish(TokenTuri.OCHIQ_KVADRAT)
        
        elementlar = []
        while self.joriy_token and self.joriy_token.turi != TokenTuri.YOPIQ_KVADRAT:
            elementlar.append(self._ifoda_parse())
            
            if self.joriy_token and self.joriy_token.turi == TokenTuri.VERGUL:
                self._keyingi()
        
        self._kutish(TokenTuri.YOPIQ_KVADRAT)
        return Royxat(elementlar)
    
    def _lugat_parse(self) -> Lugat:
        """Lug'atni parse qilish"""
        self._kutish(TokenTuri.OCHIQ_FIGURALI)
        
        juftliklar = []
        while self.joriy_token and self.joriy_token.turi != TokenTuri.YOPIQ_FIGURALI:
            kalit = self._ifoda_parse()
            self._kutish(TokenTuri.IKKI_NUQTA)
            qiymat = self._ifoda_parse()
            juftliklar.append((kalit, qiymat))
            
            if self.joriy_token and self.joriy_token.turi == TokenTuri.VERGUL:
                self._keyingi()
        
        self._kutish(TokenTuri.YOPIQ_FIGURALI)
        return Lugat(juftliklar)
    
    def _ast_to_str(self, node: ASTNode) -> str:
        """AST nodeni satrga o'girish"""
        if isinstance(node, Identifikator):
            return node.nom
        elif isinstance(node, Atribut):
            return f"{self._ast_to_str(node.obyekt)}.{node.atribut}"
        return str(node)
