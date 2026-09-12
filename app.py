import streamlit as st
import re, cv2, numpy as np
from urllib.parse import urlparse
from datetime import datetime
import pandas as pd
from fpdf import FPDF
from PIL import Image

st.set_page_config(page_title="كاشف V4 - نظام التخرج", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
    .stApp { background: #f5f7fb; }
    .hero { background: linear-gradient(135deg, #0d47a1, #42a5f5); padding:30px; border-radius:18px; text-align:center; color:white; }
    .hero h1 { color:white !important; margin:0; font-size:38px; }
    .card { background:white; padding:18px; border-radius:14px; border:1px solid #eef0f4; box-shadow: 0 2px 10px rgba(0,0,0,0.04); margin-bottom:15px; }
    input[type="text"] { background:white !important; color:black !important; border:2px solid #1976d2 !important; }
    .stTextInput input { background:white !important; color:black !important; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero"><h1>🛡️ كاشف V4</h1><p>نظام متكامل لكشف التصيد - مشروع تخرج - سلمان القحطاني 2026</p></div>', unsafe_allow_html=True)
st.write("")

if 'history' not in st.session_state: st.session_state.history = []

def analyze_url(url):
    score=0; reasons=[]; parsed=urlparse(url)
    if not url.startswith("https://"): score+=25; reasons.append("🔓 لا يستخدم HTTPS آمن")
    if len(url)>75: score+=20; reasons.append(f"📏 رابط طويل جداً ({len(url)} حرف) - محاولة إخفاء")
    if re.search(r"\d+\.\d+\.\d+\.\d+", url): score+=45; reasons.append("🌐 يستخدم عنوان IP بدل اسم موقع - خطير جداً")
    if "@" in url: score+=25; reasons.append("🎭 يحتوي رمز @ لخداع المستخدم")
    if parsed.netloc.count("-")>2 or parsed.netloc.count(".")>3: score+=15; reasons.append("🔗 دومين مقلد بكثرة النقاط/الشرطات")
    if any(w in url.lower() for w in ["login","verify","bank","secure","update","free","gift","wallet"]): score+=15; reasons.append("🎣 يحتوي كلمات تصيد احتيالي شائعة")
    # تحليل عمر الدومين (محاكاة)
    if len(parsed.netloc) < 10: score+=10; reasons.append("⏰ اسم نطاق قصير ومريب")
    return score, reasons

def create_pdf(url, status, score, reasons):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Kashef V4 - Phishing Detection Report", ln=True, align="C")
    pdf.set_font("Arial", "", 11)
    pdf.ln(10)
    pdf.cell(0, 8, f"URL: {url}", ln=True)
    pdf.cell(0, 8, f"Status: {status}", ln=True)
    pdf.cell(0, 8, f"Risk Score: {score}%", ln=True)
    pdf.cell(0, 8, f"Date: {datetime.now()}", ln=True)
    pdf.ln(5)
    pdf.cell(0, 8, "Reasons:", ln=True)
    for r in reasons: pdf.cell(0, 8, f"- {r}", ln=True)
    pdf.ln(10)
    pdf.cell(0, 8, "Developed by: Salman Al-Qahtani - 2026", ln=True, align="C")
    return pdf.output(dest='S').encode('latin-1', 'ignore')

c1, c2 = st.columns([2,1])

with c1:
    tab1, tab2 = st.tabs(["🔗 فحص رابط", "📷 فحص QR حقيقي"])
    
    with tab1:
        st.write("### 🔍 الصق الرابط المشبوه")
        url = st.text_input("url", placeholder="https://example.com", label_visibility="collapsed")
        if st.button("افحص الآن 🚀", use_container_width=True):
            if not url: st.warning("الصق رابط أولاً")
            else:
                if not url.startswith("http"): url="http://"+url
                score, reasons = analyze_url(url)
                
                if score < 30:
                    st.success(f"### ✅ آمن بنسبة {100-score}%"); status="آمن"
                elif score < 65:
                    st.warning(f"### ⚠️ مشبوه - خطورة {score}%"); [st.write("- "+r) for r in reasons]; status="مشبوه"
                else:
                    st.error(f"### 🚨 خطير جداً {score}% - لا تفتحه أبداً!"); [st.write("- "+r) for r in reasons]; status="خطير"
                
                st.session_state.history.append({"الرابط":url[:35], "الحالة":status, "الخطورة":score, "الوقت":datetime.now().strftime("%H:%M")})
                
                # PDF تقرير
                pdf_bytes = create_pdf(url, status, score, reasons)
                st.download_button("📄 حمّل تقرير PDF رسمي", pdf_bytes, file_name=f"kashef_report_{datetime.now().strftime('%Y%m%d')}.pdf", mime="application/pdf", use_container_width=True)

    with tab2:
        st.write("### 📷 ارفع صورة QR Code")
        qr_file = st.file_uploader("رفع QR", type=["png","jpg","jpeg"], label_visibility="collapsed")
        if qr_file:
            img = Image.open(qr_file)
            st.image(img, width=250)
            # قراءة QR حقيقية بـ OpenCV
            cv_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            detector = cv2.QRCodeDetector()
            data, bbox, _ = detector.detectAndDecode(cv_img)
            if data:
                st.success(f"✅ تم قراءة الرابط: {data}")
                st.write(f"**الرابط المقروء:** {data}")
                score, reasons = analyze_url(data)
                if score < 30: st.success(f"النتيجة: آمن {100-score}%")
                else: st.error(f"النتيجة: خطير {score}% - " + ", ".join(reasons))
            else:
                st.error("❌ لم أتمكن من قراءة QR، تأكد الصورة واضحة")

with c2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📊 لوحة تحكم المشروع")
    if st.session_state.history:
        df=pd.DataFrame(st.session_state.history)
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.metric("إجمالي الفحوصات", len(df))
        st.bar_chart(df["الحالة"].value_counts())
    else:
        st.info("لا يوجد فحوصات بعد - ابدأ الآن")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card"><b>🎓 معلومات المشروع</b><br><br>الاسم: كاشف<br>الإصدار: V4 النهائي<br>الطالب: سلمان القحطاني<br>الهدف: حماية المستخدمين من التصيد<br>التقنيات: Python, OpenCV, AI Pattern Analysis</div>', unsafe_allow_html=True)

st.caption("كاشف V4 | مشروع تخرج | جميع الحقوق محفوظة 2026")
