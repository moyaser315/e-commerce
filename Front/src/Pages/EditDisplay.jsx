import "./EditDisplay.css";
import PropTypes from "prop-types";
import { useState } from "react";
import { Link } from "react-router-dom";

const EditDisplay = (props) => {
  const { product } = props;

  const [formData, setFormData] = useState({
    image: "",
    name: "",
    description: "",
    price: 0,
    quantity: 0,
    category: "Electronics & Devices",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    // TODO: Handle Error
    e.preventDefault();
    // Call a function to add the product to your data store
    // addProduct(formData);
    // Clear the form fields
    setFormData({
      image: "",
      name: "",
      description: "",
      price: 0,
      quantity: 0,
      category: "Electronics & Devices",
    });
  };

  return (
    <div className="editdisplay">
      <div className="editdisplay-left">
        <div className="editdisplay-img">
          {product && (
            <img
              className="editdisplay-main-img"
              src={product.imgPath}
              alt={formData.name}
            />
          )}
        </div>
        <h3>{formData.name}</h3>
        <p className="description">{formData.description}</p>
        <p>Quantity: {formData.quantity}</p>
        <div className="price">Price: ${formData.price}</div>
      </div>
      <div className="editdisplay-right">
        <form className="add-product-form" onSubmit={handleSubmit}>
          {" "}
          {/*TODO   Edit Product specified by seller*/}
          <p>Name</p>
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            placeholder="Product Name"
            required
          />
          <p>Description</p>
          <textarea
            name="description"
            value={formData.description}
            onChange={handleChange}
            placeholder="Description"
            required
          ></textarea>
          <p>Price</p>
          <input
            type="number"
            name="price"
            value={formData.price}
            onChange={handleChange}
            placeholder="Price"
            required
          />
          <p>Quantity</p>
          <input
            type="number"
            name="quantity"
            value={formData.quantity}
            onChange={handleChange}
            placeholder="Quantity"
            required
          />
          <p>Category</p>
          <select
            name="category"
            value={formData.category}
            onChange={handleChange}
            required
          >
            <option value="Electronics & Devices">Electronics & Devices</option>
            <option value="Clothes">Clothes</option>
            <option value="Accessories">Accessories</option>
          </select>
          <p>Image</p>
          <input
            type="text"
            name="image"
            value={formData.image}
            onChange={handleChange}
            placeholder="Image URL"
            required
          />
          <Link to="/products">
            <button type="submit" className="submit-btn">
              Submit
            </button>
          </Link>
        </form>
      </div>
    </div>
  );
};

EditDisplay.propTypes = {
  product: PropTypes.shape({
    id: PropTypes.number.isRequired,
    imgPath: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired,
    quantity: PropTypes.number.isRequired,
    price: PropTypes.number.isRequired,
    description: PropTypes.string,
  }).isRequired,
};

export default EditDisplay;
