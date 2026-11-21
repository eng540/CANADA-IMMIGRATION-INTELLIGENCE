# قاعدة: Federal Skilled Trades (FST) — مولدة من البطاقة الموثقة

- البطاقة: `03-ALL-PROGRAMS/federal/fst-federal-skilled-trades.md` (تحقق 2026-11-22)
- المصادر: S26, S29, S22, S23

```yaml
rule_id: ca.federal.express_entry.fst
program_type: permanent_residence
intake: express_entry_pool
status: open_conditional
hard_gates:
  - id: trade_experience
    rule: خبرة حرفية مدفوعة >= 3120 ساعة خلال آخر 5 سنوات، كلها في NOC واحد ضمن المجموعات المقبولة (72 عدا 726، 73، 82، 83، 92، 93 عدا 932، 6320، 62200)، في بلد كان المتقدم مؤهلًا للمزاولة فيه
    source: card field 8 / S29
    if_fail: غير مؤهل — خبرة خارج المجموعات أو موزعة على أكثر من NOC
  - id: offer_or_certificate
    rule: عرض عمل صالح دوام كامل >= سنة، أو شهادة كفاءة كندية في المهنة (مقاطعة/إقليم/فيدرالي)
    source: card field 10 / S29
    if_fail: غير مؤهل — لا عرض ولا شهادة (هذا هو البوابة الأقسى لمن خارج كندا)
  - id: language
    rule: تحدث/استماع CLB 5 · قراءة/كتابة CLB 4 (أو NCLC 5/4)
    source: card field 9 / S26
    if_unknown: محتمل — مستوى اللغة غير معروف
  - id: funds
    rule: إثبات أموال إلا بالإعفاء الثنائي (عمل قانوني حالي + عرض صالح)
    source: card field 12 / S29
  - id: admissibility
    rule: قبول عام
    source: card field 14 / S29
  - id: quebec_intent
    rule: نية سكن خارج كيبيك
    source: S29
no_requirement:
  - education (نقاط فقط) / S29
notes:
  - شهادة الكفاءة تتطلب تقييم جهة المهنة في المقاطعة وقد تستلزم حضورًا أو خبرة كندية — تكلفة وزمن يُدرجان في 08
```
