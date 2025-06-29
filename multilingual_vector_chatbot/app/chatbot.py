from openai import OpenAI

client = OpenAI()

def generate_answer(question, context_list):
    context_text = "\n".join([f"- {item['text']}" for item in context_list])
    prompt = f"""
Answer the following question using the provided context.

Context:
{context_text}

Question: {question}
Answer:
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

