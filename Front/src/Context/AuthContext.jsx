import React, { useState, useEffect } from 'react';

export const AuthContext = React.createContext({
  isLoggedIn: false,
  setLoggedIn: () => {},
});

export const AuthProvider = ({ children }) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    const loggedIn = localStorage.getItem('isLoggedIn');
    setIsLoggedIn(loggedIn === 'true');
  }, []);

  const setLoggedIn = (value) => {
    setIsLoggedIn(value);
    localStorage.setItem('isLoggedIn', value);
  };

  return (
    <AuthContext.Provider value={{ isLoggedIn, setLoggedIn }}>
      {children}
    </AuthContext.Provider>
  );
};