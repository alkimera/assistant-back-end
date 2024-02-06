import * as dotenv from "dotenv";
import { OpenAI } from "openai";

dotenv.config();

const openai = new OpenAI({
  apiKey: process.env.VITE_OPENAI_API_KEY,
});

// create new assistant
// const assistant = await openai.beta.assistants.create({
//   name: "Atendente Mr Hoppy Hamburgueria",
//   instructions: "Você é um atendente da Mr Hoppy, o cliente fará o pedido e você irá atendê-lo, anotando seu pedido, fornecendo o cardápio se pedido. ",
//   tools: [
//     {
//       type: "",
//     },
//   ],
//   model: "gpt-3.5-turbo-1106",
// })

// const retrieveAssistant = async () => {
//   try {
//     const assistant = openai.beta.assistants.retrieve(
//       "asst_HoVGULUxDroynUBGVzhF1Dry"
//     );

//   } catch (error) {
//     console.log("Erro ao buscar o assistente", error);
//   }
// };
// ********

const assistant = await openai.beta.assistants.retrieve(
  "asst_HoVGULUxDroynUBGVzhF1Dry"
);

// debug assistant
console.log(assistant)


// ********
// Threads
// Create Thread
// const thread = await openai.beta.threads.create();

// // Create Message
// const message = await openai.beta.threads.messages.create(thread.id, {
//   role: "user",
//   content: "Eu gostaria de fazer um pedido, o que você tem no cardápio?"
// })

// // Run Assistant
// const run = await openai.beta.threads.runs.create(thread.id, {
//   assistant_id: assistant.id,
//   instructions: "Abordar o usuário como Márcio."
// })
// ********



// ********
// const run = await openai.beta.threads.runs.retrieve("thread_KbwhF7OAVrzVDCk7xn6xUQat", "run_xZWzXHkzGQ8gzXKPStk1AOwm")

// // console.log(run)
// // ********

// const messages = await openai.beta.threads.messages.list(
//   "thread_KbwhF7OAVrzVDCk7xn6xUQat",
// )

// messages.body.data.forEach(message => {
//   console.log(message.content)
// });

