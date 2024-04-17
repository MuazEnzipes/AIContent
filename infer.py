"""
This code a slight modification of perplexity by hugging face
https://huggingface.co/docs/transformers/perplexity

Both this code and the orignal code are published under the MIT license.

by Burhan Ul tayyab and Nicholas Chua
"""

from model import GPT2PPLV2 as GPT2PPL

# initialize the model
model = GPT2PPL()

sentence = "In the bustling city, people rush about their daily routines with purpose. The morning sun shines brightly, casting a warm glow over the skyscrapers. Birds chirp cheerfully, and the streets fill with the sounds of traffic."

model(sentence, 100, "v1.1")
