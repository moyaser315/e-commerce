import React, { useState, useEffect } from "react";
import axios from "axios";

export const ProductContext = React.createContext();

export const ProductProvider = (props) => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://localhost:8000/", {
          headers: {
            "Content-Type": "application/json",
          },
        });
        setProducts(response.data);
        setLoading(false);
        console.log(response.data);
      } catch (error) {
        console.error("Error fetching products", error);
      }
    };

    fetchData();
  }, []);

  return (
    <ProductContext.Provider value={{ products, loading }}>
      {props.children}
    </ProductContext.Provider>
  );
};
