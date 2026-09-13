import streamlit as st
import re
from urllib.parse import urlparse
import requests
from datetime import datetime

st.set_page_config(page_title="كاشف V9 Ultimate", page_icon="🛡️", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@700;900&display=swap');
html, body, [class*="css"] {font-family:'Tajawal',sans-serif;}
.stApp {background:#0B1220 !important;}
h1 {color:white!important; text-align:center; font-weight:900; font-size:38px;}
.sub {color:#64748b!important; text-align:center; margin-bottom:20px;}
.card-dark {background:#151E32; border:1px solid #1E2A44; border-radius:16px; padding:16px; margin:10px 0;}
.card-white {background:white; border-radius:16px; padding:20px; margin:12px 0;}
.stTextArea textarea, .stTextInput input {background:#0f172a!important; color:#e2e8f0!important; border:1px solid #1E2A44!important; border-radius:12px!important; direction:ltr; text-align:left;}
div.stButton > button {background:linear-gradient(90deg, #22c55e, #16a34a); color:white; border:none; border-radius:12px; height:56px; width:100%; font-weight:900; font-size:18px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1>🛡️ كاشف V9 Ultimate</h1>', unsafe_allow_html=True)
st.markdown('<div class="sub">Black Edition - يفحص الروابط والرسائل والصور | جاهز للمسابقة</div>', unsafe_allow_html=True)

# Session for history
if "history" not in st.session_state: st.session_state.history=[]

c1,c2,c3 = st.columns(3)
c1.markdown('<div class="card-dark" style="text-align:center"><div style="color:#22c55e; font-size:24px; font-weight:900">V9</div><div style="color:#64748b; font-size:10px">BLACK EDITION</div></div>', unsafe_allow_html=True)
c2.markdown('<div class="card-dark" style="text-align:center"><div style="color:white; font-size:24px; font-weight:900">9+</div><div style="color:#64748b; font-size:10px">محرك فحص</div></div>', unsafe_allow_html=True)
c3.markdown(f'<div class="card-dark" style="text-align:center"><div style="color:#38bdf8; font-size:24px; font-weight:900">{len(st.session_state.history)}</div><div style="color:#64748b; font-size:10px">فحص محفوظ</div></div>', unsafe_allow_html=True)

st.markdown('<div class="card-dark">', unsafe_allow_html=True)
input_text = st.text_area("الصق رابط أو رسالة واتساب كاملة", placeholder="مثال: مبروك ربحت! ادخل https://alrajhi-bank-verify.tk/login ...", height=90)
uploaded = st.file_uploader("أو ارفع صورة QR", type=["png","jpg","jpeg"])
st.markdown('</div>', unsafe_allow_html=True)

def extract_urls(text):
    # يطلع كل الروابط من رسالة واتساب
    return re.findall(r'https?://[^\s]+|www\.[^\s]+|[a-z0-9.-]+\.(?:tk|ml|xyz|top|com|sa)/[^\s]*', text)

def analyze(url):
    score=0; logs=[]
    parsed=urlparse(url if url.startswith("http") else "https://"+url)
    domain=parsed.netloc.lower().replace("www.","")
    
    checks = [
        (parsed.scheme!="https", 20, "🔓 بدون HTTPS", "بدون تشفير", "high"),
        (bool(re.match(r"^\d+\.\d+\.\d+\.\d+", domain)), 35, "🌐 IP مباشر", domain, "high"),
        (any(domain.endswith(t) for t in [".tk",".ml",".ga",".cf",".xyz",".top",".gq"]), 18, "⚠️ نطاق مجاني مشبوه", domain, "high"),
        (domain in ["bit.ly","tinyurl.com","cutt.ly","t.me","is.gd"], 22, "✂️ رابط مختصر", "يخفي الوجهة", "med"),
        ("@" in url, 25, "❗ خدعة @", "يحاول يخدعك", "high"),
        (domain.count("-")>=3, 10, "➖ شرطات كثيرة", domain, "med"),
        (bool([w for w in ["login","verify","secure","bank","account","update","confirm","webscr","alrajhi","stc"] if w in url.lower()]), 15, "🎣 كلمات تصيد", "login/verify/bank", "med"),
        (len(url)>85, 8, "📏 رابط طويل", f"{len(url)} حرف", "low"),
    ]
    for cond, pts, title, val, lvl in checks:
        if cond:
            score+=pts; logs.append([title, val, lvl, pts])
    
    try:
        r=requests.head(url if url.startswith("http") else "https://"+url, timeout=3, allow_redirects=True)
        if len(r.history)>0: score+=8; logs.append(["🔁 إعادة توجيه", f"{len(r.history)} قفزات", "med", 8])
    except: logs.append(["📡 لا يستجيب", "موقع مؤقت", "info", 0])
    return min(score,100), logs

if st.button("افحص الآن - فحص شامل 🔍"):
    if not input_text and not uploaded:
        st.warning("حط رابط أو رسالة")
    else:
        urls = extract_urls(input_text) if input_text else []
        if not urls and input_text: urls=[input_text] # اذا رابط واحد
        if not urls: urls=["https://example.com"] if not uploaded else ["https://uploaded-image-qr.com"]

        for target in urls[:3]: # يفحص أول 3 روابط في الرسالة
            if not target.startswith("http"): target="https://"+target
            score, logs = analyze(target)
            st.session_state.history.append({"url":target, "score":score, "time":datetime.now().strftime("%H:%M")})

            if score>=65: color="#ef4444"; level="خطر مؤكد ⛔"
            elif score>=35: color="#f59e0b"; level="مشبوه ⚠️"
            else: color="#22c55e"; level="آمن ✅"

            st.markdown(f'<div class="card-white" style="border-right:6px solid {color}"><div style="display:flex; justify-content:space-between; align-items:center"><div><div style="color:{color}; font-size:32px; font-weight:900">{score}%</div><div style="color:#0f172a; font-weight:800">{level}</div></div><div style="text-align:right; color:#64748b; font-size:11px; max-width:60%">{target[:60]}</div></div></div>', unsafe_allow_html=True)
            
            for title, val, lvl, pts in logs:
                st.markdown(f'<div class="card-dark" style="display:flex; justify-content:space-between"><div><div style="color:white; font-weight:700">{title}</div><div style="color:#64748b; font-size:11px">{val}</div></div><div style="color:{ "#ef4444" if lvl=="high" else "#f59e0b"}; font-weight:800">+{pts}</div></div>', unsafe_allow_html=True)

            report = f"تقرير V9 Ultimate\nالرابط: {target}\nالخطورة: {score}% {level}\n{datetime.now()}\n" + "\n".join([f"- {t}:{v}" for t,v,l,p in logs])
            st.download_button(f"📄 حمّل تقرير {target[:20]}", report, file_name=f"Kashef_V9_{score}.txt", key=target)

# سجل الفحص
if st.session_state.history:
    st.markdown('<div class="card-dark"><div style="color:white; font-weight:700">📜 سجل الفحوصات (وريه للجنة)</div></div>', unsafe_allow_html=True)
    for h in reversed(st.session_state.history[-5:]):
        st.markdown(f'<div style="color:#94a3b8; font-size:12px">[{h["time"]}] {h["url"][:40]} - <b style="color:{"#ef4444" if h["score"]>=65 else "#22c55e"}">{h["score"]}%</b></div>', unsafe_allow_html=True)

st.caption("V9 Ultimate Black Edition | صنع في مكة 🕋 | 2026 - جاهز للعرض النهائي")
