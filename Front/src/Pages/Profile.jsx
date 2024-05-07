import axios from "axios";
import { useEffect, useState } from "react";

const Profile = () => {
  const [user, setUser] = useState(null);
  const [products, setProducts] = useState(null);
  const [pdfLocation, setPdfLocation] = useState(null);

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const token = localStorage.getItem("accessToken");
        console.log(`Access token: ${token}`);
        const response = await axios.get("http://localhost:8000/dashboard", {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
        });
        if (response.data.user_info) {
          setUser(response.data.user_info);
          setProducts(response.data.products);
        } else {
          setUser(response.data);
        }
      } catch (error) {
        console.error("Error fetching user", error);
      }
    };

    fetchUser();
  }, []);

  const fetchReports = async () => {
    try {
      const url = `http://localhost:8000/report/`;
      const response = await axios.get(url, {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
        },
      });
      setPdfLocation(response.data.pdf_url); // Assuming response.data contains the PDF file location as a string
      const pdfUrl = response.data.pdf_url;

      if (pdfUrl) {
        // Open the PDF URL in a new tab
        window.open(pdfUrl, "_blank", "noopener,noreferrer");
      } else {
        console.error("Unexpected response format:", response.data);
      }
      console.log("PDF file location:", response.data);
    } catch (error) {
      // Handle error
      console.error("Error fetching reports:", error);
    }
  };

  if (!user) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <p>{user.name}</p>
      <p>This user is a {user.user_type}</p>
      <p>{user.email}</p>
      {user.user_type === "seller" && <p>Sellers Product: {products}</p>}
      <button onClick={fetchReports}>Genereate Reports</button>
    </div>
  );
};
export default Profile;
