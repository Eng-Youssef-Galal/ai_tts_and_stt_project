def handle_move():
    return "Navigating to the adjust page for you."

def handle_receive():
    return "Please specify the quantity and location for the items you want to receive."

def handle_adjust():
    return "Adjust the quantity, person, or location for a specific item."

def handle_dispose():
    return "Item disposed and quantity decreased accordingly."

def process_business_logic(intent):
    if intent == "move":
        return handle_move()
    elif intent == "receive":
        return handle_receive()
    elif intent == "adjust":
        return handle_adjust()
    elif intent == "dispose":
        return handle_dispose()
    return "Unknown business logic operation."
