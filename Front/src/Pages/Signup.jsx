import "./Signup.css";
import { Link, useNavigate } from "react-router-dom";
import Select from "react-select";
import { useState } from "react";
import axios from "axios";


const options = [
  { value: "Buyer", label: "Buyer" },
  { value: "Seller", label: "Seller" },
];

const customStyles = {
  control: (provided) => ({
    ...provided,
    border: "1px solid grey",
    color: "rgb(20, 45, 155)",
    fontSize: "16px",
  }),
  singleValue: (provided) => ({
    ...provided,
    color: "rgb(20, 45, 155)",
  }),
};


const Signup = () => {
  const [data, setData] = useState({
    accountType: "",
    name: "",
    email: "",
    password: "",
    confirmPassword: "",
    agreesToConditions: false,
  });
  const [errorMessage, setErrorMessage] = useState("");
  const navigate = useNavigate();

  const validateUsername = (name) => {
    return name.length >=3 && !/\s/.test(name);
  }
  const registerUser = async (e) => {
    e.preventDefault();
    setErrorMessage("");
    if (data.password !== data.confirmPassword) {
      setErrorMessage("Passwords do not match");
      return;
    }
    if (!data.agreesToConditions) {
      setErrorMessage("Please agree to the terms and conditions")
      return;
    }
    if (!validateUsername(data.name)) {
      setErrorMessage("Username must be at least 3 characters long and contain no spaces")
      return;
    }
    try {
      const response = await axios.post(
        'http://localhost:8000/users/signup',
        {
          name: data.name,
          email: data.email,
          user_type: data.accountType,
          balance: 0,
          password: data.password,
        },
        {
          headers: {
            'Content-Type': 'application/json',
          }
        }
      );
      console.log(response.data);
      console.log("User registered");
      navigate("/login");
      alert("User registered successfully, Please login to your account.")
    } catch (error) {
      console.error('Error creating user', error.response);
      setErrorMessage("An error occured while creating the user. Please try again.")
    }
  };
  return (
    <div className="signup">
      <div className="signupContainer">
        <form onSubmit={registerUser} method="post">
          <h1>Sign Up</h1>
          <div className="signupFields">
            <Select
              styles={customStyles}
              options={options}
              placeholder="Account Type"
              value={options.find(
                (option) => option.value === data.accountType
              )}
              onChange={(selectedOption) =>
                setData({ ...data, accountType: selectedOption.value })
              }
            />
            <input
              type="text"
              placeholder="Your Name"
              value={data.name}
              onChange={(e) => setData({ ...data, name: e.target.value })}
            />
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
            <input
              type="password"
              placeholder="Re-enter password"
              value={data.confirmPassword}
              onChange={(e) =>
                setData({ ...data, confirmPassword: e.target.value })
              }
            />
          </div>
          <div className="agree">
            <input
              type="checkbox"
              name=""
              id=""
              checked={data.agreesToConditions}
              onChange={(e) =>
                setData({ ...data, agreesToConditions: e.target.checked })
              }
            />
            <p>By continuing, I agree to the terms of use & privacy policy.</p>
          </div>
          {errorMessage && <p className="error-message">{errorMessage}</p>}
          <button type="submit">Continue</button>
        </form>
        <p className="loginDirect">
          Already have an account ?
          <Link className="link" to="/login">
            <span>Login here</span>
          </Link>
        </p>
      </div>
    </div>
  );
};

export default Signup;
