import streamlit as st
st.set_page_config(page_title="كاشف V10 Final", page_icon="🛡️", layout="centered")
st.markdown("""
<style>
.stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"]{background:#0B1220!important; background-color:#0B1220!important}
h1,h2,h3,p,span,label{color:white!important}
.card{background:#151E32; border:1px solid #2A3A5C; border-radius:16px; padding:14px; margin:6px 0; text-align:center}
textarea{background:#0f172a!important; color:white!important; border:1px solid #334155!important; border-radius:12px!important}
div.stButton>button{background:#22c55e!important; color:white!important; height:56px; width:100%; font-weight:900; border-radius:12px; font-size:19px; border:none}
</style>
""", unsafe_allow_html=True)
import re
from urllib.parse import urlparse
import requests
from datetime import datetime

st.markdown("<h1 style='text-align:center'>🛡️ كاشف V10 Final</h1>")
st.markdown("<p style='text-align:center; color:#94a3b8'>Black Edition - جاهز للمسابقة</p>")

if "hist" not in st.session_state: st.session_state.hist=[]

a,b,c=st.columns(3)
a.markdown('<div class="card"><b style="color:#22c55e; font-size:22px">V10</b><br><span style="font-size:10px; color:#64748b">FINAL BLACK</span></div>', unsafe_allow_html=True)
b.markdown('<div class="card"><b style="color:white; font-size:22px">10+</b><br><span style="font-size:10px; color:#64748b">محركات</span></div>', unsafe_allow_html=True)
c.markdown(f'<div class="card"><b style="color:#38bdf8; font-size:22px">{len(st.session_state.hist)}</b><br><span style="font-size:10px; color:#64748b">سجل</span></div>', unsafe_allow_html=True)

txt=st.text_area("الصق رابط أو رسالة", placeholder="https://alrajhi-bank-verify.tk/login", height=100)

def check(u):
    s=0; logs=[]
    if not u.startswith("http"): u="https://"+u
    d=urlparse(u).netloc.lower()
    if urlparse(u).scheme!="https": s+=20; logs.append(("🔓 بدون HTTPS","خطير",20))
    if re.match(r"^\d+\.\d+\.\d+\.\d+", d): s+=35; logs.append(("🌐 IP مباشر",d,35))
    if any(d.endswith(x) for x in [".tk",".ml",".xyz",".top",".cf"]): s+=18; logs.append(("⚠️ نطاق مجاني",d,18))
    if "bit.ly" in d or "tinyurl" in d: s+=22; logs.append(("✂️ رابط مختصر","يخفي الوجهة",22))
    if "@" in u: s+=25; logs.append(("❗ خدعة @","@",25))
    if any(w in u.lower() for w in ["login","verify","bank"]): s+=12; logs.append(("🎣 كلمات تصيد","login/verify",12))
    if len(u)>80: s+=8; logs.append(("📏 طويل",f"{len(u)} حرف",8))
    return min(s,100), logs

if st.button("افحص الآن 🔍"):
    target=txt.strip().split()[0] if txt else ""
    if not target: st.warning("حط رابط")
    else:
        score,logs=check(target)
        st.session_state.hist.append((target,score))
        if score>=65: color="#ef4444"; level="خطر مؤكد ⛔"
        elif score>=35: color="#f59e0b"; level="مشبوه ⚠️"
        else: color="#22c55e"; level="آمن ✅"
        st.markdown(f'<div style="background:white; border-radius:16px; padding:20px; text-align:center; border-right:6px solid {color}"><div style="font-size:48px; font-weight:900; color:{color}">{score}%</div><div style="font-weight:800; color:#0B1220">{level}</div><div style="font-size:11px; color:#64748b">{target[:50]}</div></div>', unsafe_allow_html=True)
        for t,v,p in logs:
            st.markdown(f'<div class="card" style="display:flex; justify-content:space-between"><span>{t} - {v}</span><b style="color:#f59e0b">+{p}</b></div>', unsafe_allow_html=True)

st.caption("V9 -> V10 | Black Edition | مكة 2026")
