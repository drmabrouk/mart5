# -*- coding: utf-8 -*-
import sys
import os

from build_report import CSS_STYLES
from pages_1_10 import PAGES_CONTENT
from pages_11_15 import PAGES_CONTENT_11_20 as PAGES_11_15
from pages_16_20 import PAGES_CONTENT_16_20 as PAGES_16_20
from pages_21_30 import PAGES_CONTENT_21_30 as PAGES_21_30

# Merge dictionaries
ALL_PAGES = {}

# Pages 1 to 10
for k, v in PAGES_CONTENT.items():
    ALL_PAGES[k] = v

# Pages 11 to 15
for k, v in PAGES_11_15.items():
    ALL_PAGES[k] = v

# Pages 16 to 31
for k, v in PAGES_16_20.items():
    ALL_PAGES[k] = v

# Pages 32 to 48
for k, v in PAGES_21_30.items():
    ALL_PAGES[k] = v

total_pages = len(ALL_PAGES)

# Start compiling MART.html
html_out = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>دراسة جدوى تفصيلية شاملة - منصة ومستودعات تاجر (Tager)</title>
    <!-- خطوط متميزة ومحملة عبر الويب للتصميم الرقمي -->
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
"""

html_out += CSS_STYLES

html_out += """
    </style>
</head>
<body>
"""

for page_num in sorted(ALL_PAGES.keys()):
    html_out += f"""
    <!-- ================= PAGE {page_num} ================= -->
    <div class="page-container" id="page-{page_num}">
        <div class="doc-header">
            <div class="logo-area">
                <span class="logo-text">تاجر</span>
            </div>
            <div class="meta-info">دراسة جدوى استراتيجية متكاملة V6.5</div>
        </div>
        <div class="page-content">
"""
    html_out += ALL_PAGES[page_num]
    html_out += f"""
        </div>
        <div class="doc-footer">
            <div>V Smart General Trading L.L.C. - دراسة الجدوى الاستثمارية</div>
            <div class="page-num">صفحة {page_num} من {total_pages}</div>
        </div>
    </div>
"""

html_out += """
</body>
</html>
"""

# Write to file
with open("MART.html", "w", encoding="utf-8") as f:
    f.write(html_out)

print(f"MART.html compiled successfully with exactly {total_pages} pages!")
