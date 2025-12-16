"""
AL Lexer (Lekser)
Matnni tokenlarga ajratish
"""

import re
from typing import List, Generator
from .tokens import Token, TokenTuri, KALIT_SOZLAR, OPERATORLAR, QAVSLAR, BELGILAR
from .errors import LeksikXato


class Lexer:
    """AL dasturlash tili uchun lekser"""
    
    def __init__(self, manba: str, fayl_nomi: str = "<stdin>"):
        self.manba = manba
        self.fayl_nomi = fayl_nomi
        self.pozitsiya = 0
        self.qator = 1
        self.ustun = 1
        self.joriy_belgi = self.manba[0] if manba else None
        self.tokenlar: List[Token] = []
        self.indent_stack = [0]  # Indent darajalarini kuzatish
    
    def _keyingi(self):
        """Keyingi belgiga o'tish"""
        self.pozitsiya += 1
        self.ustun += 1
        
        if self.pozitsiya < len(self.manba):
            self.joriy_belgi = self.manba[self.pozitsiya]
        else:
            self.joriy_belgi = None
    
    def _oldinga_qara(self, qadamlar: int = 1) -> str:
        """Oldinga qarash"""
        pozitsiya = self.pozitsiya + qadamlar
        if pozitsiya < len(self.manba):
            return self.manba[pozitsiya]
        return None
    
    def _boshliq_otkazish(self):
        """Bo'shliq va tablarni o'tkazib yuborish (satr boshidagi emas)"""
        while self.joriy_belgi and self.joriy_belgi in ' \t' and self.ustun > 1:
            self._keyingi()
    
    def _indent_hisoblash(self) -> int:
        """Satr boshidagi bo'shliqlarni hisoblash"""
        boshliq = 0
        while self.joriy_belgi and self.joriy_belgi in ' \t':
            if self.joriy_belgi == ' ':
                boshliq += 1
            else:  # tab
                boshliq += 4
            self._keyingi()
        return boshliq
    
    def _raqam_olish(self) -> Token:
        """Raqam tokenini olish"""
        natija = ""
        nuqta_bor = False
        
        while self.joriy_belgi and (self.joriy_belgi.isdigit() or self.joriy_belgi == '.'):
            if self.joriy_belgi == '.':
                if nuqta_bor:
                    break
                if self._oldinga_qara() and not self._oldinga_qara().isdigit():
                    break
                nuqta_bor = True
            natija += self.joriy_belgi
            self._keyingi()
        
        return Token(TokenTuri.RAQAM, natija, self.qator, self.ustun)
    
    def _satr_olish(self) -> Token:
        """Satr tokenini olish"""
        qo_shtirnoq = self.joriy_belgi  # ' yoki "
        self._keyingi()
        natija = ""
        
        while self.joriy_belgi and self.joriy_belgi != qo_shtirnoq:
            if self.joriy_belgi == '\\' and self._oldinga_qara() in [qo_shtirnoq, '\\', 'n', 't', 'r']:
                self._keyingi()
                if self.joriy_belgi == 'n':
                    natija += '\n'
                elif self.joriy_belgi == 't':
                    natija += '\t'
                elif self.joriy_belgi == 'r':
                    natija += '\r'
                else:
                    natija += self.joriy_belgi
            else:
                if self.joriy_belgi == '\n':
                    raise LeksikXato("Satr yopilmagan", self.qator, self.ustun, self.fayl_nomi)
                natija += self.joriy_belgi
            self._keyingi()
        
        if self.joriy_belgi is None:
            raise LeksikXato("Satr yopilmagan", self.qator, self.ustun, self.fayl_nomi)
        
        self._keyingi()  # Yopuvchi qo'shtirnoqni o'tkazish
        return Token(TokenTuri.SATR, natija, self.qator, self.ustun)
    
    def _identifikator_olish(self) -> Token:
        """Identifikator yoki kalit so'z tokenini olish"""
        natija = ""
        
        while self.joriy_belgi and (self.joriy_belgi.isalnum() or self.joriy_belgi == '_'):
            natija += self.joriy_belgi
            self._keyingi()
        
        # Kalit so'z tekshirish
        if natija in KALIT_SOZLAR:
            # Mantiqiy qiymatlar
            if natija == 'togri':
                return Token(TokenTuri.MANTIQIY, 'True', self.qator, self.ustun)
            elif natija == 'notogri':
                return Token(TokenTuri.MANTIQIY, 'False', self.qator, self.ustun)
            elif natija == 'hech':
                return Token(TokenTuri.HECH, 'None', self.qator, self.ustun)
            return Token(TokenTuri.KALIT_SOZ, natija, self.qator, self.ustun)
        
        return Token(TokenTuri.IDENTIFIKATOR, natija, self.qator, self.ustun)
    
    def _izoh_otkazish(self):
        """Izohni o'tkazib yuborish"""
        while self.joriy_belgi and self.joriy_belgi != '\n':
            self._keyingi()
    
    def _operator_olish(self) -> Token:
        """Operator tokenini olish"""
        # Ikki belgili operatorlarni tekshirish
        ikki_belgili = self.joriy_belgi + (self._oldinga_qara() or '')
        
        if ikki_belgili in OPERATORLAR:
            self._keyingi()
            self._keyingi()
            return Token(OPERATORLAR[ikki_belgili], ikki_belgili, self.qator, self.ustun)
        
        if ikki_belgili in BELGILAR:
            self._keyingi()
            self._keyingi()
            return Token(BELGILAR[ikki_belgili], ikki_belgili, self.qator, self.ustun)
        
        # Bir belgili operatorlar
        belgi = self.joriy_belgi
        
        if belgi in OPERATORLAR:
            self._keyingi()
            return Token(OPERATORLAR[belgi], belgi, self.qator, self.ustun)
        
        if belgi in QAVSLAR:
            self._keyingi()
            return Token(QAVSLAR[belgi], belgi, self.qator, self.ustun)
        
        if belgi in BELGILAR:
            self._keyingi()
            return Token(BELGILAR[belgi], belgi, self.qator, self.ustun)
        
        raise LeksikXato(f"Noto'g'ri belgi: '{belgi}'", self.qator, self.ustun, self.fayl_nomi)
    
    def tokenizatsiya(self) -> List[Token]:
        """Manbani tokenlarga ajratish"""
        self.tokenlar = []
        yangi_qator_boshi = True
        
        while self.joriy_belgi is not None:
            # Yangi qator boshida indentni tekshirish
            if yangi_qator_boshi and self.joriy_belgi not in '\n\r':
                indent = self._indent_hisoblash()
                joriy_indent = self.indent_stack[-1]
                
                if indent > joriy_indent:
                    self.indent_stack.append(indent)
                    self.tokenlar.append(Token(TokenTuri.INDENT, str(indent), self.qator, 1))
                elif indent < joriy_indent:
                    while self.indent_stack and self.indent_stack[-1] > indent:
                        self.indent_stack.pop()
                        self.tokenlar.append(Token(TokenTuri.DEDENT, "", self.qator, 1))
                
                yangi_qator_boshi = False
                continue
            
            # Bo'shliq
            if self.joriy_belgi in ' \t':
                self._keyingi()
                continue
            
            # Yangi qator
            if self.joriy_belgi in '\n\r':
                if self.joriy_belgi == '\r' and self._oldinga_qara() == '\n':
                    self._keyingi()
                self.tokenlar.append(Token(TokenTuri.YANGI_QATOR, "\\n", self.qator, self.ustun))
                self._keyingi()
                self.qator += 1
                self.ustun = 1
                yangi_qator_boshi = True
                continue
            
            # Izoh
            if self.joriy_belgi == '#':
                self._izoh_otkazish()
                continue
            
            # Raqam
            if self.joriy_belgi.isdigit():
                self.tokenlar.append(self._raqam_olish())
                continue
            
            # Satr
            if self.joriy_belgi in '"\'':
                self.tokenlar.append(self._satr_olish())
                continue
            
            # Identifikator yoki kalit so'z
            if self.joriy_belgi.isalpha() or self.joriy_belgi == '_':
                self.tokenlar.append(self._identifikator_olish())
                continue
            
            # F-string tekshirish
            if self.joriy_belgi == 'f' and self._oldinga_qara() in '"\'':
                self._keyingi()
                satr_token = self._satr_olish()
                satr_token.qiymat = 'f"' + satr_token.qiymat + '"'
                self.tokenlar.append(satr_token)
                continue
            
            # Operator va belgilar
            self.tokenlar.append(self._operator_olish())
        
        # Qolgan DEDENTlarni qo'shish
        while len(self.indent_stack) > 1:
            self.indent_stack.pop()
            self.tokenlar.append(Token(TokenTuri.DEDENT, "", self.qator, 1))
        
        # EOF
        self.tokenlar.append(Token(TokenTuri.FAYL_OXIRI, "", self.qator, self.ustun))
        
        return self.tokenlar
    
    def __iter__(self) -> Generator[Token, None, None]:
        """Iterator sifatida ishlatish"""
        if not self.tokenlar:
            self.tokenizatsiya()
        yield from self.tokenlar
