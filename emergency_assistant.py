def get_emergency_response(message):

    message = message.lower().strip()

    if not message:
        return "Please describe your emergency."

    # Medical emergency
    if any(word in message for word in [
        "heart", "chest pain", "bleeding", "injury",
        "unconscious", "medical"
    ]):
        return (
            "MEDICAL EMERGENCY DETECTED\n\n"
            "1. Stay calm and move to a safe place.\n"
            "2. Contact your local emergency service immediately.\n"
            "3. If someone is injured, avoid unnecessary movement.\n"
            "4. Ask nearby people for help.\n"
            "5. Provide first aid only if you know how to do it safely."
        )

    # Fire emergency
    if any(word in message for word in [
        "fire", "smoke", "burning"
    ]):
        return (
            "FIRE EMERGENCY DETECTED\n\n"
            "1. Move away from the fire immediately.\n"
            "2. Alert people nearby.\n"
            "3. Use an emergency exit if available.\n"
            "4. Do not use elevators during a fire.\n"
            "5. Contact emergency services."
        )

    # Accident
    if any(word in message for word in [
        "road accident", "car accident", "bike accident",
        "collision", "crash"
    ]):
        return (
            "ACCIDENT EMERGENCY DETECTED\n\n"
            "1. Move to a safe location if possible.\n"
            "2. Check whether anyone needs urgent medical help.\n"
            "3. Contact emergency services.\n"
            "4. Do not move seriously injured people unless there is immediate danger."
        )

    # Safety / danger
    if any(word in message for word in [
        "danger", "police", "threat", "attack", "unsafe"
    ]):
        return (
            "SAFETY EMERGENCY DETECTED\n\n"
            "1. Move to a safe and public location.\n"
            "2. Avoid confrontation.\n"
            "3. Contact local emergency services or police.\n"
            "4. Inform a trusted person about your situation."
        )

    # Missing person
    if any(word in message for word in [
        "missing", "lost person", "lost child"
    ]):
        return (
            "MISSING PERSON ASSISTANCE\n\n"
            "1. Stay calm.\n"
            "2. Contact family members or trusted people.\n"
            "3. Contact local authorities if necessary.\n"
            "4. Note the person's last known location and description."
        )

    # Natural disaster
    if any(word in message for word in [
        "earthquake", "flood", "cyclone", "storm"
    ]):
        return (
            "NATURAL DISASTER ASSISTANCE\n\n"
            "1. Move to a safer location.\n"
            "2. Follow official emergency instructions.\n"
            "3. Keep drinking water and essential items with you.\n"
            "4. Avoid damaged buildings and dangerous areas."
        )

    # General emergency
    if any(word in message for word in [
        "help", "emergency", "urgent", "save me"
    ]):
        return (
            "EMERGENCY MODE ACTIVATED\n\n"
            "Please stay calm and move to a safe location.\n"
            "Contact your local emergency service or a trusted person.\n"
            "Describe your exact situation so the assistant can provide relevant guidance."
        )

    return (
        "I am your Offline Emergency Communication Assistant.\n\n"
        "You can ask about:\n"
        "• Medical emergencies\n"
        "• Fire\n"
        "• Road accidents\n"
        "• Personal safety\n"
        "• Missing persons\n"
        "• Floods, earthquakes and storms\n\n"
        "Example: 'There is a fire' or 'Someone has chest pain'."
    )