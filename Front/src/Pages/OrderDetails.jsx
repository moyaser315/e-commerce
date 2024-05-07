import { useContext } from "react";
import { useParams } from "react-router-dom";
import { ProductContext } from "../Context/ProductContext.jsx";
import OrderDetailsDisplay from "./OrderDetailsDisplay.jsx";

const OrderDetails = () => {
  {
    /*TODO  Get orders of user*/
  }
  const { loading } = useContext(ProductContext);
  const { orderId } = useParams();

  const order = orders?.find((e) => e.id === Number(orderId));
  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <OrderDetailsDisplay order={order} />
    </div>
  );
};

export default OrderDetails;
