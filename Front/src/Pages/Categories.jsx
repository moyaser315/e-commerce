import { Link } from "react-router-dom";
import "./Categories.css";

const Categories = () => {
  return (
    <div className="category-selection">
      <button>
        <Link to="/electronics">Electronics & Devices</Link>
      </button>
      <button>
        <Link to="/clothes">Clothes</Link>
      </button>
      <button>
        <Link to="/accessories">Accessories</Link>
      </button>
      {/* Add more categories as needed */}
    </div>
  );
};

export default Categories;
