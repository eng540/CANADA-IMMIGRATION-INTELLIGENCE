# محرك اختيار المسار — تفاعلي

أدخل بياناتك واحصل على مقارنة فورية لكل عائلات المسارات الموثقة في هذا الدليل: الخمسة الفيدرالية بقواعد صلبة (FSW / CEC / FST / تصريح عمل / تصريح دراسة)، والعائلات الإقليمية والخاصة (PNP / AIP / RCIP / كيبيك / لمّ الشمل / الأعمال / الحماية) بمخرجات «يحتاج تحقق يدوي» حيث لا تكفي الأدلة لحسم آلي. التقييم يجري في متصفحك؛ لا تُرسل بياناتك لأي جهة. النتائج **مؤشر تحقيق أولي لا قرار رسمي ولا تأكيد أهلية** — الحسم لصفحات البرامج الرسمية.

<div id="de-app" dir="rtl" style="max-width:900px">
<style>
#de-app fieldset{border:1px solid #bbb;border-radius:8px;margin:0 0 12px;padding:10px}
#de-app label{display:block;margin:6px 0 2px;font-weight:600}
#de-app select,#de-app input{width:100%;max-width:380px;padding:6px;border:1px solid #999;border-radius:6px}
#de-app button{background:#b71c1c;color:#fff;border:0;border-radius:8px;padding:10px 26px;font-size:1.05em;cursor:pointer}
#de-app .card{border-right:6px solid #999;background:var(--md-default-bg-color);border-radius:8px;padding:10px 14px;margin:10px 0}
#de-app .ok{border-color:#2e7d32}#de-app .maybe{border-color:#ef6c00}#de-app .no{border-color:#c62828}#de-app .info{border-color:#546e7a}
#de-app .v{font-weight:700}
#de-app ul{margin:6px 0}
#de-app .cost{opacity:.85;font-size:.95em}
</style>

<fieldset><legend>بياناتك</legend>
<label>العمر</label><input id="age" type="number" min="17" max="70" value="30">
<label>أعلى مستوى لغة إنجليزية/فرنسية (CLB/NCLC) — أضعف قدرة من الأربع</label>
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
<label>خبرة حرفية مدفوعة (سنتان/3,120 ساعة خلال 5 سنوات) + عرض عمل سنة أو شهادة كفاءة؟</label>
<select id="trade"><option value="no">لا</option><option value="exp">خبرة بلا عرض/شهادة</option><option value="full">خبرة + عرض/شهادة</option></select>
<label>هل مهنتك الحرفية ضمن مجموعات NOC المؤهلة لـFST؟ (72 عدا 726، 73، 82، 83، 92، 93 عدا 932، الثانوية 6320، الوحدة 62200)</label>
<select id="fstnoc"><option value="unknown">لا أعرف / لم أتحقق</option><option value="yes">نعم — مهنتي ضمنها</option><option value="no">لا</option></select>
<label>قريب من الدرجة الأولى مواطن كندي أو مقيم دائم (زوج/شريك أو والد)؟</label>
<select id="rel"><option value="no">لا</option><option value="yes">نعم</option></select>
<label>الأموال المتاحة لإثبات القدرة (CAD)</label><input id="funds" type="number" min="0" value="0">
<label>عدد أفراد الأسرة المهاجرين (بما فيهم أنت)</label>
<select id="fam"><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4+</option></select>
<label>قبول جامعي من DLI معتمدة (لمسار الدراسة)؟</label>
<select id="loa"><option value="no">لا</option><option value="yes">نعم</option></select>
<label>نية السكن في كيبيك؟</label>
<select id="qc"><option value="no">لا — خارج كيبيك</option><option value="yes">نعم</option></select>
<br><button onclick="deRun()">قارن كل المسارات</button>
</fieldset>
<div id="de-out"></div>
</div>

<script>
function deRun(){
 const g=id=>document.getElementById(id).value;
 const clb=+g('clb'),fexp=+g('fexp'),cexp=+g('cexp'),cteer=+g('cteer'),edu=g('edu'),eca=g('eca'),
 offer=g('offer'),desig=g('desig'),trade=g('trade'),fstnoc=g('fstnoc'),rel=g('rel'),
 funds=+g('funds'),fam=+g('fam'),loa=g('loa'),qc=g('qc');
 const FUNDS={1:15263,2:19001,3:23360,4:28362}[fam];
 const hasFunds=funds>=FUNDS;
 const CALC='<a href="../../10-PRACTICAL-TOOLS/cost-calculator/">حاسبة التكلفة</a>';
 const PRFEE='رسوم حكومية مرجعية (2026-11-22): رئيسي شامل RPRF 1,590$ + بيومترية 85$ (+1,590$ للشريك و270$ لكل طفل) — '+CALC;
 const R=[];
 // FSW
 let f=[],u=[];
 if(fexp<1)f.push('خبرة مهرة أقل من سنة (1,560 ساعة) خلال 10 سنوات — بوابة قاسية');
 if(clb===0)u.push('نتيجة اختبار لغة معتمد (IELTS/CELPIP/PTE أو TEF/TCF)');
 else if(clb<7)f.push('CLB/NCLC 7 حد أدنى للغة الأولى');
 if(edu==='hs')f.push('شبكة الـ67 تصعب بلا مؤهل فوق الثانوي');
 if(eca==='unknown')u.push('إصدار ECA للمؤهل الأجنبي (مثل WES)');
 const fswExempt=(offer!=='none')&&cexp>=12;
 if(!fswExempt&&!hasFunds)f.push('إثبات أموال ('+FUNDS.toLocaleString()+'$ بجدول يوليو 2025) — الإعفاء يتطلب عملاً قانونياً حالياً في كندا + عرض عمل صالح');
 if(qc==='yes')f.push('نية سكن في كيبيك — FSW خارج كيبيك فقط');
 R.push({n:'FSW — العمال المهرة الفيدرالي (Express Entry)',f,u,note:'بعد البوابات: تُحسب <a href="../../06-APPLICATION-GUIDES/fsw-67-grid/">شبكة الـ67</a> ثم تنافسية CRS بأرقام الجولات الرسمية فقط — لا يحسم هذا المحرك القبول التنافسي.',cost:PRFEE+' + إثبات أموال ما لم يعفَ',next:'اختبار لغة + ECA ثم تحقق من بطاقة <a href="../../03-ALL-PROGRAMS/federal/fsw-express-entry/">FSW الكاملة</a>.'});
 // CEC
 f=[];u=[];
 if(cexp<12)f.push('لا توجد خبرة كندية مصرّح بها ≥ 12 شهراً خلال 3 سنوات');
 const need=cteer===1?7:5;
 if(clb===0)u.push('نتيجة اختبار لغة');else if(clb<need)f.push('الحد الأدنى لفئتك: CLB '+need);
 if(qc==='yes')f.push('نية سكن في كيبيك');
 R.push({n:'CEC — فئة الخبرة الكندية (Express Entry)',f,u,note:'لا شرط تعليم ولا إثبات أموال.',cost:PRFEE,next:'تجميع الخبرة الكندية عبر تصريح عمل/PGWP ثم بطاقة <a href="../../03-ALL-PROGRAMS/federal/cec-canadian-experience-class/">CEC</a>.'});
 // FST
 f=[];u=[];
 if(trade==='no')f.push('يتطلب سنتَي خبرة حرفية مدفوعة (3,120 ساعة) خلال 5 سنوات في NOC واحد');
 if(trade==='exp')f.push('يتطلب عرض عمل دوام كامل ≥ سنة أو شهادة كفاءة كندية في الحرفة');
 if(fstnoc==='no')f.push('مهنتك خارج مجموعات NOC المؤهلة لـFST — TEER 2-3 وحده لا يكفي');
 if(fstnoc==='unknown'&&trade!=='no')u.push('مطابقة مهنتك مع مجموعات NOC المؤهلة في <a href="https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/who-can-apply/federal-skilled-trades.html">صفحة FST الرسمية</a>');
 if(clb===0)u.push('نتيجة اختبار لغة');else if(clb<4)f.push('الحد الأدنى CLB 5 تحدث/استماع وCLB 4 قراءة/كتابة');else if(clb<5)u.push('تحقق أن التحدث/الاستماع ≥ CLB 5');
 if(!fswExempt&&!hasFunds)f.push('إثبات أموال ('+FUNDS.toLocaleString()+'$) ما لم ينطبق الإعفاء الثنائي');
 if(qc==='yes')f.push('نية سكن في كيبيك');
 R.push({n:'FST — المهن الحرفية الفيدرالية (Express Entry)',f,u,note:'الأهلية بمجموعات NOC محددة (72 عدا 726، 73، 82، 83، 92، 93 عدا 932، 6320، 62200) وليس بفئة TEER وحدها — تحقق 2026-11-22 من الصفحة الرسمية.',cost:PRFEE,next:'مطابقة NOC ثم بطاقة <a href="../../03-ALL-PROGRAMS/federal/fst-federal-skilled-trades/">FST</a>.'});
 // Work permit
 f=[];u=[];
 if(offer==='none')f.push('لا عرض عمل — هو بوابة هذا المسار كله');
 if(offer==='lmia')u.push('صدور LMIA الإيجابي (على صاحب العمل، 1,000$/منصب — يُحظر تحميلك أي رسوم توظيف)');
 if(offer==='exempt')u.push('تأكد أن رمز الإعفاء معترف به لحالتك (C61-C63/C16/C18/C15...)');
 if(offer!=='none'&&desig==='yes')u.push('اعتماد صاحب العمل يفتح أيضاً AIP/RCIP/PNP — قارن المسار الدائم الموازي');
 R.push({n:'تصريح عمل بصاحب عمل (TFWP/IMP)',f,u,note:'رسوم العامل: 155$ تصريح + 85$ بيومترية. تحقق من قائمة أصحاب العمل غير الملتزمين (S55).',cost:'155$ تصريح + 85$ بيومترية — '+CALC,next:'البحث عن عرض عمل عبر <a href="../../04-WORK-IN-CANADA/work-and-employers/">دليل العمل وأصحاب العمل</a>.'});
 // Study
 f=[];u=[];
 if(loa==='no')f.push('لا قبول من DLI');
 const studyNeed=23448;
 if(funds<studyNeed)f.push('إثبات أموال دراسة: معيشة '+studyNeed.toLocaleString()+'$/سنة + رسوم أول سنة (+~6,300$ لكل مرافق)');
 u.push('PAL/TAL أو إعفاء موثق (ماجستير/دكتوراه DLI عامة معفاة من 2026-01-01)');
 R.push({n:'تصريح دراسة',f,u,note:'الدراسة لا تضمن PR؛ المسار الشائع PGWP ثم CEC/PNP.',cost:'150$ تصريح + 85$ بيومترية + أموال إثبات — '+CALC,next:'قبول DLI ثم بطاقة <a href="../../03-ALL-PROGRAMS/study/study-permit/">تصريح الدراسة</a>.'});
 // PNP family (manual)
 f=[];u=[];
 let pnpNote='71 مساراً إقليمياً بشروط تتغير بجولات متكررة — لا يحسمها محرك آلي.';
 if(offer!=='none')u.push('تحقق من تيارات عرض العمل في مقاطعة صاحب العمل (بطاقات 03-ALL-PROGRAMS/provincial)');
 else if(fexp>=1&&clb>=4)u.push('تحقق يدوي: تيارات مرتبطة بـExpress Entry أو بمهن مطلوبة (SINP/OINP/AAIP...)');
 else u.push('تحقق يدوي: معظم التيارات تتطلب عرض عمل أو ملف Express Entry أو صلة بالمقاطعة');
 if(qc==='yes')u.push('كيبيك لها نظامها الخاص — انظر بطاقة كيبيك أدناه');
 R.push({n:'PNP — برامج ترشيح المقاطعات',f,u,note:pnpNote+' لا يُستبعد ولا يُقبل آلياً هنا.',cost:'رسوم المقاطعة تختلف (بعضها مجاني/بعضها مئات الدولارات) + رسوم PR الفيدرالية — '+CALC,next:'افتح <a href="../../03-ALL-PROGRAMS/provincial/">بطاقات المقاطعات الـ13</a> وقارن تياراً واحداً بملفك.'});
 // AIP / RCIP
 f=[];u=[];
 if(offer==='none')f.push('لا عرض عمل — بوابة البرامجين');
 if(offer!=='none'&&desig!=='yes')u.push(desig==='unknown'?'تأكد أن صاحب العمل معتمد (designated) في AIP أو مصنّف في RCIP':'صاحب العمل غير معتمد — البوابة غير مستوفاة حتى يعتمد');
 R.push({n:'AIP / RCIP — الأطلسي والمجتمعات الريفية',f,u,note:'مسارات مبنية على صاحب عمل معتمد في منطقة مؤهلة.',cost:'رسوم PR الفيدرالية نفسها — '+CALC,next:'قوائم أصحاب العمل المعتمدين في <a href="../../04-WORK-IN-CANADA/work-and-employers/">04</a> وبطاقة البرنامج.'});
 // Quebec
 f=[];u=[];
 if(qc==='no'){R.push({n:'كيبيك (Arrima/PEQ/أعمال)',info:true,f,u,note:'خارج نطاق نيتك الحالية (اخترت «لا كيبيك»). لكيبيك نظام اختيار خاص عبر MIFI يتطلب عموماً الفرنسية.',cost:'',next:'إن غيّرت نيتك: <a href="../../03-ALL-PROGRAMS/provincial/quebec-system/">بطاقة كيبيك</a>.'});}
 else{u.push('تقييم يدوي عبر نظام كيبيك (MIFI/Arrima) — الفرنسية شرط محوري');R.push({n:'كيبيك (Arrima/PEQ/أعمال)',f,u,note:'اختيار مزدوج: CSQ من MIFI ثم PR فيدرالي.',cost:'رسوم كيبيك + فيدرالية — '+CALC,next:'<a href="../../03-ALL-PROGRAMS/provincial/quebec-system/">بطاقة كيبيك (النظام المستقل)</a>.'});}
 // Family sponsorship
 f=[];u=[];
 if(rel==='no')f.push('لا قريب مؤهل مصرحاً عنه — الكفالة تتطلب زوجاً/شريكاً أو والداً مواطناً أو مقيماً دائماً');
 else u.push('تحقق من أهلية الكفيل (إقامة، دخل/تعهد، لا إعانات) وصحة إثبات العلاقة');
 R.push({n:'لمّ الشمل — كفالة زوج/شريك/والدين',f,u,note:rel==='yes'?'كفالة الزوج/الشريك مفتوحة؛ PGP للوالدين متوقف حالياً (البديل: Super Visa).':'',cost:'كفالة زوج/شريك شاملة 1,260$ (2026-11-22) — '+CALC,next:rel==='yes'?'<a href="../../03-ALL-PROGRAMS/family/spousal-sponsorship/">بطاقة كفالة الزوج/الشريك</a>.':''});
 // Business (static)
 R.push({n:'الأعمال والاستثمار',info:true,f:[],u:[],note:'SUV وبرنامج العاملين لحسابهم <b>متوقفان</b> (تحقق 2026-11-22)؛ برنامجا المستثمر/رائد الأعمال الفيدراليان مغلقان منذ 2014؛ لا يوجد مسار «استثمار مقابل إقامة» فيدرالي. المتاح: كيبيك للأعمال بشروط MIFI.',cost:'',next:'<a href="../../03-ALL-PROGRAMS/provincial/quebec-business/">بطاقة كيبيك للأعمال</a> · <a href="../../03-ALL-PROGRAMS/closed-paused/suv-startup-visa/">بطاقة SUV</a>.'});
 // Protection (static)
 R.push({n:'مسارات الحماية (لجوء/إعادة توطين/H&C)',info:true,f:[],u:[],note:'ليست مسارات هجرة اختيارية ولا تُقيَّم ذاتياً: اللجوء يتطلب وجوداً داخل كندا وأسباب حماية فعلية (قواعد 2026 مشددة)، وإعادة التوطين لا تُقبل إلا بإحالة UNHCR أو كفيل مؤهل.',cost:'',next:'<a href="../../03-ALL-PROGRAMS/protection/asylum-in-canada/">بطاقات الحماية</a>.'});
 // rank
 const order=r=>r.info?3:r.f.length===0&&r.u.length===0?0:r.f.length===0?1:2;
 const ranked=R.filter(r=>!r.info).sort((a,b)=>order(a)-order(b));
 let h='';
 for(const r of R){
  const cls=r.info?'info':r.f.length?'no':r.u.length?'maybe':'ok';
  const verdict=r.info?'معلومة — خارج التقييم الآلي':r.f.length?'مستبعد حالياً ببوابة صلبة':r.u.length?'قابل للتحقيق — معلومات/وثائق ناقصة':'مستوفٍ مبدئياً للبوابات الموثقة (لا يعني قبولاً)';
  h+='<div class="card '+cls+'"><div class="v">'+r.n+' ← '+verdict+'</div>';
  if(r.f.length)h+='<ul>'+r.f.map(x=>'<li>يستبعد: '+x+'</li>').join('')+'</ul>';
  if(r.u.length)h+='<ul>'+r.u.map(x=>'<li>ينقص/يحتاج تحقق: '+x+'</li>').join('')+'</ul>';
  if(r.note)h+='<div style="opacity:.8">'+r.note+'</div>';
  if(r.cost)h+='<div class="cost">'+r.cost+'</div>';
  if(r.next)h+='<div class="cost">الخطوة التالية: '+r.next+'</div>';
  h+='</div>';
 }
 // top three + backup
 const inv=ranked.filter(r=>order(r)<=1);
 const top3=inv.slice(0,3);
 const backup=inv.length>3?inv[3]:(ranked.find(r=>order(r)===2&&!top3.includes(r))||null);
 h+='<div class="card"><div class="v">خلاصة المقارنة — أقرب المسارات للتحقيق (وليست تأكيد أهلية):</div>';
 if(top3.length){
  h+='<ol>'+top3.map(r=>'<li><b>'+r.n+'</b>'+(r.u.length?' — بشرط استكمال: '+r.u.join('؛ '):' — البوابات الموثقة مستوفاة مبدئياً؛ القبول النهائي تنافسي/تقديري لدى IRCC')+'</li>').join('')+'</ol>';
  if(backup)h+='<div>خيار احتياطي: <b>'+backup.n+'</b>'+(backup.f.length?' — حالياً مستبعد: '+backup.f[0]:'')+'</div>';
 }else{
  h+='<div>لا مسار قريب حالياً — عالج أسباب الاستبعاد بدءاً بالبوابة الأسهل (غالباً اللغة أو عرض العمل)، ثم أعد المقارنة.</div>';
 }
 h+='<br><span style="opacity:.8">مقارنة آلية أولية بقواعد بتاريخ تحقق 2026-11-22؛ القرار النهائي لضباط IRCC ولصفحات البرامج الرسمية. العائلات الإقليمية والخاصة أُدرجت بمخرجات «يحتاج تحقق يدوي» لأن أدلتها لا تدعم حسمًا آلياً. لا تُحتسب هنا نسب نجاح — لا توجد بيانات رسمية لذلك.</span></div>';
 document.getElementById('de-out').innerHTML=h;
 document.getElementById('de-out').scrollIntoView({behavior:'smooth'});
}
</script>

## حدود هذا المحرك

- يحسم آلياً بوابات المسارات الفيدرالية الخمسة الموثقة بقواعد YAML فقط؛ عائلات PNP وAIP/RCIP وكيبيك ولمّ الشمل تُدرج دائماً في المقارنة بمخرجات «يحتاج تحقق يدوي» مع بواباتها الشائعة وروابط بطاقاتها، ولا تُتجاهل ولا تُحسم بلا أدلة.
- الأعمال والحماية تظهر كبطاقات معلومات بحالتها الرسمية (متوقف/مشروط) ولا تُقيَّم كمسارات اختيارية.
- لا يحسب نقاط CRS التفصيلية ولا شبكة الـ67 رقماً — يوجهك لأدلتها الرسمية والداخلية.
- FST: الأهلية بمجموعات NOC المحددة في الصفحة الرسمية (تحقق 2026-11-22)، وTEER وحده لا يؤهل ولا يستبعد.
- كل قاعدة هنا مأخوذة حرفياً من ملفات القواعد الموثقة بتاريخها ومصادرها؛ عند تعارض، البطاقة ومصدرها الرسمي يتقدمان.
