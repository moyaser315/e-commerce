import PropTypes from "prop-types";
import axios from "axios";
import { useEffect, useState, useContext } from "react";
import "./SellerItem.css";
import { Link } from "react-router-dom";

const SellerItem = (props) => {
  const handleDelete = async () => {
    /* TODO  Set quantity of product to zero and delete it from database */
    try {
      const url = `http://localhost:8000/dashboard/${props.id}`;
      console.log(url);
      const response = await axios.delete(url, {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
        },
      });

      if (response.status === 204) {
        alert("Item deleted successfully!");
        window.location.reload();
      }
    } catch (error) {
      console.error("Error deleting item:", error);
      alert("Failed to delete the item. Please try again.");
    }
  };

  return (
    <div className="sellercard">
      <img src={props.image} alt={props.name} />
      <div className="sellercard-content">
        <h3>{props.name}</h3>
        <p className="description">{props.description}</p>
        <p>Quantity: {props.quantity}</p>
        <div className="price">
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
