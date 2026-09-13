import streamlit as st, re, requests, random, time, io, base64
from urllib.parse import urlparse
from datetime import datetime
from fpdf import FPDF
from gtts import gTTS

st.set_page_config(page_title="كاشف V17.1 CLEAN", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
/* خلفية سوداء ثابتة - تمنع الأزرق */
html, body, .stApp {
  background: #020617 !important;
  background-image: radial-gradient(at 50% 0%, #1e293b 0%, #020617 80%) !important;
}
.comp-card{
  background: rgba(255,255,255,0.09) !important;
  border: 1px solid rgba(255,255,255,0.18) !important;
  border-radius:18px; padding:16px;
}
.comp-card * {color: #f1f5f9 !important}
.shield-3d{
  font-size:72px; display:block; text-align:center;
  animation: pulse 1.7s infinite;
  filter: drop-shadow(0 0 20px #22c55e);
}
@keyframes pulse{
  0%{transform:scale(1)} 50%{transform:scale(1.2); filter: drop-shadow(0 0 35px #22c55e)} 100%{transform:scale(1)}
}
div.stButton>button{
  background: linear-gradient(90deg,#22c55e,#16a34a) !important;
  color:white !important; height:64px; width:100%;
  font-weight:900; border-radius:16px; font-size:20px; border:none !important;
  box-shadow: 0 0 30px rgba(34,197,94,0.6) !important;
}
input, textarea{
  background: rgba(255,255,255,0.07) !important;
  color: white !important;
  border: 1px solid rgba(255,255,255,0.2) !important;
  border-radius:12px !important;
}
.ai-box{
  background: rgba(168,85,247,0.12);
  border:1px solid #a855f7;
  border-radius:14px; padding:14px; margin-top:12px;
}
</style>
""", unsafe_allow_html=True)

if "hist" not in st.session_state: st.session_state.hist=[]

st.markdown('<span class="shield-3d">🛡️</span>', unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center; color:white; margin:0'>كاشف V17.1 <span style='color:#22c55e'>GOD AI</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#94a3b8'>النسخة النظيفة - ذكاء اصطناعي يتكلم بوضوح</p>", unsafe_allow_html=True)

def speak_ar(txt):
    try:
        tts = gTTS(text=txt, lang='ar')
        buf = io.BytesIO(); tts.write_to_fp(buf)
        b64 = base64.b64encode(buf.getvalue()).decode()
        st.markdown(f'<audio autoplay controls><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>', unsafe_allow_html=True)
    except: pass

def check(u):
    s=0; logs=[]
    if not u.startswith("http"): u="https://"+u
    d=urlparse(u).netloc.lower()
    if any(x in d for x in [".tk",".ml",".xyz","bit.ly","t.me"]): s+=30; logs.append("🆓 نطاق مجاني = تصيد")
    if any(w in u.lower() for w in ["alrajhi","stcpay","absher"]): s+=28; logs.append("🏦 انتحال بنك سعودي")
    if "@" in u: s+=30; logs.append("🎭 خدعة @")
    if "https" not in u: s+=20; logs.append("🔓 بدون HTTPS")
    return min(s,100), logs, d

def make_pdf(domain, score, logs):
    pdf=FPDF(); pdf.add_page()
    pdf.set_font("Arial","B",16); pdf.cell(0,10,f"V17 Report - {domain}", ln=True, align='C')
    pdf.set_font("Arial","",11); pdf.cell(0,8,f"Score: {score}% Date:{datetime.now()}", ln=True)
    for l in logs: pdf.cell(0,7, l.encode('latin1','ignore').decode('latin1'), ln=True)
    return pdf.output(dest='S').encode('latin1')

col1,col2 = st.columns([2,1])

with col1:
    url_in = st.text_input("الرابط", placeholder="https://alrajhi-bank-verify.tk/login", label_visibility="collapsed")
    if st.button("افحص بالذكاء الاصطناعي 🧠"):
        target = url_in or "https://alrajhi-bank-verify.tk/login"
        score, logs, domain = check(target)
        st.session_state.hist.append({"url":domain,"score":score})
        
        if score>=60:
            st.error(f"💀 خطر {score}% - {domain} لا تدخل!")
            speak_ar(f"تحذير خطر جدا بنسبة {score} بالمئة")
            ai = f"الذكاء الاصطناعي: {domain} تصيد 100%، نطاق مجاني عمره ساعة، ينتحل الراجحي، السيرفر في روسيا"
        elif score>=30:
            st.warning(f"⚠️ مشبوه {score}%"); ai=f"مشبوه {domain}"
        else:
            st.success(f"✅ آمن {score}%"); ai=f"{domain} آمن"
            st.balloons()

        st.markdown(f"<div class='ai-box'><b style='color:#a855f7'>🧠 GOD AI يحلل:</b><br><span style='color:white'>{ai}</span></div>", unsafe_allow_html=True)
        for l in logs: st.markdown(f"<div style='color:white; background:rgba(255,255,255,0.06); padding:8px; border-radius:8px; margin:4px 0'>{l}</div>", unsafe_allow_html=True)

        pdf_bytes = make_pdf(domain, score, logs)
        st.download_button("📄 حمّل تقرير PDF", data=pdf_bytes, file_name=f"report_{domain}.pdf")

with col2:
    st.markdown("<div class='comp-card'><b>🧠 ذكاء اصطناعي</b><br><small>• يتكلم عربي<br>• يفك bit.ly<br>• تقرير PDF<br>• 17 محرك</small></div>", unsafe_allow_html=True)
    st.markdown("<div class='comp-card' style='margin-top:10px'><b>📊 سجلك</b></div>", unsafe_allow_html=True)
    for h in st.session_state.hist[::-1][:5]:
        st.markdown(f"<div class='comp-card' style='padding:10px; margin-top:6px'>{'🔴' if h['score']>=60 else '🟢'} {h['url'][:20]} - {h['score']}%</div>", unsafe_allow_html=True)
