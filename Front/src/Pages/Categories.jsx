import { Link } from "react-router-dom";
import "./Categories.css";

const Categories = () => {
  return (
    <div className="category-selection">
      <Link to="/electronics">
        <button>Electronics & Devices</button>
      </Link>
      <Link to="/clothes">
        <button>Clothes</button>
      </Link>
      <Link to="/accessories">
        <button>Accessories</button>
      </Link>
      {/* Add more categories as needed */}
    </div>
  );
};

export default Categories;
