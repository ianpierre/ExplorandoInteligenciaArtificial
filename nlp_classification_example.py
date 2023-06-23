from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Datos de entrenamiento
sentences = [
    "El cielo es azul",
    "El sol está brillando",
    "Me gusta el verano",
    "Los pájaros cantan en los árboles",
    "Me encanta caminar por el bosque"
]
labels = ["clima", "clima", "clima", "naturaleza", "naturaleza"]

# Crear un vectorizador para convertir las frases en características numéricas
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

# Crear un clasificador Naive Bayes y entrenarlo con los datos
classifier = MultinomialNB()
classifier.fit(X, labels)

# Datos de prueba
test_sentences = [
    "Hace calor hoy",
    "Estoy disfrutando de un día soleado",
    "Estoy de paseo en el bosque"
]

# Convertir las frases de prueba en características numéricas
X_test = vectorizer.transform(test_sentences)

# Realizar predicciones con el clasificador
predictions = classifier.predict(X_test)

# Imprimir las predicciones
for sentence, prediction in zip(test_sentences, predictions):
    print(f"La frase '{sentence}' es clasificada como '{prediction}'")
