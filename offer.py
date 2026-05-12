from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

OUTPUT = "./21blooms_proposal.pdf"

# Register Cyrillic-capable fonts
pdfmetrics.registerFont(TTFont("Body", "/System/Library/Fonts/Supplemental/Arial.ttf"))
pdfmetrics.registerFont(TTFont("Body-Bold", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"))
pdfmetrics.registerFont(TTFont("Body-Italic", "/System/Library/Fonts/Supplemental/Arial Italic.ttf"))

W, H = A4

# Colors
BLACK = colors.HexColor("#1a1a1a")
GRAY = colors.HexColor("#6b6b6b")
LIGHT_GRAY = colors.HexColor("#f4f3f0")
MID_GRAY = colors.HexColor("#d0cfc7")
WHITE = colors.white
INFO_BG = colors.HexColor("#e6f1fb")
INFO_TEXT = colors.HexColor("#185fa5")

def draw_page(c):
    # --- HEADER ---
    # Top tag line
    c.setFont("Body", 8)
    c.setFillColor(GRAY)
    c.drawString(20*mm, H - 18*mm, "КОММЕРЧЕСКОЕ ПРЕДЛОЖЕНИЕ · 2025")

    # Thin line under tag
    c.setStrokeColor(MID_GRAY)
    c.setLineWidth(0.5)
    c.line(20*mm, H - 22*mm, W - 20*mm, H - 22*mm)

    # Title
    c.setFont("Body-Bold", 26)
    c.setFillColor(BLACK)
    c.drawString(20*mm, H - 38*mm, "Визуальный редизайн")

    c.setFont("Body", 26)
    c.setFillColor(GRAY)
    c.drawString(20*mm, H - 49*mm, "21blooms.com")

    # Subtitle
    c.setFont("Body", 10)
    c.setFillColor(GRAY)
    c.drawString(20*mm, H - 59*mm, "Современный фронтенд для интернет-магазина цветов —")
    c.drawString(20*mm, H - 65*mm, "без изменения структуры и логики сайта")

    # Divider
    c.setStrokeColor(MID_GRAY)
    c.setLineWidth(0.5)
    c.line(20*mm, H - 72*mm, W - 20*mm, H - 72*mm)

    # --- SCOPE SECTION ---
    y = H - 83*mm
    c.setFont("Body", 7.5)
    c.setFillColor(GRAY)
    c.drawString(20*mm, y, "ЧТО ВХОДИТ В РАБОТУ")

    # Card background
    card_y = y - 6*mm
    card_h = 48*mm
    c.setFillColor(LIGHT_GRAY)
    c.setStrokeColor(MID_GRAY)
    c.setLineWidth(0.5)
    c.roundRect(20*mm, card_y - card_h, W - 40*mm, card_h, 4*mm, fill=1, stroke=1)

    # Scope items — 2 columns
    items_left = [
        "Редизайн навбара",
        "Обновление футера",
        "Категории по событиям (свадьба, д/р и др.)",
    ]
    items_right = [
        "Новая hero-секция",
        "Секция с фото от клиентов",
    ]

    item_y = card_y - 10*mm
    col1_x = 25*mm
    col2_x = 100*mm

    for item in items_left:
        c.setFillColor(GRAY)
        c.circle(col1_x + 1.5*mm, item_y + 1.2*mm, 1.2*mm, fill=1, stroke=0)
        c.setFont("Body", 10)
        c.setFillColor(BLACK)
        c.drawString(col1_x + 4*mm, item_y, item)
        item_y -= 8*mm

    item_y = card_y - 10*mm
    for item in items_right:
        c.setFillColor(GRAY)
        c.circle(col2_x + 1.5*mm, item_y + 1.2*mm, 1.2*mm, fill=1, stroke=0)
        c.setFont("Body", 10)
        c.setFillColor(BLACK)
        c.drawString(col2_x + 4*mm, item_y, item)
        item_y -= 8*mm

    # Note inside card
    note_y = card_y - card_h + 8*mm
    c.setStrokeColor(MID_GRAY)
    c.setLineWidth(0.5)
    c.line(25*mm, note_y + 4*mm, W - 25*mm, note_y + 4*mm)
    c.setFont("Body-Italic", 8.5)
    c.setFillColor(GRAY)
    c.drawString(25*mm, note_y - 1*mm, "Структура и логика сайта остаются прежними. Изменения — исключительно визуальные.")

    # --- PRICING SECTION ---
    y2 = card_y - card_h - 12*mm
    c.setFont("Body", 7.5)
    c.setFillColor(GRAY)
    c.drawString(20*mm, y2, "СТОИМОСТЬ")

    # Base package card
    base_y = y2 - 6*mm
    base_h = 20*mm
    c.setFillColor(LIGHT_GRAY)
    c.setStrokeColor(MID_GRAY)
    c.setLineWidth(0.5)
    c.roundRect(20*mm, base_y - base_h, W - 40*mm, base_h, 4*mm, fill=1, stroke=1)

    c.setFont("Body", 12)
    c.setFillColor(BLACK)
    c.drawString(25*mm, base_y - 9*mm, "Визуальный редизайн сайта")
    c.setFont("Body", 9)
    c.setFillColor(GRAY)
    c.drawString(25*mm, base_y - 15*mm, "Навбар · Hero · Футер · UGC-секция · Event-категории")
    c.setFont("Body-Bold", 20)
    c.setFillColor(BLACK)
    c.drawRightString(W - 25*mm, base_y - 13*mm, "$800")

    # Optional block
    opt_y = base_y - base_h - 5*mm
    opt_h = 32*mm
    c.setFillColor(WHITE)
    c.setStrokeColor(MID_GRAY)
    c.setLineWidth(0.5)
    c.roundRect(20*mm, opt_y - opt_h, W - 40*mm, opt_h, 4*mm, fill=1, stroke=1)

    # Optional badge
    badge_w = 55*mm
    badge_h = 5.5*mm
    badge_x = 25*mm
    badge_y = opt_y - 7*mm
    c.setFillColor(INFO_BG)
    c.roundRect(badge_x, badge_y - badge_h + 2*mm, badge_w, badge_h, 2*mm, fill=1, stroke=0)
    c.setFont("Body", 7.5)
    c.setFillColor(INFO_TEXT)
    c.drawString(badge_x + 3*mm, badge_y - badge_h + 4.5*mm, "ОПЦИОНАЛЬНО · НЕ ВХОДИТ В БАЗОВЫЙ ПАКЕТ")

    c.setFont("Body", 12)
    c.setFillColor(BLACK)
    c.drawString(25*mm, opt_y - 16*mm, "ИИ-фотосессия товаров")
    c.setFont("Body-Bold", 20)
    c.setFillColor(BLACK)
    c.drawRightString(W - 25*mm, opt_y - 18*mm, "+$100")

    c.setFont("Body", 9)
    c.setFillColor(GRAY)
    c.drawString(25*mm, opt_y - 22*mm, "До 50 позиций — AI-визуал + 5-секундное видео по ховеру для каждого товара.")

    c.setFont("Body-Italic", 8.5)
    c.setFillColor(GRAY)
    c.drawString(25*mm, opt_y - 28*mm, "Добавляется по желанию клиента отдельно от основного редизайна.")

    # --- PAYMENT ---
    pay_y = opt_y - opt_h - 12*mm
    c.setFont("Body", 7.5)
    c.setFillColor(GRAY)
    c.drawString(20*mm, pay_y, "ОПЛАТА И СРОКИ")

    chip_top = pay_y - 6*mm
    chip_h = 20*mm
    chip_w = (W - 40*mm - 8*mm) / 3

    chips = [
        ("Предоплата", "50%", "При старте работ"),
        ("Остаток", "50%", "После сдачи"),
        ("Срок", "10 дн.", "рабочих дней"),
    ]

    for i, (label, val, desc) in enumerate(chips):
        cx = 20*mm + i * (chip_w + 4*mm)
        c.setFillColor(LIGHT_GRAY)
        c.setStrokeColor(MID_GRAY)
        c.setLineWidth(0.5)
        c.roundRect(cx, chip_top - chip_h, chip_w, chip_h, 3*mm, fill=1, stroke=1)

        c.setFont("Body", 7.5)
        c.setFillColor(GRAY)
        c.drawCentredString(cx + chip_w/2, chip_top - 7*mm, label.upper())

        c.setFont("Body-Bold", 16)
        c.setFillColor(BLACK)
        c.drawCentredString(cx + chip_w/2, chip_top - 14*mm, val)

        c.setFont("Body", 8)
        c.setFillColor(GRAY)
        c.drawCentredString(cx + chip_w/2, chip_top - 19*mm, desc)

    # --- PROCESS ---
    proc_y = chip_top - chip_h - 12*mm
    c.setFont("Body", 7.5)
    c.setFillColor(GRAY)
    c.drawString(20*mm, proc_y, "КАК МЫ РАБОТАЕМ")

    steps = [
        ("01", "Бриф", "Референсы, пожелания, доступы"),
        ("02", "Макет", "Прототип ключевых блоков"),
        ("03", "Правки", "До 2 раундов корректур"),
        ("04", "Сдача", "Финальный код / ассеты"),
    ]

    step_w = (W - 40*mm - 9*mm) / 4
    step_top = proc_y - 6*mm

    for i, (num, title, desc) in enumerate(steps):
        sx = 20*mm + i * (step_w + 3*mm)
        # Top border line
        lw = 2 if i == 0 else 0.5
        lc = BLACK if i == 0 else MID_GRAY
        c.setStrokeColor(lc)
        c.setLineWidth(lw)
        c.line(sx, step_top, sx + step_w, step_top)

        c.setFont("Body", 16)
        c.setFillColor(GRAY)
        c.drawString(sx, step_top - 9*mm, num)

        c.setFont("Body-Bold", 9)
        c.setFillColor(BLACK)
        c.drawString(sx, step_top - 15*mm, title)

        c.setFont("Body", 8)
        c.setFillColor(GRAY)
        # Wrap desc
        words = desc.split()
        line1 = " ".join(words[:3])
        line2 = " ".join(words[3:])
        c.drawString(sx, step_top - 20*mm, line1)
        if line2:
            c.drawString(sx, step_top - 24*mm, line2)

    # --- FOOTER LINE ---
    c.setStrokeColor(MID_GRAY)
    c.setLineWidth(0.5)
    c.line(20*mm, 14*mm, W - 20*mm, 14*mm)
    c.setFont("Body", 8)
    c.setFillColor(GRAY)
    c.drawString(20*mm, 9*mm, "21blooms.com · Визуальный редизайн · 2025")
    c.drawRightString(W - 20*mm, 9*mm, "Предложение действительно 14 дней")

c_obj = canvas.Canvas(OUTPUT, pagesize=A4)
draw_page(c_obj)
c_obj.save()
print("Done:", OUTPUT)
