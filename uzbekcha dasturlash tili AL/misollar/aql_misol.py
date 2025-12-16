# Sun'iy Intellekt Misoli - AL tilida

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modullar.aql import NeyronTarmog, Perseptron
from modullar.aql.malumot import ortacha, standart_chetlanish

print("🤖 AL Sun'iy Intellekt Misoli")
print("=" * 50)

# XOR masalasi
print("\n📊 XOR masalasini yechish:")
print("   Kirish: (0,0), (0,1), (1,0), (1,1)")
print("   Chiqish: 0, 1, 1, 0")

# Ma'lumotlar
kirishlar = [[0, 0], [0, 1], [1, 0], [1, 1]]
maqsadlar = [[0], [1], [1], [0]]

# Neyron tarmoq yaratish (2 kirish, 4 yashirin, 1 chiqish)
tarmoq = NeyronTarmog([2, 4, 1])

print("\n⏳ Tarmoq o'rgatilmoqda...")
tarmoq.orgatish(kirishlar, maqsadlar, epochlar=1000, tezlik=0.5)

print("\n🎯 Natijalar:")
for kirish, maqsad in zip(kirishlar, maqsadlar):
    bashorat = tarmoq.bashorat(kirish)
    yaxlitlangan = round(bashorat[0])
    print(f"   {kirish} -> {bashorat[0]:.4f} (yaxlit: {yaxlitlangan}, kutilgan: {maqsad[0]})")

# Perseptron misoli
print("\n" + "=" * 50)
print("📏 AND operatori uchun Perseptron:")

and_kirishlar = [[0, 0], [0, 1], [1, 0], [1, 1]]
and_maqsadlar = [0, 0, 0, 1]

perseptron = Perseptron(2)
perseptron.orgatish(and_kirishlar, and_maqsadlar, epochlar=100)

print("   Natijalar:")
for kirish, maqsad in zip(and_kirishlar, and_maqsadlar):
    bashorat = perseptron.bashorat(kirish)
    print(f"   {kirish} -> {bashorat} (kutilgan: {maqsad})")

# Statistika
print("\n" + "=" * 50)
print("📈 Statistika funksiyalari:")

sonlar = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(f"   Sonlar: {sonlar}")
print(f"   O'rtacha: {ortacha(sonlar)}")
print(f"   Standart chetlanish: {standart_chetlanish(sonlar):.4f}")

print("\n✅ Sun'iy intellekt misoli muvaffaqiyatli bajarildi!")
