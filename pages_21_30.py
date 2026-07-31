# -*- coding: utf-8 -*-
import sys

# Define Pages 26 to 33 for Martdia Trading & Distribution Co. (L.L.C.)
PAGES_CONTENT_21_30 = {}

# Helper function to generate clean contract layouts with simple Date and beautiful spacious writing lines.
def get_contract_page_wrapper(title_ar, doc_num, body_html, footer_html):
    return f"""
<div style="height: 100%; display: flex; flex-direction: column; justify-content: space-between; font-family: 'Cairo', sans-serif;">
    <div style="flex-grow: 1;">
        <!-- Top Simple Header -->
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #1a1a1a; padding-bottom: 6px; margin-bottom: 15px;">
            <div style="font-size: 10.5pt; font-weight: 800; color: #1a1a1a;">مجموعة المستندات التشغيلية والقانونية - شركة مارتديا للتجارة والتوزيع</div>
            <div style="font-size: 9pt; color: #64748b; font-weight: bold;">وثيقة رقم: {doc_num} / 12</div>
        </div>

        <!-- Document Date & Reference with clean underline fields -->
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <div style="font-size: 9.5pt; color: #1e293b; font-weight: bold; display: flex; align-items: center; width: 60%;">
                <span class="custom-form-label">تاريخ المستند:</span>
                <span class="custom-form-input" style="width: 180px;"></span>
            </div>
            <div style="font-size: 9.5pt; color: #1e293b; font-weight: bold; display: flex; align-items: center; width: 35%; justify-content: flex-end;">
                <span class="custom-form-label" style="margin-left: 8px;">الرقم المرجعي:</span>
                <span style="font-family: monospace; font-size: 10.5pt; color: #ff9900; font-weight: bold;">MT-DOC-{doc_num:02d}</span>
            </div>
        </div>

        <!-- Document Title -->
        <div style="text-align: center; margin: 12px 0 10px 0; padding: 8px; background-color: #f1f5f9; border: 1.5px solid #1a1a1a; border-radius: 4px;">
            <h2 style="font-size: 11.5pt; font-weight: 800; color: #1a1a1a; border: none; background: transparent; padding: 0; margin: 0; text-align: center;">{title_ar}</h2>
        </div>

        <!-- Document Body -->
        <div style="font-size: 9.3pt; line-height: 1.65; color: #1e293b; text-align: justify; margin-bottom: 15px;">
            {body_html}
        </div>
    </div>

    <!-- Signatures and footer -->
    <div>
        {footer_html}
    </div>
</div>
"""

# Helper for the multi-page Master Partnership Agreement
def get_master_agreement_page_wrapper(page_index, total_pages, title_ar, body_html, show_continuation=True):
    continuation_html = ""
    if show_continuation:
        continuation_html = """
        <div style="text-align: center; font-size: 8.5pt; font-weight: bold; color: #800020; margin-top: 10px; padding: 5px; border: 1px dashed #cbd5e1; border-radius: 4px; background-color: #fffaf0;">
            "هذا الاتفاق مستمر في الصفحة التالية ويقرأ كوثيقة قانونية واحدة متكاملة غير قابلة للتجزئة."
        </div>
        """

    if show_continuation:
        signatures_html = f"""
        <div style="display: grid; grid-template-columns: repeat(4, 1fr) 60px; gap: 8px; margin-top: 10px; border-top: 1.5px solid #1a1a1a; padding-top: 8px; font-family: 'Cairo', sans-serif;">
            <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: center; border-radius: 4px;">
                <div style="font-size: 7.5pt; font-weight: bold; color: #1a1a1a; margin-bottom: 2px;">أحمد حسام الدين علي مبروك</div>
                <div style="height: 8mm; border-bottom: 1.2px solid #64748b; margin-bottom: 2px;"></div>
                <div style="font-size: 6.5pt; color: #64748b;">توقيع / أحرف أولى</div>
            </div>
            <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: center; border-radius: 4px;">
                <div style="font-size: 7.5pt; font-weight: bold; color: #1a1a1a; margin-bottom: 2px;">محمد محجوب علي مبروك</div>
                <div style="height: 8mm; border-bottom: 1.2px solid #64748b; margin-bottom: 2px;"></div>
                <div style="font-size: 6.5pt; color: #64748b;">توقيع / أحرف أولى</div>
            </div>
            <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: center; border-radius: 4px;">
                <div style="font-size: 7.5pt; font-weight: bold; color: #1a1a1a; margin-bottom: 2px;">محمد وليد حمودة</div>
                <div style="height: 8mm; border-bottom: 1.2px solid #64748b; margin-bottom: 2px;"></div>
                <div style="font-size: 6.5pt; color: #64748b;">توقيع / أحرف أولى</div>
            </div>
            <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: center; border-radius: 4px;">
                <div style="font-size: 7.5pt; font-weight: bold; color: #1a1a1a; margin-bottom: 2px;">مازن السيد</div>
                <div style="height: 8mm; border-bottom: 1.2px solid #64748b; margin-bottom: 2px;"></div>
                <div style="font-size: 6.5pt; color: #64748b;">توقيع / أحرف أولى</div>
            </div>
            <div style="display: flex; align-items: center; justify-content: center;">
                <div class="dashed-stamp-box" style="margin: 0; width: 45px; height: 45px;"></div>
            </div>
        </div>
        """
    else:
        # Redesigned 2x2 grid for Page 33 (Execution Page)
        signatures_html = f"""
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 10px; border-top: 2px solid #1a1a1a; padding-top: 10px; font-family: 'Cairo', sans-serif;">
            <!-- Top Left: First Party (أحمد حسام الدين علي مبروك) -->
            <div style="border: 1.5px dashed #cbd5e1; padding: 10px; text-align: right; border-radius: 6px; height: 35mm; display: flex; flex-direction: column; justify-content: space-between;">
                <div style="font-size: 9pt; font-weight: 800; color: #1a1a1a; border-bottom: 1.5px solid #cbd5e1; padding-bottom: 3px; display: flex; justify-content: space-between;">
                    <span>الطرف الأول (First Party)</span>
                    <span style="color: #ff9900; font-size: 8pt;">أحمد حسام الدين علي مبروك</span>
                </div>
                <div style="font-size: 8.5pt; line-height: 1.6;">
                    <strong>الاسم الكامل:</strong> السيد أحمد حسام الدين علي مبروك<br>
                    <strong>رقم بطاقة الرقم القومي:</strong> .....................................................<br>
                    <strong>التوقيع:</strong> .......................................................................
                </div>
            </div>

            <!-- Top Right: Second Party (محمد محجوب علي مبروك) -->
            <div style="border: 1.5px dashed #cbd5e1; padding: 10px; text-align: right; border-radius: 6px; height: 35mm; display: flex; flex-direction: column; justify-content: space-between;">
                <div style="font-size: 9pt; font-weight: 800; color: #1a1a1a; border-bottom: 1.5px solid #cbd5e1; padding-bottom: 3px; display: flex; justify-content: space-between;">
                    <span>الطرف الثاني (Second Party)</span>
                    <span style="color: #ff9900; font-size: 8pt;">محمد محجوب علي مبروك</span>
                </div>
                <div style="font-size: 8.5pt; line-height: 1.6;">
                    <strong>الاسم الكامل:</strong> السيد محمد محجوب علي مبروك<br>
                    <strong>رقم بطاقة الرقم القومي:</strong> .....................................................<br>
                    <strong>التوقيع:</strong> .......................................................................
                </div>
            </div>

            <!-- Bottom Left: Third Party (محمد وليد حمودة) -->
            <div style="border: 1.5px dashed #cbd5e1; padding: 10px; text-align: right; border-radius: 6px; height: 35mm; display: flex; flex-direction: column; justify-content: space-between;">
                <div style="font-size: 9pt; font-weight: 800; color: #1a1a1a; border-bottom: 1.5px solid #cbd5e1; padding-bottom: 3px; display: flex; justify-content: space-between;">
                    <span>الطرف الثالث (Third Party)</span>
                    <span style="color: #ff9900; font-size: 8pt;">محمد وليد حمودة</span>
                </div>
                <div style="font-size: 8.5pt; line-height: 1.6;">
                    <strong>الاسم الكامل:</strong> السيد محمد وليد حمودة<br>
                    <strong>رقم بطاقة الرقم القومي:</strong> .....................................................<br>
                    <strong>التوقيع:</strong> .......................................................................
                </div>
            </div>

            <!-- Bottom Right: Fourth Party (مازن السيد) -->
            <div style="border: 1.5px dashed #cbd5e1; padding: 10px; text-align: right; border-radius: 6px; height: 35mm; display: flex; flex-direction: column; justify-content: space-between;">
                <div style="font-size: 9pt; font-weight: 800; color: #1a1a1a; border-bottom: 1.5px solid #cbd5e1; padding-bottom: 3px; display: flex; justify-content: space-between;">
                    <span>الطرف الرابع (Fourth Party)</span>
                    <span style="color: #ff9900; font-size: 8pt;">مازن السيد</span>
                </div>
                <div style="font-size: 8.5pt; line-height: 1.6;">
                    <strong>الاسم الكامل:</strong> السيد مازن السيد<br>
                    <strong>رقم بطاقة الرقم القومي:</strong> .....................................................<br>
                    <strong>التوقيع:</strong> .......................................................................
                </div>
            </div>
        </div>
        """

    return f"""
<div style="height: 100%; display: flex; flex-direction: column; justify-content: space-between; font-family: 'Cairo', sans-serif;">
    <div style="flex-grow: 1;">
        <!-- Top Simple Header -->
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #1a1a1a; padding-bottom: 6px; margin-bottom: 12px;">
            <div style="font-size: 10pt; font-weight: 800; color: #1a1a1a;">الاتفاق القانوني التأسيسي الحاكم - شركة مارتديا للتجارة والتوزيع ذ.م.م</div>
            <div style="font-size: 8.5pt; color: #64748b; font-weight: bold;">وثيقة رئيسية • صفحة {page_index - 30} من {total_pages}</div>
        </div>

        <!-- Document Date & Reference -->
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <div style="font-size: 9pt; color: #1e293b; font-weight: bold; display: flex; align-items: center; width: 60%;">
                <span class="custom-form-label">تاريخ نفاذ العقد:</span>
                <span class="custom-form-input" style="width: 180px;"></span>
            </div>
            <div style="font-size: 9pt; color: #1e293b; font-weight: bold; display: flex; align-items: center; width: 35%; justify-content: flex-end;">
                <span class="custom-form-label" style="margin-left: 8px;">الرقم المرجعي القانوني:</span>
                <span style="font-family: monospace; font-size: 10pt; color: #ff9900; font-weight: bold;">MT-MASTER-AGREEMENT</span>
            </div>
        </div>

        <!-- Title -->
        <div style="text-align: center; margin: 8px 0; padding: 6px; background-color: #f1f5f9; border: 1.5px solid #1a1a1a; border-radius: 4px;">
            <h2 style="font-size: 11pt; font-weight: 800; color: #1a1a1a; border: none; background: transparent; padding: 0; margin: 0; text-align: center;">{title_ar}</h2>
        </div>

        <!-- Body -->
        <div style="font-size: 7.6pt; line-height: 1.5; color: #1e293b; text-align: justify; margin-bottom: 8px;">
            {body_html}
        </div>
    </div>

    <!-- Continuation and signature boxes -->
    <div>
        {continuation_html}
        {signatures_html}
    </div>
</div>
"""


# ----------------- PAGE 26: Document 7 - Terms and Conditions Acknowledgement -----------------
doc_7_body = """
<p style="margin-bottom: 8px;">يتعهد ويقر الموقّع أدناه (سواء كان شريكاً، مديراً، أو موظفاً) بالالتزام التام والكامل بكافة السياسات، الشروط، الأحكام، ومواثيق العمل المعتمدة باللائحة الداخلية لشركة <strong>مارتديا للتجارة والتوزيع ذ.م.م</strong> ومستودعاتها، والموضحة كالتالي:</p>

<div class="legal-section-title" style="margin-top: 8px;">أولاً: بنود الالتزام التشغيلي والمهني بمستودعات ومنصة مارتديا</div>
<p style="margin-bottom: 6px;">1. <strong>حوكمة الباركود الإلكتروني للسلع:</strong> يلتزم الموظف التزاماً صارماً بمسح الباركود الخاص بكل كرتونة أو صندوق سلع خارج من المستودع قبل مغادرته للبوابة بشكل ميكانيكي لضمان المطابقة اليومية الفورية للأرصدة.<br>
2. <strong>جودة وسلامة الغذاء والسلع:</strong> يتعهد طاقم العمل بالالتزام بفرز وفحص صلاحية السلع، ورص كراتين المياه والأجبان والزيت على الطبالي المرتفعة، والفصل التام للمنظفات عن المواد الغذائية لمنع انتشار الروائح والتلوث.<br>
3. <strong>الالتزام بإحداثيات وتتبع الـ GPS:</strong> يقر مندوب المبيعات والتوزيع بالتزامه بتأدية الزيارات للبقالات وتسجيل الطلبات من خلال النطاق الفعلي للبقالة بمسافة لا تزيد عن 20 متراً، ويمنع تسجيل أي طلبية وهمية خارج النطاق.</p>

<div class="legal-section-title" style="margin-top: 8px;">ثانياً: سرية المعلومات وحظر المنافسة وإفشاء البيانات</div>
<p style="margin-bottom: 6px;">يقر الموقّع بالسرية التامة لبيانات البقالات المشتركة بالمنصة، وأسعار الشراء والخصومات والبونص النقدي من شركات المنصورة وطنطا، ويحظر تماماً استخدام أو إفشاء أو نسخ هذه البيانات لتأسيس أي نشاط تجاري منافس تحت طائلة القانون الجنائي والشرط الجزائي البالغ 100,000 ج.م.</p>
"""

doc_7_footer = """
<div style="display: grid; grid-template-columns: 1fr 1fr 80px; gap: 15px; margin-top: 10px; border-top: 1.5px solid #1a1a1a; padding-top: 8px;">
    <div style="border: 1px dashed #cbd5e1; padding: 6px; text-align: right; border-radius: 4px; height: 30mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8.5pt; font-weight: bold; color: #1a1a1a; border-bottom: 1px solid #cbd5e1; padding-bottom: 2px;">توقيع وإقرار الموظف بالالتزام</div>
        <div style="font-size: 7.5pt; line-height: 1.5;">
            الاسم الكامل: .....................................................<br>
            رقم بطاقة الرقم القومي: ......................................................
        </div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 6px; text-align: right; border-radius: 4px; height: 30mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8.5pt; font-weight: bold; color: #ff9900; border-bottom: 1px solid #ff9900; padding-bottom: 2px;">المصادقة والاعتماد من مجلس الإدارة</div>
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

PAGES_CONTENT_21_30[26] = get_contract_page_wrapper(
    "7. نموذج وإقرار الالتزام بالشروط والأحكام وسياسات العمل المعتمدة",
    7,
    doc_7_body,
    doc_7_footer
)


# ----------------- PAGE 27: Document 8 - Partner Withdrawal and Capital Recovery Request -----------------
doc_8_body = """
<p style="margin-bottom: 8px;">يقدم هذا الطلب رسمياً من الشريك الراغب في التخارج طواعية إلى مجلس إدارة شركة <strong>مارتديا للتجارة والتوزيع ذ.م.م</strong> ومستودعها، بموجب ميثاق التأسيس المعتمد وفترة الإخطار القانونية البالغة 90 يوماً:</p>

<div class="custom-form-group">
    <span class="custom-form-label">الاسم الكامل للشريك طالب الانسحاب:</span>
    <span class="custom-form-input"></span>
</div>
<div class="custom-form-group">
    <span class="custom-form-label">رقم بطاقة الرقم القومي للشريك:</span>
    <span class="custom-form-input" style="width: 250px;"></span>
    <span class="custom-form-label" style="margin-right: 15px;">الحصة الملكية:</span>
    <span class="custom-form-input" style="font-weight: bold; color: #ff9900;">25% حصرياً بالكامل</span>
</div>

<div class="legal-section-title" style="margin-top: 10px;">آلية استرداد وتصفية الحصة المالية والضوابط المحاسبية</div>
<p style="margin-bottom: 6px;">1. <strong>جرد وتدقيق مالي عاجل:</strong> يلتزم الشركاء بتشكيل لجنة جرد مالي وميداني فوري لكافة موجودات مستودعي طوخ الأقلام وقرية نقيطة لتقييم السيولة والمخزون وحجم الأرباح والخسائر للشركة.<br>
2. <strong>سداد الديون التجارية أولاً:</strong> تخصم كافة الالتزامات والديون التجارية للموردين من قيمة الحصة قبل التسوية والوفاء بها.<br>
3. <strong>آلية التقسيط الآمن:</strong> تسدد الحصة المالية المستحقة للشريك المتخارج على أربع دفعات متساوية طوال عام مالي كامل لضمان استقرار التدفق المالي كاش لمستودعات مارتديا وعدم الإضرار بميزانية شراء المنتجات الغذائية الأساسية.</p>

<p style="font-size: 7.5pt; margin-top: 6px;">[  ] كشف حساب بنكي مسجل معتمد باسم الشريك طالب التخارج لتلقي التحويل المالي.<br>
[  ] إقرار حظر المنافسة وإفشاء أسرار المنصة والزيارات الميدانية للبقالات طوال 3 سنوات اللاحقة للتخارج.</p>
"""

doc_8_footer = """
<div style="display: grid; grid-template-columns: repeat(3, 1fr) 70px; gap: 8px; margin-top: 10px; border-top: 1.5px solid #1a1a1a; padding-top: 8px;">
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: right; border-radius: 4px; height: 30mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8pt; font-weight: bold; color: #1a1a1a; border-bottom: 1px solid #cbd5e1; padding-bottom: 1px;">توقيع الشريك طالب الانسحاب</div>
        <div style="font-size: 7.2pt; line-height: 1.3;">
            الاسم: .............................<br>
            التوقيع: ...........................
        </div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: right; border-radius: 4px; height: 30mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8pt; font-weight: bold; color: #ff9900; border-bottom: 1px solid #ff9900; padding-bottom: 1px;">موافقات الشركاء الثلاثة</div>
        <div style="font-size: 7.2pt; line-height: 1.3;">
            القرار: [  ] موافقة  [  ] تأجيل للجرد<br>
            التواقيع: ...........................
        </div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: right; border-radius: 4px; height: 30mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8pt; font-weight: bold; color: #800020; border-bottom: 1px solid #800020; padding-bottom: 1px;">اعتماد المدير المالي</div>
        <div style="font-size: 7.2pt; line-height: 1.3;">
            الاسم: محمد محجوب علي مبروك<br>
            التوقيع والختم: ...................
        </div>
    </div>
    <div style="display: flex; align-items: center; justify-content: center;">
        <div class="dashed-stamp-box" style="margin: 0; width: 52px; height: 52px;"></div>
    </div>
</div>
"""

PAGES_CONTENT_21_30[27] = get_contract_page_wrapper(
    "8. طلب انسحاب وتخارج شريك واسترداد الحصة التأسيسية كاش",
    8,
    doc_8_body,
    doc_8_footer
)


# ----------------- PAGE 28: Document 9 - Official Warning Notice -----------------
doc_9_body = """
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

doc_9_footer = """
<div style="display: grid; grid-template-columns: repeat(3, 1fr) 70px; gap: 8px; margin-top: 10px; border-top: 1.5px solid #1a1a1a; padding-top: 8px;">
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: right; border-radius: 4px; height: 28mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8pt; font-weight: bold; color: #1a1a1a; border-bottom: 1px solid #cbd5e1; padding-bottom: 1px;">توقيع الموظف بالعلم والتعليل</div>
        <div style="font-size: 7.2pt; line-height: 1.3;">
            الاسم: .............................<br>
            التوقيع: ...........................
        </div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: right; border-radius: 4px; height: 28mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8pt; font-weight: bold; color: #ff9900; border-bottom: 1px solid #ff9900; padding-bottom: 1px;">توقيع مدير التشغيل</div>
        <div style="font-size: 7.2pt; line-height: 1.3;">
            الاسم: محمد وليد حمودة<br>
            التوقيع: ...........................
        </div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: right; border-radius: 4px; height: 28mm; display: flex; flex-direction: column; justify-content: space-between;">
        <div style="font-size: 8pt; font-weight: bold; color: #800020; border-bottom: 1px solid #800020; padding-bottom: 1px;">مصادقة الموارد البشرية</div>
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

PAGES_CONTENT_21_30[28] = get_contract_page_wrapper(
    "9. إنذار رسمي كتابي ولفت نظر داخلي للموظف المخالف",
    9,
    doc_9_body,
    doc_9_footer
)


# ----------------- PAGE 29: Document 10 - Managerial Delegation Agreement -----------------
doc_10_body = """
<p style="margin-bottom: 8px;">بموجب هذه الاتفاقية وميثاق التفويض التنظيمي المعتمد بالتوافق الكامل بين الشركاء الأربعة، تفوض إدارة شركة <strong>مارتديا للتجارة والتوزيع ذ.م.م</strong> ومستودعها كل من السيد <strong>محمود</strong> (شقيق الشريك محمد وليد حمودة) والسيد <strong>آدم</strong> (شقيق الشريك أحمد حسام الدين علي مبروك) كأعضاء وممثلين ميدانيين مفوضين لإدارة مستودع الشركة وأعمالها الميدانية اليومية كالتالي:</p>

<div class="legal-section-title" style="margin-top: 8px;">أولاً: صلاحيات التمثيل والنائب الميداني بالمستودعات</div>
<p style="margin-bottom: 6px;">
1. <strong>استلام ورص وتفريع الشحنات:</strong> تفويض كامل للنائبين محمود وآدم باستلام البضائع والمشروبات من الموردين ومصانع المنصورة، ومطابقتها يدوياً وإلكترونياً بمسح الباركود، ورصها على الطبالي المرتفعة مع الالتزام التام بفصل المنظفات.<br>
2. <strong>تجهيز طلبيات البقالات والعملاء:</strong> يتولى النائبان إعداد طلبيات البقالات والمنشآت المشتركة بالمنصة ومطابقة الفواتير، ومتابعة خروج البضائع وسائقي النقل المحلي (التوك توك أو التروسيكل) وتسجيل الزيارات بدقة.<br>
3. <strong>التوقيع الإداري للاستلام:</strong> يُفوّض محمود وآدم بالتوقيع الإداري على بوالص وإيصالات استلام البضائع من شركات التوزيع لإثبات الحيازة والتفريغ بالموقع.
</p>

<div class="legal-section-title" style="margin-top: 8px;">ثانياً: الرقابة والضوابط المالية الصارمة وحفظ الخزينة المركزية</div>
<p style="margin-bottom: 6px; color: #800020; font-weight: bold;">
يتعهد ويقر الطرفان بأن كامل الصلاحيات المالية والإدارة المالية المركزية وحوكمة الدفع والتلقي كاش تظل تحت السيطرة الفعالة والحصرية للمدير المالي المركزي للشركة السيد محمد محجوب علي مبروك. ويحظر حظراً تاماً على النائبين محمود وآدم تحصيل مبالغ مالية كاش من العملاء، أو سداد أي نفقات أو سلف تزيد عن 1,000 ج.م دون إذن كتابي رسمي ومسبق من المدير المالي، ويعد الإخلال بهذا الشرط إخلالاً بالأمانة الوظيفية.
</p>
"""

doc_10_footer = """
<div style="display: grid; grid-template-columns: repeat(4, 1fr) 60px; gap: 8px; margin-top: 10px; border-top: 1.5px solid #1a1a1a; padding-top: 8px;">
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: center; border-radius: 4px;">
        <div style="font-size: 7.5pt; font-weight: bold; color: #1a1a1a; margin-bottom: 2px;">توقيع: محمود</div>
        <div style="height: 10mm; border-bottom: 1.2px solid #64748b; margin-bottom: 2px;"></div>
        <div style="font-size: 7pt; color: #64748b;">النائب المفوض</div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: center; border-radius: 4px;">
        <div style="font-size: 7.5pt; font-weight: bold; color: #1a1a1a; margin-bottom: 2px;">توقيع: آدم</div>
        <div style="height: 10mm; border-bottom: 1.2px solid #64748b; margin-bottom: 2px;"></div>
        <div style="font-size: 7pt; color: #64748b;">النائب المفوض</div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: center; border-radius: 4px;">
        <div style="font-size: 7.5pt; font-weight: bold; color: #ff9900; margin-bottom: 2px;">محمد وليد حمودة</div>
        <div style="height: 10mm; border-bottom: 1.2px solid #64748b; margin-bottom: 2px;"></div>
        <div style="font-size: 7pt; color: #ff9900;">مدير التشغيل</div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: center; border-radius: 4px;">
        <div style="font-size: 7.5pt; font-weight: bold; color: #800020; margin-bottom: 2px;">محمد محجوب علي مبروك</div>
        <div style="height: 10mm; border-bottom: 1.2px solid #64748b; margin-bottom: 2px;"></div>
        <div style="font-size: 7pt; color: #800020;">المدير المالي</div>
    </div>
    <div style="display: flex; align-items: center; justify-content: center;">
        <div class="dashed-stamp-box" style="margin: 0;"></div>
    </div>
</div>
"""

PAGES_CONTENT_21_30[29] = get_contract_page_wrapper(
    "10. اتفاقية التفويض الإداري والصلاحيات التنفيذية المحدودة للنائبين الميدانيين محمود وآدم",
    10,
    doc_10_body,
    doc_10_footer
)


# ----------------- PAGE 30: Document 11 - Working Hours & Attendance Commitment -----------------
doc_11_body = """
<p style="margin-bottom: 8px;">بموجب هذه اللائحة الداخلية وميثاق الالتزام والانضباط المهني المعمد بالإجماع بشركة <strong>مارتديا للتجارة والتوزيع ذ.م.م</strong> ومستودعها، يلتزم كافة العاملين والموظفين والنواب الميدانيين والسائقين بالضوابط التنظيمية الصارمة التالية لساعات العمل والحضور والإنتاجية:</p>

<div class="legal-section-title" style="margin-top: 8px;">أولاً: ساعات العمل ونوبات التواجد والزيارات الميدانية المعتمدة</div>
<p style="margin-bottom: 6px;">
1. <strong>ساعات العمل الرسمية:</strong> تحدد ساعات العمل بمستودع طوخ الأقلام ومستودع قرية نقيطة بمعدل 8 ساعات يومياً تبدأ من الساعة 9:00 صباحاً وحتى الساعة 5:00 مساءً، طوال 6 أيام في الأسبوع مع استبعاد يوم الجمعة كإجازة دورية مشتركة.<br>
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

doc_11_footer = """
<div style="display: grid; grid-template-columns: repeat(4, 1fr) 60px; gap: 8px; margin-top: 10px; border-top: 1.5px solid #1a1a1a; padding-top: 8px;">
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: center; border-radius: 4px;">
        <div style="font-size: 7.5pt; font-weight: bold; color: #1a1a1a; margin-bottom: 2px;">أحمد حسام الدين علي مبروك</div>
        <div style="height: 10mm; border-bottom: 1.2px solid #64748b; margin-bottom: 2px;"></div>
        <div style="font-size: 7pt; color: #64748b;">توقيع شريك</div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: center; border-radius: 4px;">
        <div style="font-size: 7.5pt; font-weight: bold; color: #1a1a1a; margin-bottom: 2px;">محمد محجوب علي مبروك</div>
        <div style="height: 10mm; border-bottom: 1.2px solid #64748b; margin-bottom: 2px;"></div>
        <div style="font-size: 7pt; color: #64748b;">توقيع شريك</div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: center; border-radius: 4px;">
        <div style="font-size: 7.5pt; font-weight: bold; color: #ff9900; margin-bottom: 2px;">محمد وليد حمودة</div>
        <div style="height: 10mm; border-bottom: 1.2px solid #64748b; margin-bottom: 2px;"></div>
        <div style="font-size: 7pt; color: #ff9900;">توقيع شريك</div>
    </div>
    <div style="border: 1px dashed #cbd5e1; padding: 4px; text-align: center; border-radius: 4px;">
        <div style="font-size: 7.5pt; font-weight: bold; color: #800020; margin-bottom: 2px;">مازن السيد</div>
        <div style="height: 10mm; border-bottom: 1.2px solid #64748b; margin-bottom: 2px;"></div>
        <div style="font-size: 7pt; color: #800020;">توقيع شريك</div>
    </div>
    <div style="display: flex; align-items: center; justify-content: center;">
        <div class="dashed-stamp-box" style="margin: 0;"></div>
    </div>
</div>
"""

PAGES_CONTENT_21_30[30] = get_contract_page_wrapper(
    "11. ميثاق لائحة الانضباط المهني والالتزام بساعات العمل ونظام الحضور بمستودعات مارتديا",
    11,
    doc_11_body,
    doc_11_footer
)


# ----------------- MASTER FOUNDING AGREEMENT (PAGES 31, 32, 33) -----------------
# Document 12 of the Appendix, but the *Governing primary agreement* spanning exactly 3 pages.

# PAGE 31: MASTER AGREEMENT (PART 1 OF 3)
doc_12_p1_body = """
<p style="font-size: 8pt; font-weight: bold;">بموجب أحكام قانون الشركات رقم 159 لسنة 1981 ولائحته التنفيذية وقانون التجارة المصري رقم 17 لسنة 1999، تم إبرام هذا العقد كدستور قانوني حامٍ ومُنظّم لشركة "مارتديا للتجارة والتوزيع ذ.م.م" بين كل من:</p>
<p style="font-size: 7.5pt; line-height: 1.4;">
1. <strong>السيد أحمد حسام الدين علي مبروك</strong> - مصري الجنسية، المقيم بالإمارات (شريك مؤسس وعام)<br>
2. <strong>السيد محمد محجوب علي مبروك</strong> - مصري الجنسية، المقيم بالدقهلية (شريك مؤسس ومدير مالي)<br>
3. <strong>السيد محمد وليد حمودة</strong> - مصري الجنسية، المقيم بالدقهلية (شريك مؤسس ومدير تشغيل)<br>
4. <strong>السيد مازن السيد</strong> - مصري الجنسية، المقيم بالدقهلية (شريك مؤسس ومدير مبيعات وتوريد)
</p>

<div class="legal-section-title" style="margin-top: 6px;">مادة 1: التعريفات والأحكام التمهيدية</div>
<p>يقصد بالألفاظ التالية أينما وردت في هذا العقد المعاني المحددة لها: "الشركة" تعني شركة مارتديا للتجارة والتوزيع ذ.م.م. "الشركاء" هم الموقعون الأربعة مجتمعين. "صندوق التأسيس" يعني صندوق الـ المصروفات الرأسمالية الممول بالتساوي لتجهيز الفروع. "رأس مال التداول" يعني رأس مال شراء البضائع كاش البالغ 200,000 ج.م.</p>

<div class="legal-section-title" style="margin-top: 6px;">مادة 2: الأهلية القانونية وتأسيس الكيان</div>
<p>يقر الشركاء الأربعة بأهليتهم القانونية والشرعية والتعاقدية الكاملة لإبرام هذا الاتفاق وتأسيس الشركة وتحمل كافة الالتزامات المالية والمدنية الناشئة عن أعمالها التجارية واللوجستية بمستودع طوخ الأقلام ومستودع قرية نقيطة.</p>

<div class="legal-section-title" style="margin-top: 6px;">مادة 3: أغراض الشركة ونطاق تطبيق الاتفاق (مستودع طوخ الأقلام)</div>
<p>الغرض الرئيسي للشركة هو تجارة الجملة والتوزيع، التعبئة والتغليف، تشغيل المستودعات الذكية والمنصات السحابية لتوريد وتوصيل الأغذية والمشروبات والمنظفات للبقالات وسوبرماركت ومقاهي الدلتا والمحافظات الإقليمية بمصر. ويقر الشركاء الأربعة صراحةً بأن هذا العقد التأسيسي ينطبق <strong>حصرياً وبشكل قاطع</strong> على <strong>مستودع طوخ الأقلام</strong> وما يرتبط به من أعمال تأسيسية وأنشطة لوجستية وتشغيلية، وأن أي فروع أو مستودعات مستقبلية للشركة - بما في ذلك فرع <strong>قرية نقيطة</strong> المخطط له أو أي مواقع جغرافية أخرى - تخضع حتماً لملحقات عقدية مستقلة أو تعديلات اتفاقية موثقة يتم اعتمادها والتوقيع عليها بالإجماع من الشركاء لاحقاً.</p>

<div class="legal-section-title" style="margin-top: 6px;">مادة 4: رأس المال التأسيسي وتوزيع الحصص الملكية</div>
<p>حدد رأس مال تداول البضائع كاش بمبلغ <strong>200,000 جنيه مصري</strong> مقسم بالتساوي والعدل التام بين الشركاء الأربعة، بواقع <strong>50,000 جنيه مصري</strong> لكل شريك، وتوزع الحصص والملكيات والأرباح والخسائر بنسبة <strong>25%</strong> لكل شريك كاش دون أي تمييز.</p>

<div class="legal-section-title" style="margin-top: 6px;">مادة 5: موازنة التجهيز والـ المصروفات الرأسمالية المشترك المنفصل</div>
<p>اتفق الشركاء على تخصيص صندوق نفقات تأسيسية رأسمالية (المصروفات الرأسمالية) مستقل تماماً بقيمة <strong>60,000 ج.م</strong> (بواقع 15,000 ج.م لكل شريك بالتساوي) لشراء الحواسب، الكاميرات الذكية Tapo، قارئ الباركود، التراخيص السحابية، الأرفف والطبالي، ولا يجوز سحب أي مبالغ من كابيتال البضائع (200k ج.م) لهذه الأغراض.</p>

<div class="legal-section-title" style="margin-top: 6px;">مادة 6: السياسات المالية والتحكم المركزي الفوري</div>
<p>تخضع جميع التدفقات المالية لـ مارتديا لرقابة مالية مركزية صارمة، ويتعهد كافة الشركاء والنواب بتوريد المقبوضات كاش يومياً للخزينة المركزية أو الحساب البنكي المعتمد تحت إشراف وتدقيق المدير المالي السيد محمد محجوب علي مبروك.</p>

<div class="legal-section-title" style="margin-top: 6px;">مادة 7: الدورة المحاسبية والقوائم المالية والدفاتر</div>
<p>يلتزم المدير المالي بإمساك دفاتر تجارية منتظمة ومطابقة للأصول المحاسبية القياسية، وتولد لوحة التحكم السحابية WMS تقارير جرد أسبوعية وقوائم دخل دورية شهرية لمطابقتها مع الأرصدة البنكية والخزينة.</p>
"""

PAGES_CONTENT_21_30[31] = get_master_agreement_page_wrapper(
    31, 33,
    "عقد الشراكة التأسيسي الرئيسي والحاكم لشركة مارتديا للتجارة والتوزيع ذ.م.م (1/3)",
    doc_12_p1_body,
    show_continuation=True
)


# PAGE 32: MASTER AGREEMENT (PART 2 OF 3)
doc_12_p2_body = """
<div class="legal-section-title" style="margin-top: 2px;">مادة 8: السنة المالية والدورات التشغيلية للشركة</div>
<p>تبدأ السنة المالية للشركة من أول يناير وتنتهي في الحادي والثلاثين من ديسمبر من كل عام ميلادي، على أن تبدأ السنة المالية الأولى استثناءً من تاريخ نفاذ هذا العقد وحتى 31 ديسمبر من العام التالي.</p>

<div class="legal-section-title" style="margin-top: 4px;">مادة 9: فتح وتشغيل الحسابات البنكية وحوكمة الصرف كاش</div>
<p>تفتح الشركة حساباً جاريّاً رسمياً باسمها لدى أحد البنوك المصرية المعتمدة بالدقهلية، ويكون للمدير المالي محمد محجوب علي مبروك منفرداً حق التوقيع والسحب والإيداع وإبرام التحويلات البنكية للشركاء والموردين.</p>

<div class="legal-section-title" style="margin-top: 4px;">مادة 10: قواعد توزيع الأرباح والاحتياطي النظامي</div>
<p>توزع الأرباح التشغيلية الصافية للشركة بنسبة حصص الشركاء (25% لكل شريك) بعد اقتطاع احتياطي مالي نظامي بنسبة 10% من الأرباح لمواجهة الطوارئ، واستبقاء جزء تراكمي بنسبة 15% كأرباح محتجزة لتمويل تمدد فروع قرية نقيطة والإسماعيلية.</p>

<div class="legal-section-title" style="margin-top: 4px;">مادة 11: سياسة توزيع الأرباح وفترة استبقاء السيولة التأسيسية</div>
<p>تقرر معالجة وصرف توزيعات الأرباح الدورية للشركاء بشكل طبيعي في <strong>اليوم الخامس عشر (15) من كل شهر ميلادي</strong>، ويشترط لذلك اعتماد القوائم المالية والمطابقة المحاسبية وتوفر التدفقات النقدية الكافية بالشركة. واستثناءً من القاعدة العامة، يُحظر تماماً توزيع أي أرباح طوال <strong>الأشهر الثلاثة الأولى</strong> التالية لبدء العمليات والنشاط التشغيلي الفعلي للشركة، وتُحتجز كافة الأرباح المحققة خلال هذه الفترة التأسيسية الأولى وتُعاد استثمارها بالكامل لتعزيز رأس المال العامل، وتدعيم المخزون السلعي، وتثبيت الاستقرار التشغيلي وتمويل تمدد ونمو فروع الشركة.</p>

<div class="legal-section-title" style="margin-top: 4px;">مادة 12: تخصيص وتوزيع الخسائر المالية وحماية الأصول</div>
<p>في حال تحقق أي خسائر تشغيلية، يتحملها الشركاء الأربعة بالتساوي التام وبنسبة حصصهم الملكية (25% لكل شريك)، وتغطى الخسائر من الاحتياطي النظامي المالي أولاً قبل المساس بكابيتال تداول البضائع.</p>

<div class="legal-section-title" style="margin-top: 4px;">مادة 13: سلطات مجلس الإدارة المشترك والتصويت</div>
<p>يتكون مجلس الإدارة من الشركاء الأربعة مجتمعين، وتتمتع القرارات العادية بالأغلبية البسيطة للأصوات (بمعدل صوت واحد لكل شريك)، وتتم معالجة الأصوات المتساوية من خلال مراجعة وتعديل المقترح بالتوافق.</p>

<div class="legal-section-title" style="margin-top: 4px;">مادة 14: المسائل المحفوظة والتي تتطلب الإجماع المطلق</div>
<p>يتطلب اتخاذ القرارات التالية موافقة كتابية بالإجماع المطلق (100% من الشركاء): تعديل كابيتال الشركة، رهن العقارات، رهن أصول المستودعات، الاقتراض من البنوك، إدخال شريك جديد، أو حل وتصفية الكيان قانوناً.</p>

<div class="legal-section-title" style="margin-top: 4px;">مادة 15: التزامات وحقوق الشركاء المؤسسين والنواب الميدانيين</div>
<p>يتعهد كل شريك أو نائب مفوض (محمود وآدم) بأداء مهامه بكل أمانة وإخلاص، ويحظر حظراً تاماً على النواب الميدانيين تحصيل أو سداد أي نفقات تزيد عن 1,000 ج.م دون إذن المدير المالي.</p>

<div class="legal-section-title" style="margin-top: 4px;">مادة 16: تضارب المصالح وحوكمة المعاملات التجارية</div>
<p>يمتنع على أي شريك أو موظف إبرام صفقات شراء بضائع لحسابه الشخصي أو تحقيق مصالح وعوائد مالية خفية من الموردين، وتتم جميع عقود التوريد بمطابقة الأسعار الفعلية كاش لشركات المنصورة.</p>

<div class="legal-section-title" style="margin-top: 4px;">مادة 17: السرية المطلقة وحفظ وحماية قواعد بيانات المنصة</div>
<p>بيانات البقالات والمشتركين والزيارات الميدانية وأسعار الشراء والخصومات هي سر تجاري مطلق مملوك لـ مارتديا، ويتعهد الشركاء والنواب بعدم إفشاء أو استخدام هذه البيانات خارج العمل طوال مدة العقد و3 سنوات بعد التخارج.</p>

<div class="legal-section-title" style="margin-top: 4px;">مادة 18: الملكية الفكرية لبراءات وتطبيق مارتديا</div>
<p>تعد الشيفرة البرمجية للتطبيق، وقواعد بيانات AWS السحابية، والتصاميم والشعارات والهوية البصرية ملكية فكرية حصرية لشركة مارتديا ذ.م.م، ولا يجوز لأي شريك منفرداً المطالبة بها أو استغلالها شخصياً.</p>
"""

PAGES_CONTENT_21_30[32] = get_master_agreement_page_wrapper(
    32, 33,
    "عقد الشراكة التأسيسي الرئيسي والحاكم لشركة مارتديا للتجارة والتوزيع ذ.م.م (2/3)",
    doc_12_p2_body,
    show_continuation=True
)


# PAGE 33: MASTER AGREEMENT (PART 3 OF 3)
doc_12_p3_body = """
<div class="legal-section-title" style="margin-top: 2px;">مادة 19: حيازة وحفظ الأصول وتجهيزات المستودعات الرأسمالية (المصروفات الرأسمالية)</div>
<p>تعتبر كاميرات المراقبة Tapo C225، بطاقات 256GB، أجهزة الـ POS، راوتر، الأرفف المعدنية، وطبالي الرص بمثابة أصول رأسمالية دائمة ومملوكة للشركة، وتظل محتفظة بصفة الحيازة المشتركة لـ مارتديا وغير قابلة للاسترداد الفردي عند التخارج.</p>

<div class="legal-section-title" style="margin-top: 4px;">مادة 20: قبول ودخول شركاء جدد للكيان اللوجستي</div>
<p>يجوز قبول شريك جديد في الشركة بموافقة الشركاء الأربعة كتابةً وبالإجماع، شريطة سداده لحصة نقدية كاش إضافية تتناسب مع التقييم الفني والمحاسبي لأصول وعملاء منصة ومستودعات مارتديا وقت الدخول.</p>

<div class="legal-section-title" style="margin-top: 4px;">مادة 21: قواعد التنازل عن الحصص وانتقال الملكيات</div>
<p>يحظر على الشريك بيع أو رهْن حصته التأسيسية للغير إلا بعد عرضها أولاً على بقية الشركاء بموجب حق الشفعة القانوني بإخطار رسمي، وفي حال رفضهم الشراء يجوز له التصرف بها بعد موافقة مجلس الإدارة بالإجماع.</p>

<div class="legal-section-title" style="margin-top: 4px;">مادة 22: التخارج الطوعي وتصفية الحصص النقدية وسداد الديون</div>
<p>عند رغبة شريك في التخارج طواعية، يلتزم بإخطار بقية الشركاء قبل 90 يوماً على الأقل، وتُقيم حصته المحاسبية بناءً على جرد فعلي شامل للأصول والمخزون، وتُسدد له القيمة المستحقة على 4 دفعات متساوية طوال عام مالي كامل لحماية التدفق المالي كاش للمشتريات.</p>

<div class="legal-section-title" style="margin-top: 4px;">مادة 23: الوفاة أو العجز الدائم أو الإفلاس لأحد الشركاء</div>
<p>في حالة وفاة أحد الشركاء أو عجزه الدائم أو إفلاسه المالي، لا تحل الشركة قانوناً بل تستمر بين بقية الشركاء، وتنتقل الحصة المالية للورثة الشرعيين بموجب إعلان وراثة رسمي، شريطة توكيل وريث واحد يمثلهم أمام مجلس إدارة مارتديا.</p>

<div class="legal-section-title" style="margin-top: 4px;">مادة 24: بند عدم المنافسة وعدم استقطاب عملاء المنصة</div>
<p>يتعهد كل شريك ونوابهم الميدانيون بعدم تأسيس أو المشاركة في أي نشاط تجاري أو لوجستي منافس لشركة مارتديا بالدقهلية أو الدلتا طوال مدة شراكتهم ولمدة 3 سنوات لاحقة لتاريخ تخارجهم الفعلي، تحت طائلة الالتزام بشرط جزائي رادع مقداره 500,000 ج.م.</p>

<div class="legal-section-title" style="margin-top: 4px;">مادة 25: القانون الواجب التطبيق والاختصاص القضائي بالمحاكم المصرية</div>
<p>يخضع هذا العقد وتفسيره وتنفيذه بالكامل لأحكام القوانين المعمول بها بجمهورية مصر العربية، وينعقد الاختصاص القضائي الحصري للنظر في أي نزاع ينشأ عنه لمحاكم المنصورة والسنبلاوين التجارية والمدنية بمختلف درجاتها.</p>

<div class="legal-section-title" style="margin-top: 4px;">مادة 26: نسخ العقد ونفاذه الفعلي وتوقيع الشركاء الأربعة</div>
<p>حرر هذا العقد والاتفاق الحاكم من خمس نسخ أصلية، بيد كل شريك نسخة للعمل بها والاحتفاظ بها بملفه، وحفظ النسخة الخامسة الرسمية بمستندات وأرشيف الشركة القانوني بمستودع طوخ الأقلام، ويعتبر نافذاً وسارياً بمجرد توقيعه يدوياً.</p>
"""

# Page 33 is the final page of the entire document - complete execution and signatures
PAGES_CONTENT_21_30[33] = get_master_agreement_page_wrapper(
    33, 33,
    "عقد الشراكة التأسيسي الرئيسي والحاكم لشركة مارتديا للتجارة والتوزيع ذ.م.م (3/3)",
    doc_12_p3_body,
    show_continuation=False
)

print("pages_21_30.py completely shifted with Pages 26 to 33!")
