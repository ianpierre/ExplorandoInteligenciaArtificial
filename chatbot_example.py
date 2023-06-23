import openai
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Crear una instancia del chatbot
chatbot = ChatBot('MiChatBot')

# Crear un entrenador para el chatbot
trainer = ListTrainer(chatbot)

# Entrenar al chatbot con ejemplos de recetas de pan
trainer.train([
    'Cómo hacer pan casero',
    'La receta para hacer pan casero es muy sencilla. Necesitarás los siguientes ingredientes...',
    'Receta de pan de masa madre',
    'El pan de masa madre es delicioso. Aquí tienes los pasos para prepararlo...',
    # Agrega más ejemplos de recetas de pan según tus necesidades
])

while True:
    # Obtener la entrada del usuario
    user_input = input('Tú: ')

    # Obtener la respuesta del chatbot
    try:
        response = chatbot.get_response(user_input)
    except Exception as e:
        # Si no hay respuesta local, utiliza la API de OpenAI
        openai.api_key = 'tu api kay'
        response = openai.Completion.create(engine="text-davinci-003", prompt=user_input, max_tokens=60)
        response = response.choices[0].text.strip()

    # Imprimir la respuesta del chatbot
    print('ChatBot:', response)
