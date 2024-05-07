import PropTypes from "prop-types";

const Order = (props) => {
  return (
    <div>
      <div >
        <h3>{props.id}</h3>
        <div>
          <span>Total Cost: ${props.totalCost}</span>
        </div>
      </div>
    </div>
  );
};

// Prop types validation
Order.propTypes = {
  id: PropTypes.number.isRequired,
  totalCost: PropTypes.number.isRequired,
};

export default Order;
