"""
AL Interpreter (Tarjimon)
Python kodni bajarish
"""

import sys
from typing import Any, Dict
from .lexer import Lexer
from .parser import Parser
from .transpiler import Transpiler
from .errors import ALXato, python_xatosini_tarjima


class Interpreter:
    """AL kodini bajarish"""
    
    def __init__(self):
        self.global_env: Dict[str, Any] = {}
        self.local_env: Dict[str, Any] = {}
        self._init_builtins()
    
    def _init_builtins(self):
        """O'rnatilgan funksiyalarni yuklash"""
        self.global_env.update({
            'print': print, 'input': input, 'len': len, 'type': type,
            'range': range, 'list': list, 'dict': dict, 'set': set,
            'str': str, 'int': int, 'float': float, 'bool': bool,
            'abs': abs, 'round': round, 'min': min, 'max': max,
            'sum': sum, 'sorted': sorted, 'enumerate': enumerate,
            'filter': filter, 'map': map, 'all': all, 'any': any,
            'zip': zip, 'open': open, 'True': True, 'False': False, 'None': None,
            # O'zbekcha
            'chop': print, 'kiritish': input, 'uzunlik': len, 'turi': type,
            'oraliq': range, 'royxat': list, 'lugat': dict, 'toplam': set,
            'satr': str, 'butun': int, 'haqiqiy': float, 'mantiqiy': bool,
            'yaxlitlash': round, 'yigindi': sum, 'saralash': sorted,
            'togri': True, 'notogri': False, 'hech': None,
        })
    
    def bajarish(self, kod: str, fayl_nomi: str = "<stdin>") -> Any:
        """AL kodini bajarish"""
        try:
            lexer = Lexer(kod, fayl_nomi)
            tokenlar = lexer.tokenizatsiya()
            parser = Parser(tokenlar)
            ast = parser.parse()
            transpiler = Transpiler()
            python_kod = transpiler.transpile(ast)
            return self._python_bajarish(python_kod)
        except ALXato as e:
            raise e
        except Exception as e:
            raise python_xatosini_tarjima(e)
    
    def _python_bajarish(self, kod: str) -> Any:
        """Python kodni bajarish"""
        import os
        kutubxona_yoli = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if kutubxona_yoli not in sys.path:
            sys.path.insert(0, kutubxona_yoli)
        env = {**self.global_env, **self.local_env}
        exec(kod, env)
        for key, value in env.items():
            if key not in self.global_env and not key.startswith('_'):
                self.local_env[key] = value
        return None
    
    def ifoda_bajarish(self, kod: str) -> Any:
        """Bitta ifodani bajarish"""
        try:
            lexer = Lexer(kod, "<expr>")
            tokenlar = lexer.tokenizatsiya()
            parser = Parser(tokenlar)
            ast = parser.parse()
            transpiler = Transpiler()
            python_kod = transpiler.transpile(ast)
            
            qatorlar = [q for q in python_kod.split('\n') 
                       if not q.startswith('#') and not q.startswith('import') 
                       and not q.startswith('from') and not q.startswith('sys.')]
            sof_kod = '\n'.join(qatorlar).strip()
            if not sof_kod:
                return None
            
            env = {**self.global_env, **self.local_env}
            try:
                return eval(sof_kod, env)
            except SyntaxError:
                exec(sof_kod, env)
                for key, value in env.items():
                    if key not in self.global_env and not key.startswith('_'):
                        self.local_env[key] = value
                return None
        except ALXato as e:
            raise e
        except Exception as e:
            raise python_xatosini_tarjima(e)
    
    def fayl_bajarish(self, fayl_yoli: str) -> Any:
        """AL faylini bajarish"""
        with open(fayl_yoli, 'r', encoding='utf-8') as f:
            kod = f.read()
        return self.bajarish(kod, fayl_yoli)
    
    def python_kodini_olish(self, kod: str) -> str:
        """AL kodini Python ga transpile qilish"""
        lexer = Lexer(kod, "<stdin>")
        tokenlar = lexer.tokenizatsiya()
        parser = Parser(tokenlar)
        ast = parser.parse()
        transpiler = Transpiler()
        return transpiler.transpile(ast)
    
    def reset(self):
        """Interpreterni qayta boshlash"""
        self.local_env.clear()
        self._init_builtins()
