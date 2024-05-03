import Navbar from "./Navbar";
import Cart from "./Pages/Cart";
import Dashboard from "./Pages/Dashboard";
import Login from "./Pages/Login";
import Product from "./Pages/Product";
import Profile from "./Pages/Profile";
import Signup from "./Pages/Signup";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ShopCategory from "./Pages/ShopCategory.jsx";
import Footer from "./Components/Footer/Footer.jsx";

function App() {
  return (
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
        </Routes>
        <Footer />
      </BrowserRouter>
    </div>
  );
}

export default App;
