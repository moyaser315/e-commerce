import { useContext } from "react"; // Import useContext from React
import PropTypes from "prop-types"; // Import PropTypes
import { ShopContext } from "../Context/ShopContext";
import Item from "../Components/Item/Item.jsx";
import Categories from "../Components/Categories/Categories.jsx";
import "./ShopCategory.css";

const ShopCategory = (props) => {
  const { products } = useContext(ShopContext);
  console.log(products);
  console.log(props.category);

  return (
    <>
      <Categories />
      <div className="shopcategory-products">
        {products.map((item, i) => {
          if (props.category === item.cat) {
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
          } else {
            return null;
          }
        })}
      </div>
    </>
  );
};

// Prop types validation
ShopCategory.propTypes = {
  category: PropTypes.string.isRequired, // Validate category prop
};

export default ShopCategory;
