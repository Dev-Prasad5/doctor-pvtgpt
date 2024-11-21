import streamlit as st
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import json

# Load the fine-tuned GPT-2 model and tokenizer
model = GPT2LMHeadModel.from_pretrained("./fine_tuned_gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("./fine_tuned_gpt2")

# Load doctors data
with open('doctors_data.json', 'r', encoding='utf-8') as f:
    doctors_data = json.load(f)

# Helper function to find doctors by specialty
def get_doctors_by_specialty(specialty):
    matching_doctors = [doctor['name'] for doctor in doctors_data if specialty.lower() in doctor['specialty'].lower()]
    return matching_doctors

# Function to extract specialty from the prompt
def extract_specialty_from_prompt(prompt):
    specialty_mapping = {
        'bones': 'orthopedics',
        'heart': 'cardiology',
        'plastic surgery': 'plastic surgery',
        'cardiologist': 'cardiology',
        'dermatology': 'dermatology',
        'pediatrics': 'pediatrics',
        'neurology': 'neurology',
        'general medicine': 'general medicine',
        'dentist': 'dentistry',
        'orthopedics': 'orthopedics'
    }

    prompt_lower = prompt.lower()
    for keyword, specialty in specialty_mapping.items():
        if keyword in prompt_lower:
            return specialty
    return None

# Streamlit App
st.title("Doctor Private-GPT")
st.write("Ask a question related to doctors or specialties.")

# Initialize session state for chat history if not already initialized
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Input from the user
user_input = st.text_input("Ask a question (e.g., 'Who treats Heart?'):") 

# Display result and maintain chat history
if user_input:
    specialty = extract_specialty_from_prompt(user_input)
    
    if specialty:
        doctors = get_doctors_by_specialty(specialty)
        if doctors:
            doctors_list = '\n'.join(f"{idx+1}. {doctor}" for idx, doctor in enumerate(doctors))
            bot_response = f"Doctors specializing in {specialty.capitalize()}:\n{doctors_list}"
        else:
            bot_response = f"No doctors found specializing in {specialty}. Please try a different specialty."
    else:
        bot_response = "Could not detect the specialty from your query. Please try asking with specific terms like 'plastic surgery', 'dermatology', etc."

    # Add user input and bot response to the chat history
    st.session_state.chat_history.append(f"**You:** {user_input}")
    st.session_state.chat_history.append(f"**Bot:** {bot_response}")

    # Limit history to the last 5 interactions
    if len(st.session_state.chat_history) > 10:
        st.session_state.chat_history = st.session_state.chat_history[-10:]

# Display the chat history in reverse order (most recent first)
for message in reversed(st.session_state.chat_history):
    st.markdown(message)
