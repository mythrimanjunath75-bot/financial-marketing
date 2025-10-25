// chat.js
(function(){
  const messages = document.getElementById('messages');
  const input = document.getElementById('chatInput');
  const sendBtn = document.getElementById('sendBtn');
  const humanBtn = document.getElementById('humanBtn');

  function append(msg, isUser=false){
    const div = document.createElement('div');
    div.className = 'message ' + (isUser? 'msg-user' : 'msg-bot');
    div.innerHTML = msg;
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
  }

  async function send(){
    const text = input.value.trim();
    if(!text) return;
    append(text, true);
    input.value = ''; sendBtn.disabled = true;

    try {
      const res = await fetch('/api/chat', { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify({ message: text }) });
      const json = await res.json();
      append(json.reply || 'No reply from server.');
    } catch(err){
      append('Error contacting chat server. Fallback: I am a demo AI assistant. Try asking about your risk profile.');
    } finally {
      sendBtn.disabled = false;
    }
  }

  sendBtn.addEventListener('click', send);
  input.addEventListener('keydown', (e) => { if(e.key === 'Enter') send(); });

  humanBtn.addEventListener('click', () => {
    // quick connect to human advisor
    window.location.href = 'mailto:advisor@example.com?subject=Requesting%20human%20advisor';
  });
})();
