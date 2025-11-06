import axios from "axios";

// ✅ Create axios instance
const api = axios.create({
  baseURL: "http://127.0.0.1:8000", // FastAPI backend
  headers: {
    "Content-Type": "application/json",
  },
});

// ✅ Add token to all requests if available
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});




export default api;
