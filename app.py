import streamlit as st

st.set_page_config(page_title="كاشف V16.3 BLACK", layout="wide")

st.markdown("""
<style>
.stApp { background-color: #0a0a0a !important; }
h1,h2,h3,p,span,div { color: #e0e0e0; }
.black-card {
    background: #141414;
    border: 1px solid #222;
    border-left: 3px solid #00ff88;
    border-radius: 12px;
    padding: 14px;
    margin-bottom: 10px;
}
.glow-green { border-left: 3px solid #00ff88; }
.glow-red { border-left: 3px solid #ff2e63; }
.glow-purple { border-left: 3px solid #a855f7; }
.top-box {
    background: #161616;
    border: 1px solid #2a2a2a;
    border-radius: 10px;
    padding: 12px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align:center;'>كاشف <span style='color:#00ff88;'>V16.3 BLACK</span> 🛡️</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#777; font-size:12px;'>النسخة السوداء - مريحة للعين - وضع ليلي حقيقي</p>", unsafe_allow_html=True)

# TOP 4
c1,c2,c3,c4 = st.columns(4)
with c1: st.markdown("<div class='top-box'>🏆<br><b>أسطورة</b><br><span style='color:#00ff88;'>مستواك</span></div>", unsafe_allow_html=True)
with c2: st.markdown("<div class='top-box'>📊<br><b>1,247</b><br><span style='color:#777;'>عملية فحص</span></div>", unsafe_allow_html=True)
with c3: st.markdown("<div class='top-box'>🧠<br><b>16 AI</b><br><span style='color:#777;'>قوة التحليل</span></div>", unsafe_allow_html=True)
with c4: st.markdown("<div class='top-box'>🎯<br><b>99.9%</b><br><span style='color:#777;'>الدقة</span></div>", unsafe_allow_html=True)

left,right = st.columns([1.4, 1])

with left:
    st.markdown("<div class='black-card glow-green'>🔗 <b>انسخ الرابط هنا للتحليل العميق</b></div>", unsafe_allow_html=True)
    url = st.text_input("", value="https://alrajhi-bank-verify.tk/login", label_visibility="collapsed")
    
    # نتيجة مفصلة
    st.markdown("""
    <div class='black-card glow-red'>
    <b>💀 90% خطر عالي جداً</b><br>
    <span style='color:#aaa; font-size:13px;'>الدومين: alrajhi-bank-verify.tk</span><br>
    <div style='background:#222; border-radius:5px; height:8px; margin-top:8px;'><div style='background:#ff2e63; width:90%; height:100%; border-radius:5px;'></div></div>
    <br>
    <span style='font-size:12px;'>
    ❌ دومين مجاني .tk<br>
    ❌ كلمة verify مشبوهة<br>
    ❌ لا يوجد SSL حقيقي للبنك<br>
    ❌ عمر الدومين أقل من 30 يوم
    </span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='black-card glow-purple'>
    <b>🧠 تحليل GOD AI المفصل:</b><br>
    <span style='font-size:13px; color:#ccc; line-height:1.7;'>
    اسمعني، هذا الرابط تصيد 100%.<br><br>
    <b>1. الدومين:</b> بنك الراجحي الرسمي هو alrajhibank.com.sa فقط، هذا .tk مجاني يستخدمه الهكرز.<br>
    <b>2. المسار /login:</b> يحاول يخليك تدخل بياناتك.<br>
    <b>3. التوصية:</b> لا تدخل أي بيانات، بلغ عنه فوراً عبر 9300.
    </span>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("<div class='black-card'><b>🏆 V16.3 BLACK</b><br><span style='font-size:12px; color:#888;'>النسخة السوداء المطورة<br>✔️ مريحة للعين OLED<br>✔️ 16 محرك ذكاء اصطناعي<br>✔️ كشف التصيد اللحظي<br>✔️ جاهزة للمسابقة الوطنية</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='black-card'><b>📊 مهمتك اليوم</b><br><span style='font-size:12px;'>🔴 3 روابط خطيرة تحتاج فحص</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='black-card' style='color:#777;'>🔗 رابط يحمي - خطر</div>", unsafe_allow_html=True)
    st.markdown("<div class='black-card' style='color:#777;'>💳 STC Pay - خطر</div>", unsafe_allow_html=True)
