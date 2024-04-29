import { useContext } from "react"; // Import useContext from React
import PropTypes from "prop-types"; // Import PropTypes
import { ShopContext } from "../Context/ShopContext";
import Item from "../Components/Item/Item.jsx";
import Categories from "../Components/Categories/Categories.jsx";

const ShopCategory = (props) => {
  const { all_product } = useContext(ShopContext);

  return (
    <>
      <Categories />
      <div className="shopcategory-products">
        {all_product.map((item, i) => {
          if (props.category === item.category) {
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
