import gradio as gr
from diffusers import DDPMPipeline

model_id = "MexicanVanGogh/proyecto_cc"

ddpm = DDPMPipeline.from_pretrained(model_id, use_safetensors=True).to("cuda")


def predict(num_inference_steps):
    image = ddpm(num_inference_steps=num_inference_steps).images[0]
    return image

demo=gr.Interface(
    predict,
    inputs=[
        gr.Slider(0, 100, label='Inference steps', default=25),
    ],
    outputs="image",
    title="Proyecto final",
    description="Modelo de difusión para la generación de imagenes de zapatos",
    allow_flagging='never'
)

if __name__=='__main__':
    demo.launch()