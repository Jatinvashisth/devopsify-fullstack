import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Home.css";

const Home = () => {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    name: "",
    email: "",
    phone: "",
    address: "",
  });
  const [message, setMessage] = useState("");
  const [darkMode, setDarkMode] = useState(false);

  // ✅ Check if token exists
  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) navigate("/login", { replace: true });
  }, [navigate]);

  // ✅ Logout handler
  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/login", { replace: true });
  };

  // ✅ Form change handler
  const handleChange = (e) =>
    setFormData({ ...formData, [e.target.name]: e.target.value });

  // ✅ Form submit
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post("/user/details", formData); // backend endpoint
      setMessage("Details saved successfully!");
    } catch (err) {
      setMessage("Failed to save details.");
      console.error(err);
    }
  };

  // ✅ Smooth scroll to section
  const scrollToSection = (sectionId) => {
    const section = document.getElementById(sectionId);
    if (section) {
      section.scrollIntoView({ behavior: "smooth" });
    }
  };

  return (
    <div className={`body ${darkMode ? "dark" : ""}`}>
      {/* Header */}
      <header className="header">
        <h2 className="logo">MyPortfolio</h2>
        <div className="nav-buttons">
          <button onClick={() => scrollToSection("about")}>About</button>
          <button onClick={() => scrollToSection("skills")}>Skills</button>
          <button onClick={() => scrollToSection("contact")}>Contact</button>
          <button onClick={handleLogout} className="logout-btn">
            Logout
          </button>
          <button
            onClick={() => setDarkMode(!darkMode)}
            className="darkmode-btn"
          >
            {darkMode ? "☀️" : "🌙"}
          </button>
        </div>
      </header>

      {/* Hero Section */}
      <section id="home" className="hero">
        <div className="hero-content">
          <h1>Welcome to My Portfolio</h1>
          <p>Building Modern & Aesthetic Web Experiences</p>
          <button onClick={() => scrollToSection("contact")}>Hire Me</button>
        </div>
      </section>

      {/* Skills Section */}
      <section id="skills" className="section skills-section">
        <h2 className="section-title">My Skills</h2>
        <div className="skills-grid">
          {[
            "Python",
            "FastAPI",
            "MySQL",
            "React",
            "DevOps",
            "Cloud",
            "Linux",
            "Git & GitHub",
            "Docker",
          ].map((skill, idx) => (
            <div key={idx} className="skill-card">
              <span className="skill-name">{skill}</span>
            </div>
          ))}
        </div>
      </section>

      {/* Contact Section */}
      <section id="contact" className="section contact-section">
        <h2 className="section-title">Contact Me</h2>
        <form className="form" onSubmit={handleSubmit}>
          <input
            type="text"
            name="name"
            placeholder="Full Name"
            onChange={handleChange}
            required
          />
          <input
            type="email"
            name="email"
            placeholder="Email Address"
            onChange={handleChange}
            required
          />
          <input
            type="text"
            name="phone"
            placeholder="Phone Number"
            onChange={handleChange}
          />
          <input
            type="text"
            name="address"
            placeholder="Address"
            onChange={handleChange}
          />
          <button type="submit" className="submit-btn">
            Submit
          </button>
          {message && <p className="form-message">{message}</p>}
        </form>
      </section>

      {/* About Section */}
      <section id="about" className="section about-section">
        <h2 className="section-title">About Me</h2>
        <div className="about-content">
          <img
            src="/profile.jpg"
            alt="Profile"
            className="profile-img"
          />
          <p>
            Hi! I'm a passionate web developer building modern, responsive, and
            aesthetic applications. I specialize in React, FastAPI, Python,
            and MySQL. I love creating interactive UI/UX experiences and
            exploring new technologies. Let's build something amazing together!
          </p>
        </div>
      </section>

      {/* Footer */}
      <footer className="footer">
        &copy; 2025 My Portfolio. All rights reserved.
      </footer>
    </div>
  );
};

export default Home;
