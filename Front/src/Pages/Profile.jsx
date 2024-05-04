import axios from "axios";
import { useEffect, useState} from "react";

const Profile = () => {
    const [user, setUser] = useState(null);
    const [products, setProducts] = useState(null);
    useEffect(() => {
        const fetchUser = async () => {
            try {
                const token = localStorage.getItem('accessToken');
                console.log(`Access token: ${token}`);
                const response = await axios.get('http://localhost:8000/dashboard/',
                {
                    headers: {
                        'Content-Type': 'application/json',
                        Authorization: `Bearer ${token}`,
                    },
                });
                if (response.data.user_info) {
                    setUser(response.data.user_info);
                    setProducts(response.data.products);
                }
                else {
                    setUser(response.data);
                }
            } catch (error) {
                console.error('Error fetching user', error);
            }
        };

        fetchUser();
    }, []);

    if (!user){
        return <div>Loading...</div>;
    }

    return (
        <div>
            <p>{user.name}</p>
            <p>This user is a {user.user_type}</p>
            <p>{user.email}</p>
            {user.user_type === 'seller' && <p>Sellers Product: {products}</p>}
        </div>
    );
};
export default Profile;
