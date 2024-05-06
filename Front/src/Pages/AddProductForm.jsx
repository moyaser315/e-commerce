import { useState } from "react";
import PropTypes from "prop-types";
import "./AddProductForm.css";
import { hostname } from "../assets/globalVars.js";
import axios from "axios";

const AddProductForm = ({ addProduct }) => {
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

    try {
      const response = await axios.post(
        `${hostname}/dashboard/additem`,
        {
          name: formData.name,
          description: formData.description,
          price: formData.price,
          quantity: formData.quantity,
          cat: formData.category,
          imgPath: formData.image,
        },
        {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
          },
        }
      );

      console.log(response.data);
      // navigate("/dashboard");
    } catch (error) {
      console.error("Error creating user", error.response);
      // setErrorMessage("An error occured while creating the user. Please try again.")
    }
  };

  return (
    <form className="add-product-form" onSubmit={handleSubmit}>
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
      <button type="submit" className="submit-btn">
        Submit
      </button>
    </form>
  );
};

AddProductForm.propTypes = {
  addProduct: PropTypes.func.isRequired,
};

export default AddProductForm;
