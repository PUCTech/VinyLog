import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Dashboard from "./pages/Dashboard";
import Landing from "./pages/Landing";   // ← 1) importe a página nova

function App() {
  return (
    <Routes>
      <Route path="/" element={<Landing />} />   {/* ← 2) "/" agora mostra a landing */}
      <Route path="/entrar" element={<Home />} />
      <Route path="/dashboard" element={<Dashboard />} />
    </Routes>
  );
}
export default App;