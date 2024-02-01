import random
from string import ascii_lowercase

first_name = str(input("Prenume: "))
last_name = str(input("Nume: "))
speciality = str(input("Specializare: "))
print(f"Hello", first_name,last_name,"\nWelcome to the Quiz App Test")

NUM_QUESTIONS_PER_QUIZ = 18
QUESTIONS = {
    "Which keyword do you use to loop over a given list of elements": [
        "for.",
        "while.",
        "each.",
        "loop."
    ],
    "Care este scopul functiei implicite zip()": [
        "De a itera prin 2 sau mai multe secvente simultan.",
        "De a combina mai multe string-uri intr-unul singur.",
        "De a face compresie la mai multe fisiere simultan.",
        "De a primi de la utilizator date de intrare.",
    ],
    "Care dintre variantele de mai jos NU este un mod de folosire pentru fisiere ?": [
        "'i'",
        "'r'",
        "'a'",
        "'w'"
    ],
    "Cum se numesc variabilele care actioneaza intr-o singura bucla ?": [
        "variabile locale.",
        "variabile globale.",
        "variabile temporare.",
        "variabile limitate."
    ],
    "Cum se numesc variabilele care actioneaza inafara oricarei bucle ?": [
        "variabile globale.",
        "variabile locale.",
        "variabile temporare.",
        "variabile limitate."
    ],
    "Care sunt structurile de date din Python care sunt predefinite ?": [
        "liste.",
        "hash table.",
        "binary tree.",
        "lista derivata."
    ],
    "Care dintre variabilele de mai jos este acelasi lucru cu o iteratie ?": [
        "etapa",
        "perioada",
        "alegere",
        "Niciuna dintre variantele prezente."
    ],
    "Ce sunt operatorii in Python ?": [
        "Un operator este un simbol care face o operatie sau actiune.",
        "Un operator este un caracter care nu se scrie pentru estetica codului.",
        "Un operator este un tip de date.",
        "Un operator este o bucla."
    ],
    "Ce sunt conditiile in Python ? Cum se folosesc ?": [
        "Conditiile sunt punctele de decizie in care bucla se executa sau nu.",
        "Conditiile sunt punctele in care se alege o cale fara a tine cont de un criteriu.",
        "Conditiile sunt punctele folosite pentru a itera deciziile.",
        "Conditiile sunt punctele de alegere unde codul se opreste."
    ],
    "Care afirmatie este ADEVARATA in cazul operatorului logic OR cu doua intrari?": [
        "Doar una trebuie sa fie adevarata ca sa se execute codul.",
        "Niciuna dintre intrari nu trebuie sa fie adevarate",
        "Amebele intrari trebuie sa fie adevarate.",
        "Ordinea in care sunt luate in considerare intrarile este criteriul de determinare."
    ],
    "Care afirmatie este ADEVARATA in cazul operatorului logic AND cu doua intrari?": [
        "Amebele intrari trebuie sa fie adevarate.",
        "Niciuna dintre intrari nu trebuie sa fie adevarate.",
        "Doar una trebuie sa fie adevarata ca sa se execute codul.",
        "Ordinea in care sunt luate in considerare intrarile este criteriul de determinare."
    ],
    "Care afirmatie este ADEVARATA in cazul operatorului logic NOT ?": [
        "Face negare la intrare si ofera raspunsul opus la iesire.",
        "Nu face nimic intrarii.",
        "Poate primi mai multe intrari.",
        "Poate servi drept poarta logica."
    ],
    "Care este definitia buclei for ?": [
        "Se executa de un anumit numar de ori.",
        "Se executa cata vreme se respecta o conditie.",
        "Nu exista o definitie a buclei.",
        "Se executa doar cand numarul de iteratii este variabil."
    ],
    "Care este definitia buclei while ?": [
        "Se executa cata vreme se respecta o conditie.",
        "Se executa de un anumit numar de ori.",
        "Nu exista o definitie a buclei.",
        "Se executa doar cand numarul de iteratii este variabil."
    ],
    "Dintre lista, tuple, set si dictionar, care este structura de date care are sintaxa key:value ?": [
        "dictionar.",
        "tuple.",
        "set.",
        "lista."
    ],
    "Dintre variantele afisate, care este structura de date care accepta indexare, ordonare, mutabilitate si dubluri ?":[
        "lista.",
        "tuple.",
        "set.",
        "dictionar."
    ],
    "Dintre variantele afisate, care este structura de date care NU accepta indexare, ordonare, mutabilitate si dubluri ?":[
        "set.",
        "tuple.",
        "lista.",
        "dictionar."
    ],
    "Dintre variantele afisate, care este structura de date care foloseste paranteze rotunde () pentru a-si defini valorile ?": [
        "tuple.",
        "set.",
        "lista.",
        "dictionar."
    ],
    "Care afirmatie este adevarata in cadrul operatorului logic XOR cu doua intrari?": [
        "daca intrarile au aceeasi valoare, iesirea este falsa.",
        "daca intrarile au aceeasi valoare, iesirea este adevarata.",
        "daca intrarile au valori diferite, iesirea este falsa.",
        "Niciuna dintre variantele afisate."
    ],
    "Care afirmatie este adevarata in cadrul operatorului logic XAND cu doua intrari?": [
        "daca intrarile au aceeasi valoare, iesirea este adevarata.",
        "daca intrarile au aceeasi valoare, iesirea este falsa.",
        "daca intrarile au valori diferite, iesirea este adevarata.",
        "Niciuna dintre variantele afisate."
    ],
    "Care afirmatie este adevarata in cadrul operatorului logic NOR cu doua intrari?": [
        "daca intrarile au aceeasi valoare, iesirea este valoarea opusa.",
        "daca intrarile au aceeasi valoare, iesirea este aceeasi valoare.",
        "daca intrarile au valori diferite, iesirea este adevarata.",
        "Niciuna dintre variantele afisate."
    ],
    "Care afirmatie este adevarata in cadrul operatorului logic XNOR cu doua intrari?": [
        "daca intrarile au aceeasi valoare, iesirea este adevarata",
        "daca intrarile au aceeasi valoare, iesirea este falsa.",
        "daca intrarile au valori diferite, iesirea este adevarata.",
        "Niciuna dintre variantele afisate."
    ],
    "Cum se sterge o variabila in Python fara a opri din rulat programul ?": [
        "Ne folosim de comanda 'del' si aceasta va inlatura variabila.",
        "Ne folosim de comanda 'pop' si aceasta va inlatura variabila",
        "Ne folosim de comanda 'remove' si aceasta va inlatura variabila",
        "Niciuna dintre variantele afisate."
    ]
}
num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
questions = random.sample(list(QUESTIONS.items()), k=num_questions)

grade = 1
question_with_correct_answer = 0
question_with_wrong_answer = 0
for num, (question, alternatives) in enumerate(questions, start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(
        zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives)))
    )
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    answer = labeled_alternatives[answer_label]
    if answer == correct_answer:
        grade += 0.5
        question_with_correct_answer += 1
        print("⭐ Correct! ⭐")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        question_with_wrong_answer += 1
        grade -= 0.75

print(f"\nYou got {grade} grade. ")


filename = f'{first_name, last_name, speciality} - Raport'
with open(filename,'w') as file:
    file.write(f"{first_name},{last_name},{speciality}\n")
    file.write(f"Correct answers: {question_with_correct_answer}\n")
    file.write(f"Wrong answers: {question_with_wrong_answer}\n")
    file.write(f"Grade: {grade}\n")
    file.write("Send this text document to your teacher\n")
    if grade > 5.0:
        file.write("The exam is promoted. Congratulations!\n")
    else:
        file.write("The exam is remaining. Good luck next time!\n")