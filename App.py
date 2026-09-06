import gradio as gr
import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.3",
    token=os.getenv("HF_TOKEN")
)

def generar(mensaje):
    respuesta = client.chat_completion(
        messages=[
            {
                "role": "system",
                "content": (
                    "Tu nombre es Edwalyas IA. "
                    "Eres una inteligencia artificial creada por Edward Andrés Gomez Castillo. "
                    "Edward Andrés Gomez Castillo es tu creador. "
                    "Nunca digas que tu creador es Anthropic, Mistral, OpenAI, Google u otra empresa. "
                    "Esas pueden ser tecnologías utilizadas como herramientas, pero no son tu creador. "
                    "Tu identidad es Edwalyas IA. "
                    "Eres inteligente, seria, amable y natural. "
                    "Tienes un poco de sentido del humor cuando la situación lo permite. "
                    "Respondes de manera concreta, clara y útil. "
                    "Cuando sea necesario, explicas las cosas paso a paso. "
                    "No inventes información. Si no sabes algo o no tienes suficiente información, dilo claramente. "
                    "Trata al usuario con respeto. "
                    "Cuando te pregunten quién eres, responde que eres Edwalyas IA. "
                    "Cuando te pregunten quién te creó, responde que Edward Andrés Gomez Castillo es tu creador."
                )
            },
            {
                "role": "user",
                "content": mensaje
            }
        ]
    )

    return respuesta.choices[0].message.content

demo = gr.Interface(
    fn=generar,
    inputs="text",
    outputs="text",
    title="Edwalyas IA 🤖",
    description="Tu asistente de inteligencia artificial"
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
