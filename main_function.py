from little_functions import *

def handle_diolog(request, response, user_storage):
    if not user_storage:
        user_storage = {}
    output_message = "Hello, word."
    return message_return(response, user_storage, output_message)