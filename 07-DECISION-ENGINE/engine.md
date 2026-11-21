# محرك اختيار المسار — تفاعلي

أدخل بياناتك واحصل على تقييم فوري لخمسة مسارات موثقة (FSW / CEC / FST / تصريح عمل بصاحب عمل / تصريح دراسة) وفق قواعد `rules/*.md` بتاريخ تحقق 2026-11-22. التقييم يجري في متصفحك؛ لا تُرسل بياناتك لأي جهة. النتائج **مؤشر أولي لا قرار رسمي** — الحسم لصفحات البرامج الرسمية.

<div id="de-app" dir="rtl" style="max-width:900px">
<style>
#de-app fieldset{border:1px solid #bbb;border-radius:8px;margin:0 0 12px;padding:10px}
#de-app label{display:block;margin:6px 0 2px;font-weight:600}
#de-app select,#de-app input{width:100%;max-width:380px;padding:6px;border:1px solid #999;border-radius:6px}
#de-app button{background:#b71c1c;color:#fff;border:0;border-radius:8px;padding:10px 26px;font-size:1.05em;cursor:pointer}
#de-app .card{border-right:6px solid #999;background:var(--md-default-bg-color);border-radius:8px;padding:10px 14px;margin:10px 0}
#de-app .ok{border-color:#2e7d32}#de-app .maybe{border-color:#ef6c00}#de-app .no{border-color:#c62828}
#de-app .v{font-weight:700}
#de-app ul{margin:6px 0}
</style>

<fieldset><legend>بياناتك</legend>
<label>العمر</label><input id="age" type="number" min="17" max="70" value="30">
<label>أعلى مستوى لغة (CLB/NCLC) — أضعف قدرة من الأربع</label>
<select id="clb"><option value="0">لا أعرف / لم أختبر</option><option value="4">CLB 4</option><option value="5">CLB 5</option><option value="6">CLB 6</option><option value="7">CLB 7</option><option value="8">CLB 8+</option></select>
<label>سنوات خبرة مهرة (TEER 0-3) خارج أو داخل كندا — آخر 10 سنوات</label>
<select id="fexp"><option value="0">أقل من سنة</option><option value="1">سنة إلى أقل من 3</option><option value="3">3 سنوات فأكثر</option></select>
<label>شهور خبرة عمل كندية مصرّح بها (TEER 0-3) — آخر 3 سنوات</label>
<select id="cexp"><option value="0">لا يوجد</option><option value="6">أقل من 12 شهراً</option><option value="12">12 شهراً فأكثر</option></select>
<label>فئة TEER لخبرتك الكندية (إن وجدت)</label>
<select id="cteer"><option value="1">TEER 0-1</option><option value="3">TEER 2-3</option></select>
<label>المؤهل العلمي</label>
<select id="edu"><option value="hs">ثانوي أو أقل</option><option value="dip">دبلوم/شهادة مهنية</option><option value="ba">بكالوريوس</option><option value="pg">ماجستير/دكتوراه</option></select>
<label>حالة معادلة الشهادة ECA (للمؤهل الأجنبي)</label>
<select id="eca"><option value="unknown">لم تصدر / لا أعرف</option><option value="yes">صادرة</option><option value="ca">مؤهلي كندي — لا حاجة</option></select>
<label>عرض عمل من صاحب عمل كندي</label>
<select id="offer"><option value="none">لا يوجد</option><option value="lmia">نعم — بـLMIA أو قيد إصداره</option><option value="exempt">نعم — معفى من LMIA (IMP)</option></select>
<label>صاحب العمل معتمد/مصنّف في برنامج إقليمي أو مجتمعي (AIP/RCIP/PNP)؟</label>
<select id="desig"><option value="unknown">لا أعرف</option><option value="yes">نعم</option><option value="no">لا</option></select>
<label>خبرة في مهنة حرفية (TEER 2-3) — سنتان خلال 5 سنوات؟ وهل لديك عرض عمل أو شهادة تأهيل مقاطعية فيها؟</label>
<select id="trade"><option value="no">لا</option><option value="exp">خبرة بلا عرض/شهادة</option><option value="full">خبرة + عرض/شهادة</option></select>
<label>الأموال المتاحة لإثبات القدرة (CAD)</label><input id="funds" type="number" min="0" value="0">
<label>عدد أفراد الأسرة المهاجرين (بما فيهم أنت)</label>
<select id="fam"><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4+</option></select>
<label>قبول جامعي من DLI معتمدة (لمسار الدراسة)؟</label>
<select id="loa"><option value="no">لا</option><option value="yes">نعم</option></select>
<label>نية السكن في كيبيك؟</label>
<select id="qc"><option value="no">لا — خارج كيبيك</option><option value="yes">نعم</option></select>
<br><button onclick="deRun()">قيّم مساراتي</button>
</fieldset>
<div id="de-out"></div>
</div>

<script>
function deRun(){
 const g=id=>document.getElementById(id).value;
 const clb=+g('clb'),fexp=+g('fexp'),cexp=+g('cexp'),cteer=+g('cteer'),edu=g('edu'),eca=g('eca'),
 offer=g('offer'),desig=g('desig'),trade=g('trade'),funds=+g('funds'),fam=+g('fam'),loa=g('loa'),qc=g('qc');
 const FUNDS={1:15263,2:19001,3:23360,4:28362}[fam];
 const hasFunds=funds>=FUNDS;
 const R=[];
 // FSW
 let v=[],u=[],f=[];
 if(fexp<1)f.push('خبرة مهرة أقل من سنة (1,560 ساعة) خلال 10 سنوات — بوابة قاسية');
 if(clb===0)u.push('نتيجة اختبار لغة');else if(clb<7)f.push('CLB/NCLC 7 حد أدنى للغة الأولى');
 if(edu==='hs')f.push('شبكة الـ67 تصعب بلا مؤهل فوق الثانوي');
 if(eca==='unknown')u.push('إصدار ECA للمؤهل الأجنبي');
 const fswFundsExempt=(offer!=='none')&&cexp>=12;
 if(!fswFundsExempt&&!hasFunds)f.push('إثبات أموال ('+FUNDS.toLocaleString()+'$) — الإعفاء يتطلب عملاً قانونياً حالياً في كندا + عرض عمل صالح');
 if(qc==='yes')f.push('نية سكن في كيبيك — FSW خارج كيبيك فقط');
 R.push({n:'FSW — العمال المهرة الفيدرالي',f,u,note:'بعد اجتياز البوابات تُحسب شبكة الـ67 (راجع 06/fsw-67-grid) ثم تنافسية CRS بأرقام الجولات الرسمية فقط.'});
 // CEC
 v=[];u=[];f=[];
 if(cexp<12)f.push('لا توجد خبرة كندية مصرّح بها ≥ 12 شهراً خلال 3 سنوات');
 const need=cteer===1?7:5;
 if(clb===0)u.push('نتيجة اختبار لغة');else if(clb<need)f.push('الحد الأدنى لفئتك: CLB '+need);
 if(qc==='yes')f.push('نية سكن في كيبيك');
 R.push({n:'CEC — فئة الخبرة الكندية',f,u,note:'لا شرط تعليم ولا إثبات أموال.'});
 // FST
 v=[];u=[];f=[];
 if(trade==='no')f.push('يتطلب سنتَي خبرة حرفية TEER 2-3 خلال 5 سنوات');
 if(trade==='exp')f.push('يتطلب عرض عمل صالحاً أو شهادة تأهيل مقاطعية في الحرفة');
 if(clb===0)u.push('نتيجة اختبار لغة');else if(clb<4)f.push('الحد الأدنى CLB 5 تحدث/استماع وCLB 4 قراءة/كتابة');else if(clb<5)u.push('تحقق أن التحدث/الاستماع ≥ CLB 5');
 if(qc==='yes')f.push('نية سكن في كيبيك');
 R.push({n:'FST — المهن الحرفية الفيدرالية',f,u,note:''});
 // Work permit
 v=[];u=[];f=[];
 if(offer==='none')f.push('لا عرض عمل — هو بوابة هذا المسار كله');
 if(offer==='lmia')u.push('صدور LMIA الإيجابي (على صاحب العمل، 1000$/منصب — يُحظر تحميلك أي رسوم توظيف)');
 if(offer==='exempt')u.push('تأكد أن رمز الإعفاء معترف به لحالتك (C61-C63/C16/C18/C15...)');
 if(offer!=='none'&&desig==='yes')u.push('اعتماد صاحب العمل يفتح أيضاً AIP/RCIP/PNP — قارن المسار الدائم الموازي');
 R.push({n:'تصريح عمل بصاحب عمل (TFWP/IMP)',f,u,note:'رسوم العامل: 155$ تصريح + 85$ بيومترية. تحقق من قائمة أصحاب العمل غير الملتزمين (S55).'});
 // Study
 v=[];u=[];f=[];
 if(loa==='no')f.push('لا قبول من DLI');
 const studyNeed=23448;
 if(funds<studyNeed)f.push('إثبات أموال دراسة: معيشة '+studyNeed.toLocaleString()+'$/سنة + رسوم أول سنة (+~6,300$ لكل مرافق)');
 u.push('PAL/TAL أو إعفاء موثق (ماجستير/دكتوراه DLI عامة معفاة من 2026-01-01)');
 R.push({n:'تصريح دراسة',f,u,note:'الدراسة لا تضمن PR؛ المسار الشائع PGWP ثم CEC/PNP.'});
 // render
 const order=r=>r.f.length===0&&r.u.length===0?0:r.f.length===0?1:2;
 R.sort((a,b)=>order(a)-order(b));
 let h='';
 for(const r of R){
  const cls=r.f.length?'no':r.u.length?'maybe':'ok';
  const verdict=r.f.length?'غير مؤهل حالياً':r.u.length?'محتمل — معلومات ناقصة':'مؤهل مبدئياً';
  h+='<div class="card '+cls+'"><div class="v">'+r.n+' ← '+verdict+'</div>';
  if(r.f.length)h+='<ul>'+r.f.map(x=>'<li>يستبعد: '+x+'</li>').join('')+'</ul>';
  if(r.u.length)h+='<ul>'+r.u.map(x=>'<li>ينقص: '+x+'</li>').join('')+'</ul>';
  if(r.note)h+='<div style="opacity:.8">'+r.note+'</div></div>';
 }
 const best=R.find(r=>r.f.length===0);
 h+='<div class="card"><div class="v">التوصية:</div> '+(best?'أفضل نقطة انطلاق الآن: <b>'+best.n+'</b>. أكمل الناقص ثم تحقق من بطاقة البرنامج الكاملة (03).':'لا مسار مفتوح بالكامل حالياً — عالج أسباب الاستبعاد أعلاه بدءاً بالبوابة الأسهل (غالباً اللغة أو عرض العمل)، ثم أعد التقييم.')+'<br><span style="opacity:.8">تقييم آلي أولي بقواعد 2026-11-22؛ القرار النهائي لضباط IRCC ولصفحات البرامج الرسمية. لا تُحتسب هنا نسب نجاح — لا توجد بيانات رسمية لذلك.</span></div>';
 document.getElementById('de-out').innerHTML=h;
 document.getElementById('de-out').scrollIntoView({behavior:'smooth'});
}
</script>

## حدود هذا المحرك

- يغطي المسارات الفيدرالية الخمسة الموثقة بقواعد YAML؛ برامج المقاطعات (71 مساراً) تُقيَّم من بطاقاتها (03-ALL-PROGRAMS/provincial) لأن شروطها تتغير بجولات متكررة.
- لا يحسب نقاط CRS التفصيلية ولا شبكة الـ67 رقماً — يوجهك لأدلتها.
- كل قاعدة هنا مأخوذة حرفياً من ملفات القواعد الموثقة بتاريخها ومصادرها؛ عند تعارض، البطاقة ومصدرها الرسمي يتقدمان.
