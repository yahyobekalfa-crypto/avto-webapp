"""
AL HTML Sahifa Generator
O'zbekcha HTML yaratish
"""


class Element:
    """HTML elementi"""
    
    def __init__(self, teg, **atributlar):
        self.teg = teg
        self.atributlar = atributlar
        self.bolalar = []
        self.mazmun = ""
    
    def qoshish(self, *bolalar):
        """Bola elementlar qo'shish"""
        for bola in bolalar:
            if isinstance(bola, str):
                self.bolalar.append(bola)
            elif isinstance(bola, Element):
                self.bolalar.append(bola)
        return self
    
    def matn(self, mazmun):
        """Matn qo'shish"""
        self.mazmun = mazmun
        return self
    
    def __str__(self):
        attrs = ""
        for nom, qiymat in self.atributlar.items():
            if nom == 'sinf':
                nom = 'class'
            elif nom == 'uchun':
                nom = 'for'
            attrs += f' {nom}="{qiymat}"'
        
        if self.teg in ['img', 'br', 'hr', 'input', 'meta', 'link']:
            return f"<{self.teg}{attrs}/>"
        
        ichki = self.mazmun
        for bola in self.bolalar:
            ichki += str(bola)
        
        return f"<{self.teg}{attrs}>{ichki}</{self.teg}>"


# ============= ASOSIY ELEMENTLAR =============

def sahifa(sarlavha="", *bolalar, til="uz"):
    """HTML sahifa yaratish"""
    html = f"""<!DOCTYPE html>
<html lang="{til}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{sarlavha}</title>
</head>
<body>
"""
    for bola in bolalar:
        html += str(bola) + "\n"
    
    html += "</body>\n</html>"
    return html


def div(*bolalar, **atributlar):
    """div elementi"""
    return Element('div', **atributlar).qoshish(*bolalar)


def span(*bolalar, **atributlar):
    """span elementi"""
    return Element('span', **atributlar).qoshish(*bolalar)


# ============= SARLAVHALAR =============

def sarlavha1(matn, **atributlar):
    """h1 elementi"""
    return Element('h1', **atributlar).matn(matn)


def sarlavha2(matn, **atributlar):
    """h2 elementi"""
    return Element('h2', **atributlar).matn(matn)


def sarlavha3(matn, **atributlar):
    """h3 elementi"""
    return Element('h3', **atributlar).matn(matn)


# ============= MATN =============

def paragraf(matn, **atributlar):
    """p elementi"""
    return Element('p', **atributlar).matn(matn)


def qalin(matn):
    """b/strong elementi"""
    return Element('strong').matn(matn)


def kursiv(matn):
    """i/em elementi"""
    return Element('em').matn(matn)


def havola(matn, url, **atributlar):
    """a elementi"""
    return Element('a', href=url, **atributlar).matn(matn)


# ============= RO'YXATLAR =============

def royxat(*elementlar, tartiblangan=False, **atributlar):
    """ul/ol elementi"""
    teg = 'ol' if tartiblangan else 'ul'
    el = Element(teg, **atributlar)
    for e in elementlar:
        li = Element('li').matn(str(e))
        el.qoshish(li)
    return el


# ============= FORMA =============

def forma(*bolalar, metod="post", amal="#", **atributlar):
    """form elementi"""
    return Element('form', method=metod, action=amal, **atributlar).qoshish(*bolalar)


def kiritish(turi="text", nom="", qiymat="", **atributlar):
    """input elementi"""
    return Element('input', type=turi, name=nom, value=qiymat, **atributlar)


def tugma(matn, turi="submit", **atributlar):
    """button elementi"""
    return Element('button', type=turi, **atributlar).matn(matn)


def matn_maydoni(nom="", qatorlar=4, ustunlar=50, **atributlar):
    """textarea elementi"""
    return Element('textarea', name=nom, rows=str(qatorlar), cols=str(ustunlar), **atributlar)


# ============= JADVAL =============

def jadval(*qatorlar, sarlavhalar=None, **atributlar):
    """table elementi"""
    el = Element('table', **atributlar)
    
    if sarlavhalar:
        thead = Element('thead')
        tr = Element('tr')
        for s in sarlavhalar:
            tr.qoshish(Element('th').matn(str(s)))
        thead.qoshish(tr)
        el.qoshish(thead)
    
    tbody = Element('tbody')
    for qator in qatorlar:
        tr = Element('tr')
        for h in qator:
            tr.qoshish(Element('td').matn(str(h)))
        tbody.qoshish(tr)
    el.qoshish(tbody)
    
    return el


# ============= MEDIA =============

def rasm(url, alt="", **atributlar):
    """img elementi"""
    return Element('img', src=url, alt=alt, **atributlar)


def video(url, **atributlar):
    """video elementi"""
    return Element('video', src=url, controls="", **atributlar)


# ============= STILLAR =============

def stil(css):
    """style elementi"""
    return Element('style').matn(css)


__all__ = [
    'Element', 'sahifa', 'div', 'span', 'sarlavha1', 'sarlavha2', 'sarlavha3',
    'paragraf', 'qalin', 'kursiv', 'havola', 'royxat', 'forma', 'kiritish',
    'tugma', 'matn_maydoni', 'jadval', 'rasm', 'video', 'stil'
]
