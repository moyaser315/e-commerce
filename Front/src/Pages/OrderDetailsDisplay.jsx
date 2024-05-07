import PropTypes from "prop-types";
import "./Dashboard.css";
import OrderItem from "../Components/OrderItem/OrderItem.jsx";

const OrderDetailsDisplay = (props) => {
  const { order } = props;

  return (
    <div>
      <div className="cards">
        {order.map((item, i) => {
          return (
            <OrderItem
              key={i}
              id={item.id}
              name={item.name}
              image={item.imgPath}
              description={item.description}
              quantity={item.quantity}
              price={item.price}
            />
          );
        })}
      </div>
    </div>
  );
};

// Prop types validation
OrderDetailsDisplay.propTypes = {
  order: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      name: PropTypes.string.isRequired,
      imgPath: PropTypes.string.isRequired,
      description: PropTypes.string.isRequired,
      price: PropTypes.number.isRequired,
      category: PropTypes.string.isRequired,
    })
  ).isRequired,
};

export default OrderDetailsDisplay;
