import "./ProductDisplay.css";
import star_icon from "../../../public/star.png";
import star_dull_icon from "../../../public/stardull.png";
import PropTypes from "prop-types";
import { useContext } from "react";
import { ShopContext } from "../../Context/ShopContext";

const ProductDisplay = (props) => {
  const { product } = props;
  const { addToCart } = useContext(ShopContext);

  return (
    <div className="productdisplay">
      <div className="productdisplay-left">
        <div className="productdisplay-img-list">
        {product && <img src={product.imgPath} alt="" />}
        {product && <img src={product.imgPath} alt="" />}
        {product && <img src={product.imgPath} alt="" />}
        {product && <img src={product.imgPath} alt="" />}
        </div>
        <div className="productdisplay-img">
        {product && <img className="productdisplay-main-img" src={product.imgPath} alt="" />}        </div>
      </div>
      <div className="productdisplay-right">
        {product && <h1>{product.name}</h1>}
        <div className="productdisplay-right-stars">
          <img src={star_icon} alt="" />
          <img src={star_icon} alt="" />
          <img src={star_icon} alt="" />
          <img src={star_icon} alt="" />
          <img src={star_dull_icon} alt="" />
          <p>(122)</p>
        </div>
        <div className="productdisplay-right-prices">
          {product && <div className="productdisplay-right-price">${product.price}.00</div>}
        </div>
        <div className="productdisplay-right-description">
          Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quis debitis
          aspernatur nam, at libero voluptates fuga quam praesentium blanditiis
          sapiente harum vel dolore beatae facilis nobis accusantium totam
          soluta optio.
        </div>
        <div className="productdisplay-right-color">
          <h1>Select Color</h1>
          <div className="productdisplay-right-colors">
            <div>White</div>
            <div>Black</div>
            <div>Grey</div>
            <div>Blue</div>
            <div>Red</div>
          </div>
        </div>
        <button
          onClick={() => {
            addToCart(product.id);
          }}
        >
          ADD TO CART
        </button>
      </div>
    </div>
  );
};

ProductDisplay.propTypes = {
  product: PropTypes.shape({
    id: PropTypes.number.isRequired,
    imgPath: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired,
  }).isRequired,
};

export default ProductDisplay;
