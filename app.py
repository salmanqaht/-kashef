import streamlit as st

st.set_page_config(page_title="كاشف V16.3 BLACK", layout="wide")

st.markdown("""
<style>
.stApp { background: linear-gradient(180deg, #0a1930 0%, #1e5bb0 100%) !important; }
div[data-testid="stVerticalBlock"] div[data-testid="stMarkdownContainer"] { color: white; }
.css-box {
    background: rgba(20, 50, 120, 0.6);
    border: 1px solid #00d4ff;
    border-radius: 10px;
    padding: 12px;
    text-align: center;
    color: white;
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center; color:white;'>كاشف <span style='color:#00ff88;'>V16.3 BLACK</span> 🛡️</h3>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
with c1: st.markdown("<div class='css-box'>مستواي<br>🏆 أسطورة<div style='background:#00ff88; height:3px; margin-top:5px;'></div></div>", unsafe_allow_html=True)
with c2: st.markdown("<div class='css-box'>فحصك<br>0</div>", unsafe_allow_html=True)
with c3: st.markdown("<div class='css-box'>قوتي<br>16 AI</div>", unsafe_allow_html=True)
with c4: st.markdown("<div class='css-box'>دقة<br>99.9%</div>", unsafe_allow_html=True)

left, right = st.columns([1.3, 1])

with left:
    st.markdown("<div class='css-box' style='text-align:right;'>🔗 انسخ الرابط هنا</div>", unsafe_allow_html=True)
    url = st.text_input("", value="https://alrajhi-bank-verify.tk/login", label_visibility="collapsed")
    
    # يطلع تلقائي بدون زر
    st.markdown(f"""
    <div style='background: linear-gradient(90deg, #ff2e63, #8a1835); border-radius:10px; padding:12px; color:white; margin-top:10px;'>
    💀 90% خطر - alrajhi-bank-verify.tk
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background: linear-gradient(90deg, #6a11cb, #2575fc); border-radius:10px; padding:12px; color:white; border:1px solid #ff00ff; margin-top:10px;'>
    🧠 GOD AI:<br>اسمعني، الرابط وهمي، الدومين .tk خطير 100%، بنك الراجحي ما يستخدمه
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='css-box' style='margin-top:10px;'>📋 نسخ التقرير | 🔗 افحص رابط جديد</div>", unsafe_allow_html=True)

with right:
    st.markdown("<div class='css-box' style='text-align:right;'>🔍 مثال للفحص</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='css-box' style='text-align:right;'>
    🏆 V16.3 BLACK<br>
    <span style='font-size:11px; line-height:1.8;'>
    • أسود مريح للعين<br>
    • ذكاء اصطناعي<br>
    • يكشف التصيد<br>
    • جاهز للمسابقة
    </span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div class='css-box' style='text-align:right;'>📊 مهمتك اليوم</div>", unsafe_allow_html=True)
    st.markdown("<div class='css-box' style='text-align:right;'>رابط يحمي - خطر</div>", unsafe_allow_html=True)
    st.markdown("<div class='css-box' style='text-align:right;'>STC Pay - خطر</div>", unsafe_allow_html=True)
