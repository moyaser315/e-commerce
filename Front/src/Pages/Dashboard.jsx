import Item from "../Components/Item/Item.jsx";
import Categories from "../Components/Categories/Categories.jsx";
import "./Dashboard.css";
import { ProductContext } from "../Context/ProductContext";
import { useState, useEffect, useContext } from "react";
import axios from "axios";


const Dashboard = () => {
  const { products, loading} = useContext(ProductContext);

  if (!products) {
    return <div>Loading...</div>;
  }


  return (
    <ProductContext.Provider value={{ products, loading} }>
      <div>
        <Categories />
        <div className="cards">
          {products.map((item, i) => {
            return (
              <Item
                key={i}
                id={item.id}
                name={item.name}
                image={item.imgPath}
                description={item.description}
                price={item.price}
                category={item.category}
              />
            );
          })}
        </div>
      </div>
    </ProductContext.Provider>
  );
};

export default Dashboard;

