from openai import OpenAI
from assistant.env import gpt_key
import time

class GPT:
    def __init__(self) -> None:
        self.client = OpenAI(api_key=gpt_key)
        self.assistant_id = 'asst_UrIDUN3nQaQPvD52nm1WNN3y'
             
    def retrive_assistant(self):
        return self.client.beta.assistants.retrieve(self.assistant_id)
    
    def list_assistants(self):
        return self.client.beta.assistants.list(
            order='desc',
            limit='20'
        )
        
    def _create_thread(self):
        return self.client.beta.threads.create()
    
    def creat_message(self, message: str, thread_id):
        return self.client.beta.threads.messages.create(
            thread_id=thread_id,
            role='user',
            content=message
        )
    
    def run_assistant(self, thread_id, assistant_id):
        return self.client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id
        )
        
    def check_status_queue(self, thread_id, run_id):
        return self.client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run_id
        )

    def show_response_assistant(self, message_user):
        assistant = self.retrive_assistant()
        thread = self._create_thread()
        message = self.creat_message(message_user, thread.id)
        run = self.run_assistant(thread.id, assistant.id)
        
        while run.status != 'completed':
            time.sleep(1)
        
        return run
