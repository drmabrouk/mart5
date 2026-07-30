# -*- coding: utf-8 -*-
import sys

# Define Pages 22 to 26 for Martdia Trading & Distribution Co. (L.L.C.)
PAGES_CONTENT_21_30 = {}

# Helper function to generate clean contract layouts with simple Date and beautiful spacious writing lines.
def get_contract_page_wrapper(title_ar, doc_num, body_html, footer_html):
    return f"""
<div style="height: 100%; display: flex; flex-direction: column; justify-content: space-between; font-family: 'Cairo', sans-serif;">
    <div style="flex-grow: 1;">
        <!-- Top Simple Header -->
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #0f172a; padding-bottom: 8px; margin-bottom: 18px;">
            <div style="font-size: 10.5pt; font-weight: 800; color: #0f172a;">مجموعة المستندات التشغيلية والقانونية</div>
            <div style="font-size: 9.5pt; color: #64748b; font-weight: bold;">وثيقة رقم: {doc_num} / 10</div>
        </div>

        <!-- Document Date -->
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
            <div style="font-size: 11pt; color: #1e293b; font-weight: bold;">تاريخ المستند: ............................................</div>
            <div style="font-size: 11pt; color: #1e293b; font-weight: bold;">الرقم المرجعي: MT-DOC-{doc_num:02d}</div>
        </div>

        <!-- Document Title -->
        <div style="text-align: center; margin: 20px 0; padding: 10px; background-color: #f1f5f9; border: 1.5px solid #0f172a; border-radius: 4px;">
            <h2 style="font-size: 14pt; font-weight: 800; color: #0f172a; border: none; background: transparent; padding: 0; margin: 0; text-align: center;">{title_ar}</h2>
        </div>

        <!-- Document Body -->
        <div style="font-size: 10pt; line-height: 1.7; color: #1e293b; text-align: justify; margin-bottom: 20px;">
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
<p style="margin-bottom: 12px; font-size: 10.5pt;">بموجب هذه الاتفاقية الرسمية، يقر الموظف / الطرف الموقّع أدناه باستلام الأصول والأدوات التقنية واللوجستية التالية كعهدة عينية شخصية في ذمته المالية، ويتعهد بالحفاظ التام عليها وإعادتها فوراً للشركة بنفس الحالة الفنية عند طلبها أو عند إنهاء العمل:</p>

<div class="legal-section-title" style="font-size: 11pt; margin-top: 15px;">أولاً: بيانات الموظف المستلم للعهدة</div>
<p style="margin-bottom: 10px; font-size: 10pt;">الاسم الكامل للموظف: .................................................................................................................................... <br>
رقم الهوية الوطنية: .................................................... الوظيفة الحالية بالمستودع: ........................................................</p>

<div class="legal-section-title" style="font-size: 11pt; margin-top: 15px;">ثانياً: جدول تفصيل الأصول والمعدات المسلمة عهدة</div>
<table style="width: 100%; border-collapse: collapse; margin: 12px 0; font-size: 9.5pt;">
    <thead>
        <tr style="background-color: #0f172a; color: white;">
            <th style="padding: 8px; border: 1px solid #cbd5e1; width: 35%; text-align: right;">الأصل المسلم عهدة</th>
            <th style="padding: 8px; border: 1px solid #cbd5e1; width: 15%; text-align: right;">الكمية</th>
            <th style="padding: 8px; border: 1px solid #cbd5e1; width: 25%; text-align: right;">الرقم التسلسلي / الموديل</th>
            <th style="padding: 8px; border: 1px solid #cbd5e1; width: 25%; text-align: right;">توقيع المستلم بالاستلام الفعلي</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="padding: 8px; border: 1px solid #cbd5e1; font-weight: bold;">1. قارئ الباركود اللاسلكي (Barcode Scanner)</td>
            <td style="padding: 8px; border: 1px solid #cbd5e1;">عدد ...........</td>
            <td style="padding: 8px; border: 1px solid #cbd5e1;">.....................................</td>
            <td style="padding: 8px; border: 1px solid #cbd5e1;">.....................................</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #cbd5e1; font-weight: bold;">2. جهاز حاسوب مركزي وإدارة الـ POS</td>
            <td style="padding: 8px; border: 1px solid #cbd5e1;">عدد ...........</td>
            <td style="padding: 8px; border: 1px solid #cbd5e1;">.....................................</td>
            <td style="padding: 8px; border: 1px solid #cbd5e1;">.....................................</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #cbd5e1; font-weight: bold;">3. كاميرات مراقبة IP عالية الدقة</td>
            <td style="padding: 8px; border: 1px solid #cbd5e1;">عدد 2 كاميرا</td>
            <td style="padding: 8px; border: 1px solid #cbd5e1;">.....................................</td>
            <td style="padding: 8px; border: 1px solid #cbd5e1;">.....................................</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #cbd5e1; font-weight: bold;">4. راوتر شبكات ذكي وأجهزة الربط</td>
            <td style="padding: 8px; border: 1px solid #cbd5e1;">عدد ...........</td>
            <td style="padding: 8px; border: 1px solid #cbd5e1;">.....................................</td>
            <td style="padding: 8px; border: 1px solid #cbd5e1;">.....................................</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #cbd5e1; font-weight: bold;">5. أرفف تخزين معدنية ثقيلة (Shelving)</td>
            <td style="padding: 8px; border: 1px solid #cbd5e1;">عدد ...........</td>
            <td style="padding: 8px; border: 1px solid #cbd5e1;">.....................................</td>
            <td style="padding: 8px; border: 1px solid #cbd5e1;">.....................................</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #cbd5e1; font-weight: bold;">6. طبالي رص بلاستيكية / خشبية (Pallets)</td>
            <td style="padding: 8px; border: 1px solid #cbd5e1;">عدد ...........</td>
            <td style="padding: 8px; border: 1px solid #cbd5e1;">.....................................</td>
            <td style="padding: 8px; border: 1px solid #cbd5e1;">.....................................</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #cbd5e1; font-weight: bold;">7. مكتب إداري خشبي وكرسي متحرك</td>
            <td style="padding: 8px; border: 1px solid #cbd5e1;">عدد ...........</td>
            <td style="padding: 8px; border: 1px solid #cbd5e1;">.....................................</td>
            <td style="padding: 8px; border: 1px solid #cbd5e1;">.....................................</td>
        </tr>
        <tr>
            <td style="padding: 8px; border: 1px solid #cbd5e1; font-weight: bold;">8. طابعة ليزر ثقيلة لإذن التسليم والفواتير</td>
            <td style="padding: 8px; border: 1px solid #cbd5e1;">عدد ...........</td>
            <td style="padding: 8px; border: 1px solid #cbd5e1;">.....................................</td>
            <td style="padding: 8px; border: 1px solid #cbd5e1;">.....................................</td>
        </tr>
    </tbody>
</table>
"""

doc_6_footer = """
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 15px; border-top: 1.5px solid #0f172a; padding-top: 12px; padding-bottom: 10px;">
    <div style="border: 1px dashed #cbd5e1; padding: 10px; text-align: center; border-radius: 4px; height: 32mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 9pt; font-weight: bold; color: #0f172a; border-bottom: 1px solid #cbd5e1; padding-bottom: 4px; margin-bottom: 6px;">إقرار وتوقيع الموظف المستلم</div>
        <div style="text-align: right; font-size: 8pt; line-height: 1.5;">
            الاسم الكامل: .....................................................<br>
            التوقيع الشخصي: ................................................<br>
            التاريخ: ............................................................
        </div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 10px; text-align: center; border-radius: 4px; height: 32mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 9pt; font-weight: bold; color: #0284c7; border-bottom: 1px solid #0284c7; padding-bottom: 4px; margin-bottom: 6px;">عن إدارة المستودعات والشركة المانحة</div>
        <div style="text-align: right; font-size: 8pt; line-height: 1.5;">
            الاسم: محمد وليد حمودة (مدير العمليات)<br>
            التوقيع والاعتماد: ................................................<br>
            خاتم الشركة المعتمد: .............................................
        </div>
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
<p style="margin-bottom: 12px; font-size: 10.5pt;">تستخدم هذه الاستمارة لطلب واعتماد صرف مبالغ النقدية (كاش) لتغطية النفقات والمصاريف التشغيلية الطارئة والدورية للمستودعات ومواقع العمل الميداني:</p>

<div class="legal-section-title" style="font-size: 11pt; margin-top: 15px;">أولاً: بيانات وتفاصيل النفقة المطلوبة</div>
<p style="margin-bottom: 10px; font-size: 10pt;">اسم طالب الصرف الميداني: ................................................................................................................................ <br>
المستودع المعني بالصرف: [  ] مستودع طوخ الأقلام   [  ] مستودع ميت خميس</p>

<table style="width: 100%; border-collapse: collapse; margin: 12px 0; font-size: 10pt;">
    <thead>
        <tr style="background-color: #0f172a; color: white;">
            <th style="padding: 10px; border: 1px solid #cbd5e1; width: 40%; text-align: right;">بند النفقة التشغيلية المطلوبة</th>
            <th style="padding: 10px; border: 1px solid #cbd5e1; width: 30%; text-align: right;">القيمة التقريبية (ج.م)</th>
            <th style="padding: 10px; border: 1px solid #cbd5e1; width: 30%; text-align: right;">البيان والملاحظات والمستند المرفق</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">1. اشتراك الإنترنت والشبكة السريعة</td>
            <td style="padding: 10px; border: 1px solid #cbd5e1;">...................................................</td>
            <td style="padding: 10px; border: 1px solid #cbd5e1;">...................................................</td>
        </tr>
        <tr>
            <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">2. استهلاك الكهرباء والخدمات الطاقية</td>
            <td style="padding: 10px; border: 1px solid #cbd5e1;">...................................................</td>
            <td style="padding: 10px; border: 1px solid #cbd5e1;">...................................................</td>
        </tr>
        <tr>
            <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">3. خدمات النظافة والتعقيم اليومي الداخلي</td>
            <td style="padding: 10px; border: 1px solid #cbd5e1;">...................................................</td>
            <td style="padding: 10px; border: 1px solid #cbd5e1;">...................................................</td>
        </tr>
        <tr>
            <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">4. صيانة طارئة للأرفف أو الباركود أو الكاميرات</td>
            <td style="padding: 10px; border: 1px solid #cbd5e1;">...................................................</td>
            <td style="padding: 10px; border: 1px solid #cbd5e1;">...................................................</td>
        </tr>
        <tr style="background-color: #f1f5f9; font-weight: bold;">
            <td style="padding: 10px; border: 1px solid #cbd5e1;">إجمالي المبلغ المطلوب كاش للصرف</td>
            <td style="padding: 10px; border: 1px solid #cbd5e1;" colspan="2">........................................................................................................................ جنيه مصري.</td>
        </tr>
    </tbody>
</table>

<div class="legal-section-title" style="font-size: 11pt; margin-top: 15px;">ثانياً: تعهد ومطابقة إحضار الفواتير الأصلية</div>
<p style="font-size: 9.5pt; line-height: 1.5; color: #475569;">
يتعهد طالب الصرف بإحضار وتسليم الفواتير الضريبية والإيصالات الرسمية لمطابقة القيد المالي المحاسبي بالدفاتر في موعد أقصاه 72 ساعة فقط من تاريخ الاستلام الفعلي للكاش، ويتحمل كامل المسؤولية المالية في حال التقصير.
</p>
"""

doc_7_footer = """
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-top: 15px; border-top: 1.5px solid #0f172a; padding-top: 12px; padding-bottom: 10px;">
    <div style="border: 1px dashed #cbd5e1; padding: 8px; text-align: center; border-radius: 4px; height: 32mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8.5pt; font-weight: bold; color: #0f172a; border-bottom: 1px solid #cbd5e1; padding-bottom: 2px; margin-bottom: 4px;">توقيع مقدم الطلب</div>
        <div style="text-align: right; font-size: 7.5pt; line-height: 1.4;">
            الاسم: .............................<br>
            التوقيع: ...........................<br>
            التاريخ: ............................
        </div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 8px; text-align: center; border-radius: 4px; height: 32mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8.5pt; font-weight: bold; color: #0284c7; border-bottom: 1px solid #0284c7; padding-bottom: 2px; margin-bottom: 4px;">رأي ومراجعة الحسابات</div>
        <div style="text-align: right; font-size: 7.5pt; line-height: 1.4;">
            الحالة: [  ] مطابق للموازنة<br>
            ملاحظات: ........................<br>
            التوقيع: ...........................
        </div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 8px; text-align: center; border-radius: 4px; height: 32mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8.5pt; font-weight: bold; color: #b45309; border-bottom: 1px solid #b45309; padding-bottom: 2px; margin-bottom: 4px;">اعتماد وتوقيع المدير المالي</div>
        <div style="text-align: right; font-size: 7.5pt; line-height: 1.4;">
            الاسم: محمد مبروك<br>
            القرار: [  ] يعتمد الصرف فورا<br>
            التوقيع والختم: ...................
        </div>
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
<p style="margin-bottom: 12px; font-size: 10.5pt;">يتعهد ويقر الموقّع أدناه (سواء كان شريكاً، مديراً، أو موظفاً) بالالتزام التام والكامل بكافة السياسات، الشروط، الأحكام، ومواثيق العمل المعتمدة باللائحة الداخلية لشركة <strong>مارتديا للتجارة والتوزيع ذ.م.م</strong> ومستودعات <strong>تاجر</strong>، والموضحة كالتالي:</p>

<div class="legal-section-title" style="font-size: 11pt; margin-top: 15px;">أولاً: بنود الالتزام التشغيلي والمهني بمستودعات تاجر</div>
<p style="margin-bottom: 8px; font-size: 10pt;">1. <strong>حوكمة الباركود الإلكتروني:</strong> يلتزم الموظف التزاماً صارماً بمسح الباركود الخاص بكل كرتونة أو صندوق سلع خارج من المستودع قبل مغادرته للبوابة بشكل ميكانيكي لضمان المطابقة اليومية الفورية للأرصدة.<br>
2. <strong>جودة وسلامة الغذاء والسلع:</strong> يتعهد طاقم العمل بالالتزام بفرز وفحص صلاحية السلع، ورص كراتين المياه والأجبان والزيت على الطبالي المرتفعة، والفصل التام للمنظفات عن المواد الغذائية لمنع انتشار الروائح والتلوث.<br>
3. <strong>الالتزام بإحداثيات وتتبع الـ GPS:</strong> يقر مندوب المبيعات والتوزيع بالتزامه بتأدية الزيارات للبقالات وتسجيل الطلبات من خلال النطاق الفعلي للبقالة بمسافة لا تزيد عن 20 متراً، ويمنع تسجيل أي طلبية وهمية خارج النطاق.</p>

<div class="legal-section-title" style="font-size: 11pt; margin-top: 15px;">ثانياً: سرية المعلومات وحظر المنافسة وإفشاء البيانات</div>
<p style="margin-bottom: 8px; font-size: 10pt;">يقر الموقّع بالسرية التامة لبيانات البقالات المشتركة بالمنصة، وأسعار الشراء والخصومات والبونص النقدي من شركات المنصورة وطنطا، ويحظر تماماً استخدام أو إفشاء أو نسخ هذه البيانات لتأسيس أي نشاط تجاري منافس تحت طائلة القانون الجنائي والشرط الجزائي البالغ 100,000 ج.م.</p>

<div class="legal-section-title" style="font-size: 11pt; margin-top: 15px;">ثالثاً: الإقرارات العامة والمسؤولية القانونية</div>
<p style="font-size: 9.5pt; line-height: 1.5; color: #475569;">
يقر الموقّع بأن أي مخالفة لأي من البنود الواردة في هذا الإقرار تعرضه للمساءلة القانونية المباشرة، وإيقاف كافة صلاحياته البرمجية والإدارية، وفصله الفوري من العمل مع احتفاظ الشركة بكامل حقوقها المالية والقضائية في طلب التعويض.
</p>
"""

doc_8_footer = """
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 15px; border-top: 1.5px solid #0f172a; padding-top: 12px; padding-bottom: 10px;">
    <div style="border: 1px dashed #cbd5e1; padding: 10px; text-align: center; border-radius: 4px; height: 35mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 9pt; font-weight: bold; color: #0f172a; border-bottom: 1px solid #cbd5e1; padding-bottom: 4px; margin-bottom: 6px;">توقيع وإقرار الطرف المعني بالالتزام</div>
        <div style="text-align: right; font-size: 8pt; line-height: 1.5;">
            الاسم الكامل: .....................................................<br>
            رقم الهوية الوطنية: ................................................<br>
            التوقيع الشخصي: ................................................
        </div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 10px; text-align: center; border-radius: 4px; height: 35mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 9pt; font-weight: bold; color: #0284c7; border-bottom: 1px solid #0284c7; padding-bottom: 4px; margin-bottom: 6px;">المصادقة والاعتماد من مجلس الإدارة</div>
        <div style="text-align: right; font-size: 8pt; line-height: 1.5;">
            الاسم والممثّل المفوّض: ..........................................<br>
            الصفة والمسؤولية: .............................................<br>
            التوقيع والختم الرسمي: .........................................
        </div>
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
<p style="margin-bottom: 12px; font-size: 10.5pt;">يقدم هذا الطلب رسمياً من الشريك الراغب في التخارج طواعية إلى مجلس إدارة شركة <strong>مارتديا للتجارة والتوزيع ذ.م.م</strong> ومستودع <strong>تاجر</strong>، بموجب ميثاق التأسيس المعتمد وفترة الإخطار القانونية البالغة 90 يوماً:</p>

<div class="legal-section-title" style="font-size: 11pt; margin-top: 15px;">أولاً: بيانات الشريك طالب التخارج والانسحاب</div>
<p style="margin-bottom: 10px; font-size: 10pt;">الاسم الكامل للشريك طالب الانسحاب: .................................................................................................................... <br>
الرقم القومي / جواز السفر: .................................................... الحصة الملكية الحالية بالشركة: 25% (خمسة وعشرون بالمائة).</p>

<div class="legal-section-title" style="font-size: 11pt; margin-top: 15px;">ثانياً: آلية استرداد وتصفية الحصة المالية والضوابط المحاسبية</div>
<p style="margin-bottom: 8px; font-size: 10pt;">1. <strong>جرد وتدقيق مالي عاجل:</strong> يلتزم الشركاء بتشكيل لجنة جرد مالي وميداني فوري لكافة موجودات مستودعي طوخ الأقلام وميت خميس لتقييم السيولة والمخزون وحجم الأرباح والخسائر للشركة.<br>
2. <strong>سداد الديون التجارية أولاً:</strong> تخصم كافة الالتزامات والديون التجارية للموردين من قيمة الحصة قبل التسوية والوفاء بها.<br>
3. <strong>آلية التقسيط الآمن:</strong> تسدد الحصة المالية المستحقة للشريك المتخارج على أربع دفعات متساوية طوال عام مالي كامل لضمان استقرار التدفق المالي كاش لمستودع تاجر وعدم الإضرار بميزانية شراء المنتجات الغذائية الأساسية.</p>

<div class="legal-section-title" style="font-size: 11pt; margin-top: 15px;">ثالثاً: وثائق ومستندات المطابقة المالية المرفقة بالطلب</div>
<p style="margin-bottom: 8px; font-size: 10pt;">برجاء إرفاق ما يلي لتأكيد سلامة المطابقة والحسابات الفنية:</p>
<p style="font-size: 10pt; line-height: 1.6;">
[  ] كشف حساب بنكي مسجل معتمد باسم الشريك المستلم بالبنك لتلقي التحويل المالي.<br>
[  ] إقرار خطي ببراءة ذمة الإدارة المالية والشركاء الآخرين تماماً فور استلام الدفعة الرابعة والأخيرة من الحصة.<br>
[  ] إقرار حظر المنافسة وإفشاء أسرار المنصة والزيارات الميدانية للبقالات طوال 3 سنوات اللاحقة للتخارج.
</p>
"""

doc_9_footer = """
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-top: 15px; border-top: 1.5px solid #0f172a; padding-top: 12px; padding-bottom: 10px;">
    <div style="border: 1px dashed #cbd5e1; padding: 8px; text-align: center; border-radius: 4px; height: 35mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8.5pt; font-weight: bold; color: #0f172a; border-bottom: 1px solid #cbd5e1; padding-bottom: 2px; margin-bottom: 4px;">توقيع الشريك طالب الانسحاب</div>
        <div style="text-align: right; font-size: 7.5pt; line-height: 1.4;">
            الاسم: .............................<br>
            التوقيع: ...........................<br>
            التاريخ: ............................
        </div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 8px; text-align: center; border-radius: 4px; height: 35mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8.5pt; font-weight: bold; color: #0284c7; border-bottom: 1px solid #0284c7; padding-bottom: 2px; margin-bottom: 4px;">مراجعة وقرار الشركاء الثلاثة</div>
        <div style="text-align: right; font-size: 7.5pt; line-height: 1.4;">
            القرار: [  ] موافقة  [  ] تأجيل للجرد<br>
            الملاحظات: ........................<br>
            التواقيع: ...........................
        </div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 8px; text-align: center; border-radius: 4px; height: 35mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8.5pt; font-weight: bold; color: #b45309; border-bottom: 1px solid #b45309; padding-bottom: 2px; margin-bottom: 4px;">مصادقة واعتماد المدير المالي</div>
        <div style="text-align: right; font-size: 7.5pt; line-height: 1.4;">
            الاسم: محمد مبروك<br>
            الاعتماد: [  ] تم الجرد والجدولة<br>
            التوقيع والختم: ...................
        </div>
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
<p style="margin-bottom: 12px; font-size: 10.5pt;">يوجه هذا الإنذار الرسمي المكتوب من إدارة الموارد البشرية والتشغيل بشركة <strong>مارتديا للتجارة والتوزيع ذ.م.م</strong> إلى الموظف المخالف نتيجة للتقصير أو الإهمال المهني أو السلوكي بمستودعات ومنصة <strong>تاجر</strong>:</p>

<div class="legal-section-title" style="font-size: 11pt; margin-top: 15px;">أولاً: بيانات الموظف الموجه إليه الإنذار واللفت نظر</div>
<p style="margin-bottom: 10px; font-size: 10pt;">اسم الموظف بالكامل: .................................................................................................................................... <br>
المسمى الوظيفي الحالي: .................................................... القسم / المستودع التابع له: ........................................................</p>

<div class="legal-section-title" style="font-size: 11pt; margin-top: 15px;">ثانياً: تفاصيل ونوع المخالفة التقصيرية المرصودة بالمستودع</div>
<p style="margin-bottom: 8px; font-size: 10pt;">الرجاء تحديد نوع وتفاصيل المخالفة التشغيلية الموجه على إثرها لفت النظر المكتوب:</p>
<div style="border: 1px dashed #cbd5e1; background-color: #f8fafc; padding: 12px; font-size: 9.5pt; line-height: 1.8; border-radius: 4px; margin-bottom: 12px;">
[  ] الإهمال الفني في حوكمة الباركود الإلكتروني للسلع وعجز الأرصدة بقاعدة البيانات AWS.<br>
[  ] عدم الالتزام بنظام الفصل التام للمنظفات ومواد التنظيف الكيماوية عن المواد الغذائية الحساسة.<br>
[  ] التقصير في إجراءات الكنس والنظافة والتعقيم اليومي لممرات تخزين مياه الشرب والألبان.<br>
[  ] عدم تسجيل طلبيات مبيعات POS من الإحداثيات الفعلية لل GPS للبقالات والعملاء الميدانيين.<br>
المخالفة بالتفصيل: ..................................................................................................................................................<br>
......................................................................................................................................................................................
</div>

<div class="legal-section-title" style="font-size: 11pt; margin-top: 15px;">ثالثاً: الإجراء الجزائي المترتب وتوقيع الموظف بالعلم والرد المكتوب</div>
<p style="margin-bottom: 8px; font-size: 10pt;">الإجراء الإداري المتخذ: [  ] لفت نظر أول   [  ] إنذار ثاني مع خصم من الراتب   [  ] إيقاف مؤقت عن العمل لمدة ............ أيام.<br>
• رد وتعليل الموظف المكتوب على الإنذار: ..................................................................................................................</p>
"""

doc_10_footer = """
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-top: 15px; border-top: 1.5px solid #0f172a; padding-top: 12px; padding-bottom: 10px;">
    <div style="border: 1px dashed #cbd5e1; padding: 8px; text-align: center; border-radius: 4px; height: 35mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8.5pt; font-weight: bold; color: #0f172a; border-bottom: 1px solid #cbd5e1; padding-bottom: 2px; margin-bottom: 4px;">توقيع الموظف بالعلم بالإنذار</div>
        <div style="text-align: right; font-size: 7.5pt; line-height: 1.4;">
            الاسم: .............................<br>
            التوقيع: ...........................<br>
            التاريخ: ............................
        </div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 8px; text-align: center; border-radius: 4px; height: 35mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8.5pt; font-weight: bold; color: #0284c7; border-bottom: 1px solid #0284c7; padding-bottom: 2px; margin-bottom: 4px;">توقيع واعتماد مدير التشغيل</div>
        <div style="text-align: right; font-size: 7.5pt; line-height: 1.4;">
            الاسم: محمد وليد حمودة<br>
            الصفة: مدير الجودة والسلامة<br>
            التوقيع: ...........................
        </div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 8px; text-align: center; border-radius: 4px; height: 35mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8.5pt; font-weight: bold; color: #b45309; border-bottom: 1px solid #b45309; padding-bottom: 2px; margin-bottom: 4px;">مصادقة وختم الشركة الرسمي</div>
        <div style="text-align: right; font-size: 7.5pt; line-height: 1.4;">
            الجهة: الموارد البشرية والتشغيل<br>
            حالة الإجراء: [  ] تم التسجيل بالملف<br>
            الختم والتوقيع: ...................
        </div>
    </div>
</div>
"""

PAGES_CONTENT_21_30[26] = get_contract_page_wrapper(
    "10. إنذار رسمي كتابي ولفت نظر داخلي للموظف المخالف",
    10,
    doc_10_body,
    doc_10_footer
)

print("pages_21_30.py completely redefined with Documents 6-10!")
