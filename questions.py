import random
import sys

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden
# que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, en el
# mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
total_score = 0
# El usuario deberá contestar 3 preguntas
# Se seleccionan 3 preguntas aleatorias
questions_to_ask = random.choices((list(zip(questions,
                                            answers,
                                            correct_answers_index))), k=3)

for question, possible_answers, correct_answer in questions_to_ask:
    # Se muestra la pregunta y las respuestas posibles
    print(question)
    for i, answer in enumerate(possible_answers):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder
    # correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        # Se valida la respuesta
        if  not user_answer.isdigit():
            print("Respuesta no válida.")
            sys.exit(1)

        user_answer = int(user_answer) - 1
        if not 0 <= user_answer < 4:
            print("Respuesta no válida.")
            sys.exit(1)

        # Se verifica si la respuesta es correcta
        if user_answer == correct_answer:
            total_score += 1
            print("¡Correcto!")
            break

        if total_score > 0:
            total_score -= 0.5
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(possible_answers[correct_answer])

    # Se imprime un blanco al final de la pregunta
    print()


if total_score.is_integer():
    print(f"Puntaje: {int(total_score)}")
else:
    print(f"Puntaje: {total_score}")
