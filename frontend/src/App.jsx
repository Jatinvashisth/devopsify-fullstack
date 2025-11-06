import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./Components/login";
import Home from "./Components/Home";
import Chat from "./chat";  

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/home" element={<Home />} />
        <Route path="/chat" element={<Chat />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
