import Navbar from "./Navbar";
import Cart from "./Pages/Cart";
import Dashboard from "./Pages/Dashboard";
import Login from "./Pages/Login";
import Product from "./Pages/Product";
import Signup from "./Pages/Signup";
import { AuthContext } from "./AuthContext";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useState } from "react";
import ShopCategory from "./Pages/ShopCategory.jsx";
import Footer from "./Components/Footer/Footer.jsx";
import SellerDashboard from "./Pages/SellerDashboard.jsx";
import Profile from "./Pages/Profile.jsx";
import MultiSearch from "./Pages/Search"; // Import the MultiSearch component
import SearchResults from "./Pages/SearchResults";

function App() {
  const [isLoggedIn, setLoggedIn] = useState(false);
  return (
    <AuthContext.Provider value={{ isLoggedIn, setLoggedIn }}>
      <div>
        <BrowserRouter>
          <Navbar />
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route
              path="/electronics"
              element={<ShopCategory category="Electronics" />}
            />
            <Route
              path="/clothes"
              element={<ShopCategory category="Clothes" />}
            />
            <Route
              path="/accessories"
              element={<ShopCategory category="Accessories" />}
            />
            <Route path="/product" element={<Product />}>
              <Route path=":productId" element={<Product />} />
            </Route>
            <Route path="/cart" element={<Cart />} />
            <Route path="/login" element={<Login />} />
            <Route path="/signup" element={<Signup />} />
            <Route path="/profile" element={<Profile />} />
            <Route path="/products" element={<SellerDashboard />} />
            <Route path="/search" element={<MultiSearch />} /> {/* Route for the search page */}
            <Route path="/search-results" element={<SearchResults />} /> {/* Define route for SearchResults component */}
          </Routes>
          <Footer />
        </BrowserRouter>
      </div>
    </AuthContext.Provider>
  );
}

export default App;
