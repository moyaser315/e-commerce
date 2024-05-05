import { useState } from "react";
import AddProductForm from "./AddProductForm.jsx";
import "./SellerDashboard.css";
import data_product from "../assets/data.js";
import SellerItem from "../Components/SellerItem/SellerItem.jsx";

const SellerDashboard = () => {
  const [showForm, setShowForm] = useState(false);

  const toggleForm = () => {
    setShowForm(!showForm);
  };

  const filteredProducts = data_product.filter((item) => item.quantity > 0);

  return (
    <div className="seller-dashboard">
      <button className="add-product-btn" onClick={toggleForm}>
        Add Product
      </button>
      {showForm && <AddProductForm />}
      <h1>Your Products:</h1>
      <div className="product-cards">
        {filteredProducts.map((item, i) => (
          <SellerItem
            key={i}
            id={item.id}
            name={item.name}
            image={item.image}
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
