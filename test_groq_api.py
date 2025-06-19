import openai

openai.api_key = "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"
openai.api_base = "https://openrouter.ai/api/v1"  # Required

response = openai.ChatCompletion.create(
    model="meta-llama/llama-3-70b-instruct",  # or llama-3-8b-instruct
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Summarize this journal entry..."}
    ]
)

print(response['choices'][0]['message']['content'])
