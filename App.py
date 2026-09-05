import gradio

def generar(texto):
    return f"🤖 Edwalyas IA recibió: {texto}"
demo = gradio.Interface(fn=generar, inputs="text", outputs="text")
demo.launch()

