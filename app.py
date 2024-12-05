import streamlit as st
from prompts import generate_prompt
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
print('Successfully connected')

st.title("Recipe Generator 🍳")
st.write("Generate recipes based on the ingredients in your fridge")

# Step 1: User Inputs Ingredients
ingredients = st.text_area("Enter the ingredients you have (comma-separated):", placeholder="e.g., chicken, garlic, onion")

# Step 2: Choose Cuisine Type
cuisine = st.selectbox("Choose a cuisine type:", ["Korean", "Vietnamese", "Japanese", "Chinese", "Italian", "Mexican", "Indian", "Fusion"])

# Generate Recipe Button
if st.button("Generate Recipe"):
    if ingredients and cuisine:
        # Create the prompt
        prompt = generate_prompt(ingredients, cuisine)
        
        try:
            # Call OpenAI GPT Model
            completion = client.chat.completions.create(
                model="gpt-4o-mini",  # Ensure the correct model name is used
                messages=[
                    {"role": "system", "content": "You are a professional chef."},
                    {"role": "user", "content": prompt},
                ]
            )

            # Extract recipe content from the response
            recipe = completion.choices[0].message.content  # Access the `content` attribute directly

            # Display the recipe
            st.subheader("Generated Recipe:")
            st.write(recipe)

        except Exception as e:
            # Handle errors gracefully
            st.error(f"An error occurred while generating the recipe: {e}")
    else:
        st.error("Please enter ingredients and select a cuisine type!")
