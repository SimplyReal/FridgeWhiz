# recipe_model.py
import os
import base64
from openai import OpenAI

# Set your Nebius API key
os.environ["NEBIUS_API_KEY"] = "eyJhbGciOiJIUzI1NiIsImtpZCI6IlV6SXJWd1h0dnprLVRvdzlLZWstc0M1akptWXBvX1VaVkxUZlpnMDRlOFUiLCJ0eXAiOiJKV1QifQ.eyJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMzgyNzc1NDk0NTQ5NDQ1NjU1MSIsInNjb3BlIjoib3BlbmlkIG9mZmxpbmVfYWNjZXNzIiwiaXNzIjoiYXBpX2tleV9pc3N1ZXIiLCJhdWQiOlsiaHR0cHM6Ly9uZWJpdXMtaW5mZXJlbmNlLmV1LmF1dGgwLmNvbS9hcGkvdjIvIl0sImV4cCI6MTkwMDM5MjI2NCwidXVpZCI6IjIwZGU4ZDFkLTVmMTQtNDUwNC1iNDY0LTUyMzE1OWNkZjRhNSIsIm5hbWUiOiJORUJJVVNfQVBJX0tFWSIsImV4cGlyZXNfYXQiOiIyMDMwLTAzLTIyVDA2OjQ0OjI0KzAwMDAifQ.W2x5McNJiZa1Rux6zesKd7peIFE_6aebQ4ye3iVdw38"

# Initialize Nebius API client
client = OpenAI(
    base_url="https://api.studio.nebius.com/v1/",
    api_key=os.environ.get("NEBIUS_API_KEY")
)

def extract_ingredients(image_path):
    """Extract ingredients from an image using the Qwen model."""
    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    # Prompt to extract ingredients
    prompt = "List all the ingredients visible in the image. Be detailed and accurate."

    # Send image + prompt to Qwen2 model
    response = client.chat.completions.create(
        model="Qwen/Qwen2-VL-72B-Instruct",
        max_tokens=500,
        temperature=0.7,
        top_p=0.9,
        presence_penalty=0.3,
        extra_body={"top_k": 50},
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}},
                ],
            }
        ],
    )

    # Return the detected ingredients
    return response.choices[0].message.content

def generate_recipes(ingredients_text, filters):
    """Generate recipes based on extracted ingredients and user filters."""
    # Create prompt automatically
    prompt = f"""
    You are a helpful AI chef. Using only the following ingredients:
    {ingredients_text}

    Suggest 3 simple and creative meal ideas or recipes I can make. Include basic steps and use only these ingredients.
    Apply the following filters: {', '.join(filters)}.

    For each recipe:
    1. Provide a creative name.
    2. List the ingredients.
    3. Write step-by-step instructions.
    4. Estimate the total cooking time (in minutes).
    5. Estimate the total calories per serving.
    """

    # Send to model
    response = client.chat.completions.create(
        model="Qwen/Qwen2-VL-72B-Instruct",
        max_tokens=700,
        temperature=0.7,
        top_p=0.9,
        presence_penalty=0.3,
        extra_body={"top_k": 50},
        messages=[{"role": "user", "content": prompt}],
    )

    # Return the generated recipes
    return response.choices[0].message.content