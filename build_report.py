# -*- coding: utf-8 -*-
import sys

# Define CSS styles for A4 Portrait Simulation with updated Premium Corporate Visual Identity
CSS_STYLES = """
:root {
    --primary: #1a1a1a;       /* Charcoal Black - Primary Corporate */
    --primary-light: #2d2d2d; /* Medium Charcoal */
    --accent: #ff9900;        /* Warm Amazon-Style Orange - Primary Accent */
    --accent-light: #fff7ed;  /* Super Soft Orange Tint for Highlights */
    --secondary: #800020;     /* Elegant Burgundy - Secondary Accent (Alerts/Notices) */
    --secondary-light: #fff1f2; /* Soft Burgundy Tint */
    --success: #10b981;       /* Emerald Green */
    --success-light: #d1fae5; /* Soft Emerald Tint */
    --danger: #ef4444;        /* Coral Red */
    --danger-light: #fee2e2;  /* Coral Tint */
    --bg-base: #fcfcfc;       /* Premium Clean Off-White */
    --bg-card: #ffffff;       /* Pure White for Page Backgrounds */
    --text-dark: #1a1a1a;     /* Dark Charcoal Text for Ultimate Readability */
    --text-muted: #555555;    /* Sophisticated Gray for Subtext */
    --border-color: #cccccc;  /* Clear Visible Borders for Printing */
    --font-main: 'Cairo', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

@page {
    size: A4 portrait;
    margin: 0;
}

@media print {
    body {
        background-color: #ffffff;
        color: #1a1a1a;
        font-size: 10pt;
        line-height: 1.5;
    }
    .page-container {
        width: 210mm;
        height: 297mm;
        margin: 0 !important;
        padding: 10mm 15mm 10mm 15mm !important; /* Expanded margins for premium print layout */
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
        padding: 10mm 15mm 10mm 15mm; /* Expanded margins for premium screen layout */
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.15);
        border-radius: 8px;
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
    line-height: 1.55; /* Increased line spacing */
    background-color: var(--bg-base);
    text-align: right;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}

h1 {
    font-size: 14pt; /* Increased font size */
    border-bottom: 3px solid var(--accent);
    padding-bottom: 5px;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
    color: var(--primary);
    font-weight: 800;
}

h2 {
    font-size: 11pt; /* Increased font size */
    border-right: 4px solid var(--accent); /* Consistent orange accents */
    padding-right: 8px;
    margin-top: 14px;
    margin-bottom: 8px;
    background-color: #fdfdfd;
    padding-top: 3px;
    padding-bottom: 3px;
    color: var(--primary);
    font-weight: 800;
}

h3 {
    font-size: 10pt;
    color: var(--accent);
    margin-top: 8px;
    margin-bottom: 4px;
    font-weight: 800;
}

p {
    margin-bottom: 10px; /* Increased paragraph spacing */
    text-align: justify;
    color: #2c2c2c; /* More visible text */
    font-size: 9.5pt; /* Increased font size */
    line-height: 1.6;
}

.doc-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 5px;
    margin-bottom: 10px;
    height: 8mm;
}

.doc-header .logo-area {
    display: flex;
    align-items: center;
    gap: 6px;
}

.doc-header .logo-text {
    font-weight: 900;
    font-size: 11pt;
    color: var(--primary);
}

.doc-header .logo-text span {
    color: var(--accent);
}

.doc-header .meta-info {
    font-size: 8pt;
    color: var(--text-muted);
    font-weight: 600;
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
    padding-top: 5px;
    font-size: 8pt;
    color: var(--text-dark);
    height: 6mm;
}

.page-content {
    height: 257mm; /* Adjusted to balance larger text and expanded paddings */
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
    font-size: 25pt; /* Increased for impact */
    font-weight: 900;
    color: var(--primary);
    line-height: 1.4;
    margin-bottom: 15px;
}

.cover-title-main span {
    color: var(--accent);
}

.cover-subtitle {
    font-size: 12pt;
    color: var(--text-muted);
    font-weight: 600;
    margin-bottom: 25px;
    line-height: 1.6;
}

.cover-divider {
    width: 120px;
    height: 6px;
    background: linear-gradient(to left, var(--accent), var(--accent));
    margin-bottom: 25px;
    border-radius: 3px;
}

.cover-meta-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
    text-align: right;
    background-color: #fafafa;
    border: 1.5px solid var(--border-color);
    padding: 20px;
    border-radius: 8px;
    margin-top: 15px;
}

.meta-item {
    font-size: 9.5pt;
}

.meta-item strong {
    color: var(--primary);
    display: block;
    margin-bottom: 4px;
    font-size: 10pt;
}

.meta-item span {
    color: var(--text-dark);
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0; /* Increased margin */
    font-size: 9pt; /* Increased from 7.5pt for perfect readability */
    background-color: var(--bg-card);
    border: 1.5px solid var(--border-color);
}

th, td {
    padding: 6px 10px; /* Greatly expanded padding for comfortable layout */
    text-align: right;
    border-bottom: 1.5px solid var(--border-color);
    line-height: 1.45;
}

th {
    background-color: var(--primary);
    color: #ffffff;
    font-weight: 800;
    font-size: 9.5pt;
    border-left: 1.5px solid #334155;
}

tr:nth-child(even) td {
    background-color: #fcfcfc;
}

.table-total {
    font-weight: 900;
    background-color: #e2e8f0 !important;
    border-top: 2px solid var(--primary);
    color: var(--primary);
}

.kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
    margin: 10px 0;
}

.kpi-card {
    background-color: var(--bg-card);
    border: 1.5px solid var(--border-color);
    border-top: 3.5px solid var(--accent); /* Amazon Orange */
    padding: 8px 10px;
    border-radius: 5px;
    text-align: center;
}

.kpi-title {
    font-size: 8pt;
    color: var(--text-muted);
    margin-bottom: 3px;
    font-weight: 700;
}

.kpi-value {
    font-size: 11pt;
    font-weight: 900;
    color: var(--primary);
}

.kpi-unit {
    font-size: 8pt;
    color: var(--text-muted);
}

.kpi-card.gold { border-top-color: var(--accent); }
.kpi-card.success { border-top-color: var(--success); }
.kpi-card.danger { border-top-color: var(--danger); }

.info-callout {
    background-color: var(--accent-light);
    border-right: 4px solid var(--accent);
    padding: 8px 12px;
    border-radius: 0 6px 6px 0;
    margin: 8px 0;
    font-size: 9pt;
}

.info-callout h5 {
    color: var(--primary);
    margin-bottom: 3px;
    font-weight: 800;
    font-size: 9.5pt;
}

.gold-callout {
    background-color: var(--accent-light);
    border-right: 4px solid var(--accent);
    padding: 8px 12px;
    border-radius: 0 6px 6px 0;
    margin: 8px 0;
    font-size: 9pt;
}

.gold-callout h5 {
    color: var(--primary);
    margin-bottom: 3px;
    font-weight: 800;
    font-size: 9.5pt;
}

.danger-callout {
    background-color: var(--secondary-light); /* Styled as elegant Burgundy tint */
    border-right: 4px solid var(--secondary);
    padding: 8px 12px;
    border-radius: 0 6px 6px 0;
    margin: 8px 0;
    font-size: 9pt;
}

.danger-callout h5 {
    color: var(--secondary);
    margin-bottom: 3px;
    font-weight: 800;
    font-size: 9.5pt;
}

.grid-2 {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
    margin: 10px 0;
}

.grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    margin: 10px 0;
}

.card-box {
    background-color: var(--bg-card);
    border: 1.5px solid var(--border-color);
    padding: 8px 10px;
    border-radius: 5px;
}

.card-box h4 {
    color: var(--primary);
    font-size: 9.5pt;
    margin-bottom: 4px;
    border-bottom: 1.5px solid var(--border-color);
    padding-bottom: 3px;
    font-weight: 800;
}

.card-box p {
    font-size: 8.5pt;
    margin-bottom: 0;
}

/* Priority badges with clear bold design */
.badge-success {
    background-color: var(--success-light);
    color: var(--success);
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: 800;
    font-size: 7.5pt;
    white-space: nowrap;
    display: inline-block;
}

.badge-gold {
    background-color: var(--accent-light);
    color: var(--accent);
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: 800;
    font-size: 7.5pt;
    white-space: nowrap;
    display: inline-block;
}

.badge-accent {
    background-color: var(--accent-light);
    color: var(--accent);
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: 800;
    font-size: 7.5pt;
    white-space: nowrap;
    display: inline-block;
}

.step-timeline {
    display: flex;
    justify-content: space-between;
    margin: 15px 0;
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
    width: 24%;
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
    font-weight: 800;
    color: var(--accent);
    margin: 0 auto 5px auto;
    font-size: 8pt;
}

.timeline-node.completed .node-circle {
    background-color: var(--accent);
    color: #ffffff;
}

.node-text {
    font-size: 7.5pt;
    font-weight: 700;
    line-height: 1.35;
}

/* Custom Write-In / Spacious fields for handwriting */
.custom-write-line {
    border-bottom: 1.5px solid var(--primary);
    display: inline-block;
    height: 24px;
    margin: 0 6px;
    vertical-align: bottom;
}
.custom-form-group {
    margin-bottom: 16px; /* Increased vertical spacing between fields */
    display: flex;
    align-items: center;
}
.custom-form-label {
    font-weight: 800;
    color: var(--primary);
    white-space: nowrap;
    font-size: 9.5pt; /* Enlarged label text */
}
.custom-form-input {
    flex-grow: 1;
    border-bottom: 2.2px solid var(--primary); /* Robust writing lines */
    margin-right: 8px;
    height: 28px; /* Significantly expanded handwriting area height */
}
.dashed-stamp-box {
    border: 2px dashed var(--accent);
    border-radius: 50%;
    width: 70px; /* Enlarged stamp circle */
    height: 70px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--accent);
    font-size: 7pt;
    font-weight: bold;
    text-align: center;
    line-height: 1.2;
    margin: 4px auto;
}
.legal-section-title {
    font-size: 10pt;
    font-weight: 800;
    color: var(--primary);
    border-right: 3.5px solid var(--accent);
    padding-right: 8px;
    margin-top: 16px;
    margin-bottom: 8px;
    background-color: var(--accent-light);
    padding-top: 3px;
    padding-bottom: 3px;
}
"""

print("CSS styles defined successfully in build_report.py")
