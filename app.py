import streamlit as st
import re
from urllib.parse import urlparse
import math, requests
from datetime import datetime

st.set_page_config(page_title="كاشف V7 Ultra", page_icon="🛡️", layout="centered")

# --- تصميم Ultra ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap');
html, body, [class*="css"] {font-family: 'Tajawal', sans-serif;}
.stApp {background: radial-gradient(ellipse at top, #1e40af 0%, #1e3a8a 40%, #0f172a 100%);}

.main-title {text-align:center; color:white!important; font-size:42px; font-weight:900; margin-bottom:0;}
.sub-title {text-align:center; color:#93c5fd!important; font-size:16px; margin-top:5px;}

.glass {background: rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.15); border-radius:20px; padding:22px; backdrop-filter: blur(16px); margin:12px 0;}
.input-box input {background: rgba(0,0,0,0.35)!important; color:white!important; border-radius:14px!important; height:56px!important; border:1px solid rgba(255,255,255,0.2)!important; font-size:16px; direction:ltr; text-align:left;}

.score-circle {width:110px; height:110px; border-radius:50%; display:flex; align-items:center; justify-content:center; margin:0 auto; font-size:36px; font-weight:900; color:white;}

.detail-row {display:flex; justify-content:space-between; align-items:center; padding:12px 0; border-bottom:1px solid rgba(255,255,255,0.08);}
.detail-row:last-child {border-bottom:none;}
.badge-high {background:#ef4444; color:white; padding:3px 10px; border-radius:20px; font-size:11px;}
.badge-med {background:#f59e0b; color:white; padding:3px 10px; border-radius:20px; font-size:11px;}
.badge-low {background:#22c55e; color:white; padding:3px 10px; border-radius:20px; font-size:11px;}
.badge-info {background:rgba(255,255,255,0.15); color:#cbd5e1; padding:3px 10px; border-radius:20px; font-size:11px;}

div.stButton > button {background: linear-gradient(90deg, #22c55e, #16a34a); color:white; border:none; border-radius:14px; height:54px; font-weight:800; font-size:18px; width:100%; box-shadow: 0 8px 20px rgba(34,197,94,0.3);}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🛡️ كاشف</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">V7 Ultra - نظام كشف التصيد الذكي بـ 9 محركات فحص</div>', unsafe_allow_html=True)

st.markdown('<div class="glass input-box">', unsafe_allow_html=True)
url_input = st.text_input("رابط", placeholder="https://example.com/login", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

POPULAR_DOMAINS = ["paypal.com","google.com","apple.com","microsoft.com","facebook.com","stc.com.sa","alinma.com"]

def analyze_ultra(url):
    score=0
    checks=[]
    parsed=urlparse(url)
    domain=parsed.netloc.lower().replace("www.","")

    # 1
    if parsed.scheme!="https":
        score+=20; checks.append(("التشفير","بدون HTTPS - البيانات مكشوفة","🔓",20,"high","الموقع لا يستخدم شهادة آمنة، أي بيانات تدخلها تنسرق بسهولة"))
    else:
        checks.append(("التشفير","يستخدم HTTPS","🔒",0,"low","جيد، لكن التصيد صار يستخدم HTTPS بعد"))

    # 2
    if re.match(r"^\d+\.\d+\.\d+\.\d+", domain):
        score+=30; checks.append(("نوع الدومين","رابط IP مباشر","🌐",30,"high","المواقع الحقيقية لها اسم، الهاكرز يستخدمون أرقام لإخفاء الهوية"))
    # 3
    if any(domain.endswith(t) for t in [".tk",".ml",".ga",".cf",".xyz",".top"]):
        score+=15; checks.append(("نطاق مجاني",".tk /.xyz","⚠️",15,"med","90% من مواقع التصيد تستخدم نطاقات مجانية"))
    # 4
    typo=False
    for pop in POPULAR_DOMAINS:
        if pop in domain and domain!=pop:
            typo=True; break
    if typo:
        score+=25; checks.append(("انتحال علامة","يحاول يقلد موقع مشهور","🎭",25,"high",f"الدومين {domain} يقلد مواقع معروفة مثل {POPULAR_DOMAINS[0]}"))
    # 5
    if "@" in url:
        score+=20; checks.append(("خدعة @","فيه رمز @","❗",20,"high","المتصفح يقرأ ما بعد @ فقط، اللي قبله خدعة"))
    if domain.count("-")>=3:
        score+=10; checks.append(("شرطات كثيرة","- - -","➖",10,"med","المواقع الأصلية ما تستخدم شرطات كثيرة"))
    # 6
    found=[w for w in ["login","verify","secure","account","webscr","update","bank"] if w in url.lower()]
    if found:
        score+=12; checks.append(("كلمات ضغط"," ".join(found),"🎣",12,"med","كلمات تخليك تستعجل وتدخل بياناتك"))
    # 7
    if len(url)>90:
        score+=8; checks.append(("طول الرابط",f"{len(url)} حرف","📏",8,"med","الرابط الطويل يخفي الدومين الحقيقي"))
    # 8
    try:
        r=requests.head(url, timeout=3, allow_redirects=True)
        if len(r.history)>=1:
            score+=8; checks.append(("إعادة توجيه",f"{len(r.history)} قفزات","🔁",8,"med","يمررك على مواقع وسيطة لتتبعك"))
    except:
        checks.append(("الاتصال","لا يستجيب","📡",0,"info","الموقع مغلق أو يمنع الفحص"))

    return min(score,100), checks

if st.button("افحص الآن - فحص عميق 🔍"):
    if not url_input.strip():
        st.warning("حط رابط أول")
    else:
        url = url_input.strip()
        if not url.startswith("http"): url="https://"+url

        with st.spinner("نفحص بـ 9 محركات..."):
            score, checks = analyze_ultra(url)

        # دائرة النتيجة
        if score>=65: color="#ef4444"; level="خطر مؤكد"
        elif score>=35: color="#f59e0b"; level="مشبوه"
        else: color="#22c55e"; level="آمن"

        st.markdown(f"""
        <div class="glass" style="text-align:center; border-top:4px solid {color}">
            <div class="score-circle" style="background:{color}; box-shadow:0 0 30px {color}80">{score}%</div>
            <h2 style="color:white!important; margin:15px 0 5px 0">{level}</h2>
            <p style="margin:0; opacity:0.8">نسبة الخطورة</p>
            <div style="background:rgba(255,255,255,0.15); height:10px; border-radius:10px; margin-top:15px">
                <div style="width:{score}%; background:{color}; height:100%; border-radius:10px; transition:1s"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # التفاصيل
        st.markdown('<div class="glass">', unsafe_allow_html=True)
        st.markdown("**📋 تقرير الفحص التفصيلي:**")
        for name, value, icon, pts, lvl, explain in checks:
            badge = "badge-high" if lvl=="high" else "badge-med" if lvl=="med" else "badge-low" if lvl=="low" else "badge-info"
            badge_txt = "خطر" if lvl=="high" else "متوسط" if lvl=="med" else "جيد" if lvl=="low" else "معلومة"
            st.markdown(f"""
            <div class="detail-row" style="text-align:right">
                <div>
                    <div style="font-weight:700; color:white">{icon} {name}: {value} <span class="{badge}">{badge_txt} +{pts}</span></div>
                    <div style="font-size:12px; color:#94a3b8; margin-top:4px">{explain}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # توصية
        if score>=65:
            st.error("⛔ توصية: لا تدخل أي بيانات! هذا تصيد واضح. بلّغ عنه فوراً.")
        elif score>=35:
            st.warning("⚠️ توصية: لا تسجل دخولك قبل ما تتأكد من الدومين حرف حرف.")

        report = f"تقرير كاشف V7 Ultra\nالرابط: {url}\nالخطورة: {score}% - {level}\nالتاريخ: {datetime.now()}\n\n" + "\n".join([f"- {n}: {v} | {e}" for n,v,i,p,l,e in checks])
        st.download_button("📄 حمّل تقرير المسابقة", report, "Kashef_V7_Report.txt")
else:
    st.markdown("""
    <div class="glass" style="text-align:right">
        <b style="color:white">✨ وش يخلي V7 أقوى؟</b><br><br>
        <div style="font-size:13px; color:#cbd5e1; line-height:22px">
        🔍 <b>9 محركات فحص</b> بدل 3<br>
        📊 <b>بار خطورة متحرك</b> + دائرة نسبة<br>
        🧠 <b>شرح لكل نقطة</b> - مو بس "خطر"، يقولك ليش<br>
        🎭 <b>كشف انتحال البنوك</b> والشركات<br>
        📄 <b>تقرير جاهز للجنة التحكيم</b><br>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.caption("Kashef V7 Ultra | صنع في مكة 🕋 | 2026")
