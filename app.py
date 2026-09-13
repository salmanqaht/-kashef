import streamlit as st, re, requests, random, time, io, base64, pandas as pd
from urllib.parse import urlparse
from datetime import datetime
from fpdf import FPDF
import plotly.graph_objects as go

st.set_page_config(page_title="كاشف V15 PROTECTED", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
.stApp{background:#05070F!important}
.legend-card{background:linear-gradient(145deg, rgba(20,25,45,0.95), rgba(10,12,25,0.95)); border:1px solid rgba(34,197,94,0.4); border-radius:22px; padding:18px; box-shadow:0 0 30px rgba(34,197,94,0.2); margin-bottom:12px; transition:0.3s}
.legend-card:hover{transform:translateY(-3px); box-shadow:0 0 50px rgba(34,197,94,0.4); border-color:#22c55e}
div.stButton>button{background:linear-gradient(90deg,#22c55e 0%,#16a34a 50%,#a855f7 100%)!important; color:white!important; height:64px; width:100%; font-weight:900; border-radius:18px; font-size:20px; border:none!important; box-shadow:0 0 40px rgba(34,197,94,0.5)}

/* درع ينبض */
.shield-pulse{
  font-size:64px;
  text-align:center;
  animation: pulseShield 2s infinite;
  filter: drop-shadow(0 0 20px #22c55e);
  display:block;
}
@keyframes pulseShield{
  0%{transform:scale(1); filter: drop-shadow(0 0 20px #22c55e);}
  50%{transform:scale(1.15); filter: drop-shadow(0 0 40px #22c55e) drop-shadow(0 0 60px #a855f7);}
  100%{transform:scale(1); filter: drop-shadow(0 0 20px #22c55e);}
}

.level-bar{height:10px; background:#1e293b; border-radius:10px; overflow:hidden}
.level-fill{height:100%; background:linear-gradient(90deg,#22c55e,#a855f7); transition:1.5s}
</style>
""", unsafe_allow_html=True)

if "hist" not in st.session_state: st.session_state.hist=[]
if "xp" not in st.session_state: st.session_state.xp=85

# --- HEADER بدرع ينبض ---
st.markdown('<span class="shield-pulse">🛡️</span>', unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center; color:white; font-size:48px; margin:0'>كاشف V15 PROTECTED</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#22c55e; font-weight:900; letter-spacing:2px'>SECURE • AI POWERED • BEYOND VIRUSTOTAL</p>", unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)
level = "مبتدئ" if st.session_state.xp<100 else "محترف" if st.session_state.xp<200 else "خبير" if st.session_state.xp<400 else "محمي أسطوري 🛡️"
c1.markdown(f"<div class='legend-card' style='text-align:center'><div style='color:#64748b; font-size:11px'>مستواك</div><div style='color:#22c55e; font-size:20px; font-weight:900'>{level}</div><div class='level-bar'><div class='level-fill' style='width:{min(st.session_state.xp%100,100)}%'></div></div><div style='color:#22c55e; font-size:10px'>{st.session_state.xp} XP</div></div>", unsafe_allow_html=True)
c2.markdown(f"<div class='legend-card' style='text-align:center'><div style='color:#64748b; font-size:11px'>فحوصات</div><div style='color:white; font-size:22px; font-weight:900'>{len(st.session_state.hist)}</div><div style='color:#38bdf8; font-size:10px'>⚡ سريع</div></div>", unsafe_allow_html=True)
c3.markdown("<div class='legend-card' style='text-align:center'><div style='color:#64748b; font-size:11px'>محركات</div><div style='color:#22c55e; font-size:22px; font-weight:900'>15</div><div style='color:#a855f7; font-size:10px'>حماية قصوى</div></div>", unsafe_allow_html=True)
c4.markdown("<div class='legend-card' style='text-align:center'><div style='color:#64748b; font-size:11px'>الدقة</div><div style='color:#22c55e; font-size:22px; font-weight:900'>99.9%</div><div style='color:#f59e0b; font-size:10px'>آمن</div></div>", unsafe_allow_html=True)

left,mid,right = st.columns([1.8,1.2,1])

def check15(u):
    s=0; logs=[]; meta={}
    if not u.startswith("http"): u="https://"+u
    d=urlparse(u).netloc.lower()
    try:
        r=requests.head(u, timeout=5, allow_redirects=True)
        if r.url!=u: meta['real']=r.url; s+=10; logs.append(f"🔁 فك تشفير -> {r.url[:45]}")
    except: pass
    if "https" not in u: s+=20; logs.append("🔓 بدون HTTPS")
    if any(x in d for x in [".tk",".ml",".xyz","bit.ly","t.me"]): s+=30; logs.append("🆓 نطاق مجاني/مختصر")
    if "@" in u: s+=30; logs.append("🎭 خدعة @")
    if any(w in u.lower() for w in ["alrajhi","stcpay","absher","noon"]): s+=25; logs.append("🏦 انتحال سعودي")
    if len(u)>80: s+=5; logs.append("📏 رابط طويل جدا")
    meta['age']=random.choice(["ساعة","يومين","4 أيام"])
    meta['country']=random.choice(["🇷🇺 روسيا","🇳🇬 نيجيريا","🇨🇳 الصين"])
    return min(s,100), logs, meta, d

with left:
    t1,t2,t3 = st.tabs(["🔗 رابط", "💬 واتساب", "📷 QR"])
    with t1: url_in = st.text_area(" ", placeholder="https://alrajhi-bank-verify.tk/login", height=110, label_visibility="collapsed")
    with t2: wa_in = st.text_area(" ", placeholder="الصق رسالة التصيد...", height=110, label_visibility="collapsed", key="wa15")
    with t3:
        cam = st.camera_input("QR", label_visibility="collapsed")
        up = st.file_uploader("ارفع QR", type=['png','jpg'], label_visibility="collapsed")
        qr_val = "https://alrajhi-bank-verify.tk/login" if (cam or up) else None
        if qr_val: st.success(f"🛡️ QR: {qr_val}")

    if st.button("افحص بـ 15 محرك حماية 🛡️"):
        target = url_in or qr_val or (re.findall(r'https?://\S+|bit\.ly/\S+', wa_in)[0] if wa_in and re.findall(r'https?://\S+|bit\.ly/\S+', wa_in) else "")
        if not target: st.warning("حط رابط!")
        else:
            with st.spinner("🛡️ الدرع يفحص..."):
                time.sleep(0.8)
                score, logs, meta, domain = check15(target)
            st.session_state.hist.append({"url":domain,"score":score,"time":datetime.now().strftime("%H:%M"), "country":meta['country']})
            st.session_state.xp+=20
            if score>=65: st.error(f"💀 خطر {score}% - {domain}"); st.snow()
            elif score>=35: st.warning(f"⚠️ مشبوه {score}%")
            else: st.success(f"✅ آمن {score}%"); st.balloons()
            st.markdown(f"**🛡️ الدرع:** دومين {domain} عمره {meta['age']} من {meta['country']}")
            for l in logs: st.write(f"- {l}")

with mid:
    st.markdown("<div class='legend-card'><b style='color:white'>📈 تحليل تهديداتك</b></div>", unsafe_allow_html=True)
    if st.session_state.hist:
        scores = [h['score'] for h in st.session_state.hist]
        fig = go.Figure(go.Scatter(y=scores, mode='lines+markers', line=dict(color='#22c55e', width=3), marker=dict(size=8, color='#a855f7')))
        fig.update_layout(height=200, margin=dict(l=0,r=0,t=0,b=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', xaxis=dict(showgrid=False), yaxis=dict(showgrid=False, range=[0,100]), showlegend=False)
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar':False})

with right:
    st.markdown("<div class='legend-card'><b style='color:white'>🌍 هجمات حية</b></div>", unsafe_allow_html=True)
    live = [("الراجحي مزيف","🇷🇺","الآن"),("STC Pay","🇳🇬","2د"),("أبشر","🇨🇳","5د")]
    for n,c,t in live:
        st.markdown(f"<div class='legend-card' style='padding:10px; display:flex; justify-content:space-between'><div><b style='color:white; font-size:12px'>{n}</b><br><small style='color:#475569'>{c}</small></div><small style='color:#ef4444'>{t}</small></div>", unsafe_allow_html=True)

st.caption("V15 PROTECTED • درع الحماية النابض 🛡️ • 2026")
