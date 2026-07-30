# -*- coding: utf-8 -*-
import sys

# Define Pages 32 to 48 for V Smart General Trading L.L.C.
PAGES_CONTENT_21_30 = {}


def render_legal_document(title_ar, title_en, doc_ref, body_html, footer_type="standard", partner_label="الشريك المعني"):
    """
    Renders a unified, extremely professional standalone A4 legal document with corporate headers,
    metadata table, body, signature fields, financial manager signoff, and company stamp placeholder.
    """
    html = f"""
    <!-- Legal Header Table -->
    <table class="legal-header-table">
        <tr>
            <td style="width: 25%; font-weight: bold;">اسم الشركة:</td>
            <td style="width: 40%;">شركة في سمارت للتجارة العامة ذ.م.م</td>
            <td style="width: 15%; font-weight: bold;">رقم المستند:</td>
            <td style="width: 20%;">{doc_ref}</td>
        </tr>
        <tr>
            <td style="font-weight: bold;">الإدارة المصدرة:</td>
            <td>الإدارة القانونية والمالية المشتركة</td>
            <td style="font-weight: bold;">تاريخ الإصدار:</td>
            <td>29 يوليو 2026</td>
        </tr>
        <tr>
            <td style="font-weight: bold;">إعداد:</td>
            <td>الشؤون القانونية والمحاسبة</td>
            <td style="font-weight: bold;">مراجعة واعتماد:</td>
            <td>مجلس إدارة V Smart General Trading</td>
        </tr>
    </table>

    <div class="legal-title">
        <div style="font-size: 11pt; font-weight: 800; color: #0f172a; letter-spacing: 0.5px;">{title_ar}</div>
        <div style="font-size: 7.5pt; font-weight: bold; color: #475569; margin-top: 2px;">{title_en}</div>
    </div>

    <div class="legal-body">
        {body_html}
    </div>
    """

    if footer_type == "witness":
        html += f"""
        <div class="legal-footer-grid-witness">
            <div class="legal-footer-box">
                <span style="font-weight: bold; color: #0f172a; border-bottom: 1px solid #cbd5e1; padding-bottom: 2px; display: block; margin-bottom: 4px;">توقيع الطرف المعني / الشركاء</span>
                <div style="text-align: right; font-size: 6.5pt; flex-grow: 1;">
                    الاسم: <span class="print-field" style="min-width: 90px; height: 10px; border-bottom-style: dotted;"></span><br>
                    الصفة: <span class="print-field" style="min-width: 90px; height: 10px; border-bottom-style: dotted;"></span><br>
                    التوقيع: <span class="print-field" style="min-width: 90px; height: 10px; border-bottom-style: dotted;"></span>
                </div>
            </div>
            <div class="legal-footer-box" style="border-style: solid; border-color: #0284c7;">
                <span style="font-weight: bold; color: #0284c7; border-bottom: 1px solid #0284c7; padding-bottom: 2px; display: block; margin-bottom: 4px;">اعتماد وختم الشركة الرسمي</span>
                <div style="flex-grow: 1; display: flex; align-items: center; justify-content: center; flex-direction: column;">
                    <div class="stamp-box">V SMART STAMP</div>
                    <span style="font-size: 5pt; color: #64748b; margin-top: 3px;">خاتم الشركة القانوني والتشغيلي</span>
                </div>
            </div>
            <div class="legal-footer-box">
                <span style="font-weight: bold; color: #0f172a; border-bottom: 1px solid #cbd5e1; padding-bottom: 2px; display: block; margin-bottom: 4px;">الشهود القانونيون (Witnesses)</span>
                <div style="text-align: right; font-size: 6.5pt; flex-grow: 1; line-height: 1.35;">
                    شاهد 1: <span class="print-field" style="min-width: 80px; height: 10px; border-bottom-style: dotted;"></span><br>
                    التوقيع: <span class="print-field" style="min-width: 80px; height: 10px; border-bottom-style: dotted;"></span><br>
                    شاهد 2: <span class="print-field" style="min-width: 80px; height: 10px; border-bottom-style: dotted;"></span><br>
                    التوقيع: <span class="print-field" style="min-width: 80px; height: 10px; border-bottom-style: dotted;"></span>
                </div>
            </div>
        </div>
        """
    else:
        html += f"""
        <div class="legal-footer-grid">
            <div class="legal-footer-box">
                <span style="font-weight: bold; color: #0f172a; border-bottom: 1px solid #cbd5e1; padding-bottom: 2px; display: block; margin-bottom: 4px;">توقيع ومصادقة الشركاء</span>
                <div style="text-align: right; font-size: 6.5pt; flex-grow: 1; line-height: 1.45;">
                    الاسم: <span class="print-field" style="min-width: 90px; height: 10px; border-bottom-style: dotted;"></span><br>
                    الصفة: <span class="print-field" style="min-width: 90px; height: 10px; border-bottom-style: dotted;"></span><br>
                    البطاقة: <span class="print-field" style="min-width: 90px; height: 10px; border-bottom-style: dotted;"></span><br>
                    التوقيع: <span class="print-field" style="min-width: 90px; height: 10px; border-bottom-style: dotted;"></span>
                </div>
            </div>
            <div class="legal-footer-box" style="border-style: solid; border-color: #0f172a;">
                <span style="font-weight: bold; color: #0f172a; border-bottom: 1px solid #cbd5e1; padding-bottom: 2px; display: block; margin-bottom: 4px;">مساحة الختم والمطابقة</span>
                <div style="flex-grow: 1; display: flex; align-items: center; justify-content: center; flex-direction: column;">
                    <div class="stamp-box">V SMART STAMP</div>
                    <span style="font-size: 5pt; color: #64748b; margin-top: 3px;">خاتم الإدارة المالية والقانونية</span>
                </div>
            </div>
            <div class="legal-footer-box" style="border-style: solid; border-color: #b45309;">
                <span style="font-weight: bold; color: #b45309; border-bottom: 1px solid #b45309; padding-bottom: 2px; display: block; margin-bottom: 4px;">اعتماد وتوقيع المدير المالي للشركة</span>
                <div style="text-align: right; font-size: 6.5pt; flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between;">
                    <div>الاسم: محمد محجوب مبروك</div>
                    <div>الصفة: المدير المالي المركزي للشركة</div>
                    <div>توقيع المدير المالي: <span class="print-field" style="min-width: 90px; height: 10px; border-bottom-style: dotted;"></span></div>
                </div>
            </div>
        </div>
        """
    return html


# ----------------- PAGE 32: Salary and Profit Transfer Authorization -----------------
PAGES_CONTENT_21_30[32] = render_legal_document(
    "16. استمارة تفويض تحويل الرواتب والأرباح الدورية للشركاء والمديرين",
    "Salary and Profit Transfer Authorization & Payment Order",
    "Ref-VS-016",
    """
    <p>تستخدم هذه الاستمارة لمنح تفويض صريح للإدارة المالية المركزية لشركة <strong>V Smart General Trading L.L.C.</strong> بتحويل كافة المستحقات من رواتب إدارية وتوزيعات الأرباح للشركاء:</p>

    <div class="legal-section-title">أولاً: بيانات المفوض والمستفيد</div>
    <table class="legal-form-table">
        <tr>
            <td style="width:30%; font-weight:bold; background:#f8fafc;">الاسم الكامل للمستفيد:</td>
            <td style="width:70%;"><span class="print-field" style="min-width:250px;"></span></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">المسمى الوظيفي والصفة القانونية:</td>
            <td>[  ] شريك مؤسس  [  ] ممثل ميداني  [  ] مدير تنفيذي  [  ] أخرى</td>
        </tr>
    </table>

    <div class="legal-section-title">ثانياً: نوع وتفاصيل الحساب وتفويض الخصم والتحويل</div>
    <p>بموجب هذا المستند، أفوض الإدارة المالية المركزية رسمياً بتحويل:</p>
    <div class="print-box" style="line-height: 1.5; font-size: 7.2pt;">
        [  ] الراتب والبدلات الشهرية المقررة بقيمة: <span class="print-field" style="min-width:100px;"></span> ج.م<br>
        [  ] نسبة الأرباح الموزعة السنوية البالغة 25% من مجموع الحصص المحققة.<br>
        التحويل إلى حسابي البنكي المسجل رسمياً بفرع بنك: <span class="print-field" style="min-width:120px;"></span> رقم الآيبان: <span class="print-field" style="min-width:180px;"></span>
    </div>
    <p style="margin-top:5px; font-size:6.5pt; color:#475569;">* يعتبر هذا التفويض مستنداً سارياً لإبراء ذمة الإدارة المالية تماماً فور إثبات التحويل البنكي أو قيد السند البنكي بدفاتر الشركة.</p>
    """,
    "standard"
)

# ----------------- PAGE 33: Advance Payment Request Form -----------------
PAGES_CONTENT_21_30[33] = render_legal_document(
    "17. نموذج وطلب سلفة ودفعات مالية مقدمة عهدة تشغيلية",
    "Official Advance Payment Request Form",
    "Ref-VS-017",
    """
    <p>طلب مالي يقدم للإدارة المالية لشركة <strong>V Smart General Trading L.L.C.</strong> لاعتماد سلفة مالية أو دفعة مقدمة لتسيير الأعمال الطارئة بالمستودعات:</p>

    <div class="legal-section-title">أولاً: تفاصيل وقيمة السلفة المطلوبة</div>
    <table class="legal-form-table">
        <tr>
            <td style="width:30%; font-weight:bold; background:#f8fafc;">الاسم مقدم الطلب:</td>
            <td style="width:70%;"><span class="print-field" style="min-width:250px;"></span></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">المبلغ المطلوب بالأرقام (ج.م):</td>
            <td><strong><span class="print-field" style="min-width:150px;"></span> جنيه مصري</strong></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">المبرر التجاري والجدوى للطلب:</td>
            <td><span class="print-field" style="min-width:250px; height:20px;"></span></td>
        </tr>
    </table>

    <div class="legal-section-title">ثانياً: طريقة السداد والخصم المحاسبي المقترح</div>
    <p>يتعهد مقدم الطلب برد السلفة أو تسوية العهدة بموجب إيصالات فواتير معتمدة في موعد أقصاه <span class="print-field" style="min-width:100px;"></span>، أو خصمها من مستحقاته كالتالي:</p>
    <p>[  ] خصم دفعة واحدة من راتب الشهر القادم  [  ] تقسيط على <span class="print-field" style="min-width:40px;"></span> أقساط شهرية متساوية.</p>

    <div class="legal-section-title">ثالثاً: مراجعة واعتماد الإدارة المالية الحسابية</div>
    <p>توصية إدارة الحسابات: [  ] مقبول بالكامل  [  ] مرفوض مع التعليل  [  ] معلق لحين جلب فواتير العهد السابقة.</p>
    """,
    "standard"
)

# ----------------- PAGE 34: Cash Receipt Acknowledgement -----------------
PAGES_CONTENT_21_30[34] = render_legal_document(
    "18. سند استلام نقدية وإيصال قبض كاش رسمي للشركة",
    "Official Cash Receipt Acknowledgement",
    "Ref-VS-018",
    """
    <p>يستخدم لتوثيق عمليات استلام النقدية (الكاش) المقبوضة فورا لصالح خزينة شركة <strong>V Smart General Trading L.L.C.</strong> من العملاء أو الشركاء:</p>

    <div class="legal-section-title">أولاً: تفاصيل النقدية المقبوضة والمطابقة</div>
    <table class="legal-form-table">
        <tr>
            <td style="width:30%; font-weight:bold; background:#f8fafc;">رقم السند المالي المقيد:</td>
            <td style="width:70%;"><span class="print-field" style="min-width:250px;"></span></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">استلمنا من السيد / الشركة:</td>
            <td><span class="print-field" style="min-width:250px;"></span></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">مبلغ وقدره بالأرقام والحروف:</td>
            <td><strong><span class="print-field" style="min-width:250px;"></span></strong></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">وذلك مقابل استحقاق:</td>
            <td>[  ] ثمن بضائع مبيعات POS  [  ] سداد حصة رأس مال  [  ] أخرى: <span class="print-field" style="min-width:100px;"></span></td>
        </tr>
    </table>

    <div class="legal-section-title">ثانياً: تفاصيل وعملية الحفظ والاعتماد بالخزينة</div>
    <p>أقر أنا أمين الخزينة المستلم بأن المبلغ المذكور أعلاه قد تم جرد ومطابقة سلامته النقدية بالكامل وقيده بدفاتر الخزينة المركزية للشركة بموجب هذا المستند.</p>
    """,
    "standard"
)

# ----------------- PAGE 35: Cash Payment Authorization -----------------
PAGES_CONTENT_21_30[35] = render_legal_document(
    "19. إذن صرف نقدية وتفويض مالي كاش معتمد للشركة",
    "Official Cash Payment Authorization",
    "Ref-VS-019",
    """
    <p>يستخدم هذا المستند لاعتماد وصرف المبالغ النقدية كاش من الخزينة لـشركة <strong>V Smart General Trading L.L.C.</strong> لتغطية النفقات العادية والطارئة:</p>

    <div class="legal-section-title">أولاً: بيانات الصرف والقيمة المستهدفة</div>
    <table class="legal-form-table">
        <tr>
            <td style="width:30%; font-weight:bold; background:#f8fafc;">يصرف كاش إلى السيد:</td>
            <td style="width:70%;"><span class="print-field" style="min-width:250px;"></span></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">مبلغ وقدره بالأرقام والحروف:</td>
            <td><strong><span class="print-field" style="min-width:250px;"></span></strong></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">بند النفقة المحدد بالدفاتر:</td>
            <td>[  ] إيجار مستودع  [  ] فواتير إنترنت/كهرباء  [  ] شراء بضائع عاجلة  [  ] صيانة</td>
        </tr>
    </table>

    <div class="legal-section-title">ثانياً: الاعتمادات المالية والرقابة الحسابية والتوقيع</div>
    <p>يتعهد موظف الصرف بمطابقة الفواتير الضريبية الأصلية وإرفاقها بهذا السند لإنهاء قيد التسوية المحاسبي بالدفاتر المالية فوراً.</p>
    """,
    "standard"
)

# ----------------- PAGE 36: Asset Handover Form -----------------
PAGES_CONTENT_21_30[36] = render_legal_document(
    "20. نموذج تسليم واستلام العهد والأصول الرأسمالية للشركة",
    "Official Asset Handover & Receipt Form",
    "Ref-VS-020",
    """
    <p>نموذج مخصص لإثبات وحفظ عهدة الأصول التقنية والإلكترونية والمعدات الممنوحة للموظفين في شركة <strong>V Smart General Trading L.L.C.</strong>:</p>

    <div class="legal-section-title">أولاً: بيانات الطرف المستلم والموظف المسؤول</div>
    <table class="legal-form-table">
        <tr>
            <td style="width:30%; font-weight:bold; background:#f8fafc;">الاسم الكامل للمستلم:</td>
            <td style="width:70%;"><span class="print-field" style="min-width:250px;"></span></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">الوظيفة والقسم بالهيكل:</td>
            <td>[  ] نائب ميداني  [  ] مندوب توزيع  [  ] مسؤول لوجستي  [  ] أخرى</td>
        </tr>
    </table>

    <div class="legal-section-title">ثانياً: مواصفات وحالة الأصول المسلمة عهدة</div>
    <table class="legal-form-table">
        <tr style="background:#f8fafc; font-weight:bold;">
            <td>اسم الأصل / الجهاز بالتفصيل</td>
            <td>الرقم التسلسلي Serial Number</td>
            <td>الحالة الفنية عند التسليم</td>
            <td>القيمة التقديرية للأصل</td>
        </tr>
        <tr>
            <td>1. جهاز حاسوب POS ومشتملاته</td>
            <td><span class="print-field" style="min-width:100px;"></span></td>
            <td>[  ] جديد  [  ] ممتاز  [  ] مستعمل بحالة جيدة</td>
            <td><span class="print-field" style="min-width:80px;"></span></td>
        </tr>
        <tr>
            <td>2. قارئ الباركود اللاسلكي الذكي</td>
            <td><span class="print-field" style="min-width:100px;"></span></td>
            <td>[  ] جديد  [  ] ممتاز  [  ] مستعمل بحالة جيدة</td>
            <td><span class="print-field" style="min-width:80px;"></span></td>
        </tr>
        <tr>
            <td>3. طابعة فواتير وإيصالات حرارية</td>
            <td><span class="print-field" style="min-width:100px;"></span></td>
            <td>[  ] جديد  [  ] ممتاز  [  ] مستعمل بحالة جيدة</td>
            <td><span class="print-field" style="min-width:80px;"></span></td>
        </tr>
    </table>

    <div class="legal-section-title">ثالثاً: إقرار وتعهد بالحفاظ والتسليم عند الطلب</div>
    <p style="font-size: 6.5pt; color: #475569;">يتعهد الموقّع أدناه بالحفاظ التام على الأصول المسلمة إليه واستخدامها الحصري لأغراض العمل، وإعادتها فوراً وبحالة فنية سليمة للشركة عند الطلب أو إنهاء خدماته.</p>
    """,
    "standard"
)

# ----------------- PAGE 37: Warehouse Responsibility Handover Form -----------------
PAGES_CONTENT_21_30[37] = render_legal_document(
    "21. نموذج تسليم واستلام العهد والمسؤولية الكاملة للمستودع",
    "Warehouse Responsibility Handover Form",
    "Ref-VS-021",
    """
    <p>مستند رسمي لإثبات ونقل عهدة المخزون والمسؤولية الأمنية واللوجستية بمستودع <strong>تاجر</strong> التابع لـشركة <strong>V Smart General Trading L.L.C.</strong>:</p>

    <div class="legal-section-title">أولاً: بيانات أطراف عملية التسليم والاستلام الميداني</div>
    <table class="legal-form-table">
        <tr>
            <td style="width:25%; font-weight:bold; background:#f8fafc;">المستودع الجغرافي:</td>
            <td style="width:35%;">[  ] طوخ الأقلام  [  ] ميت خميس</td>
            <td style="width:15%; font-weight:bold; background:#f8fafc;">تاريخ الاستلام:</td>
            <td style="width:25%;"><span class="print-field" style="min-width:100px;"></span></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">المسلّم المسؤول الحالي:</td>
            <td><span class="print-field" style="min-width:140px;"></span></td>
            <td style="font-weight:bold; background:#f8fafc;">المستلم المسؤول الجديد:</td>
            <td><span class="print-field" style="min-width:100px;"></span></td>
        </tr>
    </table>

    <div class="legal-section-title">ثانياً: مطابقة جرد المخزون الفعلي والأصول الثابتة</div>
    <p>تم إجراء جرد شامل ومطابقة تامة لمحتويات المستودع وأسفرت النتيجة عن:</p>
    <div class="print-box" style="line-height: 1.4; font-size:7pt;">
        - إجمالي عدد كراتين المنتجات الغذائية والمشروبات الفعلي: <span class="print-field" style="min-width:100px;"></span> كرتونة.<br>
        - حالة النظافة والتهوية والتأمين العام للمستودع: [  ] ممتاز وخالي من الملاحظات  [  ] ملاحظات مدونة بالتقرير الملحق.<br>
        - حالة وجودة أجهزة كاميرات المراقبة الـ CCTV والتأمين الإلكتروني: [  ] سليم وتعمل بالكامل.
    </div>
    <p style="margin-top:5px; font-size:6.5pt; color:#475569;">* بموجب التوقيع أدناه، تنتقل المسؤولية الأمنية واللوجستية والمالية الكاملة للمستودع ومخزونه إلى عهدة المستلم الجديد.</p>
    """,
    "witness"
)

# ----------------- PAGE 38: Employee Appointment Approval Form -----------------
PAGES_CONTENT_21_30[38] = render_legal_document(
    "22. نموذج واعتماد تعيين موظف وانضمامه لهيكل العمل للشركة",
    "Employee Appointment Approval Form",
    "Ref-VS-022",
    """
    <p>يستخدم لاعتماد تعيين الموظفين والعمال في شركة <strong>V Smart General Trading L.L.C.</strong> ومستودعات تاجر وتحديد ميزانية الرواتب والبدلات:</p>

    <div class="legal-section-title">أولاً: البيانات الشخصية والمهنية للمرشح للوظيفة</div>
    <table class="legal-form-table">
        <tr>
            <td style="width:30%; font-weight:bold; background:#f8fafc;">الاسم الكامل للمرشح:</td>
            <td style="width:70%;"><span class="print-field" style="min-width:250px;"></span></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">المسمى الوظيفي المستهدف:</td>
            <td>[  ] نائب ميداني  [  ] مندوب توزيع  [  ] أمين مخزن  [  ] عامل تجميع</td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">القسم بالهيكل الاستراتيجي:</td>
            <td><span class="print-field" style="min-width:250px;"></span></td>
        </tr>
    </table>

    <div class="legal-section-title">ثانياً: تفاصيل الراتب الأساسي والامتيازات والبدلات المعتمدة</div>
    <table class="legal-form-table">
        <tr>
            <td style="width:25%; font-weight:bold; background:#f8fafc;">الراتب الأساسي (ج.م):</td>
            <td style="width:25%;"><span class="print-field" style="min-width:100px;"></span></td>
            <td style="width:25%; font-weight:bold; background:#f8fafc;">البدلات والحوافز البيعية:</td>
            <td style="width:25%;"><span class="print-field" style="min-width:100px;"></span></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">تاريخ مباشرة العمل الفعلي:</td>
            <td><span class="print-field" style="min-width:100px;"></span></td>
            <td style="font-weight:bold; background:#f8fafc;">فترة التجربة والتقييم:</td>
            <td>3 أشهر (مائة وعشرون يوماً)</td>
        </tr>
    </table>

    <div class="legal-section-title">ثالثاً: قرار ومصادقة مجلس الإدارة المشترك والشركاء</div>
    <p>تم مراجعة الطلب والموافقة على التعيين: [  ] مقبول  [  ] مرفوض  [  ] معلق للحصول على المستندات الرسمية.</p>
    """,
    "standard"
)

# ----------------- PAGE 39: Internal Warning Notice -----------------
PAGES_CONTENT_21_30[39] = render_legal_document(
    "23. نموذج وإنذار ولفت نظر رسمي داخلي للموظفين المقصرين",
    "Official Internal Warning Notice",
    "Ref-VS-023",
    """
    <p>نموذج رسمي يوجه للموظفين والعمال في حالة التقصير المهني أو إهمال السلامة ومستلزمات الأمن بمستودعات <strong>تاجر</strong>:</p>

    <div class="legal-section-title">أولاً: بيانات الموظف الموجه إليه لفت النظر والإنذار</div>
    <table class="legal-form-table">
        <tr>
            <td style="width:30%; font-weight:bold; background:#f8fafc;">اسم الموظف بالكامل:</td>
            <td style="width:70%;"><span class="print-field" style="min-width:250px;"></span></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">المسمى الوظيفي والمستودع:</td>
            <td><span class="print-field" style="min-width:250px;"></span></td>
        </tr>
    </table>

    <div class="legal-section-title">ثانياً: أسباب لفت النظر ووصف المخالفة المرتكبة</div>
    <div class="print-box" style="height: 38mm; font-size:7pt; line-height:1.45;">
        تاريخ المخالفة الفعلي: <span class="print-field" style="min-width:100px;"></span><br>
        وصف المخالفة التقصيرية بالتفصيل:<br>
        [  ] التقصير في عمليات كنس وتعقيم ممرات تخزين الألبان والمشروبات يومياً.<br>
        [  ] الإهمال في رص كراتين المياه على طبالي بلاستيكية مرتفعة عن الأرض 15 سم.<br>
        [  ] التأخر الغير مبرر في تسليم طلبيات مبيعات الـ POS للبقالات.<br>
        [  ] أخرى: <span class="print-field" style="min-width:350px;"></span>
    </div>

    <div class="legal-section-title">ثالثاً: الإجراء الجزئي المتخذ وتوقيع الموظف بالعلم</div>
    <p>يترتب على تكرار المخالفة المذكورة لثلاث مرات الفصل النهائي من العمل دون حقوق أو مكافآت مع تحميل الموظف قيمة التلفيات.</p>
    """,
    "standard"
)

# ----------------- PAGE 40: Confidentiality and Non-Disclosure Declaration -----------------
PAGES_CONTENT_21_30[40] = render_legal_document(
    "24. إقرار وتعهد السرية وحظر المنافسة وإفشاء أسرار المنصة",
    "Confidentiality and Non-Disclosure Agreement (NDA)",
    "Ref-VS-024",
    """
    <p>يتعهد موقع هذا الإقرار بالالتزام بالسرية المطلقة لحماية الأصول البرمجية وحركة العملاء للبقالات في شركة <strong>V Smart General Trading L.L.C.</strong>:</p>

    <div class="legal-section-title">أولاً: أطراف التعهد والبيان</div>
    <p>يتعهد الطرف الموقع أدناه (موظف/مستشار/شريك) بالحفاظ التام على سرية المعلومات التقنية والتجارية لشركة <strong>V Smart General Trading L.L.C.</strong> ومنصة <strong>تاجر</strong> ومستودعاتها.</p>

    <div class="legal-section-title">ثانياً: تعريف الأسرار التجارية والبرمجية المحظورة</div>
    <p>تشمل المعلومات السرية المحمية بموجب هذا التعهد وتعد أسرار تجارية هامة للشركة:</p>
    <div class="print-box" style="line-height:1.4; font-size:7pt;">
        - قائمة وأسماء وعناوين البقالات والسوبرماركت وقواعد البيانات المسجلة بالتطبيق.<br>
        - أسعار الشراء والخصومات والبونص كاش الممنوحة من شركات المنصورة وطنطا.<br>
        - الأكواد البرمجية وتصميم واجهات تطبيق POS ونظام الـ WMS للمستودعات.<br>
        - استراتيجية التسعير الرشيدة ونموذج "فوارق القروش" التنافسي المعتمد.
    </div>

    <div class="legal-section-title">ثالثاً: المسؤولية الجنائية والشرط الجزائي للمخالفة</div>
    <p style="font-size: 6.5pt; color: #475569;">يوافق الطرف الموقع على سداد شرط جزائي عاجل وقدره 100,000 ج.م في حال ثبوت إفشائه لأي معلومة سرية أو استخدامها لتأسيس مشروع منافس في النطاق الجغرافي للجمهورية.</p>
    """,
    "witness"
)

# ----------------- PAGE 41: Receipt of Company Assets Declaration -----------------
PAGES_CONTENT_21_30[41] = render_legal_document(
    "25. إقرار رسمي باستلام سيارات أو عهد عينية ومعدات تشغيلية",
    "Receipt of Company Assets and Vehicles Declaration",
    "Ref-VS-025",
    """
    <p>تستخدم لتسجيل عهدة سيارات التوزيع أو الدراجات النارية والتروسيكلات الممنوحة لمناديب التوصيل في شركة <strong>V Smart General Trading L.L.C.</strong>:</p>

    <div class="legal-section-title">أولاً: البيانات الفنية والتعريفية للمركبة أو العهدة المسلمة</div>
    <table class="legal-form-table">
        <tr>
            <td style="width:30%; font-weight:bold; background:#f8fafc;">نوع المركبة / العهدة:</td>
            <td style="width:70%;"><span class="print-field" style="min-width:250px;"></span></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">رقم اللوحة / الشاسيه بالتفصيل:</td>
            <td><span class="print-field" style="min-width:250px;"></span></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">الشركة المصنعة والموديل والسنة:</td>
            <td><span class="print-field" style="min-width:250px;"></span></td>
        </tr>
    </table>

    <div class="legal-section-title">ثانياً: شروط الاستخدام والمسؤولية والالتزام بقوانين المرور</div>
    <p>1. يقر المستلم بحصوله على رخصة قيادة سارية وحمله المركبة عهدة شخصية لاستخدامها فقط لتوصيل طلبيات البقالات للمستودع.<br>
    2. يتعهد السائق بالصيانة الدورية للزيت والوقود وفحص سلامة الفرامل دورياً وجلب إيصالات الصيانة للمدير المالي لتسويتها.<br>
    3. يتحمل السائق بمفرده كامل قيمة أي مخالفات مرورية تقع على المركبة بسبب مخالفته لقواعد المرور في جمهورية مصر العربية.</p>
    """,
    "standard"
)

# ----------------- PAGE 42: Document Amendment Request Form -----------------
PAGES_CONTENT_21_30[42] = render_legal_document(
    "26. طلب رسمي لتعديل وثيقة أو نظام محاسبي وإداري معتمد",
    "Official Document Amendment and Change Request Form",
    "Ref-VS-026",
    """
    <p>نموذج مخصص لتنظيم التعديلات التشغيلية، التقنية، أو المالية على القوانين والمحاضر المعتمدة لشركة <strong>V Smart General Trading L.L.C.</strong>:</p>

    <div class="legal-section-title">أولاً: بيانات الوثيقة والجهة صاحبة الطلب للتعديل</div>
    <table class="legal-form-table">
        <tr>
            <td style="width:30%; font-weight:bold; background:#f8fafc;">اسم وتفاصيل الوثيقة المستهدفة:</td>
            <td style="width:70%;"><span class="print-field" style="min-width:250px;"></span></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">رقم المرجع والتاريخ للإصدار الفعلي:</td>
            <td><span class="print-field" style="min-width:250px;"></span></td>
        </tr>
    </table>

    <div class="legal-section-title">ثانياً: تفاصيل التعديل الفعلي المقترح وأسبابه ومبرراته</div>
    <div class="print-box" style="height: 42mm; font-size:7pt; line-height:1.45;">
        نص الوثيقة الأصلي المراد تعديله:<br>
        <span class="print-field" style="min-width:450px; height:14px;"></span><br>
        النص الجديد المقترح البديل بالكامل:<br>
        <span class="print-field" style="min-width:450px; height:18px; border-bottom-style:solid;"></span><br>
        المبررات والجدوى للتعديل لعمل المنصة: <span class="print-field" style="min-width:300px;"></span>
    </div>

    <div class="legal-section-title">ثالثاً: مراجعة وإقرار مجلس الإدارة للتنفيذ</div>
    <p>تم دراسة الطلب وتقرر التعديل: [  ] مقبول ويفعل فوراً  [  ] مرفوض لعدم جدواه  [  ] مؤجل لحين الجلسة الاستشارية القادمة.</p>
    """,
    "standard"
)

# ----------------- PAGE 43: Internal Audit Observation Form -----------------
PAGES_CONTENT_21_30[43] = render_legal_document(
    "27. تقرير التدقيق المالي والرقابي الداخلي لمطابقة الخزينة",
    "Internal Audit Observation & Compliance Form",
    "Ref-VS-027",
    """
    <p>يستخدم لتوثيق وإثبات نتائج لجان المراجعة والمراقبة المالية الداخلية على أعمال الخزانة والمستودع لشركة <strong>V Smart General Trading L.L.C.</strong>:</p>

    <div class="legal-section-title">أولاً: بيانات عملية الجرد والتدقيق المالي والمستودع</div>
    <table class="legal-form-table">
        <tr>
            <td style="width:30%; font-weight:bold; background:#f8fafc;">تاريخ ومكان التدقيق:</td>
            <td style="width:70%;"><span class="print-field" style="min-width:250px;"></span></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">الشخص المدقق عليه والمسؤولية:</td>
            <td>[  ] أمين الخزينة  [  ] أمين مستودع طوخ الأقلام  [  ] نائب مبيعات POS</td>
        </tr>
    </table>

    <div class="legal-section-title">ثانياً: الملاحظات الرقابية والانحرافات المرصودة فعلياً</div>
    <div class="print-box" style="height: 38mm; font-size:7pt; line-height:1.45;">
        الملاحظات المرصودة وسير العمل الفعلي:<br>
        [  ] عدم تطابق رصيد الكاش بالخزينة مع تقارير مبيعات POS وقيمة الفارق: <span class="print-field" style="min-width:100px;"></span> ج.م.<br>
        [  ] وجود تلفيات أو عجز في جرد صنف: <span class="print-field" style="min-width:120px;"></span> بالمستودع.<br>
        التوصية الفورية للإدارة المالية: <span class="print-field" style="min-width:350px;"></span>
    </div>

    <div class="legal-section-title">ثالثاً: إجراءات التصحيح والمدد المقررة للتسوية والالتزام</div>
    <p>يتعهد المسؤول بتصحيح كافة الملاحظات وإعادة تسوية العجز في موعد أقصاه 7 أيام من تاريخه لتلافي العقوبات القانونية.</p>
    """,
    "standard"
)

# ----------------- PAGE 44: Inventory Count Report -----------------
PAGES_CONTENT_21_30[44] = render_legal_document(
    "28. تقرير الجرد الفعلي والسنوي للمخزون بالمستودعات",
    "Inventory Count and Discrepancy Report",
    "Ref-VS-028",
    """
    <p>تقرير معتمد يوثق عمليات الجرد الميداني الشامل لمحتويات مستودعات <strong>تاجر</strong> التابع لـشركة <strong>V Smart General Trading L.L.C.</strong>:</p>

    <div class="legal-section-title">أولاً: بيانات الجرد والمطابقة الدفترية الرقمية بالباركود</div>
    <table class="legal-form-table">
        <tr>
            <td style="width:25%; font-weight:bold; background:#f8fafc;">المستودع وموقعه:</td>
            <td style="width:35%;">[  ] طوخ الأقلام  [  ] ميت خميس</td>
            <td style="width:15%; font-weight:bold; background:#f8fafc;">تاريخ الجرد الفعلي:</td>
            <td style="width:25%;"><span class="print-field" style="min-width:100px;"></span></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">مسؤول لجنة الجرد المالي:</td>
            <td><span class="print-field" style="min-width:140px;"></span></td>
            <td style="font-weight:bold; background:#f8fafc;">تطابق النظام الدفتري:</td>
            <td>[  ] مطابق بالكامل  [  ] فروقات تم تسجيلها</td>
        </tr>
    </table>

    <div class="legal-section-title">ثانياً: جدول مطابقة الأصناف وسلع الاستقطاب الكبرى وفروقات الجرد</div>
    <table class="legal-form-table">
        <tr style="background:#f8fafc; font-weight:bold;">
            <td>اسم المنتج وكود الباركود</td>
            <td>الرصيد الدفتري بالنظام WMS</td>
            <td>الرصيد الفعلي بالجرد الميداني</td>
            <td>الفارق الفعلي (عجز / زيادة)</td>
            <td>القيمة المالية للفارق (ج.م)</td>
        </tr>
        <tr>
            <td>1. مياه معبأة (كرتونة)</td>
            <td><span class="print-field" style="min-width:85px;"></span></td>
            <td><span class="print-field" style="min-width:85px;"></span></td>
            <td><span class="print-field" style="min-width:85px;"></span></td>
            <td><span class="print-field" style="min-width:85px;"></span></td>
        </tr>
        <tr>
            <td>2. زيت طعام عباد (زجاجة)</td>
            <td><span class="print-field" style="min-width:85px;"></span></td>
            <td><span class="print-field" style="min-width:85px;"></span></td>
            <td><span class="print-field" style="min-width:85px;"></span></td>
            <td><span class="print-field" style="min-width:85px;"></span></td>
        </tr>
        <tr>
            <td>3. كرتونة منظفات ومساحيق</td>
            <td><span class="print-field" style="min-width:85px;"></span></td>
            <td><span class="print-field" style="min-width:85px;"></span></td>
            <td><span class="print-field" style="min-width:85px;"></span></td>
            <td><span class="print-field" style="min-width:85px;"></span></td>
        </tr>
    </table>
    """,
    "standard"
)

# ----------------- PAGE 45: Stock Adjustment Authorization -----------------
PAGES_CONTENT_21_30[45] = render_legal_document(
    "29. إذن وتفويض رسمي لتسوية الفروقات وعجز المخزون بالدفاتر",
    "Stock Adjustment and Inventory Correction Authorization",
    "Ref-VS-029",
    """
    <p>يصدر هذا التفويض الحسابي من المدير المالي لشركة <strong>V Smart General Trading L.L.C.</strong> لتسوية ومعالجة عجز أو تلف السلع الغذائية بالمنظومة:</p>

    <div class="legal-section-title">أولاً: تفاصيل العجز أو التلف المراد تسويته دفترياً ونظامياً</div>
    <table class="legal-form-table">
        <tr>
            <td style="width:30%; font-weight:bold; background:#f8fafc;">رقم تقرير الجرد المرفق:</td>
            <td style="width:70%;"><span class="print-field" style="min-width:250px;"></span></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">السبب الفعلي للمطابقة والتسوية:</td>
            <td>[  ] تلف ناتج عن الرطوبة وعوامل الطقس  [  ] كسر عبوات  [  ] خطأ إدخال بالباركود</td>
        </tr>
    </table>

    <div class="legal-section-title">ثانياً: تفاصيل وعملية قيد التسوية بالدفاتر وحساب الأرباح والخسائر</div>
    <table class="legal-form-table">
        <tr style="background:#f8fafc; font-weight:bold;">
            <td>اسم المنتج الغذائي</td>
            <td>الكمية للتسوية بالوحدة</td>
            <td>سعر التكلفة الأصلي للوحدة</td>
            <td>القيمة المالية الإجمالية للتسوية</td>
        </tr>
        <tr>
            <td>1. <span class="print-field" style="min-width:140px;"></span></td>
            <td><span class="print-field" style="min-width:60px;"></span></td>
            <td><span class="print-field" style="min-width:80px;"></span></td>
            <td><span class="print-field" style="min-width:80px;"></span></td>
        </tr>
        <tr>
            <td>2. <span class="print-field" style="min-width:140px;"></span></td>
            <td><span class="print-field" style="min-width:60px;"></span></td>
            <td><span class="print-field" style="min-width:80px;"></span></td>
            <td><span class="print-field" style="min-width:80px;"></span></td>
        </tr>
    </table>
    <p style="margin-top:5px; font-size:6.5pt; color:#475569;">* يوجه لتسوية هذا العجز الفعلي وتحميله على حساب أرباح وخسائر الكيان لعدم ثبوت أي شبهة إهمال بشري من الطاقم الميداني.</p>
    """,
    "standard"
)

# ----------------- PAGE 46: Procurement Approval Form -----------------
PAGES_CONTENT_21_30[46] = render_legal_document(
    "30. نموذج واعتماد طلب شراء وتوريد بضائع كاش للشركة",
    "Official Procurement and Inventory Purchase Approval Form",
    "Ref-VS-030",
    """
    <p>يستخدم لاعتماد ميزانيات شراء السلع الأساسية وسلع الاستقطاب من مصانع وموردي منطقة المنصورة وطنطا لـشركة <strong>V Smart General Trading L.L.C.</strong>:</p>

    <div class="legal-section-title">أولاً: بيانات المورد والتفاصيل المالية لطلب الشراء المعتمد</div>
    <table class="legal-form-table">
        <tr>
            <td style="width:30%; font-weight:bold; background:#f8fafc;">اسم المورد / الشركة الوطنية:</td>
            <td style="width:70%;"><span class="print-field" style="min-width:250px;"></span></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">إجمالي قيمة الفاتورة بالأرقام:</td>
            <td><strong><span class="print-field" style="min-width:150px;"></span> جنيه مصري</strong></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">طريقة السداد المطلوبة للتفعيل:</td>
            <td>[  ] كاش فوري للحصول على خصم البونص  [  ] تحويل بنكي مقدم  [  ] شيك مؤجل</td>
        </tr>
    </table>

    <div class="legal-section-title">ثانياً: تفاصيل ومواصفات الأصناف والمشروبات المطلوبة</div>
    <table class="legal-form-table">
        <tr style="background:#f8fafc; font-weight:bold;">
            <td>اسم المنتج وكود الباركود</td>
            <td>الكمية المطلوبة بالكرتونة</td>
            <td>سعر الشراء الفعلي للكرتونة</td>
            <td>الإجمالي المالي المقدر كاش</td>
        </tr>
        <tr>
            <td>1. مياه معبأة أحجام مختلفة</td>
            <td><span class="print-field" style="min-width:100px;"></span></td>
            <td><span class="print-field" style="min-width:80px;"></span></td>
            <td><span class="print-field" style="min-width:80px;"></span></td>
        </tr>
        <tr>
            <td>2. كراتين زيت خليط وسكر</td>
            <td><span class="print-field" style="min-width:100px;"></span></td>
            <td><span class="print-field" style="min-width:80px;"></span></td>
            <td><span class="print-field" style="min-width:80px;"></span></td>
        </tr>
    </table>
    """,
    "standard"
)

# ----------------- PAGE 47: Supplier Registration Form -----------------
PAGES_CONTENT_21_30[47] = render_legal_document(
    "31. نموذج واستمارة تسجيل الموردين والشركات الوطنية المعتمدة",
    "Official Supplier Registration & Validation Form",
    "Ref-VS-031",
    """
    <p>تستخدم لتوثيق وتسجيل بيانات كبار مصانع وموزعي المواد الغذائية والمشروبات المعتمدين في شركة <strong>V Smart General Trading L.L.C.</strong> لضمان حوكمة الشراء:</p>

    <div class="legal-section-title">أولاً: البيانات العامة والتعريفية للشركة الموردة</div>
    <table class="legal-form-table">
        <tr>
            <td style="width:30%; font-weight:bold; background:#f8fafc;">اسم الشركة الموردة بالكامل:</td>
            <td style="width:70%;"><span class="print-field" style="min-width:250px;"></span></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">رقم السجل التجاري والبطاقة الضريبية:</td>
            <td>سجل رقم: <span class="print-field" style="min-width:100px;"></span> بطاقة ضريبية رقم: <span class="print-field" style="min-width:100px;"></span></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">العنوان الجغرافي والإدارة المركزية:</td>
            <td><span class="print-field" style="min-width:250px;"></span></td>
        </tr>
    </table>

    <div class="legal-section-title">ثانياً: تفاصيل التواصل وممثلي الشركة والحساب البنكي للتسوية</div>
    <table class="legal-form-table">
        <tr>
            <td style="width:25%; font-weight:bold; background:#f8fafc;">اسم مندوب المبيعات المعني:</td>
            <td style="width:30%;"><span class="print-field" style="min-width:140px;"></span></td>
            <td style="width:20%; font-weight:bold; background:#f8fafc;">رقم هاتف المندوب:</td>
            <td style="width:25%;"><span class="print-field" style="min-width:100px;"></span></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">الحساب البنكي والآيبان للمورد:</td>
            <td colspan="3"><span class="print-field" style="min-width:350px;"></span></td>
        </tr>
    </table>
    <p style="margin-top:5px; font-size:6.5pt; color:#475569;">* تلتزم إدارة الحسابات بالشركة بالتحقق من جودة ومطابقة صلاحية تراخيص المورد والتحقق من سلامة البضائع قبل تفعيل كود المورد على المنصة.</p>
    """,
    "standard"
)

# ----------------- PAGE 48: Customer Credit Approval Form -----------------
PAGES_CONTENT_21_30[48] = render_legal_document(
    "32. نموذج طلب واعتماد التسهيلات الائتمانية والبيع الآجل للبقالات الكبرى",
    "Customer Credit Approval & Limits Authorization Form",
    "Ref-VS-032",
    """
    <p>يستخدم هذا النموذج لتنظيم مبيعات الآجل للعملاء الاستراتيجيين للبقالات والسوبرماركت الكبرى لـشركة <strong>V Smart General Trading L.L.C.</strong> لضمان حماية السيولة:</p>

    <div class="legal-section-title">أولاً: البيانات التعريفية للعميل وحجم مبيعات الـ POS بالمنصة</div>
    <table class="legal-form-table">
        <tr>
            <td style="width:30%; font-weight:bold; background:#f8fafc;">اسم العميل / البقالة بالكامل:</td>
            <td style="width:70%;"><span class="print-field" style="min-width:250px;"></span></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">العنوان التجاري الفعلي ورقم السجل:</td>
            <td><span class="print-field" style="min-width:250px;"></span></td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">متوسط المبيعات الشهرية الحالية بالمنصة:</td>
            <td><strong><span class="print-field" style="min-width:150px;"></span> جنيه مصري</strong></td>
        </tr>
    </table>

    <div class="legal-section-title">ثانياً: التسهيلات الائتمانية الموصى بها وسقف الدين وفترة التحصيل</div>
    <table class="legal-form-table">
        <tr>
            <td style="width:25%; font-weight:bold; background:#f8fafc;">سقف الائتمان المقترح (ج.م):</td>
            <td style="width:25%;"><span class="print-field" style="min-width:100px;"></span></td>
            <td style="width:25%; font-weight:bold; background:#f8fafc;">فترة السداد القصوى المسموحة:</td>
            <td style="width:25%;">[  ] 7 أيام  [  ] 15 يوماً  [  ] 30 يوماً</td>
        </tr>
        <tr>
            <td style="font-weight:bold; background:#f8fafc;">شروط الضمان المقبولة قانوناً:</td>
            <td colspan="3">[  ] شيك على بياض كضمان مالي  [  ] إيصال أمانة موقع يدوياً بقيمة: <span class="print-field" style="min-width:100px;"></span> ج.م.</td>
        </tr>
    </table>

    <div class="legal-section-title">ثالثاً: قرار ومصادقة المدير المالي ومجلس الإدارة المشترك</div>
    <p>القرار المالي النهائي: [  ] مقبول بسقف: <span class="print-field" style="min-width:80px;"></span> ج.م  [  ] مرفوض لارتفاع مخاطر التحصيل والسيولة.</p>
    """,
    "standard"
)

print("pages_21_30.py successfully redefined with Pages 32-48!")
