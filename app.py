import streamlit as st

st.set_page_config(page_title="كاشف V16.3 BLACK", layout="wide")

st.markdown("""
<style>
.stApp { background: linear-gradient(180deg, #0a1930 0%, #1a4b8c 100%); }
.css-box {
    background: rgba(255,255,255,0.08);
    border: 1px solid #00ff88;
    border-radius: 12px;
    padding: 15px;
    text-align: center;
    color: white;
}
.risk-box { background: linear-gradient(90deg, #ff2e63, #ff758c); border-radius: 10px; padding: 12px; color: white; }
.god-box { background: linear-gradient(90deg, #6a11cb, #2575fc); border-radius: 10px; padding: 12px; color: white; border: 1px solid #ff00ff; }
</style>
""", unsafe_allow_html=True)

# العنوان
st.markdown("<h2 style='text-align:center; color:white;'>كاشف <span style='color:#00ff88;'>V16.3 BLACK</span> 🛡️</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#8892b0; font-size:12px;'>النسخة السوداء - مريحة للعين V16.3</p>", unsafe_allow_html=True)

# 4 كروت فوق
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown("<div class='css-box'>مستوى<br>🏆 أسطورة<div style='background:#00ff88; height:4px; margin-top:8px;'></div></div>", unsafe_allow_html=True)
with c2:
    st.markdown("<div class='css-box'>فحصك<br>0</div>", unsafe_allow_html=True)
with c3:
    st.markdown("<div class='css-box'>قوة<br>16 AI</div>", unsafe_allow_html=True)
with c4:
    st.markdown("<div class='css-box'>دقة<br>99.9%</div>", unsafe_allow_html=True)

st.write("")

left, right = st.columns([1.2, 1])

with left:
    st.markdown("<div class='css-box' style='text-align:right;'>🔗 انسخ الرابط هنا</div>", unsafe_allow_html=True)
    url = st.text_input("", value="https://alrajhi-bank-verify.tk/login", label_visibility="collapsed")
    if st.button("افحص الآن ✅", use_container_width=True):
        st.session_state['checked'] = True
    
    if st.session_state.get('checked'):
        st.markdown("<div class='risk-box'>💀 90% خطر - alrajhi-bank-verify.tk</div>", unsafe_allow_html=True)
        st.write("")
        st.markdown("<div class='god-box'>🧠 GOD AI:<br>اسمعني، هذا الرابط وهمي، الدومين .tk خطير 100%، اصلا بنك الراجحي ما يستخدمه</div>", unsafe_allow_html=True)
        st.markdown("<div class='css-box' style='text-align:right; margin-top:10px;'>📋 نسخ التقرير</div>", unsafe_allow_html=True)
        st.markdown("<div class='css-box' style='text-align:right; margin-top:10px;'>🔗 افحص رابط جديد</div>", unsafe_allow_html=True)

with right:
    st.markdown("<div class='css-box' style='text-align:right;'>🔍 مثال للفحص</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='css-box' style='text-align:right;'>
    🏆 V16.3 BLACK<br>
    <span style='font-size:12px;'>
    • أسود مريح للعين<br>
    • ذكاء اصطناعي<br>
    • يكشف التصيد<br>
    • جاهز للمسابقة
    </span>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.markdown("<div class='css-box' style='text-align:right;'>📊 مهمتك اليوم</div>", unsafe_allow_html=True)
    st.markdown("<div class='css-box' style='text-align:right;'>رابط يحمي - خطر</div>", unsafe_allow_html=True)
    st.markdown("<div class='css-box' style='text-align:right;'>STC Pay - خطر</div>", unsafe_allow_html=True)
