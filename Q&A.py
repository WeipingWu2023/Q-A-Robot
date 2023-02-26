import openai

openai.api_key = "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"

start_sequence = "\nA:"
restart_sequence = "\n\nQ: "

print("\tHi 主人， 我是您的智能问答机器人，我会尽我所能回答您的问题!\n")

while 1==1:
    prompt = input(restart_sequence)
    if prompt == 'quit':
        break
    else:
        response = openai.Completion.create(
          model="text-davinci-003",
          prompt = prompt,
          temperature=0,
          max_tokens=100,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0,
        )

        print(start_sequence,response["choices"][0]["text"].strip())
