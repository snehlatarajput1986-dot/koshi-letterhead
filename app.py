import streamlit as st
import datetime

st.set_page_config(page_title="KOSHI ENTERPRISES - Auto Highlight Letter", page_icon="📝", layout="wide")

st.title("📝 KOSHI ENTERPRISES Automatic Letter Generator")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📋 Application Inputs")
    patrank = st.text_input("पत्रांक (Ref No.)", value="....................")
    tarikh = st.text_input("दिनांक (Date)", value="....................")
    
    seva_me = st.text_area("सेवा में (To Address)", 
                           value="जिला शिक्षा पदाधिकारी", 
                           height=80)
    
    vishay = st.text_input("विषय (Subject)", value="KOSHI ENTERPRISES मधेपुरा के द्वारा कार्यक्रम आयोजित करने के संबंध में")
    
    # Naya Editable Vivran Box
    vivran = st.text_area("विवरण (Body Text / Main Content)", 
                          value="उपरोक्त विषयक संबंध में सादर पूर्वक कहना है कि कोशी इंटरप्राइजेज मधेपुरा के द्वारा कार्यक्रम सफलतापूर्वक संचालित किया गया।", 
                          height=150)
    
    prog_name = st.text_input("कार्यक्रम का नाम व तिथि", value="विश्व दिव्यांग दिवस (03-12-2025)")
    prog_loc = st.text_input("कार्यक्रम का स्थान", value="अधिकलाल मध्य विद्यालय के मैदान में")
    
    st.subheader("💰 Amount Details (Auto Highlight)")
    amount_num = st.text_input("राशि (अंकों में)", value="134910/-")
    amount_words = st.text_input("राशि (शब्दों में)", value="एक लाख तैंतीस हजार नौ सौ दस")

with col2:
    st.subheader("📄 Auto-Highlighted Preview")
    
    # Printable/Rendered Letterhead View
    html_code = f"""
    <div style="border:1px solid #ccc; padding:20px; font-family:Arial, sans-serif; background-color:#fff; color:#000;">
        <div style="background-color:#1e3c72; color:white; padding:15px; text-align:center; border-radius:5px;">
            <p style="margin:0; font-size:12px; font-weight:bold;">GSTIN: 10CJAPK9167R1ZQ</p>
            <h1 style="margin:5px 0; font-size:24px; color:white;">KOSHI ENTERPRISES</h1>
            <p style="margin:0; font-size:12px;">Sukhasan Uttarwari, Ward No.- 07, Near Kali Sthan, Madhepura, Bihar - 852113</p>
        </div>
        <br>
        <div style="display:flex; justify-content:space-between;">
            <p><b>पत्रांक :-</b> {patrank}</p>
            <p><b>दिनांक :-</b> {tarikh}</p>
        </div>
        <p><b>सेवा में,</b><br>{seva_me.replace('\n', '<br>')}</p>
        <p style="background-color:#e8f0fe; padding:8px; border-radius:4px;"><b>विषय :- {vishay}</b></p>
        <p><b>महाशय,</b></p>
        <p style="line-height:1.6;">{vivran.replace('\n', '<br>')}</p>
        <p>कार्यक्रम का नाम व तिथि: <b>{prog_name}</b>, स्थान: <b>{prog_loc}</b></p>
        <p>जिसका कुल व्यय राशि <span style="background-color:#d1e7dd; padding:2px 6px; font-weight:bold; border-radius:3px;">{amount_num} ({amount_words} रुपया)</span> है।</p>
        <p>अतः श्रीमान से आग्रह है कि कोशी इंटरप्राइजेज मधेपुरा को कुल राशि <span style="background-color:#d1e7dd; padding:2px 6px; font-weight:bold; border-radius:3px;">{amount_num} ({amount_words} रुपया)</span> भुगतान करने की कृपा की जाय। इसके लिए हम सदैव आपके आभारी रहेंगे।</p>
        <br><br>
        <div style="text-align:right;">
            <p><b>विश्वासभाजन</b><br>KOSHI ENTERPRISES</p>
        </div>
    </div>
    """
    st.components.v1.html(html_code, height=650, scrolling=True)
