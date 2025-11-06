import React, { useState, useEffect, useRef } from "react";
import "./chat.css";
import { useNavigate } from "react-router-dom";

const Chat = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const listRef = useRef(null);
  const navigate = useNavigate();

  // Check login token on mount
  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      navigate("/login", { replace: true });
    }
  }, [navigate]);

  // Auto scroll
  useEffect(() => {
    if (listRef.current) listRef.current.scrollTop = listRef.current.scrollHeight;
  }, [messages]);

  const sendMessage = () => {
    const trimmed = input.trim();
    if (!trimmed) return;

    // Add user message locally
    setMessages((prev) => [...prev, { sender: "user", text: trimmed }]);
    setInput("");
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className="chat-page">
      <div className="chat-container">
        <div className="chat-header">
          <button className="chat-back-btn" onClick={() => navigate("/home")}>
            ← Home
          </button>
          <div className="chat-header-center">
            <div className="chat-avatar">AI</div>
            <div className="chat-header-text">
              <div className="chat-title">Chat App</div>
              <div className="chat-subtitle">React 💬</div>
            </div>
          </div>
        </div>

        <div className="chat-messages" ref={listRef}>
          {messages.map((m, i) => (
            <div key={i} className={`chat-message ${m.sender}`}>
              <div className="chat-message-text">{m.text}</div>
            </div>
          ))}
        </div>

        <div className="chat-composer">
          <textarea
            className="chat-input"
            placeholder="Type a message... (Enter to send)"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
          />
          <button
            className="chat-send-btn"
            onClick={sendMessage}
            disabled={!input.trim()}
          >
            ➤
          </button>
        </div>
      </div>
    </div>
  );
};

export default Chat;
