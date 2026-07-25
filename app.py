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
    st.subheader("📄 Live Preview")
    
    highlighted_amount = f'<span style="background-color:#cce5ff; color:#004085; padding:2px 6px; border-radius:3px; font-weight:bold; -webkit-print-color-adjust: exact;">{amount_num} ({amount_words})</span>'

    html_content = f"""
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            * {{
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
                box-sizing: border-box;
            }}
            
            body {{
                font-family: Arial, Helvetica, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #ffffff;
            }}

            .a4-container {{
                width: 100%;
                max-width: 800px;
                margin: 0 auto;
                background: #ffffff;
                border: 1px solid #ddd;
            }}

            .content-wrapper {{
                padding: 20px;
            }}

            @media print {{
                .no-print {{
                    display: none !important;
                }}
                .a4-container {{
                    border: none !important;
                    width: 100% !important;
                    max-width: 100% !important;
                }}
            }}
        </style>
    </head>
    <body>
        <!-- Print Button Always Visible -->
        <div class="no-print" style="margin-bottom: 12px; position: sticky; top: 0; background: #fff; z-index: 99; padding: 5px 0;">
            <button onclick="window.print()" style="background-color:#0052cc; color:white; border:none; padding:12px 20px; font-size:15px; border-radius:6px; cursor:pointer; font-weight:bold; width: 100%; max-width: 250px;">
                🖨️ Download / Print PDF
            </button>
        </div>
        
        <div class="a4-container">
            <!-- Header -->
            <div style="background: linear-gradient(135deg, #002b80, #0052cc) !important; color:white !important; padding:18px 20px; border-bottom: 4px solid #ff9900;">
                <div style="display:flex; justify-content:space-between; font-size:11px; font-weight:bold;">
                    <span style="border:1px solid rgba(255,255,255,0.5); padding:2px 6px; border-radius:10px;">GSTIN: 10CJAPK9167R1ZQ</span>
                    <span>📞 +91 8541887622</span>
                </div>
                <h1 style="margin:10px 0 5px 0; text-align:center; font-size:24px; color:#ffffff !important; letter-spacing:1px; font-weight:800;">KOSHI ENTERPRISES</h1>
                <div style="display:flex; justify-content:space-between; font-size:10px; margin-top:6px;">
                    <span>📍 Sukhasan Uttarwari, Ward No.- 07, Near Kali Sthan, Madhepura, Bihar - 852113</span>
                    <span>✉️ chandrasukhasan@gmail.com</span>
                </div>
            </div>

            <div class="content-wrapper">
                <!-- Patrank & Date -->
                <div style="display:flex; justify-content:space-between; font-size:13.5px; margin-top:5px;">
                    <p style="margin:0;"><b>पत्रांक :-</b> {patrank}</p>
                    <p style="margin:0;"><b>दिनांक :-</b> {tarikh}</p>
                </div>
                
                <!-- Address -->
                <p style="font-size:13.5px; margin-top:18px; line-height:1.5;"><b>सेवा में,</b><br>{seva_me.replace('\n', '<br>')}</p>
                
                <!-- Subject Box -->
                <div style="background-color:#f0f4f9 !important; padding:10px 12px; border-left:4px solid #0052cc; border-radius:4px; font-size:13px; margin:18px 0; line-height:1.5;">
                    <b>विषय :- {vishay}</b>
                </div>
                
                <!-- Body -->
                <p style="font-size:13.5px; margin-bottom:8px;"><b>महाशय,</b></p>
                <p style="line-height:1.7; font-size:13.5px; margin-top:0; text-align:justify;">{patra_vivran.replace('\n', '<br>')}</p>
                
                <p style="line-height:1.7; font-size:13.5px; text-align:justify;">
                    उक्त सामग्रियों की आपूर्ति के पश्चात कुल व्यय राशि {highlighted_amount} का बिल भुगतान हेतु तैयार किया गया है। सामग्रियों की विवरणी एवं मूल विपत्र (Original Bill) इस आवेदन के साथ संलग्न है।
                </p>
                
                <p style="line-height:1.7; font-size:13.5px; text-align:justify;">
                    अतः श्रीमान से विनम्र प्रार्थना है कि सामग्रियों के सत्यापन उपरांत कोशी इंटरप्राइजेज, मधेपुरा को कुल राशि {highlighted_amount} के भुगतान की स्वीकृति प्रदान करने की कृपा की जाए। इसके लिए हम सदैव आपके आभारी रहेंगे।
                </p>

                <!-- Bank Details & Signature -->
                <div style="display:flex; justify-content:space-between; align-items:flex-end; margin-top:25px;">
                    <div style="background-color:#f8f9fa !important; border:1px solid #dce4ec; border-radius:6px; padding:10px 12px; width:56%;">
                        <h4 style="margin:0 0 8px 0; color:#0052cc !important; font-size:13px;">🏦 भुगतान हेतु बैंक विवरण (Bank Details)</h4>
                        <table style="font-size:11.5px; width:100%; border-collapse:collapse; line-height:1.5;">
                            <tr><td style="width:40%;"><b>बैंक का नाम:</b></td><td><b>HDFC MADHEPURA</b></td></tr>
                            <tr><td><b>खाता संख्या:</b></td><td><b>50200099372362</b></td></tr>
                            <tr><td><b>आईएफएससी कोड:</b></td><td><b>HDFC0002353</b></td></tr>
                        </table>
                    </div>
                    
                    <div style="text-align:center; font-size:13px; width:38%;">
                        <p style="margin-bottom:40px;"><b>विश्वासभाजन</b></p>
                        <p style="margin:0; font-weight:bold; font-size:13.5px;">कोशी इंटरप्राइजेज</p>
                        <p style="margin:2px 0 0 0; font-size:11px; color:#555;">मधेपुरा (बिहार)</p>
                    </div>
                </div>
            </div>
            
            <!-- Footer Strip -->
            <div style="background-color:#001a4d !important; color:white !important; text-align:center; padding:8px; font-size:10px;">
                KOSHI ENTERPRISES • Sukhasan Uttarwari, Ward No. 07, Madhepura, Bihar - 852113
            </div>
        </div>
    </body>
    </html>
    """
    st.components.v1.html(html_content, height=850, scrolling=True)
