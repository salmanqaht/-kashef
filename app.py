import streamlit as st

st.set_page_config(page_title="V16.3 BLACK", layout="wide")

st.markdown("""
<style>
/* --- أسود خفيف مريح --- */
.stApp { background-color: #121212 !important; background-image: none !important; }
header[data-testid="stHeader"] { background: #121212 !important; }
[data-testid="stAppViewContainer"] { background: #121212 !important; }

.shield-pulse {
    display: inline-block;
    font-size: 34px;
    animation: shield-beat 1.2s infinite;
    filter: drop-shadow(0 0 10px #00ff88);
}
@keyframes shield-beat {
    0% { transform: scale(1); }
    50% { transform: scale(1.25); }
    100% { transform: scale(1); }
}

.top-box {
    background: #1c1c1e;
    border: 1px solid #2c2c2e;
    border-radius: 12px;
    padding: 15px;
    text-align: center;
    color: #e5e5e7;
}
.progress-green { height: 3px; background: #2c2c2e; border-radius: 10px; margin-top: 10px; }
.progress-green-fill { background: #00ff88; width: 95%; height: 100%; border-radius: 10px; }

.url-box { background: #1c1c1e; border-radius: 10px; padding: 10px; border: 1px solid #2c2c2e; color: #aeaeb2; }
.risk-box {
    background: linear-gradient(90deg, #2a1218, #3a1a22);
    border: 1px solid #ff2e63;
    border-radius: 10px; padding: 12px; color: #ff8fa3;
    animation: pulse-red 1.5s infinite;
}
@keyframes pulse-red {
    0% { box-shadow: 0 0 0 0 rgba(255, 46, 99, 0.5); }
    70% { box-shadow: 0 0 0 12px rgba(255, 46, 99, 0); }
    100% { box-shadow: 0 0 0 0 rgba(255, 46, 99, 0); }
}
.god-box { background: #1a1a2e; border: 1px solid #3a3a6a; border-radius: 10px; padding: 12px; color: #c7c7ff; }
.side-box { background: #1c1c1e; border: 1px solid #2c2c2e; border-radius: 10px; padding: 12px; color: #e5e5e7; margin-bottom: 8px; font-size: 13px; }
.btn-green { background: #00ff88; color: black; border-radius: 8px; padding: 6px 12px; font-weight: bold; display: inline-block; font-size: 12px; }
</style>
""", unsafe_allow_html=True)

st.markdown("<div style='text-align:center;'><span class='shield-pulse'>🛡️</span><br><h2 style='color:white; margin-top:5px;'>كاشف <span style='color:#00ff88;'>V16.3 BLACK</span></h2><p style='color:#6e6e73; font-size:11px;'>النسخة السوداء الخفيفة - حماية نابضة</p></div>", unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)
with c1: st.markdown("<div class='top-box'>مستواي<br>🏆 <b style='color:white;'>أسطورة</b><div class='progress-green'><div class='progress-green-fill'></div></div></div>", unsafe_allow_html=True)
with c2: st.markdown("<div class='top-box'>فحصك<br><b style='color:white;'>0</b></div>", unsafe_allow_html=True)
with c3: st.markdown("<div class='top-box'>قوة التحليل<br><b style='color:white;'>16 AI</b></div>", unsafe_allow_html=True)
with c4: st.markdown("<div class='top-box'>الدقة<br><b style='color:white;'>99.9%</b></div>", unsafe_allow_html=True)

st.write("")
left,right = st.columns([1.6, 1])

with left:
    st.markdown("<div class='side-box'>🔗 انسخ الرابط هنا</div>", unsafe_allow_html=True)
    st.markdown("<div class='url-box'>https://alrajhi-bank-verify.tk/login</div>", unsafe_allow_html=True)
    st.markdown("<div style='margin-top:8px;'><span class='btn-green'>✅ فحص</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='risk-box'>💀 90% خطر عالي - alrajhi-bank-verify.tk</div>", unsafe_allow_html=True)
    st.markdown("<div class='god-box'>💬 GOD AI:<br>هذا الرابط تصيد 100% alrajhi-bank-verify.tk خطر!</div>", unsafe_allow_html=True)
    st.markdown("<div class='side-box'>📄 تحليل مبسط</div>", unsafe_allow_html=True)
    st.markdown("<div class='side-box'>🔗 اتصال بمصادر</div>", unsafe_allow_html=True)

with right:
    st.markdown("<div class='side-box'>🔍 ماذا تفحص؟</div>", unsafe_allow_html=True)
    st.markdown("<div class='side-box'>🏆 V16.3 BLACK<br>• أسود خفيف مريح<br>• ذكاء اصطناعي<br>• كشف تصيد<br>• جاهز للمسابقة</div>", unsafe_allow_html=True)
    st.markdown("<div class='side-box'>📋 مهمتك اليوم</div>", unsafe_allow_html=True)
    st.markdown("<div class='side-box'>رابط يحمي - خطر</div>", unsafe_allow_html=True)
    st.markdown("<div class='side-box'>STC Pay - خطر</div>", unsafe_allow_html=True)
