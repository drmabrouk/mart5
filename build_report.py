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
        font-size: 8.5pt;
        line-height: 1.4;
    }
    .page-container {
        width: 210mm;
        height: 297mm;
        margin: 0 !important;
        padding: 8mm 12mm 8mm 12mm !important;
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
        padding: 20px 0;
    }
    .page-container {
        width: 210mm;
        height: 297mm;
        margin: 0 auto 20px auto;
        background-color: var(--bg-card);
        padding: 8mm 12mm 8mm 12mm;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
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
    line-height: 1.4;
    background-color: var(--bg-base);
    text-align: right;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}

h1 {
    font-size: 13pt;
    border-bottom: 2.5px solid var(--accent);
    padding-bottom: 3px;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 6px;
    color: var(--primary);
    font-weight: 800;
}

h2 {
    font-size: 10pt;
    border-right: 3.5px solid var(--gold);
    padding-right: 6px;
    margin-top: 8px;
    margin-bottom: 4px;
    background-color: #f8fafc;
    padding-top: 1.5px;
    padding-bottom: 1.5px;
    color: var(--primary);
    font-weight: 700;
}

h3 {
    font-size: 9pt;
    color: var(--accent);
    margin-top: 5px;
    margin-bottom: 3px;
    font-weight: 700;
}

p {
    margin-bottom: 5px;
    text-align: justify;
    color: #334155;
    font-size: 8pt;
    line-height: 1.4;
}

.doc-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 3px;
    margin-bottom: 6px;
    height: 7mm;
}

.doc-header .logo-area {
    display: flex;
    align-items: center;
    gap: 4px;
}

.doc-header .logo-text {
    font-weight: 800;
    font-size: 9.5pt;
    color: var(--primary);
}

.doc-header .logo-text span {
    color: var(--accent);
}

.doc-header .meta-info {
    font-size: 7pt;
    color: var(--text-muted);
}

.doc-footer {
    position: absolute;
    bottom: 6mm;
    left: 12mm;
    right: 12mm;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid var(--border-color);
    padding-top: 3px;
    font-size: 7pt;
    color: var(--text-muted);
    height: 5mm;
}

.page-content {
    height: 265mm;
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
    font-size: 21pt;
    font-weight: 900;
    color: var(--primary);
    line-height: 1.3;
    margin-bottom: 8px;
}

.cover-title-main span {
    color: var(--accent);
}

.cover-subtitle {
    font-size: 10pt;
    color: var(--text-muted);
    font-weight: 500;
    margin-bottom: 15px;
    line-height: 1.45;
}

.cover-divider {
    width: 100px;
    height: 4px;
    background: linear-gradient(to left, var(--accent), var(--gold));
    margin-bottom: 15px;
    border-radius: 2px;
}

.cover-meta-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
    text-align: right;
    background-color: var(--bg-base);
    border: 1px solid var(--border-color);
    padding: 14px;
    border-radius: 5px;
    margin-top: 8px;
}

.meta-item {
    font-size: 7.8pt;
}

.meta-item strong {
    color: var(--primary);
    display: block;
    margin-bottom: 2px;
    font-size: 8pt;
}

.meta-item span {
    color: var(--text-muted);
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 5px 0;
    font-size: 7.5pt;
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
}

th, td {
    padding: 3px 5px;
    text-align: right;
    border-bottom: 1px solid var(--border-color);
    line-height: 1.3;
}

th {
    background-color: var(--primary);
    color: #ffffff;
    font-weight: 700;
    font-size: 7.8pt;
    border-left: 1px solid #334155;
}

tr:nth-child(even) td {
    background-color: #f8fafc;
}

.table-total {
    font-weight: 800;
    background-color: #cbd5e1 !important;
    border-top: 1.5px solid var(--primary);
    color: var(--primary);
}

.kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 6px;
    margin: 5px 0;
}

.kpi-card {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    border-top: 2.5px solid var(--accent);
    padding: 4px 6px;
    border-radius: 3px;
    text-align: center;
}

.kpi-title {
    font-size: 6.8pt;
    color: var(--text-muted);
    margin-bottom: 1px;
    font-weight: 600;
}

.kpi-value {
    font-size: 9.5pt;
    font-weight: 800;
    color: var(--primary);
}

.kpi-unit {
    font-size: 6.8pt;
    color: var(--text-muted);
}

.kpi-card.gold { border-top-color: var(--gold); }
.kpi-card.success { border-top-color: var(--success); }
.kpi-card.danger { border-top-color: var(--danger); }

.info-callout {
    background-color: #f0f9ff;
    border-right: 3.5px solid var(--accent);
    padding: 4px 6px;
    border-radius: 0 3px 3px 0;
    margin: 4px 0;
    font-size: 7.8pt;
}

.info-callout h5 {
    color: var(--accent);
    margin-bottom: 1px;
    font-weight: 700;
    font-size: 8pt;
}

.gold-callout {
    background-color: #fffbeb;
    border-right: 3.5px solid var(--gold);
    padding: 4px 6px;
    border-radius: 0 3px 3px 0;
    margin: 4px 0;
    font-size: 7.8pt;
}

.gold-callout h5 {
    color: var(--gold);
    margin-bottom: 1px;
    font-weight: 700;
    font-size: 8pt;
}

.danger-callout {
    background-color: #fef2f2;
    border-right: 3.5px solid var(--danger);
    padding: 4px 6px;
    border-radius: 0 3px 3px 0;
    margin: 4px 0;
    font-size: 7.8pt;
}

.danger-callout h5 {
    color: var(--danger);
    margin-bottom: 1px;
    font-weight: 700;
    font-size: 8pt;
}

.grid-2 {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 8px;
    margin: 5px 0;
}

.grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 6px;
    margin: 5px 0;
}

.card-box {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 4px 6px;
    border-radius: 3px;
}

.card-box h4 {
    color: var(--primary);
    font-size: 8pt;
    margin-bottom: 1px;
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 1px;
    font-weight: 700;
}

.card-box p {
    font-size: 7.5pt;
    margin-bottom: 0;
}

/* Priority badge modifications as requested to avoid wrapping and fit on one line */
.badge-success {
    background-color: var(--success-light);
    color: var(--success);
    padding: 1px 3px;
    border-radius: 3px;
    font-weight: 700;
    font-size: 6.5pt;
    white-space: nowrap;
    display: inline-block;
}

.badge-gold {
    background-color: var(--gold-light);
    color: var(--gold);
    padding: 1px 3px;
    border-radius: 3px;
    font-weight: 700;
    font-size: 6.5pt;
    white-space: nowrap;
    display: inline-block;
}

.badge-accent {
    background-color: var(--accent-light);
    color: var(--accent);
    padding: 1px 3px;
    border-radius: 3px;
    font-weight: 700;
    font-size: 6.5pt;
    white-space: nowrap;
    display: inline-block;
}

.step-timeline {
    display: flex;
    justify-content: space-between;
    margin: 8px 0;
    position: relative;
}

.step-timeline::before {
    content: "";
    position: absolute;
    top: 8px;
    left: 0;
    right: 0;
    height: 1.5px;
    background-color: var(--border-color);
    z-index: 1;
}

.timeline-node {
    position: relative;
    z-index: 2;
    text-align: center;
    width: 22%;
}

.node-circle {
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background-color: var(--bg-card);
    border: 1.5px solid var(--accent);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    color: var(--accent);
    margin: 0 auto 3px auto;
    font-size: 7pt;
}

.timeline-node.completed .node-circle {
    background-color: var(--accent);
    color: #ffffff;
}

.node-text {
    font-size: 6.5pt;
    font-weight: 600;
    line-height: 1.2;
}

.product-spec-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 6px;
    margin: 5px 0;
}

.product-spec-card {
    background: #fafafb;
    border: 1px solid var(--border-color);
    border-radius: 3px;
    padding: 4px 6px;
}

.product-spec-header {
    font-weight: 700;
    font-size: 7.5pt;
    color: var(--primary);
    border-bottom: 1.5px solid var(--accent);
    padding-bottom: 1px;
    margin-bottom: 3px;
}

.product-spec-item {
    font-size: 6.8pt;
    display: flex;
    justify-content: space-between;
    margin-bottom: 1.5px;
}

.product-spec-item span:first-child { color: var(--text-muted); }
.product-spec-item span:last-child { font-weight: 600; }

.org-chart {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
    margin: 8px 0;
    position: relative;
}

.org-level {
    display: flex;
    justify-content: center;
    gap: 10px;
    width: 100%;
}

.org-box {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    border-top: 3px solid var(--primary);
    padding: 6px;
    border-radius: 3px;
    text-align: center;
    width: 48%;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}

.org-box.accent { border-top-color: var(--accent); }
.org-box.gold { border-top-color: var(--gold); }

.org-title {
    font-weight: 800;
    font-size: 8pt;
    color: var(--primary);
    margin-bottom: 2px;
}

.org-desc {
    font-size: 7pt;
    color: var(--text-muted);
    line-height: 1.3;
}

/* Printable legal styles */
.print-field {
    border-bottom: 1px dashed #475569;
    display: inline-block;
    min-width: 150px;
    height: 14px;
    margin: 0 4px;
}
.print-box {
    border: 1px dashed #64748b;
    background-color: #fdfdfd;
    padding: 6px;
    margin: 4px 0;
    border-radius: 3px;
    font-size: 7.5pt;
}
.print-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 6px;
    margin: 4px 0;
}
.print-title {
    font-size: 8.5pt;
    font-weight: bold;
    color: var(--primary);
    margin-bottom: 3px;
    border-bottom: 1px solid var(--accent);
    padding-bottom: 2px;
}
"""

print("CSS variables defined successfully")
