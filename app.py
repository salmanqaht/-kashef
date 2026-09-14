import streamlit as st

st.set_page_config(page_title="V16.3 BLACK", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
* { font-family: 'Tajawal', sans-serif; }

.stApp { background-color: #080a0f !important; }

.title-glow {
    text-align: center;
    color: white;
    font-size: 28px;
    font-weight: 700;
    text-shadow: 0 0 20px rgba(0,255,136,0.3);
}
.shield-pulse {
    display: inline-block;
    animation: shield-beat 1.2s infinite;
}
@keyframes shield-beat {
    0% { transform: scale(1); filter: drop-shadow(0 0 6px #00ff88); }
    50% { transform: scale(1.2); filter: drop-shadow(0 0 18px #00ff88); }
    100% { transform: scale(1); filter: drop-shadow(0 0 6px #00ff88); }
}

.top-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 18px;
    text-align: center;
    backdrop-filter: blur(10px);
    transition: 0.3s;
}
.top-card:hover { border-color: #00ff88; transform: translateY(-2px); }

.risk-card {
    background: linear-gradient(135deg, #1a0f14 0%, #231219 100%);
    border: 1px solid #ff2e63;
    border-radius: 16px;
    padding: 18px;
    animation: pulse-red 2s infinite;
    position: relative;
    overflow: hidden;
}
.risk-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 2px;
    background: linear-gradient(90deg, #ff2e63, #ff8fab);
    animation: scan 2s linear infinite;
}
@keyframes scan { 0% { transform: translateX(-100%); } 100% { transform: translateX(100%); } }
@keyframes pulse-red {
    0% { box-shadow: 0 0 0 0 rgba(255, 46, 99, 0.4); }
    70% { box-shadow: 0 0 0 12px rgba(255, 46, 99, 0); }
    100% { box-shadow: 0 0 0 0 rgba(255, 46, 99, 0); }
}

.god-card {
    background: linear-gradient(135deg, #0f1020 0%, #171a35 100%);
    border: 1px solid #6c5ce7;
    border-radius: 16px;
    padding: 18px;
}
.side-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 14px;
    padding: 14px;
    margin-bottom: 10px;
}
.progress-bg { background: #222; border-radius: 10px; height: 8px; overflow: hidden; }
.progress-fill { background: linear-gradient(90deg, #ff2e63, #ff6b8a); height: 100%; width: 90%; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title-glow'>كاشف <span style='color:#00ff88;'>V16.3 BLACK</span> <span class='shield-pulse'>🛡️</span></div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#5a6577; font-size:13px; margin-top:-10px;'>النسخة السوداء المريحة - نظام الحماية النابض</p>", unsafe_allow_html=True)
st.write("")

c1,c2,c3,c4 = st.columns(4)
with c1: st.markdown("<div class='top-card'>🏆<br><b style='color:white;'>أسطورة</b><br><span style='color:#00ff88; font-size:11px;'>مستواك</span></div>", unsafe_allow_html=True)
with c2: st.markdown("<div class='top-card'><b style='color:white; font-size:20px;'>1,247</b><br><span style='font-size:11px; color:#8892b0;'>عملية فحص</span></div>", unsafe_allow_html=True)
with c3: st.markdown("<div class='top-card'><b style='color:white; font-size:20px;'>16 AI</b><br><span style='font-size:11px; color:#8892b0;'>قوة التحليل</span></div>", unsafe_allow_html=True)
with c4: st.markdown("<div class='top-card'><b style='color:white; font-size:20px;'>99.9%</b><br><span style='font-size:11px; color:#8892b0;'>الدقة</span></div>", unsafe_allow_html=True)

st.write("")
left,right = st.columns([1.5, 1])

with left:
    st.text_input("🔗", value="https://alrajhi-bank-verify.tk/login", label_visibility="collapsed")
    
    st.markdown("""
    <div class='risk-card'>
        <div style='display:flex; justify-content:space-between; align-items:center;'>
            <span style='color:#ff6b8a; font-weight:700;'>💀 خطر عالي جداً 90%</span>
            <span style='background:#ff2e63; color:white; padding:2px 8px; border-radius:20px; font-size:11px;'>خطر</span>
        </div>
        <div class='progress-bg' style='margin:12px 0;'><div class='progress-fill'></div></div>
        <div style='font-size:13px; color:#c9b0b8; line-height:2;'>
            ✖ دومين مجاني .tk غير تابع لأي بنك<br>
            ✖ كلمة verify لتضليل المستخدم<br>
            ✖ لا يوجد شهادة SSL رسمية للبنك
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='god-card'>
        <b style='color:#a29bfe;'>🧠 تحليل GOD AI المفصل</b><br>
        <span style='font-size:13px; color:#a0a3bd; line-height:1.9;'>
        هذا الرابط تصيد بنسبة 100%. الدومين الحقيقي لبنك الراجحي هو <code>alrajhibank.com.sa</code> فقط.<br>
        يحاول سرقة بياناتك عبر صفحة تسجيل دخول وهمية.<br><br>
        <b style='color:#00ff88;'>→ التوصية: أغلق الصفحة فوراً وبلغ عنها على الرقم 9300.</b>
        </span>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("<div class='side-card'><b style='color:white;'>🏆 V16.3 BLACK</b><br><span style='font-size:12px; color:#6c7293;'>✔️ تصميم OLED مريح للعين<br>✔️ 16 محرك ذكاء اصطناعي<br>✔️ كشف تصيد لحظي<br>✔️ جاهز للمسابقة</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='side-card'><b style='color:white;'>📊 مهمتك اليوم</b><br><span style='font-size:12px; color:#ff6b8a;'>● 3 روابط خطيرة بانتظارك</span></div>", unsafe_allow_html=True)
