import PropTypes from "prop-types";
import "./Item.css";
import { Link } from "react-router-dom";

const Item = (props) => {
  return (
    <div className="card">
      <img src={props.image} alt={props.name} />
      <hr />
      <div className="card-content">
        <h3>{props.name}</h3>
        <p>{props.description}</p>
        <div className="price-btn">
          <span>Price: ${props.price}</span>
          <button>
            <Link to="/details">View Details</Link>
          </button>
        </div>
      </div>
    </div>
  );
};

// Prop types validation
Item.propTypes = {
  image: PropTypes.string.isRequired,
  name: PropTypes.string.isRequired,
  description: PropTypes.string.isRequired,
  price: PropTypes.number.isRequired,
};

export default Item;
