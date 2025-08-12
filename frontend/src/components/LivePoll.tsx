import { useEffect, useState } from "react";

export default function LivePoll({ pollId }) {
  const [votes, setVotes] = useState({});
  const [socket, setSocket] = useState<WebSocket | null>(null);

  useEffect(() => {
    const ws = new WebSocket(`ws://localhost:8000/ws/${pollId}`);
    setSocket(ws);

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setVotes(data);
    };

    return () => ws.close();
  }, [pollId]);

  const vote = (option) => {
    socket?.send(JSON.stringify({ pollId, option }));
  };

  return (
    <div>
      <h2>Live Poll</h2>
      {["Yes", "No"].map((opt) => (
        <button key={opt} onClick={() => vote(opt)}>
          {opt} ({votes[opt] || 0})
        </button>
      ))}
    </div>
  );
}