import streamlit as st

st.set_page_config(page_title="V16.3 BLACK", layout="wide")

st.markdown("""
<style>
.stApp { background-color: #0e0e0e !important; }
.top-box { background: #1a1a1a; border: 1px solid #2d2d2d; border-radius: 12px; padding: 15px; text-align: center; color: #ccc; }
.card { background: #1a1a1a; border: 1px solid #2d2d2d; border-radius: 12px; padding: 15px; margin-bottom: 12px; color: #ddd; }

.pulse-box {
    background: linear-gradient(90deg, #1a0a0a, #2a1515);
    border: 1px solid #ff2e63;
    border-radius: 12px;
    padding: 15px;
    margin-bottom: 12px;
    animation: pulse-red 1.5s infinite;
}
@keyframes pulse-red {
    0% { box-shadow: 0 0 0 0 rgba(255, 46, 99, 0.7); }
    70% { box-shadow: 0 0 0 15px rgba(255, 46, 99, 0); }
    100% { box-shadow: 0 0 0 0 rgba(255, 46, 99, 0); }
}

/* --- نبض الدرع --- */
.shield-pulse {
    display: inline-block;
    animation: shield-beat 1.2s infinite;
    filter: drop-shadow(0 0 8px #00ff88);
}
@keyframes shield-beat {
    0% { transform: scale(1); filter: drop-shadow(0 0 5px #00ff88); }
    50% { transform: scale(1.25); filter: drop-shadow(0 0 15px #00ff88); }
    100% { transform: scale(1); filter: drop-shadow(0 0 5px #00ff88); }
}
</style>
""", unsafe_allow_html=True)

# العنوان مع الدرع النابض
st.markdown("""
<h3 style='text-align:center; color:white;'>
كاشف <span style='color:#00ff88;'>V16.3 BLACK</span> 
<span class='shield-pulse'>🛡️</span>
</h3>
<p style='text-align:center; color:#666; font-size:12px;'>النسخة السوداء المريحة - وضع الحماية النشط</p>
""", unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)
with c1: st.markdown("<div class='top-box'>🏆<br><b>أسطورة</b><br><span style='color:#00ff88; font-size:11px;'>مستواك</span></div>", unsafe_allow_html=True)
with c2: st.markdown("<div class='top-box'><b>1,247</b><br><span style='font-size:11px;'>عملية فحص</span></div>", unsafe_allow_html=True)
with c3: st.markdown("<div class='top-box'><b>16 AI</b><br><span style='font-size:11px;'>قوة التحليل</span></div>", unsafe_allow_html=True)
with c4: st.markdown("<div class='top-box'><b>99.9%</b><br><span style='font-size:11px;'>الدقة</span></div>", unsafe_allow_html=True)

left,right = st.columns([1.4, 1])

with left:
    st.markdown("<div class='card' style='border-left:3px solid #00ff88;'>🔗 انسخ الرابط هنا للتحليل</div>", unsafe_allow_html=True)
    st.text_input("", value="https://alrajhi-bank-verify.tk/login", label_visibility="collapsed")

    st.markdown("""
    <div class='pulse-box'>
    <b style='color:#ff5c85;'>💀 خطر عالي جداً 90%</b>
    <div style='background:#333; border-radius:10px; height:6px; margin:10px 0;'><div style='background:#ff2e63; width:90%; height:100%; border-radius:10px;'></div></div>
    <span style='font-size:12px; color:#aaa;'>❌ دومين .tk مجاني<br>❌ verify مشبوه<br>❌ عمر الدومين قصير</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='card' style='border-left:3px solid #a855f7;'><b>🧠 GOD AI:</b><br><span style='font-size:12px; color:#bbb;'>تصيد 100% - لا تدخل بياناتك وبلغ 9300</span></div>", unsafe_allow_html=True)

with right:
    st.markdown("<div class='card'>🏆 <b>V16.3 BLACK</b><br><span style='font-size:11px; color:#888;'>✔️ أسود OLED<br>✔️ 16 محرك AI<br>✔️ جاهز للمسابقة</span></div>", unsafe_allow_html=True)
