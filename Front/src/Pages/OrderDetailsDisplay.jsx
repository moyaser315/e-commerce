import PropTypes from "prop-types";
import Item from "../Components/Item/Item.jsx";
import "./Dashboard.css";

const OrderDetailsDisplay = (props) => {
  const { order } = props;

  return (
    <div>
      <div className="cards">
        {order.map((item, i) => {
          return (
            <Item
              key={i}
              id={item.id}
              name={item.name}
              image={item.imgPath}
              description={item.description}
              price={item.price}
              category={item.category}
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
