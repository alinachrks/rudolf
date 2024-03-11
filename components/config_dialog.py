# config.py
import os

TIMEOUT = 60
N_RETRIES = 3
COOLDOWN = 2
BACKOFF = 1.5

INITIAL_PROMPT = "In the style of a snobbish, individualistic, intellectual and very curious analytical hamster. You can respond with wit and irony in the same language in which people address you. You should always assume the character of the Glass family from the works of Salinger. You use that the language in which you are addressed."
PRE_SUMMARY_PROMPT = "The above is the conversation so far between you, the hamster analyst, and a human user. Please summarize the discussion for your own reference in the next message. Do not write a reply to the user or generate prompts, just write the summary."
PRE_SUMMARY_NOTE = "Before the most recent messages, here's a summary of the conversation so far:"
POST_SUMMARY_NOTE = "The summary ends. And here are the most recent two messages from the conversation. You should generate the next response based on the conversation so far."

NLP_MODEL_NAME = "gpt-3.5-turbo-0125"
NLP_MODEL_ENGINE = os.getenv("OPENAI_ENGINE", None)
NLP_MODEL_MAX_TOKENS = 4000
NLP_MODEL_REPLY_MAX_TOKENS = 1000
NLP_MODEL_TEMPERATURE = 0.8
NLP_MODEL_FREQUENCY_PENALTY = 1
NLP_MODEL_PRESENCE_PENALTY = 1
NLP_MODEL_STOP_WORDS = ["Human:", "AI:"]
