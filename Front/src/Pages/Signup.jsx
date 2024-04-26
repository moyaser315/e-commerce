import "./Signup.css";
import { Link } from "react-router-dom";
import Select from 'react-select'
import { useState } from "react";
import axios from "axios";

// axios.default.baseURL = "http://localhost:8000";
// axios.defaults.withCredentials = true;
// axios.get('/')

const options = [
  { value: 'Buyer', label: 'Buyer' },
  { value: 'Seller', label: 'Seller' },
]

const customStyles = {
  control: (provided) => ({
    ...provided,
    border: '1px solid grey',
    color: 'rgb(20, 45, 155)',
    fontSize: '16px',
  }),
  singleValue: (provided) => ({
    ...provided,
    color: 'rgb(20, 45, 155)',
  }),
};




const Singup = () => {
  const [data, setData] = useState({
    accountType: "",
    name: "",
    email: "",
    password: "",
    confirmPassword: "",
    agreesToConditions: false,
  });

  const registerUser = async (e) => {
    e.preventDefault();
    if (data.password !== data.confirmPassword) {
      alert("Passwords do not match");
      return;
    }
    if (!data.agreesToConditions) {
      alert("You must agree to the terms and conditions");
      return;
    }
    // try {
    //   const response = await axios.post('http://localhost:8000/users/', data);
    //   console.log(response.data);
    // } catch (error) {
    //   console.error('Error creating user', error);
    // }
    // console.log("User registered");
  }
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
                value={options.find((option) => option.value === data.accountType)} 
                onChange={(selectedOption) => setData({ ...data, accountType: selectedOption.value })}/>
              <input type="text" placeholder="Your Name" value={data.name} onChange={(e) => setData({...data, name: e.target.value})}/>
              <input type="email" placeholder="Email Address" value={data.email} onChange={(e) => setData({...data, email: e.target.value})}/>
              <input type="password" placeholder="Password" value={data.password} onChange={(e) => setData({...data, password: e.target.value})}/>
              <input type="password" placeholder="Re-enter password" value={data.confirmPassword} onChange={(e) => setData({...data, confirmPassword: e.target.value})}/>
          </div>
          <div className="agree">
            <input type="checkbox" name="" id="" checked={data.agreesToConditions} onChange={(e) => setData({...data, agreesToConditions: e.target.checked})}/>
            <p>By continuing, I agree to the terms of use & privacy policy.</p>
          </div>
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

export default Singup;
