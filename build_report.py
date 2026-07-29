# -*- coding: utf-8 -*-
import sys

# Define CSS styles for A4 Portrait Simulation
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
        font-size: 9pt;
        line-height: 1.45;
    }
    .page-container {
        width: 210mm;
        height: 297mm;
        margin: 0 !important;
        padding: 10mm 15mm 10mm 15mm !important;
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
        padding: 10mm 15mm 10mm 15mm;
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
    line-height: 1.45;
    background-color: var(--bg-base);
    text-align: right;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}

h1 {
    font-size: 14pt;
    border-bottom: 3px solid var(--accent);
    padding-bottom: 4px;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 8px;
    color: var(--primary);
    font-weight: 800;
}

h2 {
    font-size: 11pt;
    border-right: 4px solid var(--gold);
    padding-right: 8px;
    margin-top: 10px;
    margin-bottom: 6px;
    background-color: #f8fafc;
    padding-top: 2px;
    padding-bottom: 2px;
    color: var(--primary);
    font-weight: 700;
}

h3 {
    font-size: 9.5pt;
    color: var(--accent);
    margin-top: 6px;
    margin-bottom: 4px;
    font-weight: 700;
}

p {
    margin-bottom: 6px;
    text-align: justify;
    color: #334155;
    font-size: 8.5pt;
    line-height: 1.45;
}

.doc-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 4px;
    margin-bottom: 8px;
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
    font-size: 7.2pt;
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
    padding-top: 4px;
    font-size: 7.2pt;
    color: var(--text-muted);
    height: 6mm;
}

.page-content {
    height: 257mm;
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
    font-size: 22pt;
    font-weight: 900;
    color: var(--primary);
    line-height: 1.35;
    margin-bottom: 10px;
}

.cover-title-main span {
    color: var(--accent);
}

.cover-subtitle {
    font-size: 10.5pt;
    color: var(--text-muted);
    font-weight: 500;
    margin-bottom: 20px;
    line-height: 1.5;
}

.cover-divider {
    width: 120px;
    height: 5px;
    background: linear-gradient(to left, var(--accent), var(--gold));
    margin-bottom: 20px;
    border-radius: 3px;
}

.cover-meta-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
    text-align: right;
    background-color: var(--bg-base);
    border: 1px solid var(--border-color);
    padding: 16px;
    border-radius: 6px;
    margin-top: 10px;
}

.meta-item {
    font-size: 8pt;
}

.meta-item strong {
    color: var(--primary);
    display: block;
    margin-bottom: 2px;
    font-size: 8.5pt;
}

.meta-item span {
    color: var(--text-muted);
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 6px 0;
    font-size: 7.8pt;
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
}

th, td {
    padding: 4px 6px;
    text-align: right;
    border-bottom: 1px solid var(--border-color);
    line-height: 1.35;
}

th {
    background-color: var(--primary);
    color: #ffffff;
    font-weight: 700;
    font-size: 8pt;
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
    gap: 8px;
    margin: 6px 0;
}

.kpi-card {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    border-top: 3px solid var(--accent);
    padding: 6px;
    border-radius: 4px;
    text-align: center;
}

.kpi-title {
    font-size: 7pt;
    color: var(--text-muted);
    margin-bottom: 2px;
    font-weight: 600;
}

.kpi-value {
    font-size: 10.5pt;
    font-weight: 800;
    color: var(--primary);
}

.kpi-unit {
    font-size: 7pt;
    color: var(--text-muted);
}

.kpi-card.gold { border-top-color: var(--gold); }
.kpi-card.success { border-top-color: var(--success); }
.kpi-card.danger { border-top-color: var(--danger); }

.info-callout {
    background-color: #f0f9ff;
    border-right: 4px solid var(--accent);
    padding: 6px 8px;
    border-radius: 0 4px 4px 0;
    margin: 6px 0;
    font-size: 8pt;
}

.info-callout h5 {
    color: var(--accent);
    margin-bottom: 2px;
    font-weight: 700;
    font-size: 8.5pt;
}

.gold-callout {
    background-color: #fffbeb;
    border-right: 4px solid var(--gold);
    padding: 6px 8px;
    border-radius: 0 4px 4px 0;
    margin: 6px 0;
    font-size: 8pt;
}

.gold-callout h5 {
    color: var(--gold);
    margin-bottom: 2px;
    font-weight: 700;
    font-size: 8.5pt;
}

.danger-callout {
    background-color: #fef2f2;
    border-right: 4px solid var(--danger);
    padding: 6px 8px;
    border-radius: 0 4px 4px 0;
    margin: 6px 0;
    font-size: 8pt;
}

.danger-callout h5 {
    color: var(--danger);
    margin-bottom: 2px;
    font-weight: 700;
    font-size: 8.5pt;
}

.grid-2 {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
    margin: 6px 0;
}

.grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
    margin: 6px 0;
}

.card-box {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 6px;
    border-radius: 4px;
}

.card-box h4 {
    color: var(--primary);
    font-size: 8.5pt;
    margin-bottom: 2px;
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 2px;
    font-weight: 700;
}

.card-box p {
    font-size: 7.8pt;
    margin-bottom: 0;
}

.badge-success {
    background-color: var(--success-light);
    color: var(--success);
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: 700;
    font-size: 7pt;
}

.badge-gold {
    background-color: var(--gold-light);
    color: var(--gold);
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: 700;
    font-size: 7pt;
}

.badge-accent {
    background-color: var(--accent-light);
    color: var(--accent);
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: 700;
    font-size: 7pt;
}

.step-timeline {
    display: flex;
    justify-content: space-between;
    margin: 10px 0;
    position: relative;
}

.step-timeline::before {
    content: "";
    position: absolute;
    top: 10px;
    left: 0;
    right: 0;
    height: 2px;
    background-color: var(--border-color);
    z-index: 1;
}

.timeline-node {
    position: relative;
    z-index: 2;
    text-align: center;
    width: 18%;
}

.node-circle {
    width: 22px;
    height: 22px;
    border-radius: 50%;
    background-color: var(--bg-card);
    border: 2px solid var(--accent);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    color: var(--accent);
    margin: 0 auto 4px auto;
    font-size: 7.5pt;
}

.timeline-node.completed .node-circle {
    background-color: var(--accent);
    color: #ffffff;
}

.node-text {
    font-size: 7pt;
    font-weight: 600;
    line-height: 1.25;
}

.product-spec-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
    margin: 6px 0;
}

.product-spec-card {
    background: #fafafb;
    border: 1px solid var(--border-color);
    border-radius: 4px;
    padding: 6px;
}

.product-spec-header {
    font-weight: 700;
    font-size: 8pt;
    color: var(--primary);
    border-bottom: 2px solid var(--accent);
    padding-bottom: 2px;
    margin-bottom: 4px;
}

.product-spec-item {
    font-size: 7pt;
    display: flex;
    justify-content: space-between;
    margin-bottom: 2px;
}

.product-spec-item span:first-child { color: var(--text-muted); }
.product-spec-item span:last-child { font-weight: 600; }

.org-chart {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    margin: 10px 0;
    position: relative;
}

.org-level {
    display: flex;
    justify-content: center;
    gap: 12px;
    width: 100%;
}

.org-box {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    border-top: 4px solid var(--primary);
    padding: 8px;
    border-radius: 4px;
    text-align: center;
    width: 48%;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.org-box.accent { border-top-color: var(--accent); }
.org-box.gold { border-top-color: var(--gold); }

.org-title {
    font-weight: 800;
    font-size: 8.5pt;
    color: var(--primary);
    margin-bottom: 3px;
}

.org-desc {
    font-size: 7.2pt;
    color: var(--text-muted);
    line-height: 1.35;
}

/* SVGs and Icons */
.svg-icon {
    vertical-align: middle;
}
"""

print("CSS variables defined successfully")
