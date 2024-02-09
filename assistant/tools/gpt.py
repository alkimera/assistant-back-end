from openai import OpenAI
from assistant.env import gpt_key, assistant_id
import time

class OpenAIAssistantClient:
  def __init__(self):
    self.client = OpenAI(api_key=gpt_key)
    self.assistant_id = assistant_id

  def create_thread_and_run_assistant(self, user_message, timeout=90):
    attempt_count = 0

    while True:
      attempt_count += 1
      print(f"Tentativa {attempt_count}: Enviando mensagem ao assistente.")
      start_time = time.time()

      thread = self.client.beta.threads.create()

      self.client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_message
      )

      run = self.client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=self.assistant_id,
      )

      while True:
        elapsed_time = time.time() - start_time
        if elapsed_time > timeout:
          print(f"Tempo excedido ({elapsed_time:.2f} segundos). Reenviando a mensagem.")
          break  

        status = self.check_status(thread.id, run.id)
        if status.status == 'completed':
          print("Execução completada.")
          return self.retrieve_messages(thread.id)
        elif status.status == 'failed':
          print("Falha na execução:", status)
          return None

        time.sleep(10)


  def check_status(self, thread_id, run_id):
    return self.client.beta.threads.runs.retrieve(
      thread_id=thread_id,
      run_id=run_id
    )

  def retrieve_messages(self, thread_id):
    messages = self.client.beta.threads.messages.list(thread_id=thread_id)
    assistant_messages = [msg for msg in messages.data if msg.role == 'assistant']
    result_message = assistant_messages[0].content[0].text.value if assistant_messages else None
    result = {'message': result_message}
    return result
