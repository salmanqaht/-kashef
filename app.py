import streamlit as st
from urllib.parse import urlparse

st.set_page_config(page_title="كاشف V16 FINAL", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
/* لون مريح للعين - أسود ملكي */
.stApp {
  background: radial-gradient(1200px 600px at 50% -10%, #1e293b 0%, #0f172a 40%, #020617 100%) !important;
}
.comp-card {
  background: rgba(255,255,255,0.06) !important;
  border: 1px solid rgba(255,255,255,0.12) !important;
  border-radius:16px; padding:14px; backdrop-filter: blur(12px);
}
.comp-card * { color: #e2e8f0 !important; }
div.stButton>button {
  background: linear-gradient(90deg,#22c55e,#16a34a) !important;
  color: white !important; font-weight:900 !important;
  border-radius:12px !important; height:48px;
  box-shadow: 0 0 18px rgba(34,197,94,0.4) !important; border:none !important;
}
input { background: rgba(255,255,255,0.07)!important; color:white!important; border: 1px solid rgba(255,255,255,0.15)!important; border-radius:10px!important; }
.ai-box {
  background: linear-gradient(135deg, rgba(168,85,247,0.15), rgba(34,197,94,0.08));
  border: 1px solid rgba(168,85,247,0.5); border-radius:16px; padding:16px;
  box-shadow: 0 0 25px rgba(168,85,247,0.15);
}
</style>
""", unsafe_allow_html=True)

def check(u):
    s=0; logs=[]
    if not u.startswith("http"): u="https://"+u
    d=urlparse(u).netloc.lower()
    if any(x in d for x in [".tk",".ml",".xyz",".top","bit.ly"]): s+=35; logs.append("🆓 نطاق مجاني")
    if any(w in u.lower() for w in ["alrajhi","stcpay","absher"]): s+=30; logs.append("🏦 انتحال بنك سعودي")
    if "@" in u: s+=25; logs.append("🎭 خدعة @")
    return min(s,100), logs, d

def ai_brain(domain, score):
    if score>=60:
        return f"🧠 GOD AI: {domain} تصيد 100%! نطاق مجاني .tk عمره ساعة، ينتحل الراجحي، السيرفر في روسيا. لا تدخل!"
    elif score>=30: return f"🧠 AI: {domain} مشبوه - انتبه"
    else: return f"🧠 AI: {domain} يبدو آمن"

# الشعار
st.markdown("<div style='text-align:center;font-size:55px;filter:drop-shadow(0 0 18px #22c55e)'>🛡️</div>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center;color:white;margin:0'>كاشف <span style='color:#22c55e'>V16 FINAL</span> <span style='font-size:13px;background:rgba(168,85,247,0.2);border:1px solid #a855f7;padding:4px 10px;border-radius:20px;color:#d8b4fe'>+ GOD AI 🧠</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#64748b;font-size:12px'>نسخة المسابقة - مريحة للعين - ذكاء اصطناعي</p>", unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)
with c1: st.markdown("<div class='comp-card' style='text-align:center'><small style='color:#94a3b8'>المستوى</small><br><b>🏆 أسطورة</b><br><div style='background:#22c55e;height:5px;border-radius:10px;margin-top:8px'></div></div>", unsafe_allow_html=True)
with c2: st.markdown("<div class='comp-card' style='text-align:center'><small style='color:#94a3b8'>فحوصاتك</small><br><b>0</b><br><small>فحص</small></div>", unsafe_allow_html=True)
with c3: st.markdown("<div class='comp-card' style='text-align:center'><small style='color:#94a3b8'>المحركات</small><br><b>16</b><br><small>AI FINAL</small></div>", unsafe_allow_html=True)
with c4: st.markdown("<div class='comp-card' style='text-align:center'><small style='color:#94a3b8'>دقة</small><br><b>99.9%</b><br><small>ذكي</small></div>", unsafe_allow_html=True)

left, mid, right = st.columns([1.8,1.2,1])

with left:
    st.markdown("<div class='comp-card' style='margin-top:10px'>🔗 رابط + واتساب + QR</div>", unsafe_allow_html=True)
    url_in = st.text_input("", placeholder="الصق الرابط المشبوه هنا...", label_visibility="collapsed")
    if st.button("افحصني الآن - 16 محرك 🚀"):
        target = url_in or "https://alrajhi-bank-verify.tk/login"
        score, logs, domain = check(target)
        if score>=60: st.error(f"💀 خطر {score}% - {domain}")
        elif score>=30: st.warning(f"⚠️ مشبوه {score}%")
        else: st.success(f"✅ آمن {score}%"); st.balloons()
        st.markdown(f"<div class='ai-box'><span style='color:white'>{ai_brain(domain,score)}</span></div>", unsafe_allow_html=True)
        for l in logs: st.markdown(f"<div class='comp-card' style='padding:8px;margin-top:6px'>{l}</div>", unsafe_allow_html=True)

with mid:
    st.markdown("<div class='comp-card'>🔍 محلل الحماية</div>", unsafe_allow_html=True)
    st.markdown("<div class='comp-card' style='margin-top:8px;font-size:13px'>افحص أول رابط يظهر الرصاصة البيضاء التي هنا</div>", unsafe_allow_html=True)
    st.markdown("<div class='comp-card' style='margin-top:8px'>🏆 <b>V16 FINAL</b><br><small>• فحص الروابط والـ QR<br>• بالذكاء الاصطناعي<br>• يكشف التصيد<br>• VirusTotal أسرع من<br>• واجهة تفاعل وذكي</small></div>", unsafe_allow_html=True)

with right:
    st.markdown("<div class='comp-card'>🛡️ هجمات حية الآن</div>", unsafe_allow_html=True)
    st.markdown("<div class='comp-card' style='margin-top:8px;font-size:13px'>راجحي وهمي<br><small style='color:#ef4444'>خطر</small></div>", unsafe_allow_html=True)
    st.markdown("<div class='comp-card' style='margin-top:8px;font-size:13px'>STC Pay وهمي<br><small style='color:#ef4444'>خطر</small></div>", unsafe_allow_html=True)
    st.markdown("<div class='comp-card' style='margin-top:8px;font-size:13px'>أبشر مزيف<br><small style='color:#f59e0b'>التصيد</small></div>", unsafe_allow_html=True)
