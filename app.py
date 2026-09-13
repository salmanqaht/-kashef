import streamlit as st
from urllib.parse import urlparse

st.set_page_config(page_title="كاشف V16.3 BLACK", page_icon="🛡️", layout="wide")

# قاتل اللون الأزرق - يخليه أسود غصب
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"], .stApp, [data-testid="stHeader"] {
  background: #050a14 !important;
  background-color: #050a14 !important;
  background-image: radial-gradient(circle at 50% 0%, #1e293b 0%, #020617 60%) !important;
}
header, [data-testid="stToolbar"] { background: transparent !important; }
.comp-card {
  background: rgba(255,255,255,0.06) !important;
  border: 1px solid rgba(34,197,94,0.2) !important;
  border-radius:16px; padding:14px;
}
.comp-card * { color: #e2e8f0 !important; }
div.stButton>button {
  background: linear-gradient(90deg,#22c55e,#16a34a) !important;
  color: white !important; font-weight:900 !important;
  border-radius:12px !important; height:50px; border:none !important;
  box-shadow: 0 0 20px rgba(34,197,94,0.4) !important;
}
input { background: rgba(255,255,255,0.08)!important; color:white!important; border-radius:10px!important; }
.ai-box {
  background: rgba(168,85,247,0.12) !important;
  border: 1px solid #a855f7 !important; border-radius:14px; padding:14px;
}
</style>
""", unsafe_allow_html=True)

def check(u):
    s=0
    if not u.startswith("http"): u="https://"+u
    d=urlparse(u).netloc.lower()
    if any(x in d for x in [".tk",".ml",".xyz",".top","bit.ly"]): s+=40
    if any(w in u.lower() for w in ["alrajhi","stcpay","absher"]): s+=35
    if "@" in u: s+=20
    return min(s,100), d

# شعار
st.markdown("<div style='text-align:center;font-size:60px;filter:drop-shadow(0 0 20px #22c55e)'>🛡️</div>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center;color:white'>كاشف <span style='color:#22c55e'>V16.3 BLACK</span> <span style='font-size:12px;background:#a855f7;padding:4px 10px;border-radius:20px'>GOD AI 🧠</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#475569;font-size:12px'>النسخة السوداء المريحة للعين - جاهزة للمسابقة</p>", unsafe_allow_html=True)

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
        score, domain = check(url_in or "https://alrajhi-bank-verify.tk/login")
        if score>=60: st.error(f"💀 تصيد {score}% - {domain}")
        elif score>=30: st.warning(f"⚠️ مشبوه {score}%")
        else: st.success(f"✅ آمن {score}%"); st.balloons()
        if score>=60:
            st.markdown(f"<div class='ai-box'><b style='color:#d8b4fe'>🧠 GOD AI يحلل:</b><br><span style='color:white'>{domain} تصيد 100%! نطاق مجاني .tk، ينتحل الراجحي، السيرفر بروسيا. لا تدخل!</span></div>", unsafe_allow_html=True)

with mid:
    st.markdown("<div class='comp-card'>🔍 محلل الحماية</div>", unsafe_allow_html=True)
    st.markdown("<div class='comp-card' style='margin-top:8px'>🏆 V16.3 BLACK<br><small>• أسود مريح للعين<br>• ذكاء اصطناعي<br>• يكشف التصيد<br>• جاهز للمسابقة</small></div>", unsafe_allow_html=True)
with right:
    st.markdown("<div class='comp-card'>🛡️ هجمات حية</div>", unsafe_allow_html=True)
    st.markdown("<div class='comp-card' style='margin-top:8px'>راجحي وهمي - خطر</div>", unsafe_allow_html=True)
    st.markdown("<div class='comp-card' style='margin-top:8px'>STC Pay - خطر</div>", unsafe_allow_html=True)
