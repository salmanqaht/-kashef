import streamlit as st
import re
from urllib.parse import urlparse

st.set_page_config(page_title="كاشف", page_icon="🛡️", layout="centered")

st.markdown("""
<style>
body {direction: rtl;}
.stTextArea textarea {text-align: left; direction: ltr;}
</style>
""", unsafe_allow_html=True)

st.title("🛡️ كاشف - Kashef")
st.subheader("كاشف الروابط المشبوهة")

url = st.text_area("حط الرابط هنا:", placeholder="https://example.com")

def check_url(u):
    score = 0
    reasons = []
    if not u.startswith("http"):
        reasons.append("⚠️ الرابط ما يبدأ بـ https")
        score += 2
    if "@" in u or "-" in urlparse(u).netloc:
        reasons.append("⚠️ فيه رموز غريبة في الدومين")
        score += 2
    if len(u) > 75:
        reasons.append("⚠️ الرابط طويل بزيادة (تصيد غالبا)")
        score += 1
    if re.search(r"\d+\.\d+\.\d+\.\d+", u):
        reasons.append("⚠️ يستخدم IP بدل اسم موقع")
        score += 3
    suspicious = ["login", "verify", "secure", "bank", "free", "gift"]
    if any(w in u.lower() for w in suspicious):
        reasons.append("⚠️ فيه كلمات تصيد مثل login / verify")
        score += 2
    return score, reasons

if st.button("افحص"):
    if not url:
        st.warning("حط رابط أول")
    else:
        score, reasons = check_url(url)
        if score >= 4:
            st.error(f"🔴 خطر! هذا الرابط مشبوه جداً - نقاط الخطر {score}/8")
        elif score >= 2:
            st.warning(f"🟡 انتبه! فيه علامات تصيد - نقاط {score}/8")
        else:
            st.success(f"🟢 يبدو سليم - نقاط {score}/8")
        
        if reasons:
            for r in reasons:
                st.write(r)
