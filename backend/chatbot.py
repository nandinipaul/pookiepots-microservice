def get_bot_response(message):

    bad_words = ["idiot", "stupid", "fuck"]

    for word in bad_words:
        if word in message.lower():
            return "Please avoid inappropriate language"

    if "hi" in message.lower():
        return "Hello"

    if "oxygen" in message.lower():
        return "Oxygen monitoring is not connected yet."

    return "I am your plant assistant"