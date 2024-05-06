import "./CartItems.css";
import { useEffect, useState, Link, useContext } from "react";
import axios from "axios";
import remove_icon from "../../../public/removeicon.png";
import { hostname } from "../../assets/globalVars";
import { ShopContext } from "../../Context/ShopContext";
import { ProductContext } from "../../Context/ProductContext";

const CartItems = () => {
  const {
    getTotalCartAmount,
    cartItems,
    removeFromCart,
    clearCart,
    addToCart,
  } = useContext(ShopContext);
  const { products } = useContext(ProductContext);
  const [orderDetails, setOrderDetails] = useState(null);
  console.log(products);
  const handleCheckout = async () => {
    try {
      const response = await axios.get("http://localhost:8000/checkout", {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
        },
      });

      setOrderDetails(response.data);
      alert("Your order has been completed successfully");

      clearCart();
    } catch (error) {
      // Handle errors
      console.error("Error during checkout:", error);
      alert("Checkout failed. Please try again.");
    }
  };
  return (
    <div className="cartitems">
      <div className="cartitems-format-main">
        <p>Product</p>
        <p>Name</p>
        <p>Price</p>
        <p>Quantity</p>
        <p>Total</p>
        <p>Remove/Add</p>
      </div>
      <hr />
      {Array.isArray(products) &&
        cartItems.map((cartItem) => {
          const product = products.find(
            (product) => product.id === cartItem.productID
          );
          console.log(
            "Prodict ID:",
            cartItem.productID,
            "Matched product",
            product
          );
          return (
            <div key={cartItem.productID}>
              <div className="cartitems-format cartitems-format-main">
                <img
                  src={product.imgPath}
                  alt=""
                  className="carticon-product-icon"
                />
                <p>{product.name}</p>
                <p>${product.price}</p>
                <p>{cartItem.quantity}</p>
                <p>{product.price * cartItem.quantity}</p>
                <div className="cartitems-format button-container">
                  <button
                    className="remove"
                    onClick={() => removeFromCart(cartItem.productID)}
                  >
                    -
                  </button>
                  <button
                    className="add"
                    onClick={() => addToCart(cartItem.productID)}
                  >
                    +
                  </button>
                </div>
              </div>
            </div>
          );
        })}
      <hr />
      <div className="cartitems-down">
        <div className="cartitems-total">
          <h1>Cart Total</h1>
          <div>
            <div className="cartitems-total-item">
              <p>Subtotal</p>
              <p>${getTotalCartAmount()}</p>
            </div>
            <hr />
            <div className="cartitems-total-item">
              <p>Shipping Fee</p>
              <p>Free</p>
            </div>
            <hr />
            <div className="cartitems-total-item">
              <h3>Total</h3>
              <h3>${getTotalCartAmount()}</h3>
            </div>
          </div>
        </div>
        <div className="cartitems-payment">
          <p>Personal Details</p>
          <div className="cartitems-paymentbox">
            <input type="text" placeholder="Mobile Number" />
            <input type="text" placeholder="Address" />
            <input type="text" placeholder="Credit Card Number" />
            <hr />
            <button onClick={handleCheckout}>Checkout</button>
          </div>
        </div>
      </div>
      {orderDetails && (
        <div className="order-details">
          <h3>Order Details:</h3>
          <pre>{JSON.stringify(orderDetails, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default CartItems;
