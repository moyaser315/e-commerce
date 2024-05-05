import "./DescriptionBox.css";
import PropTypes from "prop-types";

const DescriptionBox = (props) => {
  const { product } = props;
  return (
    <div className="descriptionbox">
      <div className="descriptionbox-navigator">
        <div className="descriptionbox-nav-box">Description</div>
        <div className="descriptionbox-nav-box fade">Reviews (122) </div>
      </div>
      <div className="descriptionbox-description">
        <p>
          {product.description}
        </p>
      </div>
    </div>
  );
};

DescriptionBox.propTypes = {
  product: PropTypes.shape({
    description: PropTypes.string.isRequired,
  }).isRequired,
};

export default DescriptionBox;
