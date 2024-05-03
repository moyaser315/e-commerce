import { Link } from "react-router-dom";
import cart_icon from "/cart_icon.jpg";
import logo from "/R.png";
import { useContext, useState } from "react";
import { ShopContext } from "./Context/ShopContext";
import MultiSearch from "./Pages/Search";

const Navbar = () => {
  const { getTotalCartItems } = useContext(ShopContext);
 
  return (
    <div className="navbar">
      <div className="nave-logo">
        <img src={logo} alt="" />
        <p>NAME</p>
      </div>
      <ul className="nav-menu">
        <li>
          <Link className="link" to="/">
            Dashboard
          </Link>
          <hr />
        </li>
        <li>
          <Link className="link" to="/profile">
            Profile
          </Link>
          <hr />
        </li>
        <li>
          <Link className="link" to="/products">
            Products
          </Link>
          <hr />
        </li>
      </ul>
      <MultiSearch />
      <div className="nav-cart-login-signup">
        <Link to="/login">
          <button>Login</button>
        </Link>
        <Link to="/signup">
          <button>Sign up</button>
        </Link>
        <Link to="/cart">
          <img src={cart_icon} alt="" />
        </Link>
        <div className="cart-count">{getTotalCartItems()}</div>
      </div>
    </div>
  );
};

export default Navbar;





