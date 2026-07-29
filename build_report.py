# -*- coding: utf-8 -*-
import sys

# Define CSS styles
CSS_STYLES = """
:root {
    --primary: #0f172a;       /* كحلي ملكي عميق */
    --primary-light: #1e293b; /* كحلي متوسط */
    --accent: #0284c7;        /* أزرق سفاير */
    --accent-light: #e0f2fe;  /* أزرق فاتح جداً */
    --gold: #b45309;          /* ذهبي برونزي */
    --gold-light: #fef3c7;    /* ذهبي فاتح */
    --success: #10b981;       /* أخضر زمردي */
    --success-light: #d1fae5; /* أخضر فاتح */
    --danger: #ef4444;        /* أحمر مرجاني */
    --danger-light: #fee2e2;  /* أحمر فاتح */
    --bg-base: #f1f5f9;       /* رمادي فاتح جداً للخلفية */
    --bg-card: #ffffff;       /* أبيض ناصع للبطاقات */
    --text-dark: #1e293b;     /* أسود نصي */
    --text-muted: #64748b;    /* رمادي للنصوص الجانبية */
    --border-color: #cbd5e1;  /* لون الحدود */
    --font-main: 'Cairo', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

@page {
    size: A4 portrait;
    margin: 0;
}

@media print {
    body {
        background-color: #ffffff;
        color: #000000;
        font-size: 9.5pt;
        line-height: 1.5;
    }
    .page-container {
        width: 210mm;
        height: 297mm;
        margin: 0 !important;
        padding: 12mm 15mm 12mm 15mm !important;
        box-shadow: none !important;
        border-radius: 0 !important;
        page-break-after: always;
        break-after: page;
        position: relative;
        box-sizing: border-box;
    }
    .no-print {
        display: none !important;
    }
}

@media screen {
    body {
        background-color: #cbd5e1;
        padding: 30px 0;
    }
    .page-container {
        width: 210mm;
        height: 297mm;
        margin: 0 auto 30px auto;
        background-color: var(--bg-card);
        padding: 12mm 15mm 12mm 15mm;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
        border-radius: 6px;
        position: relative;
        box-sizing: border-box;
    }
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: var(--font-main);
    color: var(--text-dark);
    line-height: 1.5;
    background-color: var(--bg-base);
    text-align: right;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}

h1 {
    font-size: 15pt;
    border-bottom: 3px solid var(--accent);
    padding-bottom: 6px;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 10px;
    color: var(--primary);
    font-weight: 800;
}

h2 {
    font-size: 11.5pt;
    border-right: 4px solid var(--gold);
    padding-right: 8px;
    margin-top: 12px;
    margin-bottom: 8px;
    background-color: #f8fafc;
    padding-top: 3px;
    padding-bottom: 3px;
    color: var(--primary);
    font-weight: 700;
}

h3 {
    font-size: 10pt;
    color: var(--accent);
    margin-top: 8px;
    margin-bottom: 6px;
    font-weight: 700;
}

p {
    margin-bottom: 8px;
    text-align: justify;
    color: #334155;
    font-size: 8.8pt;
    line-height: 1.5;
}

.doc-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 4px;
    margin-bottom: 10px;
    height: 8mm;
}

.doc-header .logo-area {
    display: flex;
    align-items: center;
    gap: 6px;
}

.doc-header .logo-text {
    font-weight: 800;
    font-size: 10pt;
    color: var(--primary);
}

.doc-header .logo-text span {
    color: var(--accent);
}

.doc-header .meta-info {
    font-size: 7.5pt;
    color: var(--text-muted);
}

.doc-footer {
    position: absolute;
    bottom: 8mm;
    left: 15mm;
    right: 15mm;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid var(--border-color);
    padding-top: 6px;
    font-size: 7.5pt;
    color: var(--text-muted);
    height: 6mm;
}

.page-content {
    height: 255mm;
    overflow: hidden;
    position: relative;
}

/* Cover Styling */
.cover-wrapper {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;
}

.cover-title-main {
    font-size: 24pt;
    font-weight: 900;
    color: var(--primary);
    line-height: 1.3;
    margin-bottom: 12px;
}

.cover-title-main span {
    color: var(--accent);
}

.cover-subtitle {
    font-size: 11.5pt;
    color: var(--text-muted);
    font-weight: 500;
    margin-bottom: 25px;
    line-height: 1.6;
}

.cover-divider {
    width: 120px;
    height: 5px;
    background: linear-gradient(to left, var(--accent), var(--gold));
    margin-bottom: 25px;
    border-radius: 3px;
}

.cover-meta-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
    text-align: right;
    background-color: var(--bg-base);
    border: 1px solid var(--border-color);
    padding: 20px;
    border-radius: 8px;
    margin-top: 15px;
}

.meta-item {
    font-size: 8.5pt;
}

.meta-item strong {
    color: var(--primary);
    display: block;
    margin-bottom: 3px;
    font-size: 9pt;
}

.meta-item span {
    color: var(--text-muted);
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0;
    font-size: 8pt;
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
}

th, td {
    padding: 5px 7px;
    text-align: right;
    border-bottom: 1px solid var(--border-color);
    line-height: 1.4;
}

th {
    background-color: var(--primary);
    color: #ffffff;
    font-weight: 700;
    font-size: 8.2pt;
    border-left: 1px solid #334155;
}

tr:nth-child(even) td {
    background-color: #f8fafc;
}

.table-total {
    font-weight: 800;
    background-color: #cbd5e1 !important;
    border-top: 2px solid var(--primary);
    color: var(--primary);
}

.kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
    margin: 8px 0;
}

.kpi-card {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    border-top: 3px solid var(--accent);
    padding: 8px;
    border-radius: 4px;
    text-align: center;
}

.kpi-title {
    font-size: 7.5pt;
    color: var(--text-muted);
    margin-bottom: 3px;
    font-weight: 600;
}

.kpi-value {
    font-size: 11pt;
    font-weight: 800;
    color: var(--primary);
}

.kpi-unit {
    font-size: 7.5pt;
    color: var(--text-muted);
}

.kpi-card.gold { border-top-color: var(--gold); }
.kpi-card.success { border-top-color: var(--success); }
.kpi-card.danger { border-top-color: var(--danger); }

.info-callout {
    background-color: #f0f9ff;
    border-right: 4px solid var(--accent);
    padding: 8px 10px;
    border-radius: 0 4px 4px 0;
    margin: 8px 0;
    font-size: 8.5pt;
}

.info-callout h5 {
    color: var(--accent);
    margin-bottom: 2px;
    font-weight: 700;
    font-size: 8.8pt;
}

.gold-callout {
    background-color: #fffbeb;
    border-right: 4px solid var(--gold);
    padding: 8px 10px;
    border-radius: 0 4px 4px 0;
    margin: 8px 0;
    font-size: 8.5pt;
}

.gold-callout h5 {
    color: var(--gold);
    margin-bottom: 2px;
    font-weight: 700;
    font-size: 8.8pt;
}

.danger-callout {
    background-color: #fef2f2;
    border-right: 4px solid var(--danger);
    padding: 8px 10px;
    border-radius: 0 4px 4px 0;
    margin: 8px 0;
    font-size: 8.5pt;
}

.danger-callout h5 {
    color: var(--danger);
    margin-bottom: 2px;
    font-weight: 700;
    font-size: 8.8pt;
}

.grid-2 {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
    margin: 8px 0;
}

.grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    margin: 8px 0;
}

.card-box {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 8px;
    border-radius: 4px;
}

.card-box h4 {
    color: var(--primary);
    font-size: 9pt;
    margin-bottom: 4px;
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 3px;
    font-weight: 700;
}

.card-box p {
    font-size: 8pt;
    margin-bottom: 0;
}

.badge-success {
    background-color: var(--success-light);
    color: var(--success);
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: 700;
    font-size: 7.5pt;
}

.badge-gold {
    background-color: var(--gold-light);
    color: var(--gold);
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: 700;
    font-size: 7.5pt;
}

.badge-accent {
    background-color: var(--accent-light);
    color: var(--accent);
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: 700;
    font-size: 7.5pt;
}

/* SVGs and Icons */
.svg-icon {
    vertical-align: middle;
}
"""

print("CSS variables defined successfully")
