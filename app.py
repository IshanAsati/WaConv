import streamlit as st
import json
from io import StringIO
from waconv import parse_chat

st.set_page_config(page_title="WaConv - WhatsApp to JSON", page_icon="💬")

st.title("WaConv 💬")
st.subheader("WhatsApp Chat to JSON Converter")

st.markdown("""
Upload your exported WhatsApp chat `.txt` file below to convert it into a structured JSON format.
""")

uploaded_file = st.file_uploader("Choose a WhatsApp chat export file", type="txt")

if uploaded_file is not None:
    # To read file as string:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    
    try:
        chat_data = parse_chat(stringio)
        
        st.success(f"Successfully parsed {len(chat_data)} messages!")
        
        # Preview
        st.write("### Preview (First 5 messages)")
        st.json(chat_data[:5])
        
        # Convert to JSON string for download
        json_str = json.dumps(chat_data, indent=4, ensure_ascii=False)
        
        st.download_button(
            label="Download JSON",
            data=json_str,
            file_name="whatsapp_chat.json",
            mime="application/json"
        )
        
    except Exception as e:
        st.error(f"Error parsing file: {e}")
