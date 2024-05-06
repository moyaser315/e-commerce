import PropTypes from "prop-types";
import "./SellerItem.css";
import { Link } from "react-router-dom";

const SellerItem = (props) => {
  const handleDelete = () => {
    /* TODO  Set quantity of product to zero and delete it from database */
  };

  return (
    <div className="card">
      <img src={props.image} alt={props.name} />
      <div className="card-content">
        <h3>{props.name}</h3>
        <p className="description">{props.description}</p>
        <p>Quantity: {props.quantity}</p>
        <div className="price-btn">
          <span>Price: ${props.price}</span>
        </div>
        <div className="edit-delete">
          <Link to={`/edit/${props.id}`}>
            <button className="edit">Edit</button>
          </Link>
          <button className="delete" onClick={handleDelete}>
            Delete
          </button>
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
