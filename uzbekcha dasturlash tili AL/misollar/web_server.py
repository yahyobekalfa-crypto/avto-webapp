# Web Server Misoli - AL tilida
# Bu faylni ishga tushirish: python cli.py misollar/web_server.al

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modullar.web import WebServer, sahifa

# Server yaratish
server = WebServer(port=8080)

# Bosh sahifa
@server.get("/")
def bosh_sahifa():
    return sahifa.sahifa(
        "AL Web Server",
        sahifa.sarlavha1("🌐 AL Web Serverga Xush Kelibsiz!"),
        sahifa.paragraf("Bu veb-sahifa AL dasturlash tilida yaratilgan."),
        sahifa.royxat("Web dasturlash", "Blockchain", "Sun'iy intellekt", "Mobil ilovalar"),
        sahifa.havola("API ga o'tish", "/api"),
        til="uz"
    )

# API endpoint
@server.get("/api")
def api():
    return {
        "xabar": "Salom, bu AL API!",
        "versiya": "1.0.0",
        "mualliflar": ["AL Team"]
    }

# Salomlashish
@server.get("/salom")
def salom():
    return "<h1>Salom Dunyo!</h1><p>AL tilidan salom!</p>"

print("🚀 Web server ishga tushmoqda...")
print("📍 http://localhost:8080")
print("⛔ To'xtatish uchun Ctrl+C bosing")

server.ishga_tushirish()
