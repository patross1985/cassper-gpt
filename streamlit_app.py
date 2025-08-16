import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# Set page configuration
st.set_page_config(page_title="Cassper GPT", layout="wide")

MENU_ITEMS = [
    "Chat GPT",
    "Evidence Vault",
    "Timeline",
    "Violation Scanner",
    "Document Builder",
    "FOIP Tools",
    "Alberta Forms",
    "Settings"
]

st.sidebar.title("Cassper GPT")
choice = st.sidebar.radio("Menu", MENU_ITEMS)

st.title(choice)

if choice == "Chat GPT":
    st.write("This page would integrate with OpenAI's GPT API to provide chat functionality.")
elif choice == "Evidence Vault":
    st.write("Upload and manage evidence securely here.")
elif choice == "Timeline":
    st.write("Visualize case timelines and significant events.")
elif choice == "Violation Scanner":
    st.write("Scan documents for potential legal violations.")
elif choice == "Document Builder":
    st.write("Generate legal documents and templates.")
elif choice == "FOIP Tools":
    st.write("Tools for Freedom of Information and Protection requests.")
elif choice == "Alberta Forms":
    st.write("Access Alberta-specific legal forms.")
elif choice == "Settings":
    st.write("Configure application settings.")
