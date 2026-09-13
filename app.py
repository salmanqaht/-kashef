import streamlit as st
import re
from urllib.parse import urlparse
import math

st.set_page_config(page_title="كاشف V5", page_icon="🛡️", layout="centered", initial_sidebar_state="collapsed")

# --- ستايل V5 ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
html, body, [class*="css"] {font-family: 'Tajawal', sans-serif;}
.stApp {background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);}
h1, h2, h3, p, label {color: white!important; text-align: center;}
.stTextInput input {direction: ltr; text-align: left; border-radius: 12px; height: 50px;}
div.stButton > button {width: 100%; background: #22c55e; color: white; border: none; border-radius: 12px; height: 50px; font-weight: bold; font-size: 18px;}
.card {background: rgba(255,255,255,0.1); backdrop-filter: blur(10px); border-radius: 16px; padding: 20px; margin: 10px 0; border: 1px solid rgba(255,255,255,0.2);}
</style>
""", unsafe_allow_html=True)

st.title("🛡️ كاشف V5")
st.markdown("<p style='opacity:0.8'>الذكاء الاصطناعي لكشف التصيد والروابط المشبوهة</p>", unsafe_allow_html=True)

url_input = st.text_input("🔗 الصق الرابط هنا", placeholder="https://example.com/login")

def entropy(s):
    p, lns = {}, float(len(s))
    for c in s: p[c] = p.get(c,0)+1
    return -sum((v/lns)*math.log2(v/lns) for v in p.values())

def analyze_v5(url):
    score = 0
    details = []
    parsed = urlparse(url)
    domain = parsed.netloc.lower()

    # 1. HTTPS
    if parsed.scheme!= "https":
        score += 25
        details.append(("🔓 بدون HTTPS", "الموقع لا يستخدم تشفير آمن", "high"))

    # 2. IP بدل دومين
    if re.match(r"^\d+\.\d+\.\d+\.\d+", domain):
        score += 30
        details.append(("🌐 يستخدم IP", "المواقع الحقيقية لا تستخدم أرقام IP", "high"))

    # 3. طول الرابط
    if len(url) > 75:
        score += 15
        details.append(("📏 رابط طويل جداً", f"الطول {len(url)} حرف - غالبا لإخفاء الدومين", "medium"))

    # 4. رموز تصيد
    if "@" in url or domain.count("-") >= 3 or domain.count(".") >= 4:
        score += 20
        details.append(("⚠️ رموز مشبوهة", "فيه @ أو شرطات كثيرة لتقليد موقع ثاني", "high"))

    # 5. كلمات تصيد
    phishing_words = ["login","verify","secure","account","bank","update","free","gift","urgent"]
    found = [w for w in phishing_words if w in url.lower()]
    if found:
        score += 20
        details.append((f"🎣 كلمات تصيد: {', '.join(found)}", "كلمات تضغطك عشان تدخل بياناتك", "medium"))

    # 6. Entropy عالي = دومين عشوائي
    if domain and entropy(domain) > 4.2:
        score += 10
        details.append(("🔀 دومين عشوائي", "اسم الدومين يبدو مولد بالكمبيوتر", "low"))

    # تحديد النتيجة
    if score >= 60:
        level, color, emoji = "خطر جداً 🔴", "#ef4444", "⛔"
    elif score >= 30:
        level, color, emoji = "مشبوه 🟡", "#f59e0b", "⚠️"
    else:
        level, color, emoji = "آمن 🟢", "#22c55e", "✅"

    return min(score, 100), level, color, emoji, details

if st.button("افحص الآن 🔍"):
    if not url_input:
        st.warning("حط رابط أول!")
    else:
        if not url_input.startswith("http"):
            url_input = "http://" + url_input

        score, level, color, emoji, details = analyze_v5(url_input)

        st.markdown(f"""
        <div class="card" style="border-left: 6px solid {color}">
            <h2 style="margin:0">{emoji} {level}</h2>
            <h1 style="margin:5px 0; color:{color}!important">{score}%</h1>
            <p>نسبة الخطورة</p>
        </div>
        """, unsafe_allow_html=True)

        if details:
            st.markdown("### 📋 التفاصيل:")
            for title, desc, _ in details:
                st.markdown(f"""
                <div class="card" style="text-align:right">
                    <b>{title}</b><br><span style="opacity:0.8; font-size:14px">{desc}</span>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="card">
                <b>✅ ما لقينا علامات تصيد واضحة</b><br>
                <span style="opacity:0.8">لكن خلك حذر دائماً</span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        st.caption("كاشف V5 - مشروع مسابقة الأمن السيبراني | صنع بواسطة سلمان")

else:
    st.markdown("""
    <div class="card">
        <p>💡 <b>كيف يشتغل؟</b><br>نحلل 6 علامات تصيد معروفة عالمياً ونعطيك تقرير فوري</p>
    </div>
    """, unsafe_allow_html=True)
