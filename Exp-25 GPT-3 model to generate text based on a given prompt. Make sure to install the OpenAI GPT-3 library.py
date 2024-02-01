import os
import openai
os.environ["OPENAI_API_KEY"] = "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"
def generate_text(prompt):
    openai.api_key = os.environ['OPENAI_API_KEY']
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1000,
        temperature=0.7,
    )
    generated_text = response["choices"][0]["text"]
    return generated_text
prompt = "Write a haiku about a sunset."
generated_text = generate_text(prompt)
print(generated_text)
