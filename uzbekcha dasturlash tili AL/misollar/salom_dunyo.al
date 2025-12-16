# Salom Dunyo - AL tilida

chop("Salom Dunyo!")
chop("AL - O'zbekcha dasturlash tiliga xush kelibsiz!")

# O'zgaruvchilar
ism = "Ali"
yosh = 25
chop(f"Mening ismim {ism}, yoshim {yosh}")

# Matematik amallar
x = 10
y = 3
chop(f"{x} + {y} = {x + y}")
chop(f"{x} - {y} = {x - y}")
chop(f"{x} * {y} = {x * y}")
chop(f"{x} / {y} = {x / y}")

# Shartlar
agar yosh >= 18:
    chop("Siz kattasiz")
boshqa:
    chop("Siz yoshsiz")

# Sikl
chop("\n1 dan 5 gacha sanash:")
uchun i oraliq(1, 6) ichida:
    chop(i)

# Ro'yxat
mevalar = ["olma", "banan", "uzum"]
chop("\nMevalar:")
uchun meva mevalar ichida:
    chop(f"  - {meva}")

# Funksiya
funksiya salomlash(ism):
    qaytarish f"Salom, {ism}!"

natija = salomlash("Vali")
chop(natija)

chop("\n✅ Dastur muvaffaqiyatli bajarildi!")
