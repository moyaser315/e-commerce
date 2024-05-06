import React from 'react';
import Item from "../Components/Item/Item.jsx";
import { useLocation } from 'react-router-dom';

const SearchResults = () => {
  const location = useLocation();
  const searchResults = location.state && location.state.searchResults;

  console.log(searchResults);

  return (
    <div>
      <h1>Search Results</h1>
      <div className="cards">
        {searchResults && searchResults.map((item, i) => (
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

export default SearchResults;




