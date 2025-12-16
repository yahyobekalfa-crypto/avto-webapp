#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AL CLI (Buyruq Qatori Interfeysi)
AL dasturlarini ishga tushirish
"""

import sys
import os
import argparse

# Loyiha yo'lini qo'shish
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from al.interpreter import Interpreter
from al.repl import REPL
from al.errors import ALXato


def main():
    parser = argparse.ArgumentParser(
        prog='al',
        description='AL (Algoritm Tili) - O\'zbekcha Dasturlash Tili',
        epilog='Misol: al dastur.al'
    )
    
    parser.add_argument('fayl', nargs='?', help='Bajarish uchun .al fayl')
    parser.add_argument('-v', '--version', action='store_true', help='Versiyani ko\'rsatish')
    parser.add_argument('-p', '--python', action='store_true', help='Python kodini ko\'rsatish')
    parser.add_argument('-c', '--kod', type=str, help='Kodni to\'g\'ridan-to\'g\'ri bajarish')
    parser.add_argument('-i', '--interaktiv', action='store_true', help='Fayldan keyin REPL ochish')
    
    args = parser.parse_args()
    
    # Versiya
    if args.version:
        print("AL (Algoritm Tili) versiya 1.0.0")
        print("Python asosida o'zbekcha dasturlash tili")
        return
    
    interpreter = Interpreter()
    
    # Inline kod
    if args.kod:
        try:
            if args.python:
                python_kod = interpreter.python_kodini_olish(args.kod)
                print(python_kod)
            else:
                interpreter.bajarish(args.kod)
        except ALXato as e:
            print(f"Xato: {e}", file=sys.stderr)
            sys.exit(1)
        return
    
    # Fayl bajarish
    if args.fayl:
        if not os.path.exists(args.fayl):
            print(f"Xato: Fayl topilmadi: {args.fayl}", file=sys.stderr)
            sys.exit(1)
        
        try:
            if args.python:
                with open(args.fayl, 'r', encoding='utf-8') as f:
                    kod = f.read()
                python_kod = interpreter.python_kodini_olish(kod)
                print(python_kod)
            else:
                interpreter.fayl_bajarish(args.fayl)
        except ALXato as e:
            print(f"Xato: {e}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Xato: {e}", file=sys.stderr)
            sys.exit(1)
        
        if args.interaktiv:
            repl = REPL()
            repl.interpreter = interpreter
            repl.ishga_tushirish()
        return
    
    # REPL
    repl = REPL()
    repl.ishga_tushirish()


if __name__ == '__main__':
    main()
