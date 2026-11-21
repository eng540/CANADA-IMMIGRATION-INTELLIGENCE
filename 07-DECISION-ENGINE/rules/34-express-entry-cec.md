# قاعدة: Canadian Experience Class (CEC) — مولدة من البطاقة الموثقة

- البطاقة: `03-ALL-PROGRAMS/federal/cec-canadian-experience-class.md` (تحقق 2026-11-22)
- المصادر: S26, S28, S22, S23

```yaml
rule_id: ca.federal.express_entry.cec
program_type: permanent_residence
intake: express_entry_pool
status: open_conditional
hard_gates:
  - id: canadian_experience
    rule: خبرة عمل كندية مدفوعة مصرّح بها >= 1560 ساعة خلال آخر 3 سنوات، TEER 0-3؛ لا تُحتسب فترات الدراسة/العمل الحر/التطوع/غير المصرح؛ العمل عن بعد فقط من داخل كندا لصاحب عمل كندي
    source: card field 8 / S28
    if_fail: غير مؤهل — لا خبرة كندية مستوفاة (وجه لمسارات بدون خبرة كندية مثل FSW)
  - id: language_by_teer
    rule: TEER 0-1: CLB/NCLC 7 · TEER 2-3: CLB/NCLC 5 (القدرات الأربع)
    source: card field 9 / S26
    if_unknown: محتمل — مستوى اللغة غير معروف
  - id: admissibility
    rule: قبول عام
    source: card field 14 / S28
  - id: quebec_intent
    rule: نية سكن خارج كيبيك (خبرة كيبيك تُحتسب مع إثبات عدم نية الاستقرار)
    source: S28
no_requirement:
  - education (نقاط فقط) / S28
  - job_offer / S28
  - proof_of_funds / S28
modifiers:
  - NOC 41200: الخبرة الممولة بمنح بحثية تُحتسب (تحديث 2026-11-18) / S28
```
