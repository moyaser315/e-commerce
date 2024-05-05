import { useContext } from "react";
import "./CartItems.css";
import remove_icon from "../../../public/removeicon.png";
import { ShopContext } from "../../Context/ShopContext.jsx";
import { Link } from "react-router-dom";

const CartItems = () => {
  const {
    getTotalCartAmount,
    all_product,
    cartItems,
    removeFromCart,
    clearCart,
  } = useContext(ShopContext);
  return (
    <div className="cartitems">
      <div className="cartitems-format-main">
        <p>Products</p>
        <p>Title</p>
        <p>Price</p>
        <p>Quantity</p>
        <p>Total</p>
        <p>Remove</p>
      </div>
      <hr />
      {all_product.map((e) => { //<-- we need to loop over the products
        // Get user's cart items
        if (cartItems[e.id] > 0) { //<-- instead of this
          return (
            <div key={e.id}>
              <div className="cartitems-format cartitems-format-main">
                <img src={e.image} alt="" className="carticon-product-icon" />
                <p>{e.name}</p>
                <p>${e.price}</p>
                <button className="cartitems-quantity">
                  {cartItems[e.id]}
                </button>
                <p>${e.price * cartItems[e.id]}</p>
                <img
                  className="cartitems-remove-icon"
                  src={remove_icon}
                  onClick={() => {
                    removeFromCart(e.id);
                  }}
                  alt=""
                />
              </div>
              <hr />
            </div>
          );
        }
        return null;
      })}
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
            <Link to="/">
              {/*To Do*/}
              <button
                onClick={() => {
                  clearCart();
                  alert("Your order has been completed successfully");
                }}
              >
                Checkout
              </button>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CartItems;
