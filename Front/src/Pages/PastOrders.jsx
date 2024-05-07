import { useState, useEffect } from "react";
import Order from "../Components/Order/Order.jsx";
import axios from "axios";
import "./PastOrders.css";

const PastOrders = () => {
  const [user, setUser] = useState(null);
  const [orders, setOrders] = useState([]);

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
          setOrders(response.data.order_info);
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
    <div className="container">
      <h1>Your Orders:</h1>
      <div className="order-cards">
        {Array.isArray(orders) &&
          orders.map((item, i) => (
            <Order key={i} id={item.id} totalCost={item.totalCost} />
          ))}
      </div>
    </div>
  );
};

export default PastOrders;
