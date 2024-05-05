import PropTypes from "prop-types";
import "./Card.css";

const Card = ({ image, name, description, price }) => {
  return (
    <div className="card">
      <img src={image} alt={name} />
      <hr />
      <div className="card-content">
        <h3>{name}</h3>
        <p>Price: ${price}</p>
      </div>
    </div>
  );
};

// Prop types validation
Card.propTypes = {
  image: PropTypes.string,
  name: PropTypes.string.isRequired,
  description: PropTypes.string.isRequired,
  price: PropTypes.number.isRequired,
};

export default Card;
