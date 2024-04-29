import PropTypes from "prop-types";
import "./Item.css";
import { Link } from "react-router-dom";

const Item = (props) => {
  return (
    <div className="card">
      <Link to={`/product/${props.id}`}>
        <img src={props.image} alt={props.name} />{" "}
      </Link>
      <hr />
      <div className="card-content">
        <h3>{props.name}</h3>
        <p>{props.description}</p>
        <div className="price-btn">
          <span>Price: ${props.price}</span>
          <button>
            <Link to={`/product/${props.id}`}>View Details</Link>
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
  id: PropTypes.number.isRequired,
};

export default Item;
