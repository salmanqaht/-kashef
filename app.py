import streamlit as st
import re
from urllib.parse import urlparse
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="كاشف V3 - نظام الحماية المتقدم", page_icon="🛡️", layout="wide")

# تصميم فخم دارك + لايت
st.markdown("""
<style>
    .stApp { background-color: #f0f2f5; }
    .hero {
        background: linear-gradient(135deg, #0d47a1, #1976d2);
        padding: 40px; border-radius: 20px; color: white; text-align: center;
        box-shadow: 0 10px 30px rgba(13,71,161,0.3); margin-bottom: 25px;
    }
    .hero h1 { font-size: 55px; margin: 0; }
    .hero p { font-size: 18px; opacity: 0.9; }
    .card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border: 1px solid #eee; }
    .stButton>button { background: #1976d2; color: white; border-radius: 10px; height: 50px; font-weight: bold; width: 100%; border: none; }
    .stButton>button:hover { background: #0d47a1; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero"><h1>🛡️ كاشف V3</h1><p>نظام الحماية الذكي المتكامل - فحص روابط | فحص QR | تحليل متقدم</p></div>', unsafe_allow_html=True)

if 'history' not in st.session_state:
    st.session_state.history = []

col_main, col_side = st.columns([2, 1])

with col_main:
    tab1, tab2 = st.tabs(["🔗 فحص رابط", "📷 فحص QR Code"])
    
    with tab1:
        url = st.text_input("الصق الرابط هنا", placeholder="https://example.com")
        if st.button("افحص الآن 🚀", key="check_url"):
            if not url:
                st.warning("حط رابط أولاً")
            else:
                if not url.startswith("http"):
                    url = "http://" + url
                
                score = 0
                reasons = []
                parsed = urlparse(url)
                
                # خوارزمية متطورة
                if not url.startswith("https://"):
                    score += 25
                    reasons.append("🔓 لا يستخدم HTTPS آمن")
                if len(url) > 80:
                    score += 20
                    reasons.append(f"📏 طول الرابط مريب ({len(url)} حرف)")
                if re.search(r"\d+\.\d+\.\d+\.\d+", url):
                    score += 35
                    reasons.append("🌐 يستخدم IP بدل اسم نطاق - خطير جداً")
                if "@" in url or parsed.netloc.count("-") > 2:
                    score += 20
                    reasons.append("🎭 اسم نطاق مقلد أو فيه حيل")
                if any(w in url.lower() for w in ["login","verify","bank","free","gift","update","secure","wallet"]):
                    score += 15
                    reasons.append("🎣 يحتوي كلمات تصيد احتيالي")
                if parsed.netloc.count(".") > 3:
                    score += 10
                    reasons.append("🔗 نطاق فرعي كثير - محاولة إخفاء")

                # النتيجة
                if score < 30:
                    st.success(f"### ✅ آمن ({100-score}%) - {url}")
                    status = "آمن"
                elif score < 65:
                    st.warning(f"### ⚠️ مشبوه ({score}% خطورة)")
                    for r in reasons: st.write(r)
                    status = "مشبوه"
                else:
                    st.error(f"### 🚨 خطير جداً! ({score}% خطورة) لا تفتحه أبداً")
                    for r in reasons: st.write(r)
                    status = "خطير"
                
                st.session_state.history.append({"الرابط": url[:40], "الحالة": status, "الخطورة": score, "الوقت": datetime.now().strftime("%H:%M")})
                
                # أزرار المشاركة
                c1, c2 = st.columns(2)
                with c1:
                    st.download_button("📄 حمّل التقرير", f"كاشف V3\nالرابط: {url}\nالحالة: {status}\nالخطورة: {score}%\nالأسباب: {','.join(reasons)}", file_name="kashef_v3.txt")
                with c2:
                    wa_text = f"فحصت رابط ببرنامج كاشف: {url} - النتيجة: {status} {score}% https://bcbgaqcnxjwfewscqqbm7r.streamlit.app/"
                    st.link_button("💬 شارك على واتساب", f"https://wa.me/?text={wa_text}")

    with tab2:
        st.info("ارفع صورة QR Code وسأقرأ الرابط اللي بداخلها وأفحصه لك")
        qr_file = st.file_uploader("ارفع صورة QR", type=["png","jpg","jpeg"])
        if qr_file:
            st.image(qr_file, width=200)
            st.success("تم قراءة QR! (الميزة تحتاج مكتبة pyzbar - سأفعلها لك في V4)")
            st.write("مؤقتاً انسخ الرابط اللي داخل الصورة والصقه في تبويب فحص رابط")

with col_side:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 لوحة التحكم")
    if st.session_state.history:
        df = pd.DataFrame(st.session_state.history)
        st.dataframe(df, use_container_width=True)
        safe = len([x for x in st.session_state.history if x["الحالة"]=="آمن"])
        danger = len(st.session_state.history) - safe
        st.metric("روابط آمنة", safe)
        st.metric("روابط خطيرة/مشبوهة", danger)
        st.bar_chart(df["الحالة"].value_counts())
    else:
        st.write("لا يوجد فحوصات بعد")
        st.write("ابدأ الفحص وستظهر الإحصائيات هنا")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("💡 نصائح الحماية")
    st.write("- لا تفتح روابط من أرقام غريبة\n- تأكد من https والقفل الأخضر\n- لا تدخل بيانات بنكية من رابط واتساب\n- استخدم كاشف قبل أي رابط مشبوه")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("كاشف V3 | تطوير سلمان القحطاني | 2026 | مشروع الأمن السيبراني")
