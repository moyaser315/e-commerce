import "./Login.css";
import { useState } from "react";
import axios from "axios";
import qs from "qs";

const Login = () => {
  const [data, setData] = useState({
    email: "",
    password: "",
  });
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
    } catch (error) {
      console.error("Error logging in", error);
    }
    console.log("User logged in");
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
          <button type="submit">Continue</button>
        </form>
      </div>
    </div>
  );
};

export default Login;
