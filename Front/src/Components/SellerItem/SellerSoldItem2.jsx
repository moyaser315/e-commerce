import PropTypes from "prop-types";
import "./SellerSoldItem2.css";

const SellerItem2 = (props) => {
  return (
    <div className="sellercard">
      <img src={props.image} alt={props.name} />
      <div className="sellercard-content">
        <h3>{props.name}</h3>
        <p className="description">{props.description}</p>
        <p>Units Sold: {props.quantity}</p>
        <div className="price">
          <span>Total Revenue: ${props.price}</span>
        </div>
      </div>
    </div>
  );
};

// Prop types validation
SellerItem2.propTypes = {
  image: PropTypes.string.isRequired,
  name: PropTypes.string.isRequired,
  description: PropTypes.string.isRequired,
  quantity: PropTypes.number.isRequired,
  price: PropTypes.number.isRequired,
  id: PropTypes.number.isRequired,
};

export default SellerItem2;
