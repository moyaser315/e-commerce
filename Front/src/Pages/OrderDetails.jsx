import { useEffect, useState, useContext } from "react";
import { useParams } from "react-router-dom";
import { ProductContext } from "../Context/ProductContext.jsx";
import OrderDetailsDisplay from "./OrderDetailsDisplay.jsx";

const OrderDetails = () => {
  {
    /*TODO  Get orders of user*/
  }
  const { loading } = useContext(ProductContext);
  const { orderId } = useParams();

  const [order, setOrder] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const url = `http://localhost:8000/dashboard/${orderId}`;
        const response = await fetch(url, {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
          },
        });
        const data = await response.json();

        // Find the order in order_info array based on orderId
        // const foundOrder = data.order_info.find(
        //   (e) => e.id === Number(orderId)
        // );

        // Update the state with the found order
        setOrder(data);
      } catch (error) {
        console.error("Error fetching data: ", error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchData();
  }, [orderId]);
  if (isLoading || loading) {
    return <div>Loading...</div>;
  }

  if (!order) {
    return <div>No order found.</div>;
  }

  return (
    <div>
      <OrderDetailsDisplay order={order} />
    </div>
  );
};

export default OrderDetails;
