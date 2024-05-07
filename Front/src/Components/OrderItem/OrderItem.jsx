import PropTypes from "prop-types";
import "./OrderItem.css";

const OrderItem = (props) => {
  return (
    <div className="productcard">
      <img src={props.image} alt={props.name} />
      <div className="productcard-content">
        <h3>{props.name}</h3>
        <p className="description">{props.description}</p>
        <p>Quantity: {props.quantity}</p>
        <div className="price-tag">Price: ${props.price}</div>
      </div>
    </div>
  );
};

// Prop types validation
OrderItem.propTypes = {
  image: PropTypes.string.isRequired,
  name: PropTypes.string.isRequired,
  description: PropTypes.string.isRequired,
  category: PropTypes.string.isRequired,
  quantity: PropTypes.number.isRequired,
  price: PropTypes.number.isRequired,
  id: PropTypes.number.isRequired,
};

export default OrderItem;
