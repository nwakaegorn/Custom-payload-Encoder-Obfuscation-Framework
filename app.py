import streamlit as st
from encoder import PayloadEncoder
from obfuscator import PayloadObfuscator
from decoder import PayloadDecoder

# -----------------------------
# Page Title
# -----------------------------
st.set_page_config(
    page_title="Custom Payload Encoder & Obfuscation Framework",
    layout="centered"
)

st.title("Custom Payload Encoder & Obfuscation Framework")

st.write(
    "Encode, obfuscate, and decode payloads securely."
)

# -----------------------------
# User Input
# -----------------------------
payload = st.text_area(
    "Enter Payload",
    height=150
)

# -----------------------------
# Process Button
# -----------------------------
if st.button("Process Payload"):

    if payload.strip() == "":
        st.warning("Please enter a payload")

    else:

        try:
            encoder = PayloadEncoder()
            obfuscator = PayloadObfuscator()
            decoder = PayloadDecoder()

            # Encode
            encoded = encoder.multi_layer_encode(payload)

            # Obfuscate
            obfuscated = obfuscator.reverse_string(encoded)

            # Restore
            restored = obfuscator.reverse_string(obfuscated)

            # Decode
            decoded = decoder.multi_layer_decode(restored)

            # -----------------------------
            # Results
            # -----------------------------
            st.success("Payload Processed Successfully")

            st.subheader("Encoded Payload")
            st.code(encoded)

            st.subheader("Obfuscated Payload")
            st.code(obfuscated)

            st.subheader("Decoded Payload")
            st.code(decoded)

        except Exception as e:

            st.error(f"Error: {str(e)}")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.write("System running successfully")
