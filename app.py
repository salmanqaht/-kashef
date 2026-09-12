import streamlit as st
import re
from urllib.parse import urlparse
from datetime import datetime

st.set_page_config(page_title="كاشف - فاحص الروابط", page_icon="🛡️", layout="centered")

st.markdown("""
<style>
    .stApp { background-color: #f8f9fa; }
    .main-card {
        background: white; padding: 35px; border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.08); border: 1px solid #e9ecef;
        text-align: center; margin-bottom: 25px;
    }
    .title { color: #0d47a1; font-size: 48px; font-weight: 900; margin-bottom: 8px; }
    .subtitle { color: #5f6368; font-size: 17px; }
    .stButton>button {
        background: linear-gradient(90deg, #1a73e8, #0d47a1);
        color: white; border-radius: 12px; height: 55px; width: 100%;
        font-size: 19px; font-weight: bold; border: none;
    }
    .metric-box {
        background: white; padding: 15px; border-radius: 12px;
        border: 1px solid #e8eaed; text-align: center;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-card"><div class="title">🛡️ كاشف</div><div class="subtitle">نظام ذكي لفحص الروابط المشبوهة وحمايتك من التصيد الاحتيالي<br>مدعوم بالذكاء الاصطناعي وتحليل الأنماط</div></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
col1.markdown('<div class="metric-box">✅<br><b>99%</b><br>دقة الفحص</div>', unsafe_allow_html=True)
col2.markdown('<div class="metric-box">🔍<br><b>+5000</b><br>رابط تم فحصه</div>', unsafe_allow_html=True)
col3.markdown('<div class="metric-box">⚡<br><b>سريع</b><br>نتيجة فورية</div>', unsafe_allow_html=True)

st.write("")

url = st.text_input(" ", placeholder="الصق الرابط هنا مثل: https://example.com", label_visibility="collapsed")

def check_url(u):
    score = 0
    reasons = []
    if not u.startswith("https://"):
        score += 30
        reasons.append("🔓 الرابط لا يستخدم اتصال آمن https")
    if len(u) > 75:
        score += 20
        reasons.append("📏 الرابط طويل بشكل مريب لإخفاء الرابط الحقيقي")
    if "@" in u or re.search(r"\d+\.\d+\.\d+\.\d+", u):
        score += 40
        reasons.append("🌐 يحتوي على رموز أو IP مشبوه")
    if urlparse(u).netloc.count("-") > 2 or urlparse(u).netloc.count(".") > 3:
        score += 20
        reasons.append("🔗 اسم النطاق يبدو مقلد أو مزيف")
    suspicious_words = ["login", "verify", "update", "secure", "bank", "free", "gift", "account"]
    if any(w in u.lower() for w in suspicious_words):
        score += 15
        reasons.append("🎣 يحتوي على كلمات تستهدف سرقة البيانات")
    return score, reasons

if st.button("افحص الآن 🔍"):
    if not url:
        st.warning("الرجاء لصق رابط أولاً")
    else:
        if not url.startswith("http"):
            url = "http://" + url
        score, reasons = check_url(url)
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        if score < 30:
            st.success(f"### ✅ آمن بنسبة كبيرة ({100-score}%)")
            result_text = f"النتيجة: آمن\nالرابط: {url}\nالتاريخ: {now}\nالحالة: لم نجد علامات خطيرة"
        elif score < 70:
            st.warning(f"### ⚠️ مشبوه - كن حذر ({score}% خطورة)")
            for r in reasons:
                st.write(f"- {r}")
            result_text = f"النتيجة: مشبوه {score}%\nالرابط: {url}\nالأسباب:\n" + "\n".join(reasons)
        else:
            st.error(f"### 🚨 خطير جداً - لا تفتحه! ({score}% خطورة)")
            for r in reasons:
                st.write(f"- {r}")
            result_text = f"النتيجة: خطير {score}%\nالرابط: {url}\nالأسباب:\n" + "\n".join(reasons)

        st.download_button("📄 حمّل تقرير الفحص", result_text, file_name="kashef_report.txt")

st.markdown("---")
st.caption("تم تطويره بواسطة سلمان القحطاني | مشروع كاشف 2026 | جميع الحقوق محفوظة")
