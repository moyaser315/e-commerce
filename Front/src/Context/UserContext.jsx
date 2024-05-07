import { createContext, useState, useEffect } from 'react';

export const UserContext = createContext(null);

const UserProvider = ({ children }) => {
    const [user, setUser] = useState(() => JSON.parse(localStorage.getItem('user')) || null);

    useEffect(() => {
        localStorage.setItem('user', JSON.stringify(user));
    }, [user]);

    const value = {user, setUser};

    return (
        <UserContext.Provider value={value}>
            {children}
        </UserContext.Provider>
    );
};

export default UserProvider