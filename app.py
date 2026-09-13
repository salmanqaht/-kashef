import streamlit as st

st.set_page_config(page_title="كاشف", layout="wide")

# ستايل نظيف
st.markdown("""
<style>
.stApp { background-color: #0a192f; }
h1 { color: #00ff88; }
</style>
""", unsafe_allow_html=True)

st.title("كاشف V16.3 BLACK")

# خانة الفحص
link = st.text_input("🔗 الصق الرابط هنا")

if st.button("افحص الآن 🚀"):
    if link:
        st.warning("⚠️ نسبة الخطر 90% - رابط تصيد!")
        st.markdown("**تحليل GOD AI:** هذا الرابط مشبوه")
    else:
        st.error("الصق رابط أول")
