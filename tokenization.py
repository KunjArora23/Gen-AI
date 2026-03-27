import tiktoken



encoder =tiktoken.encoding_for_model('gpt-4o')

print("Vocab Size ",encoder.n_vocab)

text= "hey my name is Kunj Arora"



tokens=encoder.encode(text)

print("Tokens" ,tokens)

decoded=encoder.decode(tokens)

print("Decoded Text ",decoded)

