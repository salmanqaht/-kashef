import streamlit as st
import re
from urllib.parse import urlparse
import math
from datetime import datetime
import requests

st.set_page_config(page_title="كاشف V6 Pro", page_icon="🛡️", layout="centered")

# --- CSS V6 Pro ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@700;500&display=swap');
html, body, [class*="css"] {font-family: 'Tajawal', sans-serif;}
.stApp {background: radial-gradient(circle at top, #1e293b 0%, #0f172a 100%);}
h1,h2,h3,p,label,span {color: white!important;}
input {direction: ltr!important; text-align: left!important;}
.card {background: rgba(255,255,255,0.07); border: 1px solid rgba(255,255,255,0.15); border-radius: 18px; padding: 18px; margin-bottom: 12px; backdrop-filter: blur(12px);}
.metric {font-size: 32px; font-weight: 800;}
.badge {padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: bold;}
</style>
""", unsafe_allow_html=True)

st.title("🛡️ كاشف V6 Pro")
st.markdown("<p style='text-align:center; opacity:0.7'>محرك كشف التصيد المعتمد على 9 خوارزميات + فحص مباشر</p>", unsafe_allow_html=True)

url_input = st.text_input("🔗 الصق الرابط المشبوه", placeholder="https://example-bank-login.tk/verify")

POPULAR = ["google.com","youtube.com","facebook.com","twitter.com","instagram.com","paypal.com","apple.com","microsoft.com","amazon.com","bankaljazira.com","alinma.com","stc.com.sa"]

def entropy(s):
    if not s: return 0
    p, lns = {}, float(len(s))
    for c in s: p[c]=p.get(c,0)+1
    return -sum((v/lns)*math.log2(v/lns) for v in p.values())

def is_typosquat(domain):
    for pop in POPULAR:
        if pop in domain and pop!= domain and len(domain) > len(pop)+2:
            return True, pop
        # تشابه حروف
        if abs(len(domain)-len(pop))<3 and domain.replace("-","")!= pop:
            # حساب بسيط للتشابه
            if pop.split('.')[0] in domain and domain!= pop:
                return True, pop
    return False, ""

def analyze_v6(url):
    score = 0
    logs = []
    parsed = urlparse(url)
    domain = parsed.netloc.lower().replace("www.","")
    path = parsed.path + parsed.query

    # 1. HTTPS
    if parsed.scheme!= "https":
        score+=20
        logs.append(("🔓 بدون HTTPS","الموقع لا يستخدم تشفير، بياناتك مكشوفة","🔴"))
    else:
        logs.append(("🔒 يستخدم HTTPS","جيد، لكنه لا يعني أنه آمن 100%","🟢"))

    # 2. IP
    if re.match(r"^\d+\.\d+\.\d+\.\d+", domain):
        score+=35
        logs.append(("🌐 رابط IP مباشر","الهاكرز يستخدمون IP لتجاوز الحجب","🔴"))

    # 3. Shortener
    if domain in ["bit.ly","tinyurl.com","t.me","goo.gl","is.gd","cutt.ly","shorturl.at"]:
        score+=25
        logs.append(("✂️ رابط مختصر","يخفي الوجهة الحقيقية - حركة تصيد مشهورة","🟡"))

    # 4. Typosquat
    typo, orig = is_typosquat(domain)
    if typo:
        score+=30
        logs.append((f"🎭 انتحال {orig}",f"الدومين {domain} يحاول يقلد {orig}","🔴"))

    # 5. TLD مشبوه
    if any(domain.endswith(t) for t in [".tk",".ml",".ga",".cf",".gq",".xyz",".top"]):
        score+=15
        logs.append(("⚠️ نطاق مجاني مشبوه","نطاقات.tk و.xyz تستخدم كثير في التصيد","🟡"))

    # 6. طول وتعقيد
    if len(url) > 90:
        score+=10
        logs.append((f"📏 رابط طويل ({len(url)} حرف)","لإخفاء الدومين الحقيقي","🟡"))
    if "@" in url or domain.count("-")>=3:
        score+=15
        logs.append(("❗ رموز تضليل @ -","محاولة لإيهامك انه موقع ثاني","🟡"))

    # 7. كلمات تصيد
    words = ["login","verify","secure","account","update","bank","confirm","webscr"]
    found = [w for w in words if w in url.lower()]
    if found:
        score+=15
        logs.append((f"🎣 كلمات ضغط: {', '.join(found)}","يضغط عليك لتسجيل الدخول بسرعة","🟡"))

    # 8. Entropy
    if entropy(domain) > 4.3:
        score+=10
        logs.append(("🔀 اسم عشوائي","الدومين يبدو مولد آلياً","🟡"))

    # 9. فحص مباشر (Redirect)
    try:
        r = requests.head(url, timeout=4, allow_redirects=True)
        if len(r.history) >= 2:
            score+=10
            logs.append((f"🔁 يعيد توجيه {len(r.history)} مرات","يمررك عبر مواقع وسيطة لجمع بياناتك","🟡"))
    except:
        logs.append(("📡 غير متاح للفحص المباشر","الموقع لا يستجيب أو يمنع الفحص","⚪"))

    # النتيجة النهائية
    score = min(score, 100)
    if score >= 65: level, color = "خطر مؤكد - لا تدخل! ⛔", "#ef4444"
    elif score >= 35: level, color = "مشبوه جداً - انتبه ⚠️", "#f59e0b"
    else: level, color = "يبدو سليم ✅", "#22c55e"

    return score, level, color, logs

if st.button("افحص الآن بذكاء V6 🚀"):
    if not url_input.strip():
        st.warning("الصق رابط أول")
    else:
        url = url_input.strip()
        if not url.startswith("http"): url = "https://"+url

        with st.spinner("جاري فحص 9 طبقات حماية..."):
            score, level, color, logs = analyze_v6(url)

        st.markdown(f"""
        <div class="card" style="border-right:6px solid {color}; text-align:center">
            <div style="font-size:18px; opacity:0.8">{level}</div>
            <div class="metric" style="color:{color}">{score}% خطورة</div>
            <div style="height:10px; background:rgba(255,255,255,0.2); border-radius:10px; margin-top:10px">
                <div style="width:{score}%; height:100%; background:{color}; border-radius:10px"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        for title, desc, icon in logs:
            st.markdown(f"""
            <div class="card" style="text-align:right">
                <div style="display:flex; justify-content:space-between">
                    <span class="badge" style="background:rgba(255,255,255,0.15)">{icon}</span>
                    <b>{title}</b>
                </div>
                <div style="opacity:0.8; font-size:13px; margin-top:6px">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

        # زر التقرير
        report = f"تقرير كاشف V6 Pro\nالرابط: {url}\nالنتيجة: {level} ({score}%)\nالتاريخ: {datetime.now()}\n\nالتفاصيل:\n" + "\n".join([f"- {t}: {d}" for t,d,_ in logs])
        st.download_button("📄 حمّل تقرير الفحص (للمسابقة)", report, file_name="Kashef_V6_Report.txt")

        if score >= 65:
            st.error("نصيحة: لا تدخل بياناتك أبداً في هذا الرابط، وبلغ عنه في أبشر أو هيئة الأمن السيبراني")
else:
    st.markdown("""
    <div class="card" style="text-align:right">
    <b>🆕 وش الجديد في V6؟</b><br>
    <span style="font-size:13px; opacity:0.8">
    • يكشف انتحال المواقع (مثل paypa1 بدل paypal)<br>
    • يكشف الروابط المختصرة والمجانية<br>
    • يفحص إعادة التوجيه المباشرة<br>
    • يعطيك تقرير جاهز للمسابقة
    </span>
    </div>
    """, unsafe_allow_html=True)

# شريط جانبي
st.caption("V6 Pro | صنع في مكة 🕋 | لمسابقة الأمن السيبراني 2026")
