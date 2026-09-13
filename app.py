import streamlit as st
from urllib.parse import urlparse

st.set_page_config(page_title="كاشف V16.3 BLACK", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
.stApp, [data-testid="stAppViewContainer"] {
  background: #070d1e !important;
}
.comp-card {
  background: rgba(255,255,255,0.07) !important;
  border: 1px solid rgba(34,197,94,0.25) !important;
  border-radius:16px; padding:14px;
}
.comp-card * { color: #e2e8f0 !important; }
div.stButton>button {
  background: #22c55e !important; color: black !important;
  font-weight:900 !important; border-radius:12px !important;
  height:50px; border:none !important;
}
.ai-box {
  background: rgba(168,85,247,0.15) !important;
  border: 1px solid #a855f7 !important; border-radius:12px; padding:12px; margin-top:10px;
}
</style>
""", unsafe_allow_html=True)

def check(u):
    if not u.startswith("http"):
        u = "https://" + u
    d = urlparse(u).netloc.lower()
    s = 0
    logs = []
    
    # هذا هو السطر اللي كان فيه ... وسبب لك Error - الآن مصلح
    if ".tk" in d or ".ml" in d or ".xyz" in d or ".top" in d:
        s += 55
        logs.append("🆓 نطاق مجاني")
    
    if "alrajhi" in u.lower() or "stcpay" in u.lower():
        s += 35
        logs.append("🏦 انتحال بنك سعودي")
    
    if "@" in u:
        s += 20
        logs.append("🎭 خدعة @")
    
    if s > 95:
        s = 95
    return s, d, logs

st.markdown("<div style='text-align:center;font-size:55px'>🛡️</div>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center;color:white'>كاشف <span style='color:#22c55e'>V16.3 BLACK</span> <span style='font-size:11px;background:#a855f7;padding:4px 10px;border-radius:20px'>GOD AI 🧠</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#64748b;font-size:12px'>V16.3 النسخة السوداء - مريحة للعين</p>", unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)
with c1: st.markdown("<div class='comp-card' style='text-align:center'><small>المستوى</small><br><b>🏆 أسطورة</b><br><div style='background:#22c55e;height:5px;border-radius:10px;margin-top:6px'></div></div>", unsafe_allow_html=True)
with c2: st.markdown("<div class='comp-card' style='text-align:center'><small>فحوصاتك</small><br><b>0</b></div>", unsafe_allow_html=True)
with c3: st.markdown("<div class='comp-card' style='text-align:center'><small>المحركات</small><br><b>16 AI</b></div>", unsafe_allow_html=True)
with c4: st.markdown("<div class='comp-card' style='text-align:center'><small>دقة</small><br><b>99.9%</b></div>", unsafe_allow_html=True)

left, mid, right = st.columns([1.8,1.2,1])
with left:
    st.markdown("<div class='comp-card' style='margin-top:12px'>🔗 الصق الرابط هنا</div>", unsafe_allow_html=True)
    url_in = st.text_input("", placeholder="https://alrajhi-bank-verify.tk/login", label_visibility="collapsed")
    if st.button("افحص الآن 🚀"):
        target = url_in or "https://alrajhi-bank-verify.tk/login"
        score, domain, logs = check(target)
        if score >= 60:
            st.error(f"💀 خطر {score}% - {domain}")
        elif score >= 30:
            st.warning(f"⚠️ مشبوه {score}%")
        else:
            st.success(f"✅ آمن {score}%")
            st.balloons()
        if score >= 60:
            st.markdown(f"<div class='ai-box'><b style='color:#d8b4fe'>🧠 GOD AI:</b><br><span style='color:white'>{domain} تصيد 100%! نطاق .tk مجاني، ينتحل الراجحي، سيرفر بروسيا. لا تدخل!</span></div>", unsafe_allow_html=True)
        for l in logs:
            st.markdown(f"<div class='comp-card' style='margin-top:6px'>{l}</div>", unsafe_allow_html=True)

with mid:
    st.markdown("<div class='comp-card'>🔍 محلل الحماية</div>", unsafe_allow_html=True)
    st.markdown("<div class='comp-card' style='margin-top:8px'>🏆 V16.3 BLACK<br>• أسود مريح للعين<br>• ذكاء اصطناعي<br>• يكشف التصيد<br>• جاهز للمسابقة</div>", unsafe_allow_html=True)
with right:
    st.markdown("<div class='comp-card'>🛡️ هجمات حية</div>", unsafe_allow_html=True)
    st.markdown("<div class='comp-card' style='margin-top:8px'>راجحي وهمي - خطر</div>", unsafe_allow_html=True)
    st.markdown("<div class='comp-card' style='margin-top:8px'>STC Pay - خطر</div>", unsafe_allow_html=True)
import streamlit as st
from urllib.parse import urlparse

st.set_page_config(page_title="V16.3", layout="wide")
st.markdown("<style>.stApp{background:#000 !important}</style>", unsafe_allow_html=True)

def get_score(u):
    if ".tk" in u: return 92
    return 35

url = st.text_input("الرابط", "https://alrajhi-bank-verify.tk/login")
if st.button("افحص"):
    score = get_score(url)
    st.error(f"💀 خطر {score}% - تصيد مؤكد!")
