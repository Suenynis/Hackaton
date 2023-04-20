import openai

def generate_text(prompt):
    openai.api_key = "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"
    model_engine = "davinci"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()
