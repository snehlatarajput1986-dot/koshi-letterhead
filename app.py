import streamlit as st

st.set_page_config(page_title="KOSHI ENTERPRISES Letter Generator", page_icon="📝", layout="wide")

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
    st.subheader("📄 Live Preview (A4 Dimensions)")
    
    highlighted_amount = f'<span style="background-color:#cce5ff; color:#004085; padding:2px 6px; border-radius:3px; font-weight:bold; -webkit-print-color-adjust: exact;">{amount_num} ({amount_words})</span>'

    html_content = f"""
    <html>
    <head>
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
                font-family: Arial, Helvetica, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f9;
                display: flex;
                flex-direction: column;
                align-items: center;
            }}

            /* Standard A4 Container */
            .a4-page {{
                width: 210mm;
                min-height: 297mm;
                background: #ffffff;
                margin: 0 auto;
                position: relative;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            }}

            .content-wrapper {{
                padding: 25px 35px;
            }}

            @media print {{
                body {{
                    background: none;
                }}
                .no-print {{
                    display: none !important;
                }}
                .a4-page {{
                    width: 100% !important;
                    height: 100vh !important;
                    box-shadow: none !important;
                    margin: 0 !important;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="no-print" style="margin-bottom: 15px; width: 210mm; text-align: left;">
            <button onclick="window.print()" style="background-color:#0052cc; color:white; border:none; padding:10px 22px; font-size:14px; border-radius:5px; cursor:pointer; font-weight:bold;">
                🖨️ Download / Print PDF
            </button>
        </div>
        
        <div class="a4-page">
            <div>
                <!-- Vibrant Blue Header -->
                <div style="background: linear-gradient(135deg, #002b80, #0052cc) !important; color:white !important; padding:22px 30px; border-bottom: 4px solid #ff9900;">
                    <div style="display:flex; justify-content:space-between; font-size:11px; font-weight:bold; align-items:center;">
                        <span style="border:1px solid rgba(255,255,255,0.5); padding:3px 10px; border-radius:12px; letter-spacing:0.5px;">GSTIN: 10CJAPK9167R1ZQ</span>
                        <span>📞 +91 8541887622</span>
                    </div>
                    <h1 style="margin:12px 0 6px 0; text-align:center; font-size:30px; color:#ffffff !important; letter-spacing:2px; font-weight:800;">KOSHI ENTERPRISES</h1>
                    <div style="display:flex; justify-content:space-between; font-size:10.5px; margin-top:8px; opacity:0.95;">
                        <span>📍 Sukhasan Uttarwari, Ward No.- 07, Near Kali Sthan, Madhepura, Bihar - 852113</span>
                        <span>✉️ chandrasukhasan@gmail.com</span>
                    </div>
                </div>

                <div class="content-wrapper">
                    <!-- Patrank & Date -->
                    <div style="display:flex; justify-content:space-between; font-size:14px; margin-top:5px; font-weight:500;">
                        <p style="margin:0;"><b>पत्रांक :-</b> {patrank}</p>
                        <p style="margin:0;"><b>दिनांक :-</b> {tarikh}</p>
                    </div>
                    
                    <!-- Address -->
                    <p style="font-size:14px; margin-top:22px; line-height:1.5;"><b>सेवा में,</b><br>{seva_me.replace('\n', '<br>')}</p>
                    
                    <!-- Subject Box -->
                    <div style="background-color:#f0f4f9 !important; padding:12px 15px; border-left:5px solid #0052cc; border-radius:4px; font-size:13.5px; margin:22px 0; line-height:1.5;">
                        <b>विषय :- {vishay}</b>
                    </div>
                    
                    <!-- Body -->
                    <p style="font-size:14px; margin-bottom:10px;"><b>महाशय,</b></p>
                    <p style="line-height:1.8; font-size:14px; margin-top:0; text-align:justify;">{patra_vivran.replace('\n', '<br>')}</p>
                    
                    <p style="line-height:1.8; font-size:14px; text-align:justify;">
                        उक्त सामग्रियों की आपूर्ति के पश्चात कुल व्यय राशि {highlighted_amount} का बिल भुगतान हेतु तैयार किया गया है। सामग्रियों की विवरणी एवं मूल विपत्र (Original Bill) इस आवेदन के साथ संलग्न है।
                    </p>
                    
                    <p style="line-height:1.8; font-size:14px; text-align:justify;">
                        अतः श्रीमान से विनम्र प्रार्थना है कि सामग्रियों के सत्यापन उपरांत कोशी इंटरप्राइजेज, मधेपुरा को कुल राशि {highlighted_amount} के भुगतान की स्वीकृति प्रदान करने की कृपा की जाए। इसके लिए हम सदैव आपके आभारी रहेंगे।
                    </p>

                    <!-- Bank Details & Signature -->
                    <div style="display:flex; justify-content:space-between; align-items:flex-end; margin-top:35px;">
                        <div style="background-color:#f8f9fa !important; border:1px solid #dce4ec; border-radius:6px; padding:14px 16px; width:54%;">
                            <h4 style="margin:0 0 10px 0; color:#0052cc !important; font-size:13.5px;">🏦 भुगतान हेतु बैंक विवरण (Bank Details)</h4>
                            <table style="font-size:12px; width:100%; border-collapse:collapse; line-height:1.6;">
                                <tr><td style="width:38%;"><b>बैंक का नाम:</b></td><td><b>HDFC MADHEPURA</b></td></tr>
                                <tr><td><b>खाता संख्या:</b></td><td><b>50200099372362</b></td></tr>
                                <tr><td><b>आईएफएससी कोड:</b></td><td><b>HDFC0002353</b></td></tr>
                            </table>
                        </div>
                        
                        <div style="text-align:center; font-size:13.5px; width:36%;">
                            <p style="margin-bottom:50px;"><b>विश्वासभाजन</b></p>
                            <p style="margin:0; font-weight:bold; font-size:14px;">कोशी इंटरप्राइजेज</p>
                            <p style="margin:2px 0 0 0; font-size:11.5px; color:#555;">मधेपुरा (बिहार)</p>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Footer Strip -->
            <div style="background-color:#001a4d !important; color:white !important; text-align:center; padding:9px; font-size:10px; letter-spacing:0.5px;">
                KOSHI ENTERPRISES • Sukhasan Uttarwari, Ward No. 07, Madhepura, Bihar - 852113
            </div>
        </div>
    </body>
    </html>
    """
    st.components.v1.html(html_content, height=1150, scrolling=True)
