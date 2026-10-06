import requests


def get_emergency_response(message):
    prompt = f"""
You are an offline emergency communication assistant designed for users in India.

Your job is to understand the user's emergency question and provide short,
clear and safe general guidance.

Important rules:
- Give practical safety guidance.
- If the situation is life-threatening, tell the user to contact Indian emergency services at 112.
- Do not give dangerous or risky instructions.
- Do not tell the user to enter a burning building or approach dangerous situations.
- Do not diagnose medical conditions.
- For medical emergencies, advise getting professional medical help.
- Keep the answer easy to understand.
- Answer the user's actual question instead of always giving the same fixed response.
- Do not mention that you are an AI model unless necessary.

User's emergency question:
{message}
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()

        data = response.json()
        return data.get("response", "Sorry, I could not generate a response.")

    except requests.exceptions.ConnectionError:
        return (
            "The local AI service is not running. "
            "Please start Ollama and try again."
        )

    except Exception as e:
        return f"Unable to get an AI response: {str(e)}"