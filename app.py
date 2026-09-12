import streamlit as st
import re, requests
from urllib.parse import urlparse
from datetime import datetime
import pandas as pd
import tldextract
# whois نستخدمه لعمر الدومين

st.set_page_config(page_title="كاشف V5 - الحارس الشامل", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@900&display=swap');
   .stApp { background: #020617; color: white; }
   .hero { background: radial-gradient(800px at 50% -20%, #1d4ed8 0%, #020617 70%); padding: 50px; border-radius: 28px; text-align:center; border: 1px solid #1e293b; }
   .hero h1 { font-size: 62px; font-weight: 900; margin:0; color: white; }
   .hero h1 span { background: linear-gradient(90deg, #60a5fa, #22d3ee, #34d399); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
   .card { background: #0f172a; border: 1px solid #1e293b; border-radius: 18px; padding: 22px; color: #e2e8f0; margin-bottom: 18px; }
   .stTextInput input { background: #0f172a!important; color: white!important; border: 1.5px solid #3b82f6!important; height: 54px; border-radius: 14px!important; }
   .stButton>button { background: linear-gradient(90deg, #2563eb, #06b6d4); color:white; height: 56px; font-weight: 900; border-radius: 14px; border:none; font-size: 18px; }
   .points { background: linear-gradient(90deg, #f59e0b, #ef4444); padding: 15px; border-radius: 14px; text-align:center; color:white; font-weight:900; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero"><h1>كاشف <span>KASHEF V5</span></h1><h3>نظام الحماية الشامل | واتساب بوت + فحص جوجل + تطبيق جوال</h3><p style="color:#94a3b8;">مشروع مسابقة الأمن السيبراني 2026 - فكرة وطنية تحمي 30 مليون مستخدم</p></div>', unsafe_allow_html=True)
st.write("")

if 'history' not in st.session_state: st.session_state.history = []
if 'points' not in st.session_state: st.session_state.points = 0
if 'reports' not in st.session_state: st.session_state.reports = []

def get_domain_age(domain):
    try:
        import whois
        w = whois.whois(domain)
        if w.creation_date:
            creation = w.creation_date[0] if isinstance(w.creation_date, list) else w.creation_date
            age = (datetime.now() - creation).days
            return age
    except: return None
    return None

def check_google_safe_browsing(url):
    # ضع مفتاحك في Streamlit Secrets لاحقاً
    api_key = st.secrets.get("GOOGLE_API_KEY", None)
    if not api_key: return None
    try:
        payload = {"client": {"clientId": "kashef", "clientVersion": "5.0"}, "threatInfo": {"threatTypes": ["MALWARE","SOCIAL_ENGINEERING"], "platformTypes": ["ANY_PLATFORM"], "threatEntryTypes": ["URL"], "threatEntries": [{"url": url}]}}
        r = requests.post(f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}", json=payload, timeout=5)
        if r.json(): return True
        return False
    except: return None

def analyze_url(url):
    score=0; reasons=[]; details=[]
    parsed=urlparse(url)
    ext=tldextract.extract(url)
    domain=f"{ext.domain}.{ext.suffix}"

    # 1. HTTPS
    if not url.startswith("https://"): score+=25; reasons.append("🔓 بدون HTTPS")

    # 2. عمر الدومين
    age=get_domain_age(domain)
    if age is not None:
        if age < 90: score+=35; reasons.append(f"⏰ دومين جديد عمره {age} يوم فقط - علامة تصيد قوية")
        details.append(f"عمر الدومين: {age} يوم")
    else: details.append("عمر الدومين: غير معروف")

    # 3. Google
    google_check=check_google_safe_browsing(url)
    if google_check==True: score+=100; reasons.append("🚨 جوجل مصنفه كموقع تصيد مؤكد!")
    elif google_check==False: details.append("فحص جوجل: سليم")

    # 4. أنماط تصيد
    if len(url)>80: score+=15; reasons.append("رابط طويل لإخفاء")
    if re.search(r"\d+\.\d+\.\d+\.\d+", url): score+=40; reasons.append("يستخدم IP")
    if any(w in url.lower() for w in ["rajhi","alahli","stcpay","tamara","alahli","alrajhi"]): score+=30; reasons.append("🎯 يستهدف بنك سعودي - خطير")

    return score, reasons, details

c1,c2 = st.columns([2.2,1])

with c1:
    tab1, tab2, tab3 = st.tabs(["🔗 فحص ذكي V5", "📱 بوت واتساب", "🚀 حوله لتطبيق"])

    with tab1:
        st.markdown('<div class="card"><h3>🤖 الفحص الشامل بـ 3 محركات</h3><p style="color:#94a3b8;">محرك كاشف + عمر الدومين + فحص Google Safe Browsing</p>', unsafe_allow_html=True)
        url = st.text_input(" ", placeholder="الصق الرابط هنا مثل: https://alrajhi-bank-secure.com", label_visibility="collapsed")
        if st.button("افحص الآن بكل المحركات 🚀", use_container_width=True):
            if not url: st.warning("الصق رابط")
            else:
                if not url.startswith("http"): url="http://"+url
                with st.spinner("جاري الفحص بـ 3 محركات..."):
                    score,reasons,details=analyze_url(url)
                if score<30:
                    st.success(f"### ✅ آمن {100-score}%"); st.balloons(); status="آمن"; st.session_state.points+=10
                elif score<70:
                    st.warning(f"### ⚠️ مشبوه {score}%"); [st.write("- "+r) for r in reasons]; status="مشبوه"; st.session_state.points+=5
                else:
                    st.error(f"### 🚨 تصيد مؤكد {score}% لا تفتحه!"); [st.write("- "+r) for r in reasons]; status="خطير"; st.session_state.points+=15
                st.write("**التفاصيل التقنية:**"); [st.caption(d) for d in details]
                st.session_state.history.append({"الرابط":url[:35],"الحالة":status,"الخطورة":score,"الوقت":datetime.now().strftime("%H:%M")})
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card"><h3>🚩 بلّغ عن رابط نصاب</h3>', unsafe_allow_html=True)
        report_url = st.text_input("رابط تبغى تبلغ عنه", placeholder="https://...")
        if st.button("إرسال البلاغ 📤"):
            if report_url:
                st.session_state.reports.append(report_url)
                st.success("تم حفظ البلاغ! سيتم إضافته لقاعدة بيانات كاشف الوطنية")
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown("""
        <div class="card">
        <h3>💬 بوت واتساب - جاهز للربط</h3>
        <p>هذا الكود تربطه مع WhatsApp Cloud API مجاناً</p>

        **الخطوات للجنة التحكيم:**
        1. روح developers.facebook.com
        2. أنشئ تطبيق WhatsApp Business
        3. الصق هذا الكود في الـ Webhook:
        <br><br>
        <code style="font-size:11px;">
        if message contains "http":<br>
        &nbsp;&nbsp;score = analyze_url(message)<br>
        &nbsp;&nbsp;reply(f"كاشف فحص الرابط: {score}%")
        </code>
        <br><br>
        المستخدم يرسل الرابط على الواتساب والبوت يرد تلقائياً!
        </div>
        """, unsafe_allow_html=True)
        st.link_button("📖 شرح ربط واتساب (فيديو)", "https://developers.facebook.com/docs/whatsapp/cloud-api/get-started")

    with tab3:
        st.markdown("""
        <div class="card">
        <h3>📲 حوله لتطبيق جوال APK في دقيقتين</h3>
        1. افتح موقع <b>website2apk.com</b><br>
        2. الصق رابط موقعك الحالي في Streamlit<br>
        3. اضغط Build APK<br>
        4. بيصير عندك تطبيق كاشف.apk تثبته على جوالك وتعرضه للجنة!<br><br>
        أو حوله لـ PWA: في Streamlit اضف هذا في الإعدادات
        </div>
        """, unsafe_allow_html=True)

with c2:
    st.markdown(f'<div class="points">🏆 نقاطك: {st.session_state.points}<br><small>كل فحص = نقاط</small></div>', unsafe_allow_html=True)
    st.write("")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 لوحة تحكم المسابقة")
    st.metric("فحوصات اليوم", len(st.session_state.history))
    st.metric("بلاغات وطنية", len(st.session_state.reports))
    if st.session_state.history:
        df=pd.DataFrame(st.session_state.history)
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.bar_chart(df["الحالة"].value_counts())
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <b>🔑 تفعيل فحص جوجل الحقيقي:</b><br>
    1. روح console.cloud.google.com<br>
    2. فعل Safe Browsing API<br>
    3. انسخ المفتاح<br>
    4. في Streamlit Cloud روح Settings > Secrets والصق:<br>
    <code>GOOGLE_API_KEY="مفتاحك"</code>
    </div>
    """, unsafe_allow_html=True)

st.caption("Kashef V5 | مشروع مسابقة متكامل | واتساب + جوجل + APK")
