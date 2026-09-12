import streamlit as st
import re
from urllib.parse import urlparse

st.set_page_config(page_title="كاشف - فاحص الروابط", page_icon="🛡️", layout="centered")

st.markdown("""
<style>
    .stApp { background-color: #f8f9fa; }
    .main-card {
        background: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        border: 1px solid #e9ecef;
        text-align: center;
        margin-bottom: 20px;
    }
    .title { color: #1a73e8; font-size: 42px; font-weight: bold; margin-bottom: 5px; }
    .subtitle { color: #5f6368; font-size: 16px; }
    .stButton>button {
        background-color: #1a73e8;
        color: white;
        border-radius: 10px;
        height: 50px;
        width: 100%;
        font-size: 18px;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover { background-color: #1557b0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-card"><div class="title">🛡️ كاشف</div><div class="subtitle">نظام ذكي لفحص الروابط المشبوهة وحمايتك من التصيد الاحتيالي</div></div>', unsafe_allow_html=True)

url = st.text_input(" ", placeholder="الصق الرابط هنا مثل: https://example.com", label_visibility="collapsed")

def check_url(u):
    score = 0
    reasons = []
    if not u.startswith("https://"):
        score += 30
        reasons.append("الرابط لا يستخدم اتصال آمن https")
    if len(u) > 75:
        score += 20
        reasons.append("الرابط طويل بشكل مريب")
    if "@" in u or re.search(r"\d+\.\d+\.\d+\.\d+", u):
        score += 40
        reasons.append("يحتوي على رموز أو IP مشبوه")
    if urlparse(u).netloc.count("-") > 2 or urlparse(u).netloc.count(".") > 3:
        score += 20
        reasons.append("اسم النطاق يبدو مقلد")
    suspicious_words = ["login", "verify", "update", "secure", "bank", "free", "gift"]
    if any(w in u.lower() for w in suspicious_words):
        score += 15
        reasons.append("يحتوي على كلمات تستهدف سرقة البيانات")
    return score, reasons

if st.button("افحص الآن 🔍"):
    if not url:
        st.warning("الرجاء لصق رابط أولاً")
    else:
        if not url.startswith("http"):
            url = "http://" + url
        score, reasons = check_url(url)
        if score < 30:
            st.success(f"### ✅ آمن بنسبة كبيرة ({100-score}%)")
            st.write("الرابط يبدو سليم ولم نجد علامات خطيرة فيه.")
        elif score < 70:
            st.warning(f"### ⚠️ مشبوه - كن حذر ({score}% خطورة)")
            for r in reasons:
                st.write(f"- {r}")
        else:
            st.error(f"### 🚨 خطير جداً - لا تفتحه! ({score}% خطورة)")
            for r in reasons:
                st.write(f"- {r}")

st.markdown("---")
st.caption("تم تطويره بواسطة سلمان القحطاني - مشروع كاشف 2026")
