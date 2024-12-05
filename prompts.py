def generate_prompt(ingredients, cuisine):
    return f"""
    You are a professional chef specializing in {cuisine} cuisine.
    Based on the following ingredients:
    {ingredients},
    suggest a creative and delicious recipe. Include:
    - A title for the dish
    - Ingredients list
    - Step-by-step cooking instructions.
    """
