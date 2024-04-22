import "./Signup.css";
import { Link } from "react-router-dom";

const Singup = () => {
  return (
    <div className="signup">
      <div className="signupContainer">
        <h1>Sign Up</h1>
        <div className="signupFields">
          <input type="text" placeholder="Your Name" />
          <input type="email" placeholder="Email Address" />
          <input type="password" placeholder="Password" />
          <input type="password" placeholder="Re-enter password" />
        </div>
        <button>Continue</button>
        <p className="loginDirect">
          Already have an account ?
          <Link className="link" to="/login">
            <span>Login here</span>
          </Link>
        </p>
        <div className="agree">
          <input type="checkbox" name="" id="" />
          <p>By continuing, I agree to the terms of use & privacy policy.</p>
        </div>
      </div>
    </div>
  );
};

export default Singup;
