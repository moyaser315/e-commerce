import "./Login.css";
import { useState } from "react";
import axios from "axios";
import qs from "qs";

const Login = () => {
  const [data, setData] = useState({
    email: "",
    password: "",
  });
  // const requestOptions = {
  //   method: "POST",
  //   headers: { "Content-Type": "application/json" },
  //   body: JSON.stringify(data),
  // }
  // const submitLogin = async () => {
  //   const response = await fetch("http://localhost:8000/login/test", requestOptions);
  //   const data = await response.json();
  // }
  const loginUser = async (e) => {
    e.preventDefault();
    // submitLogin();
    // axios.post("http://localhost:8000/login/test", {
    //   username: data.email,
    //   password: data.password,
    // })
    // fetch("http://localhost:8000/login/test", {
    //   method: "POST",
    //   headers: {
    //     "Content-Type": "'application/x-www-form-urlencoded'",
    //   },
    //   body: JSON.stringify(data),
    // })
    // .then(response => response.json())
    // .then(data => console.log(data))
    // .catch(error => console.error('Error:', error));
    try {
      const response = await axios.post(
        "http://localhost:8000/login/test",
        qs.stringify({
          username: data.email,
          password: data.password,
        }),
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
