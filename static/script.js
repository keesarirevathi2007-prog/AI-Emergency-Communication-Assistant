function addMessage(message, sender) {
    const chatBox = document.getElementById("chatBox");

    const messageDiv = document.createElement("div");
    messageDiv.className = "message " + sender;
    messageDiv.textContent = message;

    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
    const input = document.getElementById("messageInput");
    const message = input.value.trim();

    if (message === "") {
        return;
    }

    addMessage(message, "user");
    input.value = "";

    try {
        const response = await fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        addMessage(data.response, "assistant");

    } catch (error) {
        addMessage(
            "Unable to connect to the assistant. Please try again.",
            "assistant"
        );
    }
}

function quickMessage(message) {
    document.getElementById("messageInput").value = message;
    sendMessage();
}

function handleEnter(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}

function showEmergencyNumbers() {
    addMessage(
        "Emergency Numbers (India)\n\n" +
        "112 - Emergency Services\n" +
        "100 - Police\n" +
        "101 - Fire\n" +
        "108 - Ambulance",
        "assistant"
    );
}

function startVoice() {
    const SpeechRecognition =
        window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
        alert("Voice input is not supported in this browser.");
        return;
    }

    const recognition = new SpeechRecognition();

    recognition.lang = "en-IN";
    recognition.start();

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;

        document.getElementById("messageInput").value = transcript;
    };

    recognition.onerror = function() {
        alert("Voice input could not be started.");
    };
}