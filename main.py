import langchain_helper as lch
import streamlit as st

st.title("Pet Name Generator")

animal_type = st.sidebar.selectbox(
    "Select the type of animal", ["cat", "dog", "bird", "fish", "hen", "rabbit", "cow"]
)

# Універсальна логіка для вибору кольору залежно від типу тварини
pet_color = st.sidebar.selectbox(
    f"Select the color of the {animal_type}",
    ["black", "white", "gray", "brown", "orange", "yellow"],
)

# Отримання результату за допомогою функції з langchain_helper
names, character, final_tagline = lch.generate_pet_name(animal_type, pet_color)

# Виведення результату у читабельній формі
st.subheader(f"Here are some cool names for your {animal_type}:")
st.markdown(f"**{names}**")

st.subheader("Personality of your pet:")
st.markdown(f"*{character}*")

st.subheader("Cool tagline for your pet:")
st.markdown(f"**{final_tagline}**")
