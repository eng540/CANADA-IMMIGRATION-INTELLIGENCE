# حاسبة التكلفة (نموذج ورقي)

الأرقام من [08-FINANCIAL-PLANNING/data/financial-comparison-data.json](../08-FINANCIAL-PLANNING/data/financial-comparison-data.json) بتاريخ استرجاع 2026-11-22، بعملة CAD. **تحقق من صفحة رسوم IRCC قبل الدفع — الرسوم تتغير.**

## الجدول أ: رسوم حكومية شائعة (2026-11-22)

| البند | الرسم |
|---|---|
| تصريح عمل (للشخص) | 155 |
| تصريح دراسة (للشخص) | 150 |
| تأشيرة زيارة (للشخص / عائلة 5+ بحد أقصى) | 100 / 500 |
| eTA | 7 |
| IEC | 184.75 |
| إقامة دائمة اقتصادية — رئيسي شامل RPRF (بدونه 990) | 1,590 |
| الزوج/الشريك — شامل RPRF (بدونه 990) | 1,590 |
| كل طفل معال | 270 |
| حق الإقامة الدائمة RPRF (يُسترد عند سحب/رفض) | 600 |
| بيومترية — فرد / عائلة بحد أقصى | 85 / 170 |
| رسوم امتثال صاحب العمل IMP (يدفعها صاحب العمل) | 230 |
| LMIA (يدفعها صاحب العمل، يُحظر تحميلك إياها) | 1,000/منصب |
| جنسية — بالغ / قاصر | 653 / 100 |
| بطاقة PR / وثيقة سفر PR | 50 / 50 |

## الجدول ب: إثبات أموال Express Entry (جدول يوليو 2025 الساري، أُعيد فتح الصفحة 2026-11-22)

| أفراد الأسرة | المبلغ المطلوب (CAD) |
|---|---|
| 1 | 15,263 |
| 2 | 19,001 |
| 3 | 23,360 |
| 4 | 28,362 |
| 5 | 32,168 |
| 6 | 36,280 |
| 7 | 40,392 |
| كل فرد إضافي فوق 7 | +4,112 |

## الجدول ج: تكاليف جانبية متغيرة (أدخل قيم بلدك)

| البند | تقدير | ملاحظة |
|---|---|---|
| اختبار لغة (IELTS/CELPIP/PTE) | ____ | يختلف بالبلد والمركز |
| ECA (مثل WES) + ترجمة | ____ | حسب الجهة وعدد المؤهلات |
| فحص طبي | ____ | حسب البلد والعيادة المعتمدة |
| شهادات عدم محكومية | ____ | لكل بلد أقمت فيه ≥6 أشهر |
| ترجمات معتمدة | ____ | لكل وثيقة غير إنجليزية/فرنسية |
| سفر + سكن أولي | ____ | حسب المدينة (08) |

## الحاسبة التفاعلية

اختر المسار والأفراد وتحصل على الإجمالي الحكومي + متطلب إثبات الأموال، مقارنة بميزانيتك. الأرقام من الجدول أ (2026-11-22).

<div id="cc-app" dir="rtl" style="max-width:820px">
<style>
#cc-app label{display:block;margin:6px 0 2px;font-weight:600}
#cc-app select,#cc-app input{width:100%;max-width:340px;padding:6px;border:1px solid #999;border-radius:6px}
#cc-app button{background:#b71c1c;color:#fff;border:0;border-radius:8px;padding:10px 24px;cursor:pointer}
#cc-app table{margin-top:10px}
#cc-app .ok{color:#2e7d32;font-weight:700}#cc-app .bad{color:#c62828;font-weight:700}
</style>
<label>المسار</label>
<select id="cc-path">
<option value="ee1">إقامة دائمة اقتصادية — رئيسي فقط (شامل RPRF)</option>
<option value="ee2">إقامة دائمة اقتصادية — رئيسي + زوج/شريك</option>
<option value="wp">تصريح عمل</option>
<option value="sp">تصريح دراسة</option>
<option value="trv">تأشيرة زيارة</option>
</select>
<label>أطفال معالون مرافقون (للمسارات الدائمة)</label>
<select id="cc-kids"><option>0</option><option>1</option><option>2</option><option>3+</option></select>
<label>عدد الأفراد (للبيومترية/الزيارة)</label>
<select id="cc-ppl"><option value="1">1</option><option value="2">2 (عائلة)</option></select>
<label>أفراد الأسرة المهاجرين إجمالاً (لجدول إثبات الأموال)</label>
<select id="cc-fam"><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4+</option></select>
<label>هل ينطبق عليك إعفاء إثبات الأموال؟ (CEC، أو عمل قانوني حالي في كندا + عرض عمل صالح، أو مسار لا يشترطه كلمّ شمل الزوج)</label>
<select id="cc-exempt"><option value="no">لا / لا أعرف</option><option value="yes">نعم — موثق لديّ</option></select>
<label>تكاليف جانبية (لغة + ECA + طبي + ترجمة + سفر) — تقديرك أنت، CAD</label><input id="cc-side" type="number" min="0" value="2500">
<label>ميزانيتك المتاحة — CAD</label><input id="cc-budget" type="number" min="0" value="0">
<br><button onclick="ccRun()">احسب</button>
<div id="cc-out"></div>
</div>
<script>
function ccRun(){
 const g=i=>document.getElementById(i).value;
 const p=g('cc-path'),kids=Math.min(3,+g('cc-kids')),ppl=g('cc-ppl'),fam=+g('cc-fam'),
 side=+g('cc-side'),budget=+g('cc-budget'),exempt=g('cc-exempt');
 let gov=0,items=[];
 if(p==='ee1'){gov=1590+kids*270;items.push('رئيسي شامل RPRF: 1,590');if(kids)items.push('أطفال: '+kids+'×270');}
 if(p==='ee2'){gov=3180+kids*270;items.push('رئيسي + شريك شامل RPRF: 3,180');if(kids)items.push('أطفال: '+kids+'×270');}
 if(p==='wp'){gov=155;items.push('تصريح عمل: 155');}
 if(p==='sp'){gov=150;items.push('تصريح دراسة: 150');}
 if(p==='trv'){gov=ppl==='2'?Math.min(500,200):100;items.push('زيارة: '+gov);}
 const bio=ppl==='2'?170:85; items.push('بيومترية: '+bio); gov+=bio;
 const FUNDS={1:15263,2:19001,3:23360,4:28362}[fam];
 let fundsNeed=0;
 if(exempt==='no'&&(p==='ee1'||p==='ee2')){fundsNeed=FUNDS;items.push('إثبات أموال يُبرَز ولا يُدفع (جدول سارٍ محدّث 2025-07-07، أُعيد التحقق منه على الصفحة الرسمية 2026-11-22): '+FUNDS.toLocaleString());}
 if(exempt==='no'&&p==='sp'){fundsNeed=23448;items.push('إثبات أموال دراسة يُبرَز ولا يُدفع (معيشة سنة، 2025-09 سارٍ): 23,448 + رسوم أول سنة (غير مشمولة هنا)');}
 if(exempt==='yes'){items.push('إثبات أموال: معفى بحسب إدخالك — تحقق من شرط الإعفاء في صفحة البرنامج الرسمية');}
 const total=gov+side, grand=total+fundsNeed;
 const ok=budget>=grand;
 document.getElementById('cc-out').innerHTML='<p><b>تقدير تخطيطي بتاريخ 2026-11-22</b> — ليس تأكيداً لكفاية مالية حالية ولا قراراً رسمياً؛ تحقق من صفحة رسوم IRCC يوم التقديم.</p>'+
 '<table><tr><th>البند</th><th>CAD</th></tr>'+
 items.map(x=>'<tr><td>'+x+'</td><td></td></tr>').join('')+
 '<tr><td><b>أ) رسوم وتكاليف تُدفع فعلاً (حكومية بجدول 2026-11-22 + جانبية بتقديرك)</b></td><td><b>'+total.toLocaleString()+'</b></td></tr>'+
 '<tr><td><b>ب) أموال إثبات تُبرَز ولا تُدفع (بقيت ملكك)</b></td><td><b>'+fundsNeed.toLocaleString()+'</b></td></tr>'+
 '<tr><td><b>الإجمالي المطلوب توفره (أ+ب)</b></td><td><b>'+grand.toLocaleString()+'</b></td></tr></table>'+
 '<p style="opacity:.85">غير مشمول في هذا التقدير: رسوم الدراسة للسنة الأولى (لمسار الدراسة)، تذاكر السفر والسكن الأولي، هامش طوارئ 10-15%، أي رسوم مقاطعة (PNP) أو CSQ (كيبيك). تركيبة الأسرة تغيّر الرسوم (الشريك +1,590$ وكل طفل +270$) ومبلغ الإثبات معاً.</p>'+
 (budget?('<p class="'+(ok?'ok':'bad')+'">'+(ok?'وفق هذا التقدير المؤرخ: ميزانيتك تغطي البندين (أ+ب) ✓ — أعد التحقق من الأرقام الرسمية قبل الاعتماد':'وفق هذا التقدير المؤرخ: ميزانيتك لا تغطي — الفجوة: '+(grand-budget).toLocaleString()+'$ — راجع مسارات يمولها صاحب العمل (08)')+'</p>'):'');
}
</script>

## نموذج الجمع

```
مساري: ____________
رسوم حكومية (جدول أ):                       ______
إثبات أموال مجمّد إن طُلب (جدول ب):          ______
تكاليف جانبية (جدول ج):                      ______
هامش طوارئ (اقتراح: 10-15%):                ______
─────────────────────────────────────────────
الإجمالي:                                    ______
ميزانيتي المتاحة:                            ______
الفجوة:                                      ______
```

## قراءة النتيجة (وفق خوارزمية 07)

كل ما يلي ضمن **التقدير التخطيطي المؤرخ** أعلاه، لا تأكيد كفاية حالية:

- إجمالي ≤ ميزانيتك ← المسار **قابل مالياً وفق هذا التقدير** (أعد التحقق من الأرقام الرسمية يوم التقديم).
- فجوة صغيرة ← **يحتاج تمويلاً**: أعد الحساب بعد تدبير الفرق أو قلّل المرافقين في المرحلة الأولى.
- فجوة كبيرة ← **غير قابل حالياً**: راجع مسارات يمولها صاحب العمل (LMIA/امتثال IMP عليه) وسيناريو الميزانية الصفرية في 08.

> لا تدفع أي رسم قبل التأكد من أنك على الموقع الحكومي الرسمي وحده (09-LEGAL-AND-RISK: الاحتيال).
