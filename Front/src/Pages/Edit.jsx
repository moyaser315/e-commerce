import { useContext } from "react";
import { useParams } from "react-router-dom";
import { ProductContext } from "../Context/ProductContext";
import EditDisplay from "./EditDisplay.jsx";

const Edit = () => {
  const { products, loading } = useContext(ProductContext);
  const { productId } = useParams();
  const product = products?.find((e) => e.id === Number(productId));
  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <EditDisplay product={product} />
    </div>
  );
};

export default Edit;
