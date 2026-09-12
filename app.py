import streamlit as st
import re
from urllib.parse import urlparse
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="كاشف V3", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@700;900&display=swap');
    html, body, [class*="css"] { font-family: 'Tajawal', sans-serif; }
    .stApp { background: #f5f7fb; }
    .hero {
        background: linear-gradient(135deg, #0d47a1 0%, #2196F3 100%);
        padding: 35px; border-radius: 20px; text-align: center; color: white;
        box-shadow: 0 10px 30px rgba(33,150,243,0.3);
    }
    .hero h1 { font-size: 42px; font-weight: 900; margin: 0; color: white !important; }
    .hero p { color: white !important; font-size: 16px; margin-top: 10px; }
    .card {
        background: white; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05); border: 1px solid #eef0f4;
    }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stButton>button { background: #1976d2; color: white; border-radius: 12px; height: 48px; font-weight: bold; border: none; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero"><h1>🛡️ كاشف V3</h1><p>نظام الحماية الذكي | فحص روابط - فحص QR - تحليل متقدم</p></div>', unsafe_allow_html=True)
st.write("")

if 'history' not in st.session_state:
    st.session_state.history = []

c1, c2 = st.columns([2, 1])

def analyze_url(url):
    score = 0
    reasons = []
    parsed = urlparse(url)
    if not url.startswith("https://"): score+=25; reasons.append("🔓 لا يستخدم HTTPS")
    if len(url) > 80: score+=20; reasons.append(f"📏 رابط طويل جداً ({len(url)} حرف)")
    if re.search(r"\d+\.\d+\.\d+\.\d+", url): score+=40; reasons.append("🌐 يستخدم IP مشبوه بدل دومين")
    if "@" in url: score+=20; reasons.append("🎭 يحتوي رمز @ لخداعك")
    if parsed.netloc.count("-")>2: score+=15; reasons.append("🔗 اسم النطاق فيه شرطات كثيرة")
    if any(w in url.lower() for w in ["login","verify","bank","free","gift","secure"]): score+=15; reasons.append("🎣 كلمات تصيد احتيالي")
    return score, reasons

with c1:
    tab1, tab2 = st.tabs(["🔗 فحص رابط", "📷 فحص QR"])
    with tab1:
        url = st.text_input("الصق الرابط هنا للفحص", placeholder="https://example.com")
        if st.button("افحص الآن 🚀", use_container_width=True):
            if not url: st.warning("الصق رابط أولاً")
            else:
                if not url.startswith("http"): url = "http://"+url
                score, reasons = analyze_url(url)
                if score < 30:
                    st.success(f"✅ آمن - نسبة الأمان {100-score}%"); status="آمن"
                elif score < 65:
                    st.warning(f"⚠️ مشبوه - خطورة {score}%"); 
                    for r in reasons: st.write("- "+r); status="مشبوه"
                else:
                    st.error(f"🚨 خطير جداً! {score}% - لا تفتحه"); 
                    for r in reasons: st.write("- "+r); status="خطير"
                st.session_state.history.append({"الرابط": url[:35], "الحالة": status, "الخطورة": score, "الوقت": datetime.now().strftime("%H:%M")})

    with tab2:
        st.info("📷 ارفع صورة QR وسيتم فحصها قريباً - حالياً انسخ الرابط من الصورة والصقه في التبويب الأول")
        st.file_uploader("ارفع صورة QR", type=["png","jpg","jpeg"])

with c2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 لوحة التحكم")
    if st.session_state.history:
        df = pd.DataFrame(st.session_state.history)
        st.dataframe(df, use_container_width=True, hide_index=True)
        col_a, col_b = st.columns(2)
        col_a.metric("✅ آمن", len([x for x in st.session_state.history if x["الحالة"]=="آمن"]))
        col_b.metric("🚨 خطير", len([x for x in st.session_state.history if x["الحالة"]!="آمن"]))
    else:
        st.write("لا يوجد فحوصات بعد")
    st.markdown('</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div class="card"><b>💡 نصيحة</b><br>لا تفتح أي رابط يجيك من رقم غريب على واتساب قبل ما تفحصه هنا</div>', unsafe_allow_html=True)
