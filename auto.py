import openai
import asyncio
import re
import whisper
import boto3
import pydub
from pydub import playback
import speech_recognition as sr
from EdgeGPT import Chatbot, ConversationStyle

openai.api_key = "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"

async def main():
    bot = Chatbot(cookiePath='cookies.json')

    # Prompt the user for a topic
    topic = input("Please enter a topic: ")

    # Use the bot to generate questions on the given topic
    response = await bot.ask(prompt=f"Generate questions on {topic}", conversation_style=ConversationStyle.precise)

    # Analyze the response and generate suggested questions for each question
    questions = []
    for message in response["item"]["messages"]:
        if message["author"] == "bot":
            question = message["text"].replace('\n', '')
            if len(question) > 0:
                # Use the bot to generate a response to the question
                response = await bot.ask(prompt=question, conversation_style=ConversationStyle.precise)

                # Analyze the response to generate suggested questions
                analyzed_response = analyze_response(response["item"]["messages"][-1]["text"])
                suggested_questions = generate_suggested_questions(analyzed_response)

                # Display the suggested questions to the user
                print(f"Question: {question}")
                print("Suggested questions:")
                for i, suggested_question in enumerate(suggested_questions):
                    print(f"{i+1}. {suggested_question}")

                # Allow the user to select one of the suggested questions
                selected_question = select_question(suggested_questions)

                # Add the selected question to the list of questions
                questions.append(selected_question)

                if len(questions) == 3:
                    break

    # Display the selected questions to the user
    print("Here are the selected questions:")
    for i, question in enumerate(questions):
        print(f"{i+1}. {question}")

    await bot.close()

def analyze_response(response_text):
    # Remove citations and other text that may not be relevant to the answer
    clean_text = re.sub('\[\^\d+\^\]', '', response_text)

    # Use OpenAI's GPT-3 API to analyze the text and extract keywords
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Analyze the following text and extract relevant keywords:\n\n{clean_text}\n\nKeywords:",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the keywords from the response
    keywords = [choice.text for choice in response.choices[0].text.split("\n") if len(choice.text) > 0]

    return keywords

def generate_suggested_questions(keywords):
    # Use OpenAI's GPT-3 API to generate suggested questions based on the keywords
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Generate 3 suggested questions based on the following keywords:\n\n{', '.join(keywords)}\n\nSuggested questions:",
        max_tokens=100,
        n=3,
        stop=None,
        temperature=0.5,
    )

    # Extract the suggested questions from the response
    suggested_questions = [choice.text.strip() for choice in response.choices[0].text.split("\n") if len(choice.text) > 0]

    return suggested_questions


if __name__ == "__main__":
    asyncio.run(main())
