import "./Navbar.css"
import { Link, useNavigate } from "react-router-dom";
import cart_icon from "/cart_icon.jpg";
import profile_icon from "/profile.png"
import logo from "/R.png";
import { useContext, useState } from "react";
import { ShopContext } from "./Context/ShopContext";
import MultiSearch from "./Pages/Search";

const Navbar = () => {
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const navigate = useNavigate;
  const handleLogout = () => {
    localStorage.removeItem("accessToken");
    setDropdownOpen(false);
    navigate("/");
  }
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
          <Link className="link" to="/products">
            Products
          </Link>
          <hr />
        </li>
      </ul>
      <MultiSearch />
      <div className="nav-cart-login-signup">
        {localStorage.getItem("accessToken") ? (
          <div>
            <img 
              src={profile_icon} 
              alt="Profile" 
              onClick={() => setDropdownOpen(!dropdownOpen)}
              />
              {dropdownOpen && (
                <div className="dropdown-menu">
                  <Link to="/profile" onClick={() => setDropdownOpen(false)}>
                    Profile
                  </Link>
                  <button onClick={handleLogout}>Sign out</button>
                </div>
              )}
            </div>
        ):(
        <>
        <Link to="/login">
          <button>Login</button>
        </Link>
        <Link to="/signup">
          <button>Sign up</button>
        </Link>
        </>
        )}
        <Link to="/cart">
          <img src={cart_icon} alt="" />
        </Link>
        <div className="cart-count">{getTotalCartItems()}</div>
      </div>
    </div>
  );
};

export default Navbar;
