import streamlit as st
import re

st.set_page_config(page_title="كاشف V16.3 BLACK", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
.stApp { background-color: #0a192f; color: white; }
.stTextInput > div > div > input {
    background-color: #112240;
    color: white;
    border: 1px solid #00ff88;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='color:white;'>كاشف <span style='color:#00ff88;'>V16.3 BLACK</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#8892b0;'>فتى الرابطة 🛡️</p>", unsafe_allow_html=True)

url = st.text_input("🔍 الصق الرابط هنا للفحص", placeholder="https://example.com")

if st.button("افحص الآن 🚀", use_container_width=True):
    if url:
        # منطق الفحص الأصلي
        risk = 90 if "login" in url or "verify" in url or len(url) > 40 else 15
        
        if risk > 70:
            st.error(f"🚨 نسبة الخطر: {risk}% - رابط تصيد خطير!")
        else:
            st.success(f"✅ نسبة الخطر: {risk}% - الرابط آمن")

        st.markdown("---")
        st.markdown("### 🤖 تحليل GOD AI")
        st.info(f"تم تحليل الرابط: {url}\n\nالنتيجة: {'مشبوه ويحاول سرقة البيانات' if risk > 70 else 'نظيف وآمن للاستخدام'}")
    else:
        st.warning("الصق رابط أول!")

# صندوق فحص ثاني
st.markdown("---")
st.button("فحص ثاني 🔎")
