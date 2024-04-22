import "./Login.css";

const Login = () => {
  return (
    <div className="login">
      <div className="loginContainer">
        <h1>Log In</h1>
        <div className="loginFields">
          <input type="email" placeholder="Email Address" />
          <input type="password" placeholder="Password" />
        </div>
        <button>Continue</button>
      </div>
    </div>
  );
};

export default Login;
