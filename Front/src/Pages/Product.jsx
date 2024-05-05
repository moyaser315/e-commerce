import { useContext } from "react";
import { ShopContext } from "../Context/ShopContext";
import { useParams } from "react-router-dom";
import ProductDisplay from "../Components/ProductDisplay/ProductDisplay";
import DescriptionBox from "../Components/DescriptionBox/DescriptionBox";
import { ProductContext } from "../Context/ProductContext";

//import RelatedProducts from "../Components/RelatedProducts/RelatedProducts";

const Product = () => {
  const {products, loading} = useContext(ProductContext);
  const { productId } = useParams();
  const product = products?.find((e) => e.id === Number(productId));
  if (loading) {
    return <div>Loading...</div>
  }

  return (
    <div>
      <ProductDisplay product={product} />
      <DescriptionBox product={product}/>
      {/* Related Products */}
    </div>
  );
};

export default Product;
