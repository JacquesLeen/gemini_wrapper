#!/usr/bin/env python3

"""
CLI to to submit question and interact with Gemini 2.5
"""

import os
import click
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_SECRET"))


# define main function to call the bot
def question(text: str):
    """Function to send a question to Gemini 2.5 and get a response."""
    response = client.models.generate_content(model="gemini-2.5-flash", contents=text)
    return response.text


# make a click command line interface
@click.command()
@click.option("--text", required=True, help="Text to generate content for.")
def cli(text):
    """CLI to interact with Gemini 2.5."""
    result = question(text)
    print("Generated Content:")
    print(result)


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter


