# AL (Algoritm Tili) 🇺🇿

**O'zbekcha Dasturlash Tili** - Python asosida to'liq o'zbekcha sintaksisga ega dasturlash tili.

## 🚀 Tez Boshlash

```bash
# REPL ni ishga tushirish
python cli.py

# Fayl ishga tushirish
python cli.py misollar/salom_dunyo.al

# Python kodini ko'rish
python cli.py -p misollar/salom_dunyo.al
```

## 📝 Sintaksis Misollar

### Salom Dunyo
```
chop("Salom Dunyo!")
```

### O'zgaruvchilar
```
ism = "Ali"
yosh = 25
narx = 99.99
faol = togri
```

### Shartlar
```
agar yosh >= 18:
    chop("Kattasiz")
aks_holda yosh >= 13:
    chop("O'smirsiz")
boshqa:
    chop("Bolasiz")
```

### Sikllar
```
# For sikli
uchun i oraliq(10) ichida:
    chop(i)

# While sikli
x = 0
toki x < 5:
    chop(x)
    x = x + 1
```

### Funksiyalar
```
funksiya fibonacci(n):
    agar n <= 1:
        qaytarish n
    qaytarish fibonacci(n-1) + fibonacci(n-2)

natija = fibonacci(10)
chop(natija)
```

### Sinflar
```
sinf Avtomobil:
    funksiya __init__(ozini, nomi, rangi):
        ozini.nomi = nomi
        ozini.rangi = rangi
    
    funksiya malumot(ozini):
        qaytarish f"{ozini.nomi} - {ozini.rangi}"

mashina = Avtomobil("Malibu", "oq")
chop(mashina.malumot())
```

## 📚 Kalit So'zlar

| O'zbekcha | Python | Tavsif |
|-----------|--------|--------|
| `agar` | if | Shart |
| `aks_holda` | elif | Boshqa shart |
| `boshqa` | else | Aks holda |
| `uchun` | for | Sikl |
| `toki` | while | While sikl |
| `funksiya` | def | Funksiya |
| `sinf` | class | Sinf |
| `qaytarish` | return | Qaytarish |
| `togri` | True | True |
| `notogri` | False | False |
| `hech` | None | None |
| `va` | and | Va |
| `yoki` | or | Yoki |
| `emas` | not | Emas |

## 📦 Modullar

### 🌐 Web Dasturlash
```python
from modullar.web import WebServer

server = WebServer(port=8080)

@server.get("/")
def bosh_sahifa():
    return "<h1>Salom!</h1>"

server.ishga_tushirish()
```

### ⛓️ Blockchain
```python
from modullar.blokcheyn import BlokZanjir, Hamyon

zanjir = BlokZanjir()
hamyon = Hamyon("Ali")

zanjir.tranzaksiya_qoshish(hamyon.manzil, "0x...", 100)
zanjir.blok_qazish(hamyon.manzil)
```

### 🤖 Sun'iy Intellekt
```python
from modullar.aql import NeyronTarmog

tarmoq = NeyronTarmog([2, 4, 1])
tarmoq.orgatish(kirishlar, maqsadlar)
natija = tarmoq.bashorat([0, 1])
```

### 📱 Mobil
```python
from modullar.mobil import MobilIlova

ilova = MobilIlova("Mening Ilovam")
ilova.ishga_tushirish()
```

## 🛠️ Kutubxonalar

| Kutubxona | Tavsif |
|-----------|--------|
| `kutubxona.asosiy` | chop, kiritish, uzunlik, turi |
| `kutubxona.matematika` | sin, cos, ildiz, daraja |
| `kutubxona.matn` | katta_harf, ajratish, almashtirish |
| `kutubxona.fayl` | fayl_okish, fayl_yozish, json_okish |
| `kutubxona.vaqt` | hozir, bugun, uxlash |

## 📂 Loyiha Tuzilmasi

```
al/                 # Asosiy til
kutubxona/          # Standart kutubxona
modullar/
  web/              # Web dasturlash
  blokcheyn/        # Blockchain
  aql/              # Sun'iy intellekt
  mobil/            # Mobil ilovalar
misollar/           # Misol dasturlar
cli.py              # Buyruq qatori
```

## 🔧 CLI Buyruqlar

```bash
python cli.py                    # REPL
python cli.py fayl.al            # Fayl bajarish
python cli.py -p fayl.al         # Python ga transpile
python cli.py -c "chop('Salom')" # Inline kod
python cli.py -v                 # Versiya
```

## 📜 Litsenziya

MIT License

---

**AL** - O'zbekiston uchun, O'zbek tilda! 🇺🇿
