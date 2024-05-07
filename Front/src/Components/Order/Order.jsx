import PropTypes from "prop-types";
import "./Order.css";
import { Link } from "react-router-dom";

const Order = (props) => {
  return (
    <div className="order-card">
      <p className="order-id">Order ID: {props.id}</p>
      <p className="total-cost">Total Cost: ${props.totalCost}</p>
      <Link to={`/Order/${props.id}`}>
        <button
          className="view-order-details"
          // onClick={() => viewDetails(item.id)}
        >
          View Details
        </button>
      </Link>
    </div>
  );
};

// Prop types validation
Order.propTypes = {
  id: PropTypes.number.isRequired,
  totalCost: PropTypes.number.isRequired,
};

export default Order;
