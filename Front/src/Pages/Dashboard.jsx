import Item from "../Components/Item/Item.jsx";
import Categories from "../Components/Categories/Categories.jsx";
import "./Dashboard.css";
import data_product from "../assets/data.js";
import { useState, useEffect } from "react";
import axios from "axios";


const Dashboard = () => {
  const [products, setProducts] = useState(null);
  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await axios.get("http://localhost:8000/", {
          headers: {
            "Content-Type": "application/json",
          },
        });
        setProducts(response.data);
        console.log(response.data);
      } catch (error) {
        console.error("Error fetching products", error);
      }
    };

    fetchProducts();
  }, []);

  if (!products) {
    return <div>Loading...</div>;
  }


  return (
    <div>
      <Categories />
      <div className="cards">
        {products.map((item, i) => {
          return (
            <Item
              key={i}
              id={item.id}
              name={item.name}
              image={item.image}
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

export default Dashboard;

