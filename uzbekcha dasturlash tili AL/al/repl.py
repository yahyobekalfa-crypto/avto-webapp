"""
AL REPL (Read-Eval-Print Loop)
Interaktiv muhit
"""

import sys
from .interpreter import Interpreter
from .errors import ALXato


class REPL:
    """AL interaktiv muhit"""
    
    BANNER = """
╔═══════════════════════════════════════════════════════════════╗
║     _    _        _____ _ _ _                                 ║
║    / \  | |      |_   _(_) (_)                                ║
║   / _ \ | |        | |  _| |_                                 ║
║  / ___ \| |___     | | | | | |                                ║
║ /_/   \_\_____|    |_| |_|_|_|                                ║
║                                                               ║
║  AL (Algoritm Tili) - O'zbekcha Dasturlash Tili v1.0.0        ║
║  Yordam: yordam() | Chiqish: chiqish() yoki Ctrl+C            ║
╚═══════════════════════════════════════════════════════════════╝
    """
    
    def __init__(self):
        self.interpreter = Interpreter()
        self.tarix = []
    
    def ishga_tushirish(self):
        """REPL ni ishga tushirish"""
        print(self.BANNER)
        
        while True:
            try:
                kod = self._kiritish_olish()
                if kod is None:
                    continue
                
                # Maxsus buyruqlar
                if kod.strip() == 'chiqish()':
                    print("\nXayr! AL dan foydalanganingiz uchun rahmat. 👋")
                    break
                
                if kod.strip() == 'yordam()':
                    self._yordam_korsatish()
                    continue
                
                if kod.strip() == 'tozalash()':
                    self._tozalash()
                    continue
                
                if kod.strip() == 'tarix()':
                    self._tarix_korsatish()
                    continue
                
                if kod.strip().startswith('python('):
                    self._python_korsatish(kod.strip())
                    continue
                
                # Kodni bajarish
                self.tarix.append(kod)
                natija = self.interpreter.ifoda_bajarish(kod)
                
                if natija is not None:
                    print(f"=> {natija}")
                    
            except ALXato as e:
                print(f"\033[91m{e}\033[0m")
            except KeyboardInterrupt:
                print("\n\nXayr! 👋")
                break
            except EOFError:
                print("\nXayr! 👋")
                break
            except Exception as e:
                print(f"\033[91mXato: {e}\033[0m")
    
    def _kiritish_olish(self) -> str:
        """Ko'p qatorli kiritishni olish"""
        try:
            qator = input("\033[92mAL >>> \033[0m")
        except EOFError:
            return None
        
        # Ko'p qatorli kod
        if qator.rstrip().endswith(':'):
            qatorlar = [qator]
            while True:
                try:
                    davom = input("\033[93m... \033[0m")
                    if davom == '':
                        break
                    qatorlar.append(davom)
                except EOFError:
                    break
            return '\n'.join(qatorlar)
        
        return qator
    
    def _yordam_korsatish(self):
        """Yordam ma'lumotini ko'rsatish"""
        print("""
╔════════════════════════════════════════════════════════════════╗
║                        AL YORDAM                               ║
╠════════════════════════════════════════════════════════════════╣
║ Asosiy buyruqlar:                                              ║
║   chiqish()   - REPL dan chiqish                               ║
║   yordam()    - Bu yordam sahifasi                             ║
║   tozalash()  - O'zgaruvchilarni tozalash                      ║
║   tarix()     - Buyruqlar tarixini ko'rish                     ║
║   python(kod) - AL kodini Python ga o'girish                   ║
╠════════════════════════════════════════════════════════════════╣
║ Misollar:                                                      ║
║   chop("Salom!")           - Ekranga chiqarish                 ║
║   x = 10                   - O'zgaruvchi yaratish              ║
║   uchun i oraliq(5) ichida: - For sikl                         ║
║   agar x > 5:              - If shart                          ║
║   funksiya salom():        - Funksiya yaratish                 ║
╚════════════════════════════════════════════════════════════════╝
        """)
    
    def _tozalash(self):
        """Interpreterni tozalash"""
        self.interpreter.reset()
        print("✓ O'zgaruvchilar tozalandi")
    
    def _tarix_korsatish(self):
        """Buyruqlar tarixini ko'rsatish"""
        if not self.tarix:
            print("Tarix bo'sh")
            return
        
        print("\n--- Buyruqlar Tarixi ---")
        for i, buyruq in enumerate(self.tarix[-20:], 1):
            print(f"{i}. {buyruq}")
        print("------------------------\n")
    
    def _python_korsatish(self, kod: str):
        """AL kodini Python ga o'girib ko'rsatish"""
        # python(kod) dan kod qismini olish
        ichki = kod[7:-1]  # python( va ) ni olib tashlash
        if ichki.startswith('"') or ichki.startswith("'"):
            ichki = ichki[1:-1]
        
        try:
            python_kod = self.interpreter.python_kodini_olish(ichki)
            print("\n--- Python Kod ---")
            print(python_kod)
            print("------------------\n")
        except Exception as e:
            print(f"Xato: {e}")


def main():
    """REPL ni ishga tushirish"""
    repl = REPL()
    repl.ishga_tushirish()


if __name__ == '__main__':
    main()
