import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="KOSHI ENTERPRISES Letter Generator", page_icon="📝", layout="wide")

# --- FACEBOOK-INSPIRED THEME CSS ---
st.markdown("""
<style>
    /* Main Streamlit App Background */
    .stApp {
        background-color: #f0f2f5;
        color: #1c1e21;
    }
    
    /* Sidebar / Container Polish */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #ced0d4;
    }
    
    /* Input Fields Styling */
    input, textarea, select {
        background-color: #ffffff !important;
        color: #1c1e21 !important;
        border: 1px solid #ccd0d5 !important;
        border-radius: 6px !important;
        font-size: 14px !important;
        max-width: 100% !important;
    }
    
    /* Input Labels Readability */
    .stTextInput label, .stTextArea label {
        color: #4b4f56 !important;
        font-weight: 600 !important;
    }
    
    /* Buttons Styling (Facebook Blue) */
    .stButton>button, .stDownloadButton>button {
        background-color: #1877f2 !important;
        color: white !important;
        border: none;
        border-radius: 6px;
        font-weight: bold;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .stButton>button:hover, .stDownloadButton>button:hover {
        background-color: #166fe5 !important;
    }

    /* Headers Styling */
    h1, h2, h3 {
        color: #1877f2 !important;
    }

    /* Page Scrolling & Stability */
    html, body, [data-testid="stAppViewContainer"] {
        overflow-x: hidden !important;
        scroll-behavior: smooth;
    }

    [data-testid="stVerticalBlock"] {
        transform: translateZ(0);
        backface-visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)

st.title("📝 KOSHI ENTERPRISES Automatic Letter Generator")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📋 Application Inputs")
    patrank = st.text_input("पत्रांक (Ref No.)", value="....................")
    tarikh = st.text_input("दिनांक (Date)", value="....................")
    
    seva_me = st.text_area("सेवा में (To Address)", 
                           value="जिला कार्यक्रम पदाधिकारी,\nप्राथमिक शिक्षा एवं सर्व शिक्षा अभियान,\nमधेपुरा (बिहार)।", 
                           height=90)
    
    vishay = st.text_input("विषय (Subject)", value="DIET मधेपुरा जिला एवं प्रखंड स्तरीय PBL (Project Based Learning) कार्यक्रम के उपरांत कोशी इंटरप्राइजेज द्वारा उपलब्ध कराई गई सामग्री के भुगतान के संबंध में।")
    
    patra_vivran = st.text_area(
        "पत्र का विवरण (Main Body)", 
        value="उपरोक्त विषय के संबंध में सादर निवेदन है कि कोशी-इंटरप्राइजेज, मधेपुरा द्वारा DIET मधेपुरा जिला एवं प्रखंड स्तरीय PBL (Project Based Learning) कार्यक्रम के सुचारू संचालन तथा कार्यालय कार्य हेतु आवश्यक सामग्रियां उपलब्ध कराई गई थीं।", 
        height=130
    )

    st.subheader("💰 Amount Details (Auto Highlight)")
    amount_num = st.text_input("राशि (अंकों में)", value="₹9,090/-")
    amount_words = st.text_input("राशि (शब्दों में)", value="नौ हजार नब्बे रुपये मात्र")

with col2:
    st.subheader("📄 Live Preview")

    # High-Contrast Clear Highlight for Amounts (Facebook Blue Accent)
    highlighted_amount = f'<span style="background-color:#e7f3ff; color:#1877f2; padding:3px 8px; border-radius:4px; font-weight:bold; border: 1px solid #1877f2; -webkit-print-color-adjust: exact;">{amount_num} ({amount_words})</span>'

    # Build Letter HTML with Facebook Theme for Crystal Clear Prints
    letter_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            * {{
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
                box-sizing: border-box;
            }}
            
            @page {{
                size: A4 portrait;
                margin: 0;
            }}

            body {{
                font-family: Helvetica, Arial, sans-serif;
                margin: 0;
                padding: 10px;
                background-color: #f0f2f5;
            }}

            .letter-box {{
                width: 100%;
                max-width: 850px;
                min-height: 100vh;
                margin: 0 auto;
                background: #ffffff !important;
                color: #1c1e21 !important;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                border: 1px solid #ccd0d5;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}

            .content-body {{
                padding: 35px 45px;
                flex-grow: 1;
            }}

            @media print {{
                body {{
                    padding: 0;
                    background-color: #ffffff !important;
                }}
                .letter-box {{
                    border: none !important;
                    box-shadow: none !important;
                    border-radius: 0 !important;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="letter-box">
            <div>
                <!-- Facebook Blue Header -->
                <div style="background-color: #1877f2 !important; color:white !important; padding:25px 30px; border-bottom: 4px solid #166fe5;">
                    <div style="display:flex; justify-content:space-between; font-size:12px; font-weight:bold; align-items:center;">
                        <span style="background:rgba(255,255,255,0.2); padding:3px 10px; border-radius:12px;">GSTIN: 10CJAPK9167R1ZQ</span>
                        <span style="font-size:13px;">📞 +91 8541887622</span>
                    </div>
                    <h1 style="margin:14px 0 8px 0; text-align:center; font-size:32px; color:#ffffff !important; letter-spacing:1px; font-weight:800;">KOSHI ENTERPRISES</h1>
                    <div style="display:flex; justify-content:space-between; font-size:11.5px; margin-top:10px; opacity:0.95;">
                        <span>📍 Sukhasan Uttarwari, Ward No.- 07, Near Kali Sthan, Madhepura, Bihar - 852113</span>
                        <span>✉️ chandrasukhasan@gmail.com</span>
                    </div>
                </div>

                <div class="content-body">
                    <!-- Patrank & Date -->
                    <div style="display:flex; justify-content:space-between; font-size:15px; margin-top:10px; font-weight:600; color: #4b4f56;">
                        <p style="margin:0;"><b>पत्रांक :-</b> <span style="color:#1c1e21;">{patrank}</span></p>
                        <p style="margin:0;"><b>दिनांक :-</b> <span style="color:#1c1e21;">{tarikh}</span></p>
                    </div>
                    
                    <!-- Address -->
                    <p style="font-size:15px; margin-top:30px; line-height:1.7; color: #4b4f56;"><b>सेवा में,</b><br><div style="color:#1c1e21; margin-top:3px;">{seva_me.replace('\n', '<br>')}</div></p>
                    
                    <!-- Subject Box -->
                    <div style="background-color:#e7f3ff !important; color:#1c1e21 !important; padding:15px 18px; border-left:6px solid #1877f2; border-radius:5px; font-size:15px; margin:30px 0; line-height:1.6; border: 1px solid #ccd0d5; border-left: 6px solid #1877f2;">
                        <b>विषय :- {vishay}</b>
                    </div>
                    
                    <!-- Body -->
                    <p style="font-size:15px; margin-bottom:12px; color: #4b4f56;"><b>महाशय,</b></p>
                    <p style="line-height:2.0; font-size:15px; margin-top:0; text-align:justify; color: #1c1e21;">{patra_vivran.replace('\n', '<br>')}</p>
                    
                    <p style="line-height:2.0; font-size:15px; text-align:justify; margin-top:18px; color: #1c1e21;">
                        उक्त सामग्रियों की आपूर्ति के पश्चात कुल व्यय राशि {highlighted_amount} का बिल भुगतान हेतु तैयार किया गया है। सामग्रियों की विवरणी एवं मूल विपत्र (Original Bill) इस आवेदन के साथ संलग्न है।
                    </p>
                    
                    <p style="line-height:2.0; font-size:15px; text-align:justify; margin-top:18px; color: #1c1e21;">
                        अतः श्रीमान से विनम्र प्रार्थना है कि सामग्रियों के सत्यापन उपरांत कोशी इंटरप्राइजेज, मधेपुरा को कुल राशि {highlighted_amount} के भुगतान की स्वीकृति प्रदान करने की कृपा की जाए। इसके लिए हम सदैव आपके आभारी रहेंगे।
                    </p>

                    <!-- Bank Details & Signature -->
                    <div style="display:flex; justify-content:space-between; align-items:flex-end; margin-top:55px;">
                        <div style="background-color:#f0f2f5 !important; color:#1c1e21 !important; border:1px solid #ccd0d5; border-radius:8px; padding:16px 20px; width:54%;">
                            <h4 style="margin:0 0 12px 0; color:#1877f2 !important; font-size:15px;">🏦 भुगतान हेतु बैंक विवरण (Bank Details)</h4>
                            <table style="font-size:13.5px; width:100%; border-collapse:collapse; line-height:1.8; color: #4b4f56;">
                                <tr><td style="width:38%;"><b>बैंक का नाम:</b></td><td><b style="color:#1c1e21;">HDFC MADHEPURA</b></td></tr>
                                <tr><td><b>खाता संख्या:</b></td><td><b style="color:#1c1e21;">50200099372362</b></td></tr>
                                <tr><td><b>आईएफएससी कोड:</b></td><td><b style="color:#1c1e21;">HDFC0002353</b></td></tr>
                            </table>
                        </div>
                        
                        <div style="text-align:center; font-size:15px; width:38%; color: #4b4f56;">
                            <p style="margin-bottom:65px;"><b>विश्वासभाजन</b></p>
                            <p style="margin:0; font-weight:bold; font-size:16px; color:#1c1e21;">कोशी इंटरप्राइजेज</p>
                            <p style="margin:4px 0 0 0; font-size:12.5px; color:#65676b;">मधेपुरा (बिहार)</p>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Footer Strip -->
            <div style="background-color:#1c1e21 !important; color:#ffffff !important; text-align:center; padding:12px; font-size:11px; letter-spacing:0.5px;">
                KOSHI ENTERPRISES • Sukhasan Uttarwari, Ward No. 07, Madhepura, Bihar - 852113
            </div>
        </div>
    </body>
    </html>
    """

    # Direct Native Streamlit Download Button
    st.download_button(
        label="📥 Save / Download Letter File",
        data=letter_html,
        file_name="Koshi_Enterprises_Letter.html",
        mime="text/html",
        use_container_width=True
    )
    
    st.caption("💡 **Print Tip:** File download karke browser me kholein aur Print par click karein. A4 mein bilkul perfect fit aayega!")

    # Display Preview
    components.html(letter_html, height=850, scrolling=True)
