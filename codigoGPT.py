import google.generativeai as genai
hyper_secret_token = open("/home/angel/Documents/algo/fila.txt", 'r')
tokin = hyper_secret_token.read()
# Configura tu clave de API
genai.configure(api_key=f"{tokin}")

# Crea el modelo
model = genai.GenerativeModel('gemini-2.5-flash-lite')

# Envía el prompt y obtén la respuesta
def responde_gemini(que_cosa):  
    return model.generate_content(str(que_cosa)).text

