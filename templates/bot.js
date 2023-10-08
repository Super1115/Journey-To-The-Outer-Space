function appendMessage(who, message) {
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<div><b>${who}:</b> ${message}</div>`;
}

function sendMessage() {
    const userInput = document.getElementById('user-input');
    const userMessage = userInput.value;
    userInput.value = '';
    appendMessage('You', userMessage);
    fetch('/ask', {
        method: 'POST',
        body: new URLSearchParams({'user_message': userMessage}),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(response => rPaLM_API_prompt.json())
    .then(data => appendMessage('Bot', data.bot_response));
}
