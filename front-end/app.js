
function main () {
    const utterance = document.getElementById("utterance").value;
    const userUtterance = `You: ${utterance}&#13;&#10;`;
    document.getElementById('utterance').innerHTML= '';
    document.getElementById('chat').insertAdjacentHTML('beforeend', userUtterance);
    reply(utterance);
};

function reply(utterance) {
    try {
        const url = 'http://18.232.100.1:5000/chat'
        const request = new XMLHttpRequest();
        const body = {
            "utterance": utterance
        };
        request.body = body;
        request.open('POST', url, true);
        request.send();
        console.log(request)
        const response = request.responseText;
        console.log(response)
        const botReply = `Bot: ${response.text}&#13;&#10;`;
    
        document.getElementById('chat').insertAdjacentHTML('beforeend', botReply);

    } catch(err) {
        console.log(err)
        const botReply = `Bot: There was an issue conversing. Please try again later.&#13;&#10;`;
        document.getElementById('chat').insertAdjacentHTML('beforeend', botReply);

    }
    const body = {
        "utterance": utterance
    };
};

