import { useState } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([
    { type: "bot", text: "Waiting for your question..." },
  ]);

  const sendMessage = async () => {
    if (!message.trim()) return;

    setChat((prev) => [...prev, { type: "user", text: message }]);
    setMessage("");

    try {
      setChat((prev) => [...prev, { type: "bot", text: "Fetching weather..." }]);

      const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
      });

      const data = await res.json();

      setChat((prev) => [
        ...prev.slice(0, -1),
        { type: "bot", text: data.reply },
      ]);
    } catch (err) {
      setChat((prev) => [
        ...prev.slice(0, -1),
        { type: "bot", text: "Unable to connect to server." },
      ]);
    }
  };

  return (
    <div className="app">
      <div className="glass-card">
        <h1 className="title">Weather Chat Assistant</h1>

        <div className="chat-box">
          {chat.map((c, i) => (
            <div key={i} className={`chat ${c.type}`}>
              {c.text}
            </div>
          ))}
        </div>

        <div className="input-row">
          <input
            type="text"
            placeholder="Ask about the weather of any city..."
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          />
          <button onClick={sendMessage}>Send</button>
        </div>

        <p className="footer">Powered by OpenWeather API</p>
      </div>
    </div>
  );
}

export default App;
