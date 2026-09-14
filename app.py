import streamlit as st

st.set_page_config(page_title="V16.3 BLACK", layout="wide")

st.markdown("""
<style>
.stApp { background-color: #0d1e48 !important; background-image: radial-gradient(circle at center, #1a2f6b 0%, #0d1e48 100%) !important; }
header[data-testid="stHeader"] { background: #0d1e48 !important; }

.shield-pulse {
    display: inline-block;
    font-size: 35px;
    animation: shield-beat 1.2s infinite;
    filter: drop-shadow(0 0 10px #ff8c00);
}
@keyframes shield-beat {
    0% { transform: scale(1); }
    50% { transform: scale(1.25); }
    100% { transform: scale(1); }
}

.top-box {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 12px;
    padding: 15px;
    text-align: center;
    color: white;
    position: relative;
}
.progress-green {
    position: absolute;
    bottom: 8px; left: 10px; right: 10px;
    height: 3px; background: #222;
    border-radius: 10px;
}
.progress-green-fill { background: #00ff88; width: 95%; height: 100%; border-radius: 10px; box-shadow: 0 0 10px #00ff88; }

.url-box { background: rgba(255,255,255,0.1); border-radius: 10px; padding: 10px; border: 1px solid rgba(255,255,255,0.2); color: white; }
.risk-box {
    background: linear-gradient(90deg, #c62a5a, #e84a7a);
    border-radius: 10px; padding: 12px; color: white; margin-top: 10px;
    animation: pulse-red 1.5s infinite;
    border: 1px solid #ff6b8a;
}
@keyframes pulse-red {
    0% { box-shadow: 0 0 0 0 rgba(255, 80, 120, 0.7); }
    70% { box-shadow: 0 0 0 12px rgba(255, 80, 120, 0); }
    100% { box-shadow: 0 0 0 0 rgba(255, 80, 120, 0); }
}
.god-box { background: linear-gradient(90deg, #1a1a8a, #3a1a9a); border-radius: 10px; padding: 12px; color: white; border: 1px solid #6a5aff; margin-top: 10px; }
.side-box { background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); border-radius: 10px; padding: 12px; color: white; margin-bottom: 8px; font-size: 13px; }
.btn-green { background: #00ff88; color: black; border-radius: 8px; padding: 6px 12px; font-weight: bold; display: inline-block; }
</style>
""", unsafe_allow_html=True)

st.markdown("<div style='text-align:center;'><span class='shield-pulse'>🛡️</span><br><h2 style='color:white;'>كاشف <span style='color:#7fff7f;'>V16.3 BLACK</span></h2><p style='color:#7a8ab0; font-size:11px;'>النسخة الزرقاء - مقر الحماية النشط</p></div>", unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)
with c1: st.markdown("<div class='top-box'>مستواي<br>🏆 <b>أسطورة</b><div class='progress-green'><div class='progress-green-fill'></div></div></div>", unsafe_allow_html=True)
with c2: st.markdown("<div class='top-box'>فحصك<br><b>0</b></div>", unsafe_allow_html=True)
with c3: st.markdown("<div class='top-box'>قوة التحليل<br><b>16 AI</b></div>", unsafe_allow_html=True)
with c4: st.markdown("<div class='top-box'>الدقة<br><b>99.9%</b></div>", unsafe_allow_html=True)

st.write("")
left,right = st.columns([1.6, 1])

with left:
    st.markdown("<div class='side-box'>🔗 انسخ الرابط هنا</div>", unsafe_allow_html=True)
    st.markdown("<div class='url-box'>https://alrajhi-bank-verify.tk/login</div>", unsafe_allow_html=True)
    st.markdown("<div style='margin-top:8px;'><span class='btn-green'>✅ فحص</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='risk-box'>💀 90% خطر عالي - alrajhi-bank-verify.tk</div>", unsafe_allow_html=True)
    st.markdown("<div class='god-box'>💬 GOD AI:<br>اسمعني، هذا الرابط تصيد 100% alrajhi-bank-verify.tk خطر!</div>", unsafe_allow_html=True)
    st.markdown("<div class='side-box'>📄 تحليل مبسط</div>", unsafe_allow_html=True)
    st.markdown("<div class='side-box'>🔗 اتصال بمصادر</div>", unsafe_allow_html=True)

with right:
    st.markdown("<div class='side-box'>🔍 ماذا تفحص؟</div>", unsafe_allow_html=True)
    st.markdown("<div class='side-box'>🏆 V16.3 BLACK<br>• أسود منيع للعين<br>• ذكاء اصطناعي<br>• وكشف للتصيد<br>• جاهز للمسابقة</div>", unsafe_allow_html=True)
    st.markdown("<div class='side-box'>📋 مهمتك اليوم</div>", unsafe_allow_html=True)
    st.markdown("<div class='side-box'>رابط يحمي - خطر</div>", unsafe_allow_html=True)
    st.markdown("<div class='side-box'>STC Pay - خطر</div>", unsafe_allow_html=True)
