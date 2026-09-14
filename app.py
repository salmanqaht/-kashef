import streamlit as st

st.set_page_config(page_title="V16.3 BLACK", layout="wide")

st.markdown("""
<style>
.stApp { background-color: #1a1d26 !important; }
header[data-testid="stHeader"] { background-color: #1a1d26 !important; }

.shield-pulse {
    display: inline-block;
    font-size: 36px;
    animation: beat 1.3s infinite;
    filter: drop-shadow(0 0 12px #00ff88);
}
@keyframes beat {
    0%,100% { transform: scale(1); }
    50% { transform: scale(1.2); }
}

.top-box {
    background: #252a38;
    border: 1px solid #2e3448;
    border-radius: 12px;
    padding: 16px;
    text-align: center;
    color: #a0a8c0;
    transition: 0.3s;
}
.top-box:hover { border-color: #00ff88; }
.progress-line { height: 2px; background: #2e3448; margin-top: 12px; border-radius: 10px; }
.progress-fill { height: 100%; width: 92%; background: #00ff88; box-shadow: 0 0 6px #00ff88; }

.card { background: #252a38; border: 1px solid #2e3448; border-radius: 10px; padding: 12px; color: #d0d6e8; margin-bottom: 9px; font-size: 13px; }

.risk-box {
    background: linear-gradient(90deg, #3a1e28, #4a2030);
    border: 1px solid #ff3b6e;
    border-radius: 10px; padding: 12px; color: white;
    animation: pulse 1.6s infinite;
    display: flex; justify-content: space-between; align-items: center;
}
@keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(255,59,110,0.5); } 70% { box-shadow: 0 0 0 10px rgba(255,59,110,0); } 100% { box-shadow: 0 0 0 0 rgba(255,59,110,0); } }

.god-box {
    background: linear-gradient(90deg, #1e2250, #2a2a7a);
    border: 1px solid #5a5cff;
    border-radius: 10px; padding: 12px; color: #d0d2ff;
}
.dot { width: 8px; height: 8px; background: #00ff88; border-radius: 50%; display: inline-block; animation: blink 1s infinite; margin-left: 6px; }
@keyframes blink { 0%,100% { opacity: 1; } 50% { opacity: 0.3; } }
</style>
""", unsafe_allow_html=True)

# العنوان بدون جملة أسود خفيف
st.markdown("<div style='text-align:center;'><span class='shield-pulse'>🛡️</span><br><h2 style='color:white; margin:5px;'>كاشف <span style='color:#00ff88;'>V16.3 BLACK</span></h2></div>", unsafe_allow_html=True)
st.write("")

c1,c2,c3,c4 = st.columns(4)
with c1: st.markdown("<div class='top-box'>مستواي<br>🏆 <b style='color:white;'>أسطورة</b><div class='progress-line'><div class='progress-fill'></div></div></div>", unsafe_allow_html=True)
with c2: st.markdown("<div class='top-box'>فحصك<br><b style='color:white; font-size:20px;'>0</b></div>", unsafe_allow_html=True)
with c3: st.markdown("<div class='top-box'>قوة التحليل<br><b style='color:white; font-size:20px;'>16 AI</b></div>", unsafe_allow_html=True)
with c4: st.markdown("<div class='top-box'>الدقة<br><b style='color:white; font-size:20px;'>99.9%</b></div>", unsafe_allow_html=True)

st.write("")
left,right = st.columns([1.6, 1])

with left:
    st.markdown("<div class='card'><span class='dot'></span>🔗 انسخ الرابط هنا <span style='color:#00ff88; float:left; font-size:10px;'>● مباشر</span></div>", unsafe_allow_html=True)
    st.text_input("", value="https://alrajhi-bank-verify.tk/login", label_visibility="collapsed")
    st.markdown("<div class='risk-box'><span>💀 90% خطر عالي - alrajhi-bank-verify.tk</span><span style='background:#ff3b6e; padding:2px 8px; border-radius:12px; font-size:10px;'>خطر</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='god-box' style='margin-top:8px;'><b>🧠 GOD AI <span style='color:#00ff88;'>● LIVE</span></b><br><span style='font-size:13px;'>تصيد 100% - alrajhi-bank-verify.tk ينتحل الراجحي - تم كشفه قبل 1.2 ثانية</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>📄 تحليل مبسط</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>🔗 اتصال بمصادر</div>", unsafe_allow_html=True)

with right:
    st.markdown("<div class='card'>🔍 ماذا تفحص؟</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>🏆 V16.3 BLACK<br><span style='font-size:11px; color:#7a85a0;'>◍ حماية لحظية<br>◍ ذكاء اصطناعي<br>◍ كشف تصيد متقدم</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>📋 مهمتك اليوم <span style='float:left; background:#252a38; border:1px solid #ff3b6e; color:#ff3b6e; padding:1px 6px; border-radius:10px; font-size:10px;'>3 جديد</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>🔴 رابط يحمي - خطر</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>🟠 STC Pay - مشبوه</div>", unsafe_allow_html=True)
