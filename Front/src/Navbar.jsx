import "./Navbar.css";
import { Link, useNavigate } from "react-router-dom";
import cart_icon from "/cart_icon.jpg";
import profile_icon from "/profile.png";
import logo from "/R.png";
import { useContext, useState } from "react";
import { ShopContext } from "./Context/ShopContext";
import MultiSearch from "./Pages/Search";
import { AuthContext } from "./Context/AuthContext";

const Navbar = () => {
  const { isLoggedIn, setLoggedIn } = useContext(AuthContext);
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const navigate = useNavigate;
  const handleLogout = () => {
    localStorage.removeItem("accessToken");
    setLoggedIn(false);
    setDropdownOpen(false);
    navigate("/");
  };
  const { getTotalCartItems } = useContext(ShopContext);
  return (
    <nav>
      <div className="navbar">
        <div className="nave-logo">
          <img src={logo} alt="" />
          <p>E-Commerce</p>
        </div>
        <ul className="nav-menu">
          <li>
            <Link className="link" to="/">
              Home
            </Link>
            <hr />
          </li>
          <li>
            {/* TODO: products link only visible to seller*/}
            <Link className="link" to="/products">
              Products
            </Link>
            <hr />
          </li>
        </ul>
        <MultiSearch />
        <div className="nav-cart-login-signup">
          {isLoggedIn ? (
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
          ) : (
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
    </nav>
  );
};

export default Navbar;
