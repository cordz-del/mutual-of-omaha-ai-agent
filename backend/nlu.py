import openai

openai.api_key = "YOUR_API_KEY"

def interpret_query(message):
    prompt = f"Identify intent and entities: {message}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
