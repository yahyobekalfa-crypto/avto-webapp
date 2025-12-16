"""
AL Mobil Ilova
O'zbekcha mobil ilova yaratish (Kivy asosida)

ESLATMA: Bu modul ishlashi uchun Kivy o'rnatish kerak:
pip install kivy
"""


class MobilIlova:
    """Mobil ilova asosiy sinfi"""
    
    def __init__(self, nom: str = "AL Ilova"):
        self.nom = nom
        self.sahifalar = {}
        self.joriy_sahifa = None
        self._kivy_mavjud = self._kivy_tekshirish()
    
    def _kivy_tekshirish(self) -> bool:
        try:
            import kivy
            return True
        except ImportError:
            return False
    
    def sahifa(self, nom: str):
        """Sahifa dekoratori"""
        def dekorator(sinf):
            self.sahifalar[nom] = sinf
            return sinf
        return dekorator
    
    def ishga_tushirish(self):
        """Ilovani ishga tushirish"""
        if not self._kivy_mavjud:
            print("⚠️ Kivy o'rnatilmagan. O'rnatish uchun: pip install kivy")
            print("Konsol rejimida ishlayapti...")
            self._konsol_rejimi()
            return
        
        self._kivy_ishga_tushirish()
    
    def _konsol_rejimi(self):
        """Kivy yo'q bo'lganda konsol rejimi"""
        print(f"\n📱 {self.nom}")
        print("=" * 40)
        print("Mavjud sahifalar:")
        for nom in self.sahifalar:
            print(f"  - {nom}")
        print("=" * 40)
    
    def _kivy_ishga_tushirish(self):
        """Kivy bilan ishga tushirish"""
        from kivy.app import App
        from kivy.uix.label import Label
        
        ilova = self
        
        class ALApp(App):
            def build(self):
                return Label(text=ilova.nom)
        
        ALApp().run()


class Tugma:
    """Tugma komponenti"""
    def __init__(self, matn: str, bosilganda=None):
        self.matn = matn
        self.bosilganda = bosilganda


class Matn:
    """Matn komponenti"""
    def __init__(self, matn: str, hajm: int = 16):
        self.matn = matn
        self.hajm = hajm


class KiritishMaydoni:
    """Kiritish maydoni"""
    def __init__(self, ishora: str = "", maxfiy: bool = False):
        self.ishora = ishora
        self.maxfiy = maxfiy
        self.qiymat = ""


class Rasm:
    """Rasm komponenti"""
    def __init__(self, yol: str):
        self.yol = yol


class Ustun:
    """Vertikal joylashtirish"""
    def __init__(self, *bolalar):
        self.bolalar = bolalar


class Qator:
    """Gorizontal joylashtirish"""
    def __init__(self, *bolalar):
        self.bolalar = bolalar


__all__ = ['MobilIlova', 'Tugma', 'Matn', 'KiritishMaydoni', 'Rasm', 'Ustun', 'Qator']
