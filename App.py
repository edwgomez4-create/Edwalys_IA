import gradio as gr
from huggingface_hub import InferenceClient
import os

client = InferenceClient(
    token=os.getenv("HF_TOKEN")
)

def generar(mensaje):
    respuesta = client.chat_completion(
        messages=[
            {"role": "user", "content": mensaje}
        ],
        model="Qwen/Qwen2.5-72B-Instruct"
    )

    return respuesta.choices[0].message.content

demo = gr.Interface(
    fn=generar,
    inputs=gr.Textbox(label="Escribe tu mensaje"),
    outputs=gr.Textbox(label="Respuesta de Edwalyas IA"),
    title="🤖 Edwalyas IA",
    description="Tu asistente de inteligencia artificial"
)

demo.launch()
