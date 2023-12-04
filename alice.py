###############################################################################
#                             CHATBOT                                         #
###############################################################################
# Setup
## for speech-to-text
import speech_recognition as sr

## for text-to-speech
# from gtts import gTTS

import pyttsx3

## for language model
import transformers

## for data
import os
import datetime
import numpy as np


# Build the AI
class ChatBot():
    def __init__(self, name):
        print("--- starting up", name, "---")
        self.name = name

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("listening...")
            audio = recognizer.listen(mic)
        try:
            self.text = recognizer.recognize_google(audio)
            print("me --> ", self.text)
        except:
            print("me -->  ERROR")

    @staticmethod
    def text_to_speech(text):
        print("ai --> ", text)
        speaker = pyttsx3.init()
        newVoiceRate = 145
        voices = speaker.getProperty("voices")
        speaker.setProperty('rate',newVoiceRate)
        speaker.setProperty("voice",voices[2].id)
        speaker.say(text)
        speaker.runAndWait()
        # speaker = gTTS(text=text, lang="en", slow=False)
        # speaker.save("res.mp3")
        # os.system("start res.mp3")  #mac->afplay | windows->start
        # os.remove("res.mp3")

    def wake_up(self, text):
        return True if self.name in text.lower() else False

    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime('%H:%M')


# Run the AI
if __name__ == "__main__":
    
    ai = ChatBot(name="alice")
    nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
    os.environ["TOKENIZERS_PARALLELISM"] = "true"

    while True:
        ai.speech_to_text()

        ## wake up
        if ai.wake_up(ai.text) is True:
            res = "Hello I am Alice the AI, what can I do for you?"
        
        ## action time
        elif "time" in ai.text:
            res = ai.action_time()
        
        ## respond politely
        elif any(i in ai.text for i in ["thank","thanks"]):
            res = np.random.choice(["you're welcome!","anytime!","no problem!","cool!","I'm here if you need me!","peace out!"])
        
        ## conversation
        else:   
            chat = nlp(transformers.Conversation(ai.text), pad_token_id=50256)
            # chat = "I am AI"
            res = str(chat)
            res = res[res.find("bot >> ")+6:].strip()

        ai.text_to_speech(res)