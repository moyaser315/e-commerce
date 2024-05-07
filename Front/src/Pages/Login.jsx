import "./Login.css";
import { useNavigate } from "react-router-dom";
import { useState, useContext } from "react";
import { AuthContext } from "../Context/AuthContext";
import { UserContext } from "../Context/UserContext"
import { hostname } from "../assets/globalVars";
import axios from "axios";

const Login = () => {
  const [data, setData] = useState({
    email: "",
    password: "",
  });
  const [errorMessage, setErrorMessage] = useState('');
  const navigate = useNavigate()
  const { setLoggedIn } = useContext(AuthContext);
  const { setUser } = useContext(UserContext);
  const loginUser = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        "http://localhost:8000/users/login/",
        {
          username: data.email,
          password: data.password,
        },
        {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
        }
      );
      console.log(response.data);
      // Store the access token
      localStorage.setItem("accessToken", response.data.access_token)
      const user = await axios.get(`${hostname}/dashboard`, {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${localStorage.getItem("accessToken")}`
        },
      })
      setUser(user.data);
      console.log("User logged in");
      setLoggedIn(true);
      navigate("/");
      alert("Login successful! Welcome!");

    } catch (error) {
      console.error("Error logging in", error);
      setErrorMessage("Email or Password may be incorrect. Please try again.")
    }
  };
  return (
    <div className="login">
      <div className="loginContainer">
        <form onSubmit={loginUser} method="post">
          <h1>Log In</h1>
          <div className="loginFields">
            <input
              type="email"
              placeholder="Email Address"
              value={data.email}
              onChange={(e) => setData({ ...data, email: e.target.value })}
            />
            <input
              type="password"
              placeholder="Password"
              value={data.password}
              onChange={(e) => setData({ ...data, password: e.target.value })}
            />
          </div>
          {errorMessage && <p className="error-message">{errorMessage}</p>}
          <button type="submit">Continue</button>
        </form>
      </div>
    </div>
  );
};

export default Login;
