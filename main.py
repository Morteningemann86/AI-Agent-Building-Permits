import os
from dotenv import load_dotenv
import openai
import pandas as pd

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

class BuildingPermitAgent:
    def __init__(self, drawings_folder):
        self.drawings_folder = drawings_folder
        self.drawings_data = self.load_drawings_data()

    def load_drawings_data(self):
        drawings_data = []
        for filename in os.listdir(self.drawings_folder):
            file_path = os.path.join(self.drawings_folder, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as f:
                    drawings_data.append(f.read())
        return drawings_data

    def process_application(self, application_date):
        prompt = f"""
        You are a building permit agent.
        You are given an application date and technical drawings.
        You are to determine if the application is valid or not.
        The application is valid if it is submitted between Monday and Friday.
        The application is not valid if it is submitted on Saturday or Sunday.
        The application date is {application_date}.
        The technical drawings are:
        {'\n'.join(self.drawings_data)}
        """
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0].text.strip()
