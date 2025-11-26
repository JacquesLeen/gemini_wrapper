#!/usr/bin/env python3

"""
CLI to to submit question and interact with Gemini 2.5 via Vertex AI API.
"""

import os
import click
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_SECRET"))


# define main function to call the bot
def question(text: str):
    response = client.models.generate_content(model="gemini-2.5-flash", contents=text)
    return response.text


# make a click command line interface
@click.command()
@click.option("--text", required=True, help="Text to generate content for.")
def cli(text):
    result = question(text)
    print("Generated Content:")
    print(result)


if __name__ == "__main__":
    cli()


# while True:
#     message = input("> ")
#     if message == "exit":
#         break

#     result = chat.send_message(message)
#     print(result.text)
