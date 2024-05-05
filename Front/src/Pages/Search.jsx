import React, { useState } from 'react';
import axios from 'axios'; 
import { useNavigate } from 'react-router-dom'; // Import useNavigate
import './Search.css'; 
import Dashboard from './Dashboard';

const MultiSearch = () => {
  const [searchResults, setSearchResults] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [error, setError] = useState(null); 
  const [loading, setLoading] = useState(false); 
  const navigate = useNavigate(); // Initialize useNavigate

  const handleSearch = async () => {
    setLoading(true); 
    setError(null); 
    try {
      const response = await axios.get(`http://localhost:8000?search=${searchTerm}`);
      const data = response.data;
      setSearchResults(data);

      if (data.length === 0) {
        alert('No results found'); 
      } else {
        // Navigate to /search-results with searchResults data as query parameter
        navigate('/search-results', { state: { searchResults: data } });
      }
    } catch (error) {
      console.error('Error fetching data:', error);
      setError('Failed to fetch data. Please try again.'); 
      alert('Failed to fetch data. Please try again.');
    } finally {
      setLoading(false); 
    }
  };

  return (
    <div>
      <div className="search-bar">
        <input
          type="text"
          placeholder="Search..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          onKeyPress={(e) => {
            if (e.key === 'Enter') {
              handleSearch(); 
            }
          }}
        />
        <button onClick={handleSearch} disabled={loading}>
          {loading ? 'Searching...' : 'Search'}
        </button>
      </div>
    </div>
  );
};

export default MultiSearch;



