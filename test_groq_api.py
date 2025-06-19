from groq import Groq

client = Groq(api_key="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")

try:
    response = client.chat.completions.create(
        model="llama3-8b-8192",  # smaller model for test
        messages=[
            {"role": "user", "content": "Say hello!"}
        ],
        temperature=0.5
    )
    print("✅ Response:")
    print(response.choices[0].message.content)
except Exception as e:
    print("❌ API Error:")
    print(e)
