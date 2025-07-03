import os
from dotenv import load_dotenv
import google.generativeai as genai
from google.generativeai import types

# load env
load_dotenv()
api_key = os.environ.get('GOOGLE_API_KEY')
genai.configure(api_key=api_key)
MODEL_ID = "gemini-2.0-flash-001"

# read the task from the file
def read_tasks(filepath):
    with open(filepath, 'r') as file:  #new mode to read files in python from 3.6 onwards
        return file.read()





#make a call to openai with prompt to catergorize out tasks , prompts have a choices feature now  , 
#also inside of the message we can give system prompts too using role as system 
def summarize_tasks(tasks):
    prompt = f"""
    You are a samrt task planning agent.
    Given a list of tasks, categorize them into 3 priority buckets:
    - High priority: tasks that are critical and must be completed today
    - Medium priority: tasks that are important but can be completed later
    - Low priority: tasks that are not important and can be completed later

    Tasks:
    {tasks}

    Return your response in the following text format:
    High priority:
    - task 1
    - task 2

    Medium priority:
    - task 1
    - task 2

    Low priority:
    - task 1
    - task 2
    """

    chat = genai.GenerativeModel(MODEL_ID)
    response = chat.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    task_text = read_tasks("tasks.txt")
    summary = summarize_tasks(task_text)
    print("\n Task summary \n")
    print("_"*50)
    print(summary)

