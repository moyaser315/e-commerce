import PropTypes from "prop-types";
import "./SellerItem.css";

const SellerItem = (props) => {
  return (
    <div className="row">
      <img src={props.image} alt={props.name} /> <hr />
      <div className="row-content">
        <h3>{props.name}</h3>
        <p>{props.description}</p>
        <p>Quantity: {props.quantity}</p>
        <div className="price-btn">
          <span>Price: ${props.price}</span>
        </div>
      </div>
    </div>
  );
};

// Prop types validation
SellerItem.propTypes = {
  image: PropTypes.string.isRequired,
  name: PropTypes.string.isRequired,
  description: PropTypes.string.isRequired,
  quantity: PropTypes.number.isRequired,
  price: PropTypes.number.isRequired,
  id: PropTypes.number.isRequired,
};

export default SellerItem;
