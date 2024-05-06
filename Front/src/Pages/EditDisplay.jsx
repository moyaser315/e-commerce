import "./EditDisplay.css";
import PropTypes from "prop-types";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
const EditDisplay = (props) => {
  const { product } = props;
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    imgPath: "",
    name: "",
    description: "",
    price: 0,
    quantity: 0,
    cat: "Electronics & Devices",
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
    await handleEdit(formData);
  };

  const handleEdit = async (updatedData) => {
    
    try {
      const url = `http://localhost:8000/dashboard/${props.product.id}`;
      console.log("URL:", url, "Data:", updatedData);
      console.log("Product prop in EditDisplay:", props.product);
      const response = await axios.patch(url, updatedData, {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
        },
      });
      console.log("entered here")
      console.log(response.status)
      if (response.status === 200) {
        alert("Item updated successfully!");
        navigate("http://localhost:5173/products");
      }
    } catch (error) {
      console.error("Error updating item:", error );
      alert("Failed to update the item. Please try again.");
    }
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
            name="cat"
            value={formData.cat}
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
            name="imgPath"
            value={formData.imgPath}
            onChange={handleChange}
            placeholder="Image URL"
            required
          />
          
            <button type="submit" className="submit-btn">
              Submit
            </button>
         
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
    cat: PropTypes.string.isRequired
  }).isRequired,
};

export default EditDisplay;
