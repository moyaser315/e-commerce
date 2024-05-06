import Navbar from "./Navbar";
import Cart from "./Pages/Cart";
import Dashboard from "./Pages/Dashboard";
import Login from "./Pages/Login";
import Product from "./Pages/Product";
import Signup from "./Pages/Signup";
import { AuthContext } from "./Context/AuthContext.jsx";
import  { ProductProvider } from "./Context/ProductContext.jsx";
import  ShopContextProvider  from "./Context/ShopContext.jsx";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useState, useEffect } from "react";
import ShopCategory from "./Pages/ShopCategory.jsx";
import Footer from "./Components/Footer/Footer.jsx";
import SellerDashboard from "./Pages/SellerDashboard.jsx";
import Profile from "./Pages/Profile.jsx";
import MultiSearch from "./Pages/Search"; // Import the MultiSearch component
import SearchResults from "./Pages/SearchResults";

function App() {
  const [isLoggedIn, setLoggedIn] = useState(() => {
    const savedLoginStatus = localStorage.getItem('isLoggedIn');
    return savedLoginStatus ? JSON.parse(savedLoginStatus) : false;
  });
  
  useEffect(() => {
    localStorage.setItem('isLoggedIn', JSON.stringify(isLoggedIn));
  }, [isLoggedIn]);
  return (
    <AuthContext.Provider value={{ isLoggedIn, setLoggedIn }}>
      <ProductProvider>
<<<<<<< HEAD
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
              </Routes>
              <Footer />
            </BrowserRouter>
          </div>
=======
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
>>>>>>> 657b80674f056a2e5e24505cb31c5aa1e91fe169
      </ProductProvider>
    </AuthContext.Provider>
  );
}

export default App;
