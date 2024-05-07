import Navbar from "./Navbar";
import Cart from "./Pages/Cart";
import Dashboard from "./Pages/Dashboard";
import Login from "./Pages/Login";
import Product from "./Pages/Product";
import Signup from "./Pages/Signup";
import { AuthContext } from "./Context/AuthContext.jsx";
import { ProductProvider } from "./Context/ProductContext.jsx";
import UserProvider from "./Context/UserContext.jsx";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useState, useEffect } from "react";
import ShopCategory from "./Pages/ShopCategory.jsx";
import Footer from "./Components/Footer/Footer.jsx";
import SellerDashboard from "./Pages/SellerDashboard.jsx";
import PastOrders from "./Pages/PastOrders.jsx";
import Profile from "./Pages/Profile.jsx";
import MultiSearch from "./Pages/Search"; // Import the MultiSearch component
import SearchResults from "./Pages/SearchResults";
import Edit from "./Pages/Edit.jsx";
import OrderDetails from "./Pages/OrderDetails.jsx";

function App() {
  const [isLoggedIn, setLoggedIn] = useState(() => {
    const savedLoginStatus = localStorage.getItem("isLoggedIn");
    return savedLoginStatus ? JSON.parse(savedLoginStatus) : false;
  });

  useEffect(() => {
    localStorage.setItem("isLoggedIn", JSON.stringify(isLoggedIn));
  }, [isLoggedIn]);
  return (
    <AuthContext.Provider value={{ isLoggedIn, setLoggedIn }}>
      <UserProvider>
        <ProductProvider>
          <div>
            <BrowserRouter>
              <Navbar />
              <Routes>
                <Route path="/" element={<Dashboard />} />
                <Route
                  //TODO: electronics filter
                  path="/electronics"
                  element={<ShopCategory category="Electronics & Devices" />}
                />
                <Route
                  //TODO: clothes filter
                  path="/clothes"
                  element={<ShopCategory category="Clothes" />}
                />
                <Route
                  //TODO: accessories filter
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
                <Route path="/orders" element={<PastOrders />} />
                <Route path="/edit" element={<Edit />}>
                  <Route path=":productId" element={<Edit />} />
                </Route>
                <Route path="/search" element={<MultiSearch />} />{" "}
                {/* Route for the search page */}
                <Route
                  path="/search-results"
                  element={<SearchResults />}
                />{" "}
                {/* Define route for SearchResults component */}
                <Route path="/Order" element={<OrderDetails />}>
                  <Route path=":orderId" element={<OrderDetails />} />
                </Route>
              </Routes>
              <Footer />
            </BrowserRouter>
          </div>
        </ProductProvider>
      </UserProvider>
    </AuthContext.Provider>
  );
}

export default App;
