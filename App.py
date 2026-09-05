import gradio

def generar():
         return "¡Hola! Tu IA está funcionando."
     demo = gradio.Interface(fn=generar, inputs="text", outputs="text")
demo.launch()

