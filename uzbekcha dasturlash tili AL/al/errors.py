"""
AL Xatolar
O'zbekcha xato xabarlari
"""


class ALXato(Exception):
    """Asosiy AL xatosi"""
    
    def __init__(self, xabar: str, qator: int = None, ustun: int = None, fayl: str = None):
        self.xabar = xabar
        self.qator = qator
        self.ustun = ustun
        self.fayl = fayl
        super().__init__(self._formatlash())
    
    def _formatlash(self) -> str:
        joylashuv = ""
        if self.fayl:
            joylashuv += f"Fayl: {self.fayl}, "
        if self.qator is not None:
            joylashuv += f"Qator {self.qator}"
            if self.ustun is not None:
                joylashuv += f", Ustun {self.ustun}"
            joylashuv += ": "
        return f"{self.__class__.__name__}: {joylashuv}{self.xabar}"


class SintaksisXatosi(ALXato):
    """Sintaksis xatosi"""
    pass


class LeksikXato(ALXato):
    """Leksik tahlil xatosi"""
    pass


class TurXatosi(ALXato):
    """Tur xatosi"""
    pass


class NomXatosi(ALXato):
    """Nom topilmadi xatosi"""
    pass


class QiymatXatosi(ALXato):
    """Qiymat xatosi"""
    pass


class IndeksXatosi(ALXato):
    """Indeks xatosi"""
    pass


class KalitXatosi(ALXato):
    """Kalit topilmadi xatosi"""
    pass


class BolishXatosi(ALXato):
    """Nolga bo'lish xatosi"""
    pass


class ImportXatosi(ALXato):
    """Import xatosi"""
    pass


class FaylXatosi(ALXato):
    """Fayl xatosi"""
    pass


class XotiraXatosi(ALXato):
    """Xotira xatosi"""
    pass


class VaqtXatosi(ALXato):
    """Vaqt tugashi xatosi"""
    pass


# Xato xabarlarini tarjima qilish
XATO_TARJIMALARI = {
    'SyntaxError': 'SintaksisXatosi',
    'TypeError': 'TurXatosi',
    'NameError': 'NomXatosi',
    'ValueError': 'QiymatXatosi',
    'IndexError': 'IndeksXatosi',
    'KeyError': 'KalitXatosi',
    'ZeroDivisionError': 'BolishXatosi',
    'ImportError': 'ImportXatosi',
    'FileNotFoundError': 'FaylXatosi',
    'MemoryError': 'XotiraXatosi',
    'TimeoutError': 'VaqtXatosi',
}


def python_xatosini_tarjima(xato: Exception) -> ALXato:
    """Python xatosini AL xatosiga o'girish"""
    xato_nomi = type(xato).__name__
    xabar = str(xato)
    
    if xato_nomi == 'SyntaxError':
        return SintaksisXatosi(xabar)
    elif xato_nomi == 'TypeError':
        return TurXatosi(xabar)
    elif xato_nomi == 'NameError':
        return NomXatosi(xabar)
    elif xato_nomi == 'ValueError':
        return QiymatXatosi(xabar)
    elif xato_nomi == 'IndexError':
        return IndeksXatosi(xabar)
    elif xato_nomi == 'KeyError':
        return KalitXatosi(xabar)
    elif xato_nomi == 'ZeroDivisionError':
        return BolishXatosi("Nolga bo'lish mumkin emas")
    elif xato_nomi == 'ImportError':
        return ImportXatosi(xabar)
    elif xato_nomi == 'FileNotFoundError':
        return FaylXatosi(xabar)
    else:
        return ALXato(xabar)
