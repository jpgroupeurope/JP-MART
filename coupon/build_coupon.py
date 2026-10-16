"""JP MART thermal coupon, 4x6 in portrait, 203 DPI, pure black and white.

All layout is expressed in printer dots (1 dot = 1/203 in) so every edge
lands on the dot grid. Outputs: PDF (vector), PNG (1-bit, 812x1218), QR SVG/PNG.
"""
import os
import qrcode
import pymupdf
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

OUT = os.path.dirname(os.path.abspath(__file__))
DPI = 203
W, H = 4 * DPI, 6 * DPI          # 812 x 1218 dots
U = 72.0 / DPI                   # points per dot

CODE = "WELCOME10"
SITE = "jpmart.eu"
SITE_URL = "https://jpmart.eu"
QR_URL = f"https://jpmart.eu/discount/{CODE}"   # Shopify auto-applies the code

LANGS = {
    "pl": dict(thanks="DZIĘKUJEMY, ŻE JESTEŚ Z NAMI!", gift="A PREZENT NA KOLEJNE ZAKUPY...",
               head="10% RABATU", sub="NA TWOJE NASTĘPNE ZAKUPY", codelbl="TWÓJ KOD RABATOWY:",
               scan1="ZESKANUJ KOD QR", scan2="I ODKRYJ NASZ SKLEP",
               terms="Rabat 10% na wszystkie produkty w sklepie jpmart.eu.\n"
                     "Kod jednorazowy dla jednego klienta, bez minimalnej\n"
                     "wartości zamówienia. Bez terminu ważności."),
    "cz": dict(thanks="DĚKUJEME, ŽE JSTE S NÁMI!", gift="A DÁREK NA DALŠÍ NÁKUPY...",
               head="10% SLEVA", sub="NA VÁŠ DALŠÍ NÁKUP", codelbl="VÁŠ SLEVOVÝ KÓD:",
               scan1="NASKENUJTE QR KÓD", scan2="A OBJEVTE NÁŠ OBCHOD",
               terms="Sleva 10% na všechny produkty v obchodě jpmart.eu.\n"
                     "Kód je jednorázový pro jednoho zákazníka, bez minimální\n"
                     "hodnoty objednávky. Bez data expirace."),
    "sk": dict(thanks="ĎAKUJEME, ŽE STE S NAMI!", gift="A DARČEK NA ĎALŠIE NÁKUPY...",
               head="10% ZĽAVA", sub="NA VÁŠ ĎALŠÍ NÁKUP", codelbl="VÁŠ ZĽAVOVÝ KÓD:",
               scan1="NASKENUJTE QR KÓD", scan2="A OBJAVTE NÁŠ OBCHOD",
               terms="Zľava 10% na všetky produkty v obchode jpmart.eu.\n"
                     "Kód je jednorazový pre jedného zákazníka, bez minimálnej\n"
                     "hodnoty objednávky. Bez dátumu platnosti."),
    "hu": dict(thanks="KÖSZÖNJÜK, HOGY MINKET VÁLASZTOTT!", gift="ÉS EGY AJÁNDÉK A KÖVETKEZŐ VÁSÁRLÁSÁHOZ...",
               head="10% KEDVEZMÉNY", sub="A KÖVETKEZŐ VÁSÁRLÁSÁRA", codelbl="KUPONKÓDJA:",
               scan1="OLVASSA BE A QR-KÓDOT", scan2="ÉS FEDEZZE FEL WEBSHOPUNKAT",
               terms="10% kedvezmény a jpmart.eu webshop minden termékére.\n"
                     "A kód vásárlónként egyszer használható, minimális\n"
                     "rendelési érték nélkül. Lejárati idő nélkül."),
}

FONTS = "/usr/share/fonts/truetype/liberation/"
pdfmetrics.registerFont(TTFont("B", FONTS + "LiberationSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("R", FONTS + "LiberationSans-Regular.ttf"))

def build(lang):
    global c
    L = LANGS[lang]
    PDF = os.path.join(OUT, f"jp-mart-coupon-4x6-{lang}.pdf")
    c = canvas.Canvas(PDF, pagesize=(W * U, H * U))
    c.setTitle("JP MART – 10%")
    c.setAuthor("JP MART")
    c.setFillColorRGB(0, 0, 0)
    c.setStrokeColorRGB(0, 0, 0)


    def Y(y):            # top-down dots -> PDF points
        return (H - y) * U


    def line(x1, y1, x2, y2, w=2):
        c.setLineWidth(w * U)
        c.line(x1 * U, Y(y1), x2 * U, Y(y2))


    def rect(x, y, w, h, lw=2):
        c.setLineWidth(lw * U)
        c.setLineJoin(0)
        c.rect(x * U, Y(y + h), w * U, h * U, stroke=1, fill=0)


    def text(s, baseline, size, font="B", track=0.0, maxw=None, x=None):
        """Centered text; shrinks to maxw if needed. size/track in dots."""
        s = str(s)
        if maxw:
            while pdfmetrics.stringWidth(s, font, size * U) + track * U * (len(s) - 1) > maxw * U:
                size -= 1
        w = pdfmetrics.stringWidth(s, font, size * U) + track * U * (len(s) - 1)
        x0 = (W * U - w) / 2 if x is None else x * U
        t = c.beginText(x0, Y(baseline))
        t.setFont(font, size * U)
        t.setCharSpace(track * U)
        t.textLine(s)
        c.drawText(t)
        return x0 / U, w / U, size


    def divider(y, half=250, gap=18):
        cx = W // 2
        line(cx - half, y, cx - gap, y, 2)
        line(cx + gap, y, cx + half, y, 2)
        d = 9                                    # outline diamond
        c.setLineWidth(2 * U)
        p = c.beginPath()
        p.moveTo(cx * U, Y(y - d)); p.lineTo((cx + d) * U, Y(y))
        p.lineTo(cx * U, Y(y + d)); p.lineTo((cx - d) * U, Y(y)); p.close()
        c.drawPath(p, stroke=1, fill=0)


    # ---- frame with small corner accents -------------------------------------
    M = 22
    rect(M, M, W - 2 * M, H - 2 * M, 2)
    rect(M + 10, M + 10, W - 2 * (M + 10), H - 2 * (M + 10), 1)

    # ---- header ---------------------------------------------------------------
    text("JP MART", 140, 96, "B", track=10, maxw=640)
    divider(178)

    text(L["thanks"], 228, 31, "B", track=0.5, maxw=700)
    text(L["gift"], 266, 25, "R", track=1, maxw=700)
    divider(302)

    # ---- headline ---------------------------------------------------------------
    text(L["head"], 424, 128, "B", track=2, maxw=690)
    text(L["sub"], 474, 30, "B", track=1, maxw=700)

    # ---- code box ---------------------------------------------------------------
    text(L["codelbl"], 540, 25, "R", track=2, maxw=700)
    bw, bh = 560, 96
    bx, by = (W - bw) // 2, 560
    rect(bx, by, bw, bh, 5)
    text(CODE, by + 68, 66, "B", track=6, maxw=bw - 40)
    c.linkURL(QR_URL, (bx * U, Y(by + bh), (bx + bw) * U, Y(by)), relative=0)

    # ---- QR -----------------------------------------------------------------------
    text(L["scan1"], 722, 28, "B", track=2, maxw=700)
    text(L["scan2"], 758, 28, "B", track=2, maxw=700)

    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=0, box_size=1)
    qr.add_data(QR_URL)
    qr.make(fit=True)
    M_ = qr.get_matrix()
    n = len(M_)
    mod = 8                                         # dots per module (integer = razor sharp)
    qs = n * mod
    qx, qy = (W - qs) // 2, 782
    # solid white quiet zone is the page itself; draw dark modules as row runs
    c.setFillColorRGB(0, 0, 0)
    for r, row in enumerate(M_):
        ccol = 0
        while ccol < n:
            if row[ccol]:
                s = ccol
                while ccol < n and row[ccol]:
                    ccol += 1
                c.rect((qx + s * mod) * U, Y(qy + (r + 1) * mod), (ccol - s) * mod * U, mod * U,
                       stroke=0, fill=1)
            else:
                ccol += 1
    c.linkURL(QR_URL, (qx * U, Y(qy + qs), (qx + qs) * U, Y(qy)), relative=0)

    # ---- footer -----------------------------------------------------------------------
    sx, sw, ss = text(SITE, qy + qs + 56, 40, "B", track=3, maxw=500)
    line(sx, qy + qs + 68, sx + sw, qy + qs + 68, 3)
    c.linkURL(SITE_URL, (sx * U, Y(qy + qs + 66 + 6), (sx + sw) * U, Y(qy + qs + 56 - ss)), relative=0)

    lines = L["terms"].split("\n")
    yb = qy + qs + 102
    for ln in lines:
        text(ln, yb, 21, "R", maxw=690)
        yb += 27
    LAST = yb
    c.showPage()
    c.save()

    return M_, n, mod, PDF


M_ = n = mod = None
for lang in LANGS:
    M_, n, mod, PDF = build(lang)
    # ---- standalone QR assets ------------------------------------------------------------
    qz = 4
    size = (n + 2 * qz) * mod
    im = Image.new("1", (size, size), 1)
    px = im.load()
    for r in range(n):
        for k in range(n):
            if M_[r][k]:
                for dy in range(mod):
                    for dx in range(mod):
                        px[(k + qz) * mod + dx, (r + qz) * mod + dy] = 0
    im.save(os.path.join(OUT, "qr-welcome10.png"), dpi=(DPI, DPI))
    with open(os.path.join(OUT, "qr-welcome10.svg"), "w") as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {n + 2*qz} {n + 2*qz}" '
                f'shape-rendering="crispEdges"><rect width="100%" height="100%" fill="#fff"/><path fill="#000" d="')
        for r in range(n):
            for k in range(n):
                if M_[r][k]:
                    f.write(f"M{k+qz} {r+qz}h1v1h-1z")
        f.write('"/></svg>')

    # ---- PNG: render PDF at 3x, downsample, threshold to 1-bit ------------------------------
    doc = pymupdf.open(os.path.join(OUT, f"jp-mart-coupon-4x6-{lang}.pdf"))
    pix = doc[0].get_pixmap(dpi=DPI * 3, colorspace=pymupdf.csGRAY, alpha=False)
    g = Image.frombytes("L", (pix.width, pix.height), pix.samples).resize((W, H), Image.LANCZOS)
    bw_img = g.point(lambda v: 0 if v < 140 else 255).convert("1", dither=Image.NONE)
    bw_img.save(os.path.join(OUT, f"jp-mart-coupon-4x6-{lang}-203dpi.png"), dpi=(DPI, DPI))
    print("size", bw_img.size, "qr modules", n, "lang", lang)
