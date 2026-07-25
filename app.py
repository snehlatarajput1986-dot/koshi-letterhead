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
        <style>
            /* Force print to show all background colors and graphics */
            * {{
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }}
            
            @media print {{
                body * {{
                    visibility: hidden;
                }}
                #printable-letter, #printable-letter * {{
                    visibility: visible;
                }}
                #printable-letter {{
                    position: absolute;
                    left: 0;
                    top: 0;
                    width: 100%;
                    border: none !important;
                }}
                .no-print {{
                    display: none !important;
                }}
            }}
        </style>
    </head>
    <body style="font-family:sans-serif; margin:0; padding:0; background-color:#fff;">
        <div class="no-print" style="margin-bottom: 10px;">
            <button onclick="window.print()" style="background-color:#0052cc; color:white; border:none; padding:10px 20px; font-size:14px; border-radius:5px; cursor:pointer; font-weight:bold;">
                🖨️ Download / Print PDF
            </button>
        </div>
        
        <div id="printable-letter" style="border:1px solid #ddd; padding:0; background-color:#fff; color:#000;">
            <!-- Vibrant Blue Header -->
            <div style="background: linear-gradient(135deg, #002b80, #0052cc) !important; color:white !important; padding:20px; border-bottom: 4px solid #ff9900;">
                <div style="display:flex; justify-content:space-between; font-size:11px; font-weight:bold;">
                    <span style="border:1px solid rgba(255,255,255,0.4); padding:2px 8px; border-radius:10px;">GSTIN: 10CJAPK9167R1ZQ</span>
                    <span>📞 +91 8541887622</span>
                </div>
                <h1 style="margin:10px 0 5px 0; text-align:center; font-size:28px; color:#ffffff !important; letter-spacing:1.5px; font-weight:800;">KOSHI ENTERPRISES</h1>
                <div style="display:flex; justify-content:space-between; font-size:10px; margin-top:8px;">
                    <span>📍 Sukhasan Uttarwari, Ward No.- 07, Near Kali Sthan, Madhepura, Bihar - 852113</span>
                    <span>✉️ chandrasukhasan@gmail.com</span>
                </div>
            </div>

            <div style="padding:20px;">
                <!-- Patrank & Date -->
                <div style="display:flex; justify-content:space-between; font-size:14px; margin-top:10px;">
                    <p><b>पत्रांक :-</b> {patrank}</p>
                    <p><b>दिनांक :-</b> {tarikh}</p>
                </div>
                
                <!-- Address -->
                <p style="font-size:14px; margin-top:15px;"><b>सेवा में,</b><br>{seva_me.replace('\n', '<br>')}</p>
                
                <!-- Subject -->
                <div style="background-color:#f0f4f9 !important; padding:12px; border-left:5px solid #0052cc; border-radius:4px; font-size:14px; margin:20px 0;">
                    <b>विषय :- {vishay}</b>
                </div>
                
                <!-- Body -->
                <p style="font-size:14px;"><b>महाशय,</b></p>
                <p style="line-height:1.7; font-size:14px;">{patra_vivran.replace('\n', '<br>')}</p>
                
                <p style="line-height:1.7; font-size:14px;">
                    उक्त सामग्रियों की आपूर्ति के पश्चात कुल व्यय राशि {highlighted_amount} का बिल भुगतान हेतु तैयार किया गया है। सामग्रियों की विवरणी एवं मूल विपत्र (Original Bill) इस आवेदन के साथ संलग्न है।
                </p>
                
                <p style="line-height:1.7; font-size:14px;">
                    अतः श्रीमान से विनम्र प्रार्थना है कि सामग्रियों के सत्यापन उपरांत कोशी इंटरप्राइजेज, मधेपुरा को कुल राशि {highlighted_amount} के भुगतान की स्वीकृति प्रदान करने की कृपा की जाए। इसके लिए हम सदैव आपके आभारी रहेंगे।
                </p>
                <br>

                <!-- Bank Details & Signature -->
                <div style="display:flex; justify-content:space-between; align-items:flex-end; margin-top:20px;">
                    <div style="background-color:#f8f9fa !important; border:1px solid #dce4ec; border-radius:6px; padding:12px; width:55%;">
                        <h4 style="margin:0 0 8px 0; color:#0052cc !important; font-size:14px;">🏦 भुगतान हेतु बैंक विवरण (Bank Details)</h4>
                        <table style="font-size:12px; width:100%; border-collapse:collapse;">
                            <tr><td style="padding:3px 0;"><b>बैंक का नाम:</b></td><td><b>HDFC MADHEPURA</b></td></tr>
                            <tr><td style="padding:3px 0;"><b>खाता संख्या:</b></td><td><b>50200099372362</b></td></tr>
                            <tr><td style="padding:3px 0;"><b>आईएफएससी कोड:</b></td><td><b>HDFC0002353</b></td></tr>
                        </table>
                    </div>
                    
                    <div style="text-align:center; font-size:13px; width:35%;">
                        <p style="margin-bottom:45px;"><b>विश्वासभाजन</b></p>
                        <p style="margin:0; font-weight:bold;">कोशी इंटरप्राइजेज</p>
                        <p style="margin:0; font-size:11px; color:#555;">मधेपुरा (बिहार)</p>
                    </div>
                </div>
            </div>
            
            <!-- Footer Strip -->
            <div style="background-color:#001a4d !important; color:white !important; text-align:center; padding:8px; font-size:10px; margin-top:30px;">
                KOSHI ENTERPRISES • Sukhasan Uttarwari, Ward No. 07, Madhepura, Bihar - 852113
            </div>
        </div>
    </body>
    </html>
    """
    st.components.v1.html(html_content, height=850, scrolling=True)
