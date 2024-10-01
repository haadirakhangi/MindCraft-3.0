import os
import ast
from dotenv import load_dotenv
from server.teacher.routes import session
import google.generativeai as genai


load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
class GeminiProvider:
    def __init__(self, profile=None, tools=None):
        self.gemini_client = genai.GenerativeModel("gemini-1.5-flash")
        # Initialize chat during object creation
        if profile and tools:
            self.initialize_assistant(profile, tools)
        else:
            self.chat = None  # Explicitly set self.chat to None if it's not initialized

    def generate_json_response(self, prompt):
        completion = self.gemini_client.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json"
            ),
        )
        output = ast.literal_eval(completion.text)
        return output
    
    def initialize_assistant(self, profile, tools):
        self.gemini_assistant = genai.GenerativeModel(
            "gemini-1.5-flash",
            system_instruction=f"You are ISSAC, a helpful assistant for the website Mindcraft. Use the functions provided to you to answer user's question about the Mindcraft platform. {profile}",
            tools=tools
        )
        self.chat = self.gemini_assistant.start_chat(enable_automatic_function_calling=True)
        return self.chat
    
    def return_chat(self):
        # Ensure the chat is initialized
        if self.chat is None:
            raise AttributeError("Chat has not been initialized. Call 'initialize_assistant' first.")
        return self.chat
