import { useState } from "react";
import "./Login.css";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

const Login = () => {
  const [isLogin, setIsLogin] = useState(true);
  const navigate = useNavigate();

  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  // ✅ LOGIN
  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const res = await api.post("/login", { email, password });
      localStorage.setItem("token", res.data.access_token);
      navigate("/home");
    } catch (err) {
      alert("Invalid Credentials");
    }
  };

  // ✅ SIGNUP
  const handleSignup = async (e) => {
    e.preventDefault();
    try {
      await api.post("/signup", { username, email, password });
      alert("Signup successful! Now login");
      setIsLogin(true);
    } catch (err) {
      alert("Signup failed");
    }
  };

  return (
    <div className="auth-wrapper">
      <div className="auth-container">
        <div className={`form-box ${isLogin ? "login" : "signup"}`}>
          <h2>{isLogin ? "Welcome Back" : "Create Account"}</h2>
          <p className="subtext">{isLogin ? "Login to continue" : "Join us today"}</p>

          <form onSubmit={isLogin ? handleLogin : handleSignup}>
            {!isLogin && (
              <input
                type="text"
                placeholder="Username"
                required
                onChange={(e) => setUsername(e.target.value)}
              />
            )}
            <input
              type="email"
              placeholder="Email"
              required
              onChange={(e) => setEmail(e.target.value)}
            />
            <input
              type="password"
              placeholder="Password"
              required
              onChange={(e) => setPassword(e.target.value)}
            />
            <button className="btn">{isLogin ? "Login" : "Sign Up"}</button>
          </form>

          <p className="switch-text">
            {isLogin
              ? "Don't have an account? "
              : "Already have an account? "}
            <span onClick={() => setIsLogin(!isLogin)}>
              {isLogin ? "Sign Up" : "Login"}
            </span>
          </p>
        </div>
      </div>
    </div>
  );
};

export default Login;
