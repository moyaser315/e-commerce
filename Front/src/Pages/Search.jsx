import React, { useState } from 'react';
import './Search.css'; // Import the CSS file

const MultiSearch = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState([]);

  const handleSearch = async () => {
    try {
      // Fetch data from the API
      const response = await fetch(`localhost:8000?search=${searchTerm}`);
      const data = await response.json();

      // Perform the search operation on the fetched data
      const results = data.filter(item =>
        item.title.toLowerCase().includes(searchTerm.toLowerCase())
      );

      // Update the searchResults state with the filtered results
      setSearchResults(results);
    } catch (error) {
      console.error('Error fetching data:', error);
      // Handle error gracefully (e.g., display an error message)
    }
  };

  return (
    <div className="search-bar">
      <input
        type="text"
        placeholder="Search..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />
      <button onClick={handleSearch}>Search</button>
      <ul>
        {searchResults.map((result) => (
          <li key={result.id}>{result.title}</li>
        ))}
      </ul>
    </div>
  );
};

export default MultiSearch;
