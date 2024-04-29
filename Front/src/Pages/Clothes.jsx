import Item from "../Components/Item/Item.jsx";
import Categories from "../Components/Categories/Categories.jsx";
import "./Dashboard.css";
import data_product from "../assets/data.js";

const Clothes = () => {
  const clothesItems = data_product.filter(
    (item) => item.category === "Clothes"
  );

  return (
    <div>
      <Categories />
      <div className="cards">
        {clothesItems.map((item, i) => (
          <Item
            key={i}
            id={item.id}
            name={item.name}
            image={item.image}
            description={item.description}
            price={item.price}
            category={item.category}
          />
        ))}
      </div>
    </div>
  );
};

export default Clothes;
