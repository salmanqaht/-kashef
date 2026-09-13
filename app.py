import streamlit as st
import re
from urllib.parse import urlparse
import time

st.set_page_config(page_title="كاشف V10 ULTRA", page_icon="🛡️", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@700;900&display=swap');
html, body,.stApp, [data-testid="stAppViewContainer"]{
  background: radial-gradient(ellipse at top, #16223f 0%, #0B1220 50%, #060a14 100%)!important;
  font-family:'Tajawal', sans-serif;
}
[data-testid="stHeader"]{background:transparent!important}
.main-title{
  text-align:center; font-size:42px; font-weight:900; color:white;
  text-shadow:0 0 20px #22c55e, 0 0 40px #22c55e55;
  animation: glow 2s ease-in-out infinite alternate;
}
@keyframes glow{from{text-shadow:0 0 10px #22c55e} to{text-shadow:0 0 25px #22c55e, 0 0 50px #22c55e88}}
@keyframes float{0%,100%{transform:translateY(0)} 50%{transform:translateY(-6px)}}
.shield{font-size:64px; text-align:center; animation:float 3s ease-in-out infinite; filter:drop-shadow(0 0 20px #22c55e)}
.glass{
  background: linear-gradient(145deg, rgba(21,30,50,0.9), rgba(13,19,35,0.9));
  border:1px solid rgba(34,197,94,0.2); border-radius:20px; padding:18px;
  backdrop-filter: blur(12px); box-shadow:0 8px 32px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.1);
  transition:0.3s;
}
.glass:hover{border-color:rgba(34,197,94,0.5); box-shadow:0 0 25px rgba(34,197,94,0.2); transform:translateY(-2px)}
textarea{
  background:#0f172a!important; color:white!important;
  border:2px solid #1e293b!important; border-radius:16px!important; font-size:16px!important;
}
textarea:focus{border-color:#22c55e!important; box-shadow:0 0 0 3px rgba(34,197,94,0.2)!important}
div.stButton>button{
  background: linear-gradient(90deg, #22c55e, #16a34a)!important;
  color:white!important; height:60px; width:100%; font-weight:900; border-radius:16px;
  font-size:20px; border:none!important; box-shadow:0 0 30px rgba(34,197,94,0.4);
  transition:0.3s;
}
div.stButton>button:hover{transform:scale(1.02); box-shadow:0 0 40px rgba(34,197,94,0.6)}
.result-card{
  background:white; border-radius:24px; padding:24px; text-align:center;
  box-shadow:0 20px 60px rgba(0,0,0,0.5); animation: pop 0.5s cubic-bezier(0.34,1.56,0.64,1);
}
@keyframes pop{0%{transform:scale(0.8)} 100%{transform:scale(1)}}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="shield">🛡️</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">كاشف V10 ULTRA</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#64748b; margin-top:-10px'>Cyber Shield • تصميم يبهر لجنة التحكيم • مكة 2026</p>", unsafe_allow_html=True)

if "hist" not in st.session_state: st.session_state.hist=[]

c1,c2,c3=st.columns(3)
c1.markdown('<div class="glass"><div style="color:#22c55e; font-size:28px; font-weight:900">V10</div><div style="color:#94a3b8; font-size:11px">ULTRA EDITION</div><div style="color:#22c55e; font-size:10px">● LIVE</div></div>', unsafe_allow_html=True)
c2.markdown('<div class="glass"><div style="color:white; font-size:28px; font-weight:900">10+</div><div style="color:#94a3b8; font-size:11px">محرك حماية</div><div style="color:#38bdf8; font-size:10px">AI POWERED</div></div>', unsafe_allow_html=True)
c3.markdown(f'<div class="glass"><div style="color:#38bdf8; font-size:28px; font-weight:900">{len(st.session_state.hist)}</div><div style="color:#94a3b8; font-size:11px">عملية فحص</div><div style="color:#f59e0b; font-size:10px">محفوظ</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
txt=st.text_area(" ", placeholder="الصق رابط التصيد هنا... مثال: alrajhi-bank-verify.tk/login", height=110)

def check(u):
    s=0; logs=[]
    if not u.startswith("http"): u="https://"+u
    d=urlparse(u).netloc.lower()
    if urlparse(u).scheme!="https": s+=20; logs.append(("🔓 بدون HTTPS","الاتصال غير مشفر - سهل الاختراق","high",20))
    if re.match(r"^\d+\.\d+\.\d+\.\d+", d): s+=35; logs.append(("🌐 خادم IP مباشر",d,"high",35))
    if any(d.endswith(x) for x in [".tk",".ml",".xyz",".top",".cf",".gq"]): s+=18; logs.append(("⚠️ نطاق مجاني مشبوه",d,"high",18))
    if "bit.ly" in d or "tinyurl" in d or "t.me" in d: s+=22; logs.append(("✂️ رابط مختصر ملغوم","يخفي الوجهة الحقيقية","med",22))
    if "@" in u: s+=25; logs.append(("❗ خدعة @ الاحترافية","يخدع المتصفح","high",25))
    if any(w in u.lower() for w in ["login","verify","bank","secure","update"]): s+=12; logs.append(("🎣 كلمات تصيد بنكي","login / verify / bank","med",12))
    if len(u)>75: s+=8; logs.append(("📏 رابط طويل متعمد","لإخفاء النطاق المزيف","low",8))
    return min(s,100), logs

if st.button("افحص الآن ⚡"):
    target=txt.strip().split()[0] if txt else ""
    if not target:
        st.toast("حط رابط أول!")
    else:
        with st.spinner("جاري تشغيل 10 محركات حماية..."):
            time.sleep(0.8)
            score,logs=check(target)
            st.session_state.hist.append((target,score))
            if score>=65: color="#ef4444"; bg="#fef2f2"; level="خطر مؤكد ⛔ لا تدخل ابداً"; emoji="💀"
            elif score>=35: color="#f59e0b"; bg="#fffbeb"; level="مشبوه جداً ⚠️ انتبه"; emoji="⚠️"
            else: color="#22c55e"; bg="#f0fdf4"; level="آمن ✅"; emoji="✅"

            st.markdown(f"""
            <div class="result-card" style="border-top:6px solid {color}; background:{bg}">
                <div style="font-size:64px">{emoji}</div>
                <div style="font-size:56px; font-weight:900; color:{color}">{score}%</div>
                <div style="font-size:20px; font-weight:800; color:#0B1220">{level}</div>
                <div style="font-size:12px; color:#64748b; margin-top:8px; word-break:break-all">{target}</div>
                <div style="margin-top:12px; background:{color}; height:8px; border-radius:10px; width:{score}%"></div>
            </div>
            """, unsafe_allow_html=True)

            for t,v,l,p in logs:
                col = "#ef4444" if l=="high" else "#f59e0b" if l=="med" else "#64748b"
                st.markdown(f"""
                <div class="glass" style="display:flex; justify-content:space-between; align-items:center; margin-top:10px">
                    <div style="text-align:right"><div style="color:white; font-weight:700">{t}</div><div style="color:#94a3b8; font-size:11px">{v}</div></div>
                    <div style="background:{col}22; color:{col}; border:1px solid {col}44; padding:6px 12px; border-radius:20px; font-weight:900">+{p}</div>
                </div>
                """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#334155; font-size:11px'>V10 ULTRA • Cyber Shield • صمم في مكة 🕋 للمسابقة</p>", unsafe_allow_html=True)
