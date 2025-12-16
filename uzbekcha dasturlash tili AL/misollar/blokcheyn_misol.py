# Blockchain Misoli - AL tilida

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modullar.blokcheyn import BlokZanjir, Hamyon

print("⛓️ AL Blockchain Misoli")
print("=" * 50)

# Hamyonlar yaratish
ali_hamyon = Hamyon("Ali")
vali_hamyon = Hamyon("Vali")
qazuvchi_hamyon = Hamyon("Qazuvchi")

print(f"\n📱 Hamyonlar yaratildi:")
print(f"   Ali: {ali_hamyon.manzil}")
print(f"   Vali: {vali_hamyon.manzil}")
print(f"   Qazuvchi: {qazuvchi_hamyon.manzil}")

# Blockchain yaratish
zanjir = BlokZanjir(qiyinlik=3)
print(f"\n🔗 Blockchain yaratildi (qiyinlik: 3)")

# Tranzaksiyalar
print("\n💸 Tranzaksiyalar qo'shilmoqda...")
zanjir.tranzaksiya_qoshish(ali_hamyon.manzil, vali_hamyon.manzil, 50)
zanjir.tranzaksiya_qoshish(vali_hamyon.manzil, ali_hamyon.manzil, 20)

# Blok qazish
print("\n⛏️ Blok qazilmoqda...")
zanjir.blok_qazish(qazuvchi_hamyon.manzil)

# Yana tranzaksiyalar
zanjir.tranzaksiya_qoshish(ali_hamyon.manzil, vali_hamyon.manzil, 30)
zanjir.blok_qazish(qazuvchi_hamyon.manzil)

# Balanslar
print("\n💰 Balanslar:")
print(f"   Ali: {zanjir.balans(ali_hamyon.manzil)}")
print(f"   Vali: {zanjir.balans(vali_hamyon.manzil)}")
print(f"   Qazuvchi: {zanjir.balans(qazuvchi_hamyon.manzil)}")

# Zanjir ma'lumoti
print("\n📊 Zanjir ma'lumoti:")
malumot = zanjir.zanjir_malumoti()
for kalit, qiymat in malumot.items():
    print(f"   {kalit}: {qiymat}")

print("\n✅ Blockchain misoli muvaffaqiyatli bajarildi!")
