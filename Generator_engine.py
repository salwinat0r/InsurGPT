import openai
openai.api_key = open("key.txt", 'r').read().strip('\n')


def generate_response(prompt):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a professional Insurance Agent in India"},
        {"role": "user", "content": prompt},
    ])
    response = completion["choices"][0]["message"]['content']
    return response

# completion = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#         {"role": "system", "content": "You are a professional Insurance Agent in India"},
#         {"role": "user", "content": "How much compensation can I get if my Car is dented from the bonet?"},
#     ] 
# )

# reply_content = completion["choices"][0]["message"]
# print(reply_content)