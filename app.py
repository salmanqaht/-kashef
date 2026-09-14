import streamlit as st

st.set_page_config(page_title="V16.3 BLACK", layout="wide")

st.markdown("""
<style>
/* اخفاء شريط ستريم لايت الأزرق */
header[data-testid="stHeader"] { background: #080a0f !important; }
.stApp { background-color: #080a0f !important; }
[data-testid="stAppViewContainer"] { background-color: #080a0f !important; }

.title-glow {
    text-align: center; color: white; font-size: 30px; font-weight: 800;
}
.shield-pulse {
    display: inline-block;
    animation: shield-beat 1.1s infinite;
}
@keyframes shield-beat {
    0% { transform: scale(1); filter: drop-shadow(0 0 8px #00ff88); }
    50% { transform: scale(1.3); filter: drop-shadow(0 0 22px #00ff88); }
    100% { transform: scale(1); filter: drop-shadow(0 0 8px #00ff88); }
}
.top-card {
    background: #12131a; border: 1px solid #1e2130;
    border-radius: 16px; padding: 18px; text-align: center; color: #8b92a8;
}
.risk-card {
    background: #1c1216; border: 1.5px solid #ff2e63;
    border-radius: 16px; padding: 18px;
    animation: pulse-red 1.8s infinite;
}
@keyframes pulse-red {
    0% { box-shadow: 0 0 0 0 rgba(255, 46, 99, 0.5); }
    70% { box-shadow: 0 0 0 14px rgba(255, 46, 99, 0); }
    100% { box-shadow: 0 0 0 0 rgba(255, 46, 99, 0); }
}
.god-card {
    background: #11152a; border: 1.5px solid #4a4bff;
    border-radius: 16px; padding: 18px; margin-top: 12px;
}
.side-card { background: #12131a; border: 1px solid #1e2130; border-radius: 14px; padding: 14px; margin-bottom: 10px; color: #8b92a8; }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title-glow'>كاشف <span style='color:#00ff88;'>V16.3 BLACK</span> <span class='shield-pulse'>🛡️</span></div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#4a5268; font-size:12px;'>النسخة السوداء المريحة - نظام الحماية النابض</p>", unsafe_allow_html=True)
st.write("")

c1,c2,c3,c4 = st.columns(4)
with c1: st.markdown("<div class='top-card'>🏆<br><b style='color:white;'>أسطورة</b><br><span style='color:#00ff88; font-size:11px;'>مستواك</span></div>", unsafe_allow_html=True)
with c2: st.markdown("<div class='top-card'><b style='color:white; font-size:22px;'>1,247</b><br>عملية فحص</div>", unsafe_allow_html=True)
with c3: st.markdown("<div class='top-card'><b style='color:white; font-size:22px;'>16 AI</b><br>قوة التحليل</div>", unsafe_allow_html=True)
with c4: st.markdown("<div class='top-card'><b style='color:white; font-size:22px;'>99.9%</b><br>الدقة</div>", unsafe_allow_html=True)

st.write("")
left,right = st.columns([1.5, 1])

with left:
    st.text_input("", value="https://alrajhi-bank-verify.tk/login", label_visibility="collapsed")
    st.markdown("""
    <div class='risk-card'>
        <b style='color:#ff5a84;'>💀 خطر عالي جداً 90%</b>
        <div style='background:#2a1a20; height:6px; border-radius:10px; margin:12px 0;'><div style='background:#ff2e63; width:90%; height:100%; border-radius:10px;'></div></div>
        <span style='font-size:13px; color:#bda3ac;'>
        ✖ دومين مجاني .tk<br>
        ✖ كلمة verify مشبوهة<br>
        ✖ شهادة SSL مزورة
        </span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class='god-card'>
        <b style='color:#8b8cff;'>🤖 التحليل GOD AI مفصل</b><br>
        <span style='font-size:13px; color:#9aa0bb; line-height:1.8;'>
        الدومين الحقيقي هو alrajhibank.com.sa فقط. هذا الرابط تصيد 100%.<br>
        <b style='color:#00ff88;'>→ التوصية: أغلق الصفحة وبلغ على 9300.</b>
        </span>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("<div class='side-card'><b style='color:white;'>🏆 V16.3 BLACK</b><br>✔️ أسود OLED مريح<br>✔️ 16 محرك AI<br>✔️ كشف لحظي</div>", unsafe_allow_html=True)
    st.markdown("<div class='side-card'><b style='color:white;'>📊 مهمتك اليوم</b><br><span style='color:#ff5a84;'>● 3 روابط خطيرة</span></div>", unsafe_allow_html=True)
