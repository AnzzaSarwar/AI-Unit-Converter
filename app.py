<<<<<<< HEAD
import streamlit as st
import pint
import google.generativeai as genai

# ✅ Directly set your Gemini API key
api_key = "AIzaSyDNnnGBPKWbpMnYw74mW9X4hmyO3iTlPAw"
genai.configure(api_key=api_key)

# Initialize Pint for unit conversion
ureg = pint.UnitRegistry()

# Function to convert units
def convert_units(value, from_unit, to_unit):
    try:
        result = (value * ureg(from_unit.lower())).to(to_unit.lower())
        return f"{value} {from_unit} = {result}"
    except pint.DimensionalityError:
        return "❌ Invalid conversion"
    except Exception:
        return "⚠️ Please enter a valid numeric value and unit names."

# Function to interact with Gemini AI
def ask_gemini(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text if response else "Error fetching response"

# Page configuration
st.set_page_config(page_title="Gemini Unit Converter", page_icon="♾️", layout="wide")

# Custom styling
st.markdown("""
    <style>
        body {
            background-color: #ffe6f0;
        }
        .block-container {
            background-color: #ffe6f0;
        }
        .stTextInput, .stNumberInput, .stTextArea {
            border-radius: 10px;
            padding: 10px;
            background-color: #fff0f5;
            color: #000000;
        }
        .stButton>button {
            background-color: #cc3366;
            color: white;
            border-radius: 10px;
            padding: 0.5em 1em;
        }
        .stButton>button:hover {
            background-color: #b30059;
            color: #ffffff;
        }
        section[data-testid="stSidebar"] {
            background-color: #ffccdd;
            color: #660033;
            padding: 20px;
            border-radius: 0 15px 15px 0;
        }
        .stRadio > div {
            background-color: #ffe6f0;
            border-radius: 10px;
            padding: 5px;
        }
        .css-1d391kg {
            background-color: #cc3366 !important;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🎀 Settings")
st.sidebar.markdown("Effortlessly transform your **UNITS🔮**")
mode = st.sidebar.radio("Select Options:", ["Unit Converter", "AI Assistant", "Units & Conversions Table"])

# Title
st.title("🌸 Gemini-Powered Unit Converter")
st.write("Easily convert units and ask AI-powered questions!")

# Unit Converter Section
if mode == "Unit Converter":
    st.subheader("🔮 Unit Converter")
    
    st.markdown("**Enter the details below to convert units effortlessly!**")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        value = st.text_input("🔢 Enter value:", placeholder="e.g., 10")
    
    with col2:
        from_unit = st.text_input("📏 From unit:", placeholder="e.g., meters")
    
    with col3:
        to_unit = st.text_input("🔄 To unit:", placeholder="e.g., feet")
    
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    if st.button("🚀 Convert Now", use_container_width=True):
        if value and from_unit and to_unit:
            try:
                value = float(value)
                result = convert_units(value, from_unit, to_unit)
                st.success(f"✅ {result}")
            except ValueError:
                st.error("❌ Please enter a valid numeric value.")
        else:
            st.warning("⚠️ Please fill in all fields correctly.")
    st.markdown("</div>", unsafe_allow_html=True)

# AI Assistant Section
elif mode == "AI Assistant":
    st.subheader("🧠 AI Assistant")

    st.markdown("""
        <style>
            .ai-container {
                background-color: #cc3366;
                padding: 10px;
                border-radius: 10px;
                color: white;
                text-align: center;
                box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
            }
            .ai-input {
                width: 100%;
                padding: 10px;
                border-radius: 5px;
                border: none;
                background-color: #ffe6f0;
                color: #000000;
            }
            .ai-button {
                background-color: #ff6699;
                color: white;
                padding: 10px;
                border-radius: 5px;
                border: none;
                cursor: pointer;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='ai-container'>", unsafe_allow_html=True)
    st.markdown("💬 **Ask anything, and AI will assist you!**")
    user_query = st.text_area("", placeholder="Type your question here...", height=100)

    if st.button("🚀 Get Answer", use_container_width=True):
        if user_query:
            ai_response = ask_gemini(user_query)
            st.success(f"🤖 {ai_response}")
        else:
            st.error("⚠️ Please enter a question.")
    st.markdown("</div>", unsafe_allow_html=True)

# Units & Conversions Table Section
elif mode == "Units & Conversions Table":
    st.subheader("📏 Common Units & Conversions")
    st.write("A quick reference guide for unit conversions.")
    
    conversion_data = {
        "Length": ["1 meter = 3.281 feet", "1 kilometer = 0.621 miles"],
        "Weight": ["1 kilogram = 2.205 pounds", "1 gram = 0.035 ounces"],
        "Temperature": ["0°C = 32°F", "100°C = 212°F"],
        "Volume": ["1 liter = 4.227 cups", "1 gallon = 3.785 liters"],
    }
    
    for category, conversions in conversion_data.items():
        with st.expander(f"📌 {category}"):
            for conversion in conversions:
                st.write(f"🔹 {conversion}")

# Footer
st.markdown("---")
st.markdown("💖 Developed by **Anza Sarwar** | Powered by **Gemini AI & Streamlit**")
=======
import streamlit as st
import pint
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini AI
genai.configure(api_key=api_key)

# Initialize Pint for unit conversion
ureg = pint.UnitRegistry()

# Function to convert units
def convert_units(value, from_unit, to_unit):
    try:
        result = (value * ureg(from_unit.lower())).to(to_unit.lower())
        return f"{value} {from_unit} = {result}"
    except pint.DimensionalityError:
        return "❌ Invalid conversion"
    except Exception:
        return "⚠️ Please enter a valid numeric value and unit names."

# Function to interact with Gemini AI
def ask_gemini(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text if response else "Error fetching response"

# Page configuration
st.set_page_config(page_title="Gemini Unit Converter", page_icon="♾️", layout="wide")

# Custom styling
st.markdown("""
    <style>
        body {
            background-color: #ffe6f0;
        }
        .block-container {
            background-color: #ffe6f0;
        }
        .stTextInput, .stNumberInput, .stTextArea {
            border-radius: 10px;
            padding: 10px;
            background-color: #fff0f5;
            color: #000000;
        }
        .stButton>button {
            background-color: #cc3366;
            color: white;
            border-radius: 10px;
            padding: 0.5em 1em;
        }
        .stButton>button:hover {
            background-color: #b30059;
            color: #ffffff;
        }
        /* Sidebar styling */
        section[data-testid="stSidebar"] {
            background-color: #ffccdd;
            color: #660033;
            padding: 20px;
            border-radius: 0 15px 15px 0;
        }
        .stRadio > div {
            background-color: #ffe6f0;
            border-radius: 10px;
            padding: 5px;
        }
        .css-1d391kg {
            background-color: #cc3366 !important;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🎀 Settings")
st.sidebar.markdown("Effortlessly transform your **UNITS🔮**")
mode = st.sidebar.radio("Select Options:", ["Unit Converter", "AI Assistant", "Units & Conversions Table"])

# Title
st.title("🌸 Gemini-Powered Unit Converter")
st.write("Easily convert units and ask AI-powered questions!")

# Unit Converter Section
if mode == "Unit Converter":
    st.subheader("🔮 Unit Converter")
    
    st.markdown("**Enter the details below to convert units effortlessly!**")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        value = st.text_input("🔢 Enter value:", placeholder="e.g., 10")
    
    with col2:
        from_unit = st.text_input("📏 From unit:", placeholder="e.g., meters")
    
    with col3:
        to_unit = st.text_input("🔄 To unit:", placeholder="e.g., feet")
    
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    if st.button("🚀 Convert Now", use_container_width=True):
        if value and from_unit and to_unit:
            try:
                value = float(value)
                result = convert_units(value, from_unit, to_unit)
                st.success(f"✅ {result}")
            except ValueError:
                st.error("❌ Please enter a valid numeric value.")
        else:
            st.warning("⚠️ Please fill in all fields correctly.")
    st.markdown("</div>", unsafe_allow_html=True)

# AI Assistant Section
elif mode == "AI Assistant":
    st.subheader("🧠 AI Assistant")

    st.markdown("""
        <style>
            .ai-container {
                background-color: #cc3366;
                padding: 10px;
                border-radius: 10px;
                color: white;
                text-align: center;
                box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
            }
            .ai-input {
                width: 100%;
                padding: 10px;
                border-radius: 5px;
                border: none;
                background-color: #ffe6f0;
                color: #000000;
            }
            .ai-button {
                background-color: #ff6699;
                color: white;
                padding: 10px;
                border-radius: 5px;
                border: none;
                cursor: pointer;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='ai-container'>", unsafe_allow_html=True)
    st.markdown("💬 **Ask anything, and AI will assist you!**")
    user_query = st.text_area("", placeholder="Type your question here...", height=100)

    if st.button("🚀 Get Answer", use_container_width=True):
        if user_query:
            ai_response = ask_gemini(user_query)
            st.success(f"🤖 {ai_response}")
        else:
            st.error("⚠️ Please enter a question.")
    st.markdown("</div>", unsafe_allow_html=True)

# Units & Conversions Table Section
elif mode == "Units & Conversions Table":
    st.subheader("📏 Common Units & Conversions")
    st.write("A quick reference guide for unit conversions.")
    
    conversion_data = {
        "Length": ["1 meter = 3.281 feet", "1 kilometer = 0.621 miles"],
        "Weight": ["1 kilogram = 2.205 pounds", "1 gram = 0.035 ounces"],
        "Temperature": ["0°C = 32°F", "100°C = 212°F"],
        "Volume": ["1 liter = 4.227 cups", "1 gallon = 3.785 liters"],
    }
    
    for category, conversions in conversion_data.items():
        with st.expander(f"📌 {category}"):
            for conversion in conversions:
                st.write(f"🔹 {conversion}")

# Footer
st.markdown("---")
st.markdown("💖 Developed by **Anza Sarwar** | Powered by **Gemini AI & Streamlit**")
>>>>>>> 8cdb7b52c61d0fe015b919990503c702109aec94
