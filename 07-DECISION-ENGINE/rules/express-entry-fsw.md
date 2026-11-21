# قاعدة: Federal Skilled Worker (FSW) — مولدة من البطاقة الموثقة

- البطاقة: `03-ALL-PROGRAMS/federal/fsw-express-entry.md` (تحقق 2026-11-22)
- المصادر: S21, S22, S23, S26 · القيم أعلاه قابلة للتدقيق حقلًا بحقل

```yaml
rule_id: ca.federal.express_entry.fsw
program_type: permanent_residence
intake: express_entry_pool
status: open_conditional   # جولات موقوفة مؤقتًا لإعادة حساب النقاط (S22 — بيان رسمي بتاريخ)
hard_gates:
  - id: experience
    rule: خبرة مدفوعة >= 1560 ساعة خلال آخر 10 سنوات، TEER 0-3، نفس NOC الأساسي، خارج أو داخل كندا
    source: card field 8 / S21
    if_fail: غير مؤهل — خبرة غير مستوفاة
  - id: language_first
    rule: CLB >= 7 أو NCLC >= 7 في القدرات الأربع (لغة أولى)
    source: card field 9 / S26
    if_unknown: محتمل — مستوى اللغة غير معروف
    if_fail: غير مؤهل — اللغة دون الحد
  - id: education
    rule: مؤهل مكتمل؛ للأجنبي ECA إلزامي لأغراض الهجرة
    source: card field 7 / S21
    if_unknown: محتمل — ECA غير صادر
  - id: selection_grid
    rule: مجموع >= 67/100 على شبكة عوامل FSW (لغة، تعليم، خبرة، عمر، عرض عمل صالح، تكيف)
    source: card field 6+10 / S21
    if_unknown: محتمل — يحتاج حساب الشبكة
  - id: funds
    rule: إثبات أموال إلا بإعفاء يتطلب معًا (عمل قانوني حالي في كندا + عرض عمل صالح)
    source: card field 12 / S21
    if_fail: غير مؤهل ماليًا ما لم يتحقق الإعفاء
  - id: admissibility
    rule: قبول عام (طبي/أمني)
    source: card field 14 / S21
    if_fail: غير مؤهل — عدم قبول عام (طبي/أمني)
  - id: quebec_intent
    rule: نية سكن خارج كيبيك
    source: S21
    if_fail: غير مؤهل عبر هذا البرنامج — نية سكن في كيبيك (تُوجَّه لمسارات كيبيك)
modifiers:
  - عرض عمل صالح: +10 نقاط شبكة؛ منذ 2026-11-03 لا LMIA ولا نقاط LMIA (S21/S22)
  - فئات الاختيار العشر (S23): خبرة 12 شهرًا خلال 3 سنوات في NOC واحد مدرج تفتح جولات الفئة؛ STEM يشمل NOC 21300 مدني والخبرة الخارجية تُحتسب؛ الفرنسية NCLC 7 فئة قائمة بذاتها
outputs:
  qualified: مؤهل للدخول للمجموعة؛ التنافسية تقاس بأرقام الجولات الرسمية فقط عند توفرها
  data_needed: [نتيجة اختبار اللغة، حالة ECA، حساب شبكة 67، وضع الأموال/الإعفاء]
```
