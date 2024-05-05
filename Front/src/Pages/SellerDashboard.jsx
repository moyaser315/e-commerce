import { useState, useEffect } from "react";
import AddProductForm from "./AddProductForm.jsx";
import "./SellerDashboard.css";
import SellerItem from "../Components/SellerItem/SellerItem.jsx";
import axios from "axios";

const SellerDashboard = () => {
  const [user, setUser] = useState(null);
  const [products, setProducts] = useState([]);
  const [showForm, setShowForm] = useState(false);

  const toggleForm = () => {
    setShowForm(!showForm);
  };
  useEffect(() => {
    const fetchUser = async () => {
      try {
        const token = localStorage.getItem("accessToken");
        console.log(`Access token: ${token}`);
        const response = await axios.get("http://localhost:8000/dashboard", {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
        });
        if (response.data.user_info) {
          setUser(response.data.user_info);
          setProducts(response.data.product);
          console.log(response.data.product);
        } else {
          setUser(response.data);
        }
      } catch (error) {
        console.error("Error fetching user", error);
      }
    };

    fetchUser();
  }, []);

  if (!user) {
    return <div>Loading...</div>;
  }

  return (
    <div className="seller-dashboard">
      <button className="add-product-btn" onClick={toggleForm}>
        Add Product
      </button>
      {showForm && <AddProductForm />}
      <h1>Your Products:</h1>
      <div className="product-cards">
        {Array.isArray(products) && products.map((item, i) => (
          <SellerItem
            key={i}
            id={item.id}
            name={item.name}
            image={item.imgPath}
            description={item.description}
            quantity={item.quantity}
            price={item.price}
            category={item.category}
          />
        ))}
      </div>
    </div>
  );
};

export default SellerDashboard;
