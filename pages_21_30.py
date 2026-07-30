# -*- coding: utf-8 -*-
import sys

# Define Pages 22 to 28 for Martdia Trading & Distribution Co. (L.L.C.)
PAGES_CONTENT_21_30 = {}

# Helper function to generate clean contract layouts with simple Date and beautiful spacious writing lines.
def get_contract_page_wrapper(title_ar, doc_num, body_html, footer_html):
    return f"""
<div style="height: 100%; display: flex; flex-direction: column; justify-content: space-between; font-family: 'Cairo', sans-serif;">
    <div style="flex-grow: 1;">
        <!-- Legal Warning Notice at the very top -->
        <div class="legal-warning-notice">إن أي كشط أو تعديل في هذا المستند باليد دون توقيع وإقرار الشركاء الأربعة مجتمعين يلغيه تماماً ويجعله باطلاً قانوناً وبدون أي أثر.</div>

        <!-- Top Simple Header -->
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #0f172a; padding-bottom: 4px; margin-bottom: 12px;">
            <div style="font-size: 9.5pt; font-weight: 800; color: #0f172a;">مجموعة المستندات التشغيلية والقانونية - شركة مارتديا للتجارة والتوزيع</div>
            <div style="font-size: 8.5pt; color: #64748b; font-weight: bold;">وثيقة رقم: {doc_num} / 12</div>
        </div>

        <!-- Document Date & Reference with clean underline fields -->
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <div style="font-size: 9pt; color: #1e293b; font-weight: bold; display: flex; align-items: center; width: 60%;">
                <span class="custom-form-label">تاريخ المستند:</span>
                <span class="custom-form-input" style="width: 150px;"></span>
            </div>
            <div style="font-size: 9pt; color: #1e293b; font-weight: bold; display: flex; align-items: center; width: 35%; justify-content: flex-end;">
                <span class="custom-form-label" style="margin-left: 6px;">الرقم المرجعي:</span>
                <span style="font-family: monospace; font-size: 9.5pt; color: #0284c7; font-weight: bold;">MT-DOC-{doc_num:02d}</span>
            </div>
        </div>

        <!-- Document Title -->
        <div style="text-align: center; margin: 10px 0 8px 0; padding: 5px; background-color: #f1f5f9; border: 1.5px solid #0f172a; border-radius: 4px;">
            <h2 style="font-size: 10.5pt; font-weight: 800; color: #0f172a; border: none; background: transparent; padding: 0; margin: 0; text-align: center;">{title_ar}</h2>
        </div>

        <!-- Document Body -->
        <div style="font-size: 8.2pt; line-height: 1.45; color: #1e293b; text-align: justify; margin-bottom: 10px;">
            {body_html}
        </div>
    </div>

    <!-- Signatures and footer -->
    <div>
        {footer_html}
    </div>
</div>
"""

# ----------------- PAGE 22: Document 6 - Company Asset Custody Agreement -----------------
doc_6_body = """
<p style="margin-bottom: 8px;">بموجب هذه الاتفاقية الرسمية، يقر الموظف / الطرف الموقّع أدناه باستلام الأصول والأدوات التقنية واللوجستية التالية كعهدة عينية شخصية في ذمته المالية، ويتعهد بالحفاظ التام عليها وإعادتها فوراً للشركة بنفس الحالة الفنية عند طلبها أو عند إنهاء العمل:</p>

<div class="custom-form-group">
    <span class="custom-form-label">الاسم الكامل للموظف المستلم للعهدة:</span>
    <span class="custom-form-input"></span>
</div>
<div class="custom-form-group">
    <span class="custom-form-label">رقم بطاقة الرقم القومي للموظف:</span>
    <span class="custom-form-input" style="width: 250px;"></span>
    <span class="custom-form-label" style="margin-right: 15px;">الوظيفة الحالية بالمستودع:</span>
    <span class="custom-form-input"></span>
</div>

<div class="legal-section-title" style="margin-top: 10px;">جدول تفصيل الأصول والمعدات المسلمة عهدة فنية وميدانية</div>
<table style="width: 100%; border-collapse: collapse; margin: 8px 0; font-size: 7.2pt;">
    <thead>
        <tr style="background-color: #0f172a; color: white;">
            <th style="padding: 4px; border: 1px solid #cbd5e1; width: 35%; text-align: right;">الأصل المسلم عهدة</th>
            <th style="padding: 4px; border: 1px solid #cbd5e1; width: 15%; text-align: right;">الكمية</th>
            <th style="padding: 4px; border: 1px solid #cbd5e1; width: 25%; text-align: right;">الرقم التسلسلي / الموديل</th>
            <th style="padding: 4px; border: 1px solid #cbd5e1; width: 25%; text-align: right;">توقيع المستلم بالاستلام الفعلي</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="padding: 4px; border: 1px solid #cbd5e1; font-weight: bold;">1. قارئ الباركود اللاسلكي (Barcode Scanner)</td>
            <td style="padding: 4px; border: 1px solid #cbd5e1;">عدد ...........</td>
            <td style="padding: 4px; border: 1px solid #cbd5e1;">.....................................</td>
            <td style="padding: 4px; border: 1px solid #cbd5e1;">.....................................</td>
        </tr>
        <tr>
            <td style="padding: 4px; border: 1px solid #cbd5e1; font-weight: bold;">2. جهاز حاسوب مركزي وإدارة الـ POS</td>
            <td style="padding: 4px; border: 1px solid #cbd5e1;">عدد ...........</td>
            <td style="padding: 4px; border: 1px solid #cbd5e1;">.....................................</td>
            <td style="padding: 4px; border: 1px solid #cbd5e1;">.....................................</td>
        </tr>
        <tr>
            <td style="padding: 4px; border: 1px solid #cbd5e1; font-weight: bold;">3. كاميرات مراقبة IP عالية الدقة</td>
            <td style="padding: 4px; border: 1px solid #cbd5e1;">عدد ...........</td>
            <td style="padding: 4px; border: 1px solid #cbd5e1;">.....................................</td>
            <td style="padding: 4px; border: 1px solid #cbd5e1;">.....................................</td>
        </tr>
        <tr>
            <td style="padding: 4px; border: 1px solid #cbd5e1; font-weight: bold;">4. راوتر شبكات ذكي وأجهزة الربط</td>
            <td style="padding: 4px; border: 1px solid #cbd5e1;">عدد ...........</td>
            <td style="padding: 4px; border: 1px solid #cbd5e1;">.....................................</td>
            <td style="padding: 4px; border: 1px solid #cbd5e1;">.....................................</td>
        </tr>
        <tr>
            <td style="padding: 4px; border: 1px solid #cbd5e1; font-weight: bold;">5. أرفف تخزين معدنية ثقيلة (Shelving)</td>
            <td style="padding: 4px; border: 1px solid #cbd5e1;">عدد ...........</td>
            <td style="padding: 4px; border: 1px solid #cbd5e1;">.....................................</td>
            <td style="padding: 4px; border: 1px solid #cbd5e1;">.....................................</td>
        </tr>
        <tr>
            <td style="padding: 4px; border: 1px solid #cbd5e1; font-weight: bold;">6. طبالي رص بلاستيكية / خشبية (Pallets)</td>
            <td style="padding: 4px; border: 1px solid #cbd5e1;">عدد ...........</td>
            <td style="padding: 4px; border: 1px solid #cbd5e1;">.....................................</td>
            <td style="padding: 4px; border: 1px solid #cbd5e1;">.....................................</td>
        </tr>
    </tbody>
</table>
"""

doc_6_footer = """
<div style="display: grid; grid-template-columns: 1fr 1fr 80px; gap: 15px; margin-top: 10px; border-top: 1.5px solid #0f172a; padding-top: 8px;">
    <div style="border: 1px dashed #cbd5e1; padding: 6px; text-align: right; border-radius: 4px; height: 30mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8.5pt; font-weight: bold; color: #0f172a; border-bottom: 1px solid #cbd5e1; padding-bottom: 2px;">إقرارات وتوقيع الموظف المستلم</div>
        <div style="font-size: 7.5pt; line-height: 1.5;">
            الاسم الكامل: .....................................................<br>
            التوقيع: ................................................
        </div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 6px; text-align: right; border-radius: 4px; height: 30mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8.5pt; font-weight: bold; color: #0284c7; border-bottom: 1px solid #0284c7; padding-bottom: 2px;">عن إدارة المستودعات والشركة المانحة</div>
        <div style="font-size: 7.5pt; line-height: 1.5;">
            الاسم: محمد وليد حمودة (مدير العمليات)<br>
            التوقيع والاعتماد: ................................................
        </div>
    </div>
    <div style="display: flex; align-items: center; justify-content: center;">
        <div class="dashed-stamp-box"></div>
    </div>
</div>
"""

PAGES_CONTENT_21_30[22] = get_contract_page_wrapper(
    "6. إقرار واتفاقية استلام عهدة أصول ومعدات الشركة العينية",
    6,
    doc_6_body,
    doc_6_footer
)


# ----------------- PAGE 23: Document 7 - Operational Expense Request Form -----------------
doc_7_body = """
<p style="margin-bottom: 8px;">تستخدم هذه الاستمارة لطلب واعتماد صرف مبالغ النقدية (كاش) لتغطية النفقات والمصاريف التشغيلية الطارئة والدورية للمستودعات ومواقع العمل الميداني:</p>

<div class="custom-form-group">
    <span class="custom-form-label">اسم طالب الصرف الميداني:</span>
    <span class="custom-form-input"></span>
</div>
<p style="margin-bottom: 6px;">المستودع المعني بالصرف: [  ] مستودع طوخ الأقلام   [  ] مستودع ميت خميس (المنصورة)</p>

<table style="width: 100%; border-collapse: collapse; margin: 8px 0; font-size: 7.5pt;">
    <thead>
        <tr style="background-color: #0f172a; color: white;">
            <th style="padding: 6px; border: 1px solid #cbd5e1; width: 40%; text-align: right;">بند النفقة التشغيلية المطلوبة</th>
            <th style="padding: 6px; border: 1px solid #cbd5e1; width: 25%; text-align: right;">القيمة التقريبية (ج.م)</th>
            <th style="padding: 6px; border: 1px solid #cbd5e1; width: 35%; text-align: right;">البيان والملاحظات والمستند المرفق</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="padding: 6px; border: 1px solid #cbd5e1; font-weight: bold;">1. اشتراك الإنترنت والشبكة السريعة</td>
            <td style="padding: 6px; border: 1px solid #cbd5e1;">...................................................</td>
            <td style="padding: 6px; border: 1px solid #cbd5e1;">...................................................</td>
        </tr>
        <tr>
            <td style="padding: 6px; border: 1px solid #cbd5e1; font-weight: bold;">2. استهلاك الكهرباء والخدمات الطاقية</td>
            <td style="padding: 6px; border: 1px solid #cbd5e1;">...................................................</td>
            <td style="padding: 6px; border: 1px solid #cbd5e1;">...................................................</td>
        </tr>
        <tr>
            <td style="padding: 6px; border: 1px solid #cbd5e1; font-weight: bold;">3. خدمات النظافة والتعقيم الدوري</td>
            <td style="padding: 6px; border: 1px solid #cbd5e1;">...................................................</td>
            <td style="padding: 6px; border: 1px solid #cbd5e1;">...................................................</td>
        </tr>
        <tr>
            <td style="padding: 6px; border: 1px solid #cbd5e1; font-weight: bold;">4. صيانة طارئة للأرفف أو الباركود</td>
            <td style="padding: 6px; border: 1px solid #cbd5e1;">...................................................</td>
            <td style="padding: 6px; border: 1px solid #cbd5e1;">...................................................</td>
        </tr>
        <tr style="background-color: #f1f5f9; font-weight: bold;">
            <td style="padding: 6px; border: 1px solid #cbd5e1;">إجمالي المبلغ المطلوب كاش للصرف</td>
            <td style="padding: 6px; border: 1px solid #cbd5e1;" colspan="2">........................................................................................................................ جنيه مصري.</td>
        </tr>
    </tbody>
</table>

<div class="legal-section-title" style="margin-top: 8px;">تعهد ومطابقة إحضار الفواتير الأصلية</div>
<p style="font-size: 7.8pt; line-height: 1.4; color: #475569;">
يتعهد طالب الصرف بإحضار وتسليم الفواتير الضريبية والإيصالات الرسمية لمطابقة القيد المالي المحاسبي بالدفاتر في موعد أقصاه 72 ساعة فقط من تاريخ الاستلام الفعلي للكاش، ويتحمل كامل المسؤولية المالية في حال التقصير.
</p>
"""

doc_7_footer = """
<div style="display: grid; grid-template-columns: repeat(3, 1fr) 70px; gap: 8px; margin-top: 10px; border-top: 1.5px solid #0f172a; padding-top: 8px;">
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: right; border-radius: 4px; height: 28mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8pt; font-weight: bold; color: #0f172a; border-bottom: 1px solid #cbd5e1; padding-bottom: 1px;">توقيع مقدم الطلب</div>
        <div style="font-size: 7.2pt; line-height: 1.3;">
            الاسم: .............................<br>
            التوقيع: ...........................
        </div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: right; border-radius: 4px; height: 28mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8pt; font-weight: bold; color: #0284c7; border-bottom: 1px solid #0284c7; padding-bottom: 1px;">رأي ومراجعة الحسابات</div>
        <div style="font-size: 7.2pt; line-height: 1.3;">
            البيان: [  ] مطابق للموازنة<br>
            التوقيع: ...........................
        </div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: right; border-radius: 4px; height: 28mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8pt; font-weight: bold; color: #b45309; border-bottom: 1px solid #b45309; padding-bottom: 1px;">اعتماد المدير المالي</div>
        <div style="font-size: 7.2pt; line-height: 1.3;">
            الاسم: محمد مبروك<br>
            التوقيع: ...........................
        </div>
    </div>
    <div style="display: flex; align-items: center; justify-content: center;">
        <div class="dashed-stamp-box" style="margin: 0; width: 52px; height: 52px;"></div>
    </div>
</div>
"""

PAGES_CONTENT_21_30[23] = get_contract_page_wrapper(
    "7. استمارة طلب واعتماد النفقات والمصاريف التشغيلية للمستودع",
    7,
    doc_7_body,
    doc_7_footer
)


# ----------------- PAGE 24: Document 8 - Terms and Conditions Acknowledgement -----------------
doc_8_body = """
<p style="margin-bottom: 8px;">يتعهد ويقر الموقّع أدناه (سواء كان شريكاً، مديراً، أو موظفاً) بالالتزام التام والكامل بكافة السياسات، الشروط، الأحكام، ومواثيق العمل المعتمدة باللائحة الداخلية لشركة <strong>مارتديا للتجارة والتوزيع ذ.م.م</strong> ومستودعاتها، والموضحة كالتالي:</p>

<div class="legal-section-title" style="margin-top: 8px;">أولاً: بنود الالتزام التشغيلي والمهني بمستودعات ومنصة مارتديا</div>
<p style="margin-bottom: 6px;">1. <strong>حوكمة الباركود الإلكتروني للسلع:</strong> يلتزم الموظف التزاماً صارماً بمسح الباركود الخاص بكل كرتونة أو صندوق سلع خارج من المستودع قبل مغادرته للبوابة بشكل ميكانيكي لضمان المطابقة اليومية الفورية للأرصدة.<br>
2. <strong>جودة وسلامة الغذاء والسلع:</strong> يتعهد طاقم العمل بالالتزام بفرز وفحص صلاحية السلع، ورص كراتين المياه والأجبان والزيت على الطبالي المرتفعة، والفصل التام للمنظفات عن المواد الغذائية لمنع انتشار الروائح والتلوث.<br>
3. <strong>الالتزام بإحداثيات وتتبع الـ GPS:</strong> يقر مندوب المبيعات والتوزيع بالتزامه بتأدية الزيارات للبقالات وتسجيل الطلبات من خلال النطاق الفعلي للبقالة بمسافة لا تزيد عن 20 متراً، ويمنع تسجيل أي طلبية وهمية خارج النطاق.</p>

<div class="legal-section-title" style="margin-top: 8px;">ثانياً: سرية المعلومات وحظر المنافسة وإفشاء البيانات</div>
<p style="margin-bottom: 6px;">يقر الموقّع بالسرية التامة لبيانات البقالات المشتركة بالمنصة، وأسعار الشراء والخصومات والبونص النقدي من شركات المنصورة وطنطا، ويحظر تماماً استخدام أو إفشاء أو نسخ هذه البيانات لتأسيس أي نشاط تجاري منافس تحت طائلة القانون الجنائي والشرط الجزائي البالغ 100,000 ج.م.</p>
"""

doc_8_footer = """
<div style="display: grid; grid-template-columns: 1fr 1fr 80px; gap: 15px; margin-top: 10px; border-top: 1.5px solid #0f172a; padding-top: 8px;">
    <div style="border: 1px dashed #cbd5e1; padding: 6px; text-align: right; border-radius: 4px; height: 30mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8.5pt; font-weight: bold; color: #0f172a; border-bottom: 1px solid #cbd5e1; padding-bottom: 2px;">توقيع وإقرار الموظف بالالتزام</div>
        <div style="font-size: 7.5pt; line-height: 1.5;">
            الاسم الكامل: .....................................................<br>
            رقم بطاقة الرقم القومي: ......................................................
        </div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 6px; text-align: right; border-radius: 4px; height: 30mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8.5pt; font-weight: bold; color: #0284c7; border-bottom: 1px solid #0284c7; padding-bottom: 2px;">المصادقة والاعتماد من مجلس الإدارة</div>
        <div style="font-size: 7.5pt; line-height: 1.5;">
            الممثّل المفوّض: ..........................................<br>
            التوقيع والختم: .................................................
        </div>
    </div>
    <div style="display: flex; align-items: center; justify-content: center;">
        <div class="dashed-stamp-box"></div>
    </div>
</div>
"""

PAGES_CONTENT_21_30[24] = get_contract_page_wrapper(
    "8. نموذج وإقرار الالتزام بالشروط والأحكام وسياسات العمل المعتمدة",
    8,
    doc_8_body,
    doc_8_footer
)


# ----------------- PAGE 25: Document 9 - Partner Withdrawal and Capital Recovery Request -----------------
doc_9_body = """
<p style="margin-bottom: 8px;">يقدم هذا الطلب رسمياً من الشريك الراغب في التخارج طواعية إلى مجلس إدارة شركة <strong>مارتديا للتجارة والتوزيع ذ.م.م</strong> ومستودعها، بموجب ميثاق التأسيس المعتمد وفترة الإخطار القانونية البالغة 90 يوماً:</p>

<div class="custom-form-group">
    <span class="custom-form-label">الاسم الكامل للشريك طالب الانسحاب:</span>
    <span class="custom-form-input"></span>
</div>
<div class="custom-form-group">
    <span class="custom-form-label">رقم بطاقة الرقم القومي للشريك:</span>
    <span class="custom-form-input" style="width: 250px;"></span>
    <span class="custom-form-label" style="margin-right: 15px;">الحصة الملكية:</span>
    <span class="custom-form-input" style="font-weight: bold; color: #0284c7;">25% حصرياً بالكامل</span>
</div>

<div class="legal-section-title" style="margin-top: 10px;">آلية استرداد وتصفية الحصة المالية والضوابط المحاسبية</div>
<p style="margin-bottom: 6px;">1. <strong>جرد وتدقيق مالي عاجل:</strong> يلتزم الشركاء بتشكيل لجنة جرد مالي وميداني فوري لكافة موجودات مستودعي طوخ الأقلام وميت خميس لتقييم السيولة والمخزون وحجم الأرباح والخسائر للشركة.<br>
2. <strong>سداد الديون التجارية أولاً:</strong> تخصم كافة الالتزامات والديون التجارية للموردين من قيمة الحصة قبل التسوية والوفاء بها.<br>
3. <strong>آلية التقسيط الآمن:</strong> تسدد الحصة المالية المستحقة للشريك المتخارج على أربع دفعات متساوية طوال عام مالي كامل لضمان استقرار التدفق المالي كاش لمستودعات مارتديا وعدم الإضرار بميزانية شراء المنتجات الغذائية الأساسية.</p>

<p style="font-size: 7.5pt; margin-top: 6px;">[  ] كشف حساب بنكي مسجل معتمد باسم الشريك طالب التخارج لتلقي التحويل المالي.<br>
[  ] إقرار حظر المنافسة وإفشاء أسرار المنصة والزيارات الميدانية للبقالات طوال 3 سنوات اللاحقة للتخارج.</p>
"""

doc_9_footer = """
<div style="display: grid; grid-template-columns: repeat(3, 1fr) 70px; gap: 8px; margin-top: 10px; border-top: 1.5px solid #0f172a; padding-top: 8px;">
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: right; border-radius: 4px; height: 30mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8pt; font-weight: bold; color: #0f172a; border-bottom: 1px solid #cbd5e1; padding-bottom: 1px;">توقيع الشريك طالب الانسحاب</div>
        <div style="font-size: 7.2pt; line-height: 1.3;">
            الاسم: .............................<br>
            التوقيع: ...........................
        </div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: right; border-radius: 4px; height: 30mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8pt; font-weight: bold; color: #0284c7; border-bottom: 1px solid #0284c7; padding-bottom: 1px;">موافقات الشركاء الثلاثة</div>
        <div style="font-size: 7.2pt; line-height: 1.3;">
            القرار: [  ] موافقة  [  ] تأجيل للجرد<br>
            التواقيع: ...........................
        </div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: right; border-radius: 4px; height: 30mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8pt; font-weight: bold; color: #b45309; border-bottom: 1px solid #b45309; padding-bottom: 1px;">اعتماد المدير المالي</div>
        <div style="font-size: 7.2pt; line-height: 1.3;">
            الاسم: محمد مبروك<br>
            التوقيع والختم: ...................
        </div>
    </div>
    <div style="display: flex; align-items: center; justify-content: center;">
        <div class="dashed-stamp-box" style="margin: 0; width: 52px; height: 52px;"></div>
    </div>
</div>
"""

PAGES_CONTENT_21_30[25] = get_contract_page_wrapper(
    "9. طلب انسحاب وتخارج شريك واسترداد الحصة التأسيسية كاش",
    9,
    doc_9_body,
    doc_9_footer
)


# ----------------- PAGE 26: Document 10 - Official Warning Notice -----------------
doc_10_body = """
<p style="margin-bottom: 8px;">يوجه هذا الإنذار الرسمي المكتوب من إدارة الموارد البشرية والتشغيل بشركة <strong>مارتديا للتجارة والتوزيع ذ.م.م</strong> إلى الموظف المخالف نتيجة للتقصير أو الإهمال المهني أو السلوكي بمستودعات ومنصة الشركة الميدانية:</p>

<div class="custom-form-group">
    <span class="custom-form-label">اسم الموظف بالكامل:</span>
    <span class="custom-form-input"></span>
</div>
<div class="custom-form-group">
    <span class="custom-form-label">المسمى الوظيفي الحالي:</span>
    <span class="custom-form-input" style="width: 250px;"></span>
    <span class="custom-form-label" style="margin-right: 15px;">القسم / المستودع التابع له:</span>
    <span class="custom-form-input"></span>
</div>

<div class="legal-section-title" style="margin-top: 10px;">تفاصيل ونوع المخالفة التقصيرية المرصودة بالمستودع</div>
<div style="border: 1px dashed #cbd5e1; background-color: #f8fafc; padding: 6px; font-size: 7.2pt; line-height: 1.6; border-radius: 4px; margin-bottom: 8px;">
[  ] الإهمال الفني في حوكمة الباركود الإلكتروني للسلع وعجز الأرصدة بقاعدة البيانات AWS السحابية.<br>
[  ] عدم الالتزام بنظام الفصل التام للمنظفات ومواد التنظيف الكيماوية عن المواد الغذائية الحساسة كالرز والسكر.<br>
[  ] التقصير في إجراءات الكنس والنظافة والتعقيم اليومي لممرات تخزين مياه الشرب والألبان.<br>
[  ] عدم تسجيل طلبيات مبيعات POS من الإحداثيات الفعلية لل GPS للبقالات والعملاء الميدانيين.<br>
المخالفة بالتفصيل: ..................................................................................................................................................
</div>

<div class="custom-form-group">
    <span class="custom-form-label">الإجراء الجزائي المتخذ:</span>
    <span class="custom-form-input" style="width: 250px;"></span>
    <span class="custom-form-label" style="margin-right: 15px;">توقيع مدير الموارد:</span>
    <span class="custom-form-input"></span>
</div>
"""

doc_10_footer = """
<div style="display: grid; grid-template-columns: repeat(3, 1fr) 70px; gap: 8px; margin-top: 10px; border-top: 1.5px solid #0f172a; padding-top: 8px;">
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: right; border-radius: 4px; height: 28mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8pt; font-weight: bold; color: #0f172a; border-bottom: 1px solid #cbd5e1; padding-bottom: 1px;">توقيع الموظف بالعلم والتعليل</div>
        <div style="font-size: 7.2pt; line-height: 1.3;">
            الاسم: .............................<br>
            التوقيع: ...........................
        </div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: right; border-radius: 4px; height: 28mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8pt; font-weight: bold; color: #0284c7; border-bottom: 1px solid #0284c7; padding-bottom: 1px;">توقيع مدير التشغيل</div>
        <div style="font-size: 7.2pt; line-height: 1.3;">
            الاسم: محمد وليد حمودة<br>
            التوقيع: ...........................
        </div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: right; border-radius: 4px; height: 28mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8pt; font-weight: bold; color: #b45309; border-bottom: 1px solid #b45309; padding-bottom: 1px;">مصادقة الموارد البشرية</div>
        <div style="font-size: 7.2pt; line-height: 1.3;">
            حالة الإجراء: تم الحفظ والتقييد<br>
            التوقيع والختم: ...................
        </div>
    </div>
    <div style="display: flex; align-items: center; justify-content: center;">
        <div class="dashed-stamp-box" style="margin: 0; width: 52px; height: 52px;"></div>
    </div>
</div>
"""

PAGES_CONTENT_21_30[26] = get_contract_page_wrapper(
    "10. إنذار رسمي كتابي ولفت نظر داخلي للموظف المخالف",
    10,
    doc_10_body,
    doc_10_footer
)


# ----------------- PAGE 27: Document 11 - Managerial Delegation Agreement -----------------
doc_11_body = """
<p style="margin-bottom: 8px;">بموجب هذه الاتفاقية وميثاق التفويض التنظيمي المعتمد بالتوافق الكامل بين الشركاء الأربعة، تفوض إدارة شركة <strong>مارتديا للتجارة والتوزيع ذ.م.م</strong> ومستودعها كل من السيد <strong>محمود</strong> (شقيق الشريك محمد وليد حمودة) والسيد <strong>آدم</strong> (شقيق الشريك أحمد مبروك) كأعضاء وممثلين ميدانيين مفوضين لإدارة مستودع الشركة وأعمالها الميدانية اليومية كالتالي:</p>

<div class="legal-section-title" style="margin-top: 8px;">أولاً: صلاحيات التمثيل والنائب الميداني بالمستودعات</div>
<p style="margin-bottom: 6px;">
1. <strong>استلام ورص وتفريع الشحنات:</strong> تفويض كامل للنائبين محمود وآدم باستلام البضائع والمشروبات من الموردين ومصانع المنصورة، ومطابقتها يدوياً وإلكترونياً بمسح الباركود، ورصها على الطبالي المرتفعة مع الالتزام التام بفصل المنظفات.<br>
2. <strong>تجهيز طلبيات البقالات والعملاء:</strong> يتولى النائبان إعداد طلبيات البقالات والمنشآت المشتركة بالمنصة ومطابقة الفواتير، ومتابعة خروج البضائع وسائقي النقل المحلي (التوك توك أو التروسيكل) وتسجيل الزيارات بدقة.<br>
3. <strong>التوقيع الإداري للاستلام:</strong> يُفوّض محمود وآدم بالتوقيع الإداري على بوالص وإيصالات استلام البضائع من شركات التوزيع لإثبات الحيازة والتفريغ بالموقع.
</p>

<div class="legal-section-title" style="margin-top: 8px;">ثانياً: الرقابة والضوابط المالية الصارمة وحفظ الخزينة المركزية</div>
<p style="margin-bottom: 6px; color: #b45309; font-weight: bold;">
يتعهد ويقر الطرفان بأن كامل الصلاحيات المالية والإدارة المالية المركزية وحوكمة الدفع والتلقي كاش تظل تحت السيطرة الفعالة والحصرية للمدير المالي المركزي للشركة السيد محمد مبروك. ويحظر حظراً تاماً على النائبين محمود وآدم تحصيل مبالغ مالية كاش من العملاء، أو سداد أي نفقات أو سلف تزيد عن 1,000 ج.م دون إذن كتابي رسمي ومسبق من المدير المالي، ويعد الإخلال بهذا الشرط إخلالاً بالأمانة الوظيفية.
</p>
"""

doc_11_footer = """
<div style="display: grid; grid-template-columns: repeat(4, 1fr) 60px; gap: 8px; margin-top: 10px; border-top: 1.5px solid #0f172a; padding-top: 8px;">
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: center; border-radius: 4px;">
        <div style="font-size: 7.5pt; font-weight: bold; color: #0f172a; margin-bottom: 2px;">توقيع: محمود</div>
        <div style="height: 10mm; border-bottom: 1.2px solid #64748b; margin-bottom: 2px;"></div>
        <div style="font-size: 7pt; color: #64748b;">النائب المفوض</div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: center; border-radius: 4px;">
        <div style="font-size: 7.5pt; font-weight: bold; color: #0f172a; margin-bottom: 2px;">توقيع: آدم</div>
        <div style="height: 10mm; border-bottom: 1.2px solid #64748b; margin-bottom: 2px;"></div>
        <div style="font-size: 7pt; color: #64748b;">النائب المفوض</div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: center; border-radius: 4px;">
        <div style="font-size: 7.5pt; font-weight: bold; color: #0284c7; margin-bottom: 2px;">م.وليد حمودة</div>
        <div style="height: 10mm; border-bottom: 1.2px solid #64748b; margin-bottom: 2px;"></div>
        <div style="font-size: 7pt; color: #0284c7;">مدير الجودة</div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: center; border-radius: 4px;">
        <div style="font-size: 7.5pt; font-weight: bold; color: #b45309; margin-bottom: 2px;">محمد مبروك</div>
        <div style="height: 10mm; border-bottom: 1.2px solid #64748b; margin-bottom: 2px;"></div>
        <div style="font-size: 7pt; color: #b45309;">المدير المالي</div>
    </div>
    <div style="display: flex; align-items: center; justify-content: center;">
        <div class="dashed-stamp-box" style="margin: 0;"></div>
    </div>
</div>
"""

PAGES_CONTENT_21_30[27] = get_contract_page_wrapper(
    "11. اتفاقية التفويض الإداري والصلاحيات التنفيذية المحدودة للنائبين الميدانيين محمود وآدم",
    11,
    doc_11_body,
    doc_11_footer
)


# ----------------- PAGE 28: Document 12 - Working Hours & Attendance Commitment -----------------
doc_12_body = """
<p style="margin-bottom: 8px;">بموجب هذه اللائحة الداخلية وميثاق الالتزام والانضباط المهني المعمد بالإجماع بشركة <strong>مارتديا للتجارة والتوزيع ذ.م.م</strong> ومستودعها، يلتزم كافة العاملين والموظفين والنواب الميدانيين والسائقين بالضوابط التنظيمية الصارمة التالية لساعات العمل والحضور والإنتاجية:</p>

<div class="legal-section-title" style="margin-top: 8px;">أولاً: ساعات العمل ونوبات التواجد والزيارات الميدانية المعتمدة</div>
<p style="margin-bottom: 6px;">
1. <strong>ساعات العمل الرسمية:</strong> تحدد ساعات العمل بمستودع طوخ الأقلام ومستودع ميت خميس بمعدل 8 ساعات يومياً تبدأ من الساعة 9:00 صباحاً وحتى الساعة 5:00 مساءً، طوال 6 أيام في الأسبوع مع استبعاد يوم الجمعة كإجازة دورية مشتركة.<br>
2. <strong>نظام إثبات الحضور والانصراف:</strong> يلتزم كل نائب ميداني وموظف وعامل بالبصمة الإلكترونية أو التوقيع خطياً في سجل الحضور والانصراف المعتمد عند الدخول والخروج الفعلي، ولا يعتد بأي حضور يقع خارج الدفاتر الرسمية للشركة.<br>
3. <strong>انضباط خطوط السير والتسليم:</strong> يتعهد سائقو التوزيع ومندوبو المبيعات بالبدء الفوري لزيارات البقالات وتسليم الطلبيات بانتظام وفق خطوط السير اليومية المحددة مسبقاً من الإدارة والالتزام بالوصول الدقيق وبساعات التسليم المتفق عليها مع البقالات والمتاجر لضمان كفاءة الخدمة والإنتاجية القصوى.
</p>

<div class="legal-section-title" style="margin-top: 8px;">ثانياً: الإجراءات العقابية والجزاءات التدرجية الصارمة</div>
<p style="margin-bottom: 6px;">
في حال الإخلال بساعات العمل أو الغياب غير المبرر أو التقصير الفني في مسح باركود البضائع، تطبق اللائحة الإجراءات العقابية التالية بالتدرج لضمان انضباط العمل وصيانة رأس مال الشركاء:<br>
• المخالفة الأولى: تنبيه شفوي رسمي يسجل بملف الموظف.<br>
• المخالفة الثانية: لفت نظر رسمي مكتوب (وثيقة إنذار رقم 10) مع خصم نصف يوم عمل.<br>
• المخالفة الثالثة: خصم يوم عمل كامل وحظر مؤقت من الحوافز التشغيلية كاش.<br>
• المخالفة الرابعة: العرض على الإدارة ومجلس الشركاء للنظر في إنهاء وفصل العلاقة التعاقدية كلياً فوراً.
</p>
"""

doc_12_footer = """
<div style="display: grid; grid-template-columns: repeat(4, 1fr) 60px; gap: 8px; margin-top: 10px; border-top: 1.5px solid #0f172a; padding-top: 8px;">
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: center; border-radius: 4px;">
        <div style="font-size: 7.5pt; font-weight: bold; color: #0f172a; margin-bottom: 2px;">أحمد مبروك</div>
        <div style="height: 10mm; border-bottom: 1.2px solid #64748b; margin-bottom: 2px;"></div>
        <div style="font-size: 7pt; color: #64748b;">توقيع شريك</div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: center; border-radius: 4px;">
        <div style="font-size: 7.5pt; font-weight: bold; color: #0f172a; margin-bottom: 2px;">محمد مبروك</div>
        <div style="height: 10mm; border-bottom: 1.2px solid #64748b; margin-bottom: 2px;"></div>
        <div style="font-size: 7pt; color: #64748b;">توقيع شريك</div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: center; border-radius: 4px;">
        <div style="font-size: 7.5pt; font-weight: bold; color: #0f172a; margin-bottom: 2px;">م.وليد حمودة</div>
        <div style="height: 10mm; border-bottom: 1.2px solid #64748b; margin-bottom: 2px;"></div>
        <div style="font-size: 7pt; color: #64748b;">توقيع شريك</div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: center; border-radius: 4px;">
        <div style="font-size: 7.5pt; font-weight: bold; color: #0f172a; margin-bottom: 2px;">مازن السيد</div>
        <div style="height: 10mm; border-bottom: 1.2px solid #64748b; margin-bottom: 2px;"></div>
        <div style="font-size: 7pt; color: #64748b;">توقيع شريك</div>
    </div>
    <div style="display: flex; align-items: center; justify-content: center;">
        <div class="dashed-stamp-box" style="margin: 0;"></div>
    </div>
</div>
"""

PAGES_CONTENT_21_30[28] = get_contract_page_wrapper(
    "12. ميثاق لائحة الانضباط المهني والالتزام بساعات العمل ونظام الحضور بمستودعات مارتديا",
    12,
    doc_12_body,
    doc_12_footer
)

print("pages_21_30.py completely redefined with Documents 6-12 (Pages 22-28)!")
