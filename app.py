import streamlit as st
import re
from urllib.parse import urlparse
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="كاشف V3.2", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
    .stApp { background: #f5f7fb; }
    .hero {
        background: linear-gradient(135deg, #0d47a1 0%, #42a5f5 100%);
        padding: 30px; border-radius: 18px; text-align: center; color: white;
    }
    .hero h1 { color: white !important; font-size: 40px; margin: 0; }
    .hero p { color: #e3f2fd !important; font-size: 15px; }
    .card { background: white; padding: 18px; border-radius: 14px; border: 1px solid #eef0f4; box-shadow: 0 2px 10px rgba(0,0,0,0.04); }
    
    /* هذا السطر يصلح مشكلة المربع الأسود */
    input[type="text"] {
        background-color: white !important;
        color: black !important;
        border: 2px solid #1976d2 !important;
    }
    .stTextInput input { background: white !important; color: black !important; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero"><h1>🛡️ كاشف V3.2</h1><p>نظام الحماية الذكي | فحص روابط و QR بذكاء اصطناعي</p></div>', unsafe_allow_html=True)
st.write("")

if 'history' not in st.session_state: st.session_state.history = []

def analyze_url(url):
    score=0; reasons=[]
    parsed=urlparse(url)
    if not url.startswith("https://"): score+=25; reasons.append("🔓 بدون HTTPS")
    if len(url)>75: score+=20; reasons.append(f"📏 طويل جداً ({len(url)} حرف)")
    if re.search(r"\d+\.\d+\.\d+\.\d+", url): score+=40; reasons.append("🌐 يستخدم IP مشبوه")
    if "@" in url or parsed.netloc.count("-")>2: score+=20; reasons.append("🎭 دومين مقلد")
    if any(w in url.lower() for w in ["login","verify","bank","free","gift"]): score+=15; reasons.append("🎣 كلمات تصيد")
    return score, reasons

col1, col2 = st.columns([2,1])

with col1:
    t1, t2 = st.tabs(["🔗 فحص رابط", "📷 فحص QR"])
    with t1:
        st.write("### الصق الرابط المشبوه هنا")
        url = st.text_input("الرابط", placeholder="مثال: https://example.com", label_visibility="collapsed")
        if st.button("افحص الآن 🚀", use_container_width=True):
            if not url: st.warning("الصق رابط")
            else:
                if not url.startswith("http"): url="http://"+url
                score, reasons = analyze_url(url)
                if score<30: st.success(f"✅ آمن {100-score}% - {url}"); status="آمن"
                elif score<65: st.warning(f"⚠️ مشبوه {score}%"); [st.write("- "+r) for r in reasons]; status="مشبوه"
                else: st.error(f"🚨 خطير {score}% لا تفتحه!"); [st.write("- "+r) for r in reasons]; status="خطير"
                st.session_state.history.append({"الرابط":url[:30], "الحالة":status, "الخطورة":score})

    with t2:
        st.info("ارفع صورة QR")
        st.file_uploader("QR", type=["png","jpg","jpeg"])

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 السجل")
    if st.session_state.history:
        df=pd.DataFrame(st.session_state.history)
        st.dataframe(df, use_container_width=True, hide_index=True)
    else: st.write("لا يوجد فحوصات بعد")
    st.markdown('</div>', unsafe_allow_html=True)

st.caption("كاشف V3.2 | سلمان القحطاني 2026")
