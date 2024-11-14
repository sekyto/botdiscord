from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Please enter a message'
    elif 'hello' in lowered:
        return 'Hi there!'
    elif 'how are you' in lowered:
        return 'I am fine, thank you'
    elif 'bye' in lowered:
        return 'Goodbye'

    return choice(['I am not sure', 'I am not sure', 'I am not sure'])