"""
AL Web Server
O'zbekcha web server
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
import threading


class WebServer:
    """O'zbekcha web server"""
    
    def __init__(self, port=8000, host="localhost"):
        self.port = port
        self.host = host
        self.yollar = {}  # URL -> handler mapping
        self.server = None
        self._ishlamoqda = False
    
    def yol(self, url, metodlar=None):
        """URL yo'lini ro'yxatdan o'tkazish (dekorator)"""
        if metodlar is None:
            metodlar = ["GET"]
        
        def dekorator(funksiya):
            self.yollar[url] = {
                'handler': funksiya,
                'metodlar': metodlar
            }
            return funksiya
        return dekorator
    
    def get(self, url):
        """GET so'rov uchun dekorator"""
        return self.yol(url, ["GET"])
    
    def post(self, url):
        """POST so'rov uchun dekorator"""
        return self.yol(url, ["POST"])
    
    def ishga_tushirish(self, fon=False):
        """Serverni ishga tushirish"""
        server_instance = self
        
        class Handler(BaseHTTPRequestHandler):
            def _javob_yuborish(self, status, mazmun, content_type="text/html"):
                self.send_response(status)
                self.send_header("Content-type", f"{content_type}; charset=utf-8")
                self.end_headers()
                if isinstance(mazmun, str):
                    self.wfile.write(mazmun.encode('utf-8'))
                else:
                    self.wfile.write(mazmun)
            
            def do_GET(self):
                parsed = urlparse(self.path)
                yol = parsed.path
                params = parse_qs(parsed.query)
                
                if yol in server_instance.yollar:
                    yol_info = server_instance.yollar[yol]
                    if "GET" in yol_info['metodlar']:
                        try:
                            natija = yol_info['handler']()
                            if isinstance(natija, dict):
                                self._javob_yuborish(200, json.dumps(natija, ensure_ascii=False), "application/json")
                            else:
                                self._javob_yuborish(200, str(natija))
                        except Exception as e:
                            self._javob_yuborish(500, f"Xato: {e}")
                    else:
                        self._javob_yuborish(405, "Metod ruxsat etilmagan")
                else:
                    self._javob_yuborish(404, "Sahifa topilmadi")
            
            def do_POST(self):
                parsed = urlparse(self.path)
                yol = parsed.path
                
                content_length = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(content_length).decode('utf-8')
                
                if yol in server_instance.yollar:
                    yol_info = server_instance.yollar[yol]
                    if "POST" in yol_info['metodlar']:
                        try:
                            natija = yol_info['handler'](body)
                            if isinstance(natija, dict):
                                self._javob_yuborish(200, json.dumps(natija, ensure_ascii=False), "application/json")
                            else:
                                self._javob_yuborish(200, str(natija))
                        except Exception as e:
                            self._javob_yuborish(500, f"Xato: {e}")
                    else:
                        self._javob_yuborish(405, "Metod ruxsat etilmagan")
                else:
                    self._javob_yuborish(404, "Sahifa topilmadi")
            
            def log_message(self, format, *args):
                print(f"[{self.log_date_time_string()}] {args[0]}")
        
        self.server = HTTPServer((self.host, self.port), Handler)
        self._ishlamoqda = True
        
        print(f"🌐 Server ishga tushdi: http://{self.host}:{self.port}")
        
        if fon:
            thread = threading.Thread(target=self.server.serve_forever)
            thread.daemon = True
            thread.start()
        else:
            try:
                self.server.serve_forever()
            except KeyboardInterrupt:
                print("\n⛔ Server to'xtatildi")
                self.toxtatish()
    
    def toxtatish(self):
        """Serverni to'xtatish"""
        if self.server:
            self.server.shutdown()
            self._ishlamoqda = False
            print("Server to'xtatildi")


def sorov_yuborish(url, metod="GET", malumot=None, headers=None):
    """HTTP so'rov yuborish"""
    import urllib.request
    import urllib.error
    
    if headers is None:
        headers = {}
    
    if malumot and isinstance(malumot, dict):
        malumot = json.dumps(malumot).encode('utf-8')
        headers['Content-Type'] = 'application/json'
    elif malumot and isinstance(malumot, str):
        malumot = malumot.encode('utf-8')
    
    req = urllib.request.Request(url, data=malumot, headers=headers, method=metod)
    
    try:
        with urllib.request.urlopen(req) as javob:
            return {
                'status': javob.status,
                'body': javob.read().decode('utf-8'),
                'headers': dict(javob.headers)
            }
    except urllib.error.HTTPError as e:
        return {
            'status': e.code,
            'body': e.read().decode('utf-8'),
            'xato': str(e)
        }
    except urllib.error.URLError as e:
        return {
            'status': 0,
            'xato': str(e)
        }


__all__ = ['WebServer', 'sorov_yuborish']
