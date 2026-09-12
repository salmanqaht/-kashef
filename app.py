import streamlit as st
st.title("🛡️ كاشِف")
msg = st.text_area("الصق الرسالة هنا:")
if st.button("افحص"):
    if "ايقاف" in msg or "http" in msg or "اضغط" in msg:
        st.error("⛔ احتيال 85%")
    else:
        st.success("✅ سليمة")