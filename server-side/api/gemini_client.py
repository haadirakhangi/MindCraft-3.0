import os
import ast
from dotenv import load_dotenv
from server.teacher.routes import session
import google.generativeai as genai


load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

class GeminiProvider:
    def __init__(self):
        self.gemini_client = genai.GenerativeModel("gemini-1.5-flash")

    def generate_json_response(self, prompt):
        completion =  self.gemini_client.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json"
            ),
        )
        output = ast.literal_eval(completion.choices[0].message.content)
        return output
    
    def initialize_assistant_and_thread(self, profile, tools):
        assistant = self.openai_client.beta.assistants.create(
            name="MINDCRAFT",
            instructions=f"You are ISSAC, a helpful assistant for the website Mindcraft. Use the functions provided to you to answer user's question about the Mindcraft platform. {profile}",
            model="gpt-4o-mini",
            tools=tools
        )
        thread = self.openai_client.beta.threads.create()
        return assistant, thread
    
    def create_assistant_message_and_run(self, thread_id, query):
        message = self.openai_client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content= query,
        )
        run = self.openai_client.beta.threads.runs.create_and_poll(
            thread_id=thread_id,
            assistant_id=session['assistant_id'],
        )
        return message, run
    
    def submit_tool_outputs(self, thread_id, run_id, tools_to_call, available_tools):
        tools_outputs = []
        print("function to call:- ",tools_to_call)
        for tool in tools_to_call:
            output = None
            tool_call_id = tool.id
            tool_name = tool.function.name
            tool_args = tool.function.arguments
            print('TOOL CALLED:', tool_name)
            print('ARGUMENTS:', tool_args)
            tool_to_use = available_tools.get(tool_name)
            if tool_name =='retrieval_augmented_generation':
                tool_args_dict = ast.literal_eval(tool_args)
                query = tool_args_dict['query']
                output = tool_to_use(query)
            elif tool_name == 'get_context_from_page':
                index = session.get('index_chatbot')
                output = tool_to_use(index)
            if output:
                tools_outputs.append(
                    {'tool_call_id': tool_call_id, 'output': output})

        return self.openai_client.beta.threads.runs.submit_tool_outputs_and_poll(thread_id=thread_id, run_id=run_id, tool_outputs=tools_outputs)
    
    def list_assistant_messages(self, thread_id):
        messages = self.openai_client.beta.threads.messages.list(thread_id=thread_id,order="asc")
        return messages
    
    def _client(self):
        return self.openai_client