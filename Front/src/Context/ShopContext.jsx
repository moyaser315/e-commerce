import { createContext, useState, useContext, useEffect } from "react";
import PropTypes from "prop-types";
import { ProductContext } from "./ProductContext";
import axios from "axios";
import { hostname } from "../assets/globalVars";

export const ShopContext = createContext(null);

const getDefaultCart = () => {
  let cart = [];
  return cart;
};

const ShopContextProvider = (props) => {
  const [products, setProducts] = useState([]);
  useEffect(() => {
    const fetchData = async () => {
        try {
            const response = await axios.get("http://localhost:8000/", {
                headers: {
                    "Content-Type": "application/json",
                },
            });
            setProducts(response.data);
            setLoading(false);
            console.log(response.data);
        } catch (error) {
            console.error("Error fetching products", error);
        }
    };

    fetchData();
}, []);

  console.log(products);
  const [cartItems, setCartItems] = useState(getDefaultCart());
  const [edit, setEdit] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");
  useEffect(() => {
    const updateCartFromBackend = async () => {
        try {
          const cartItemsFromBackEnd = await axios.get(`${hostname}/cart`, {
            headers: { 'Content-Type': 'application/json' ,
            "Authorization": `Bearer ${localStorage.getItem("accessToken")}`
          },
          });

          setCartItems(cartItemsFromBackEnd.data);

          // console.log("response", response.data);
          console.log("backend", cartItemsFromBackEnd.data);
          setErrorMessage("")
          setEdit(false);
        } catch (error) {
          console.error('Failed to update cart in backend:', error);
          setEdit(false);
        }
    };
  
    updateCartFromBackend();
  }, []); 


  const addToCart = async (itemId) => {
    try {
      // Get the current state of the cart
      const cartResponse = await axios.get(
        `${hostname}/cart`,
        {
          headers: {
            "Authorization": `Bearer ${localStorage.getItem("accessToken")}`
          }
        }
      );
  
      // Find the item in the cart
      const existingItem = cartResponse.data.find((item) => item.productID === itemId);
  
      // If the item exists, increment its quantity, otherwise set it to 1
      const updatedQuantity = existingItem ? existingItem.quantity + 1 : 1;
  
      const updatedItem = { "productID": itemId, "quantity": updatedQuantity };
  
      // Send the updated item back to the backend
      const response = await axios.put(
        `${hostname}/cart`,
        updatedItem,
        {
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem("accessToken")}`
          }
        }
      );
  
      console.log("response", response.data);
      setEdit(true);
    } catch (error) {
      console.error(error);
      setErrorMessage(error.response.data.detail)
    }
  };

  /*To Test*/
  const removeFromCart = async (itemId) => {
    try {
      // Get the current state of the cart
      const cartResponse = await axios.get(
        `${hostname}/cart`,
        {
          headers: {
            "Authorization": `Bearer ${localStorage.getItem("accessToken")}`
          }
        }
      );
  
      // Find the item in the cart
      const existingItem = cartResponse.data.find((item) => item.productID === itemId);
  
      if (!existingItem) {
        // If the item doesn't exist in the cart, there's nothing to remove
        return;
      }
  
      // Decrement the item's quantity or set it to 0 if it's already 1
      existingItem.quantity = existingItem.quantity > 1 ? existingItem.quantity - 1 : 0;
  
      // Send the updated item back to the backend
      const response = await axios.put(
        `${hostname}/cart`,
        existingItem,
        {
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem("accessToken")}`
          }
        }
      );
  
      console.log("response", response.data);
      setEdit(true);
    } catch (error) {
      console.error(error);
      setErrorMessage(error.response.data.detail)
    }
  };
  /*To Test*/
  const clearCart = async () => {
    try {
      // Get the current state of the cart
      const cartResponse = await axios.get(
        `${hostname}/cart`,
        {
          headers: {
            "Authorization": `Bearer ${localStorage.getItem("accessToken")}`
          }
        }
      );
  
      // Set the quantity of each item to 0
      const updatedItems = cartResponse.data.map((item) => ({ ...item, quantity: 0 }));
  
      // Send the updated items back to the backend
      for (const item of updatedItems) {
        await axios.put(
          `${hostname}/cart`,
          item,
          {
            headers: {
              "Content-Type": "application/json",
              "Authorization": `Bearer ${localStorage.getItem("accessToken")}`
            }
          }
        );
      }
  
      console.log("Cart cleared");
      setEdit(true);
    } catch (error) {
      console.error(error);
      setErrorMessage(error.response.data.detail)
    }
  };

  const getTotalCartAmount = () => {
    let totalAmount = 0;
    cartItems.forEach((item) => {
      let product = products?.find((product) => product.id === item.productID);
      if (product) {
        totalAmount += product.price * item.quantity;
      }
      console.log("Total Amount", products);
    });

    return totalAmount;
  };

  const getTotalCartItems = () => {
    let totalItem = 0;
    cartItems.forEach((item) => {
      totalItem += item.quantity;
    });
    return totalItem;
  };
  useEffect(() => {
    const updateCartFromBackend = async () => {
      if (edit) {
        try {
          const cartItemsFromBackEnd = await axios.get(`${hostname}/cart`, {
            headers: { 'Content-Type': 'application/json' ,
            "Authorization": `Bearer ${localStorage.getItem("accessToken")}`
          },
          });

          setCartItems(cartItemsFromBackEnd.data);

          // console.log("response", response.data);
          console.log("backend", cartItemsFromBackEnd.data);
          setErrorMessage("")
          setEdit(false);
        } catch (error) {
          console.error('Failed to update cart in backend:', error);
          setEdit(false);
        }
      }
    };
  
    updateCartFromBackend();
  }, [edit]); 

  const contextValue = {
    getTotalCartItems,
    getTotalCartAmount,
    cartItems,
    addToCart,
    removeFromCart,
    clearCart,
    errorMessage
  };

  return (
    <ShopContext.Provider value={contextValue}>
      {props.children}
    </ShopContext.Provider>
  );
};

ShopContextProvider.propTypes = {
  children: PropTypes.node.isRequired,
};
export default ShopContextProvider;
