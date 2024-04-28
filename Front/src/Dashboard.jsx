import Card from "./Card.jsx";
import Categories from "./Categories.jsx";
import photo from "../../public/iphone.jpeg";
import "./Dashboard.css";

const Dashboard = () => {
  return (
    <div>
      <Categories />
      <div className="cards">
        <Card image={photo} name="Name" description="Description" price="100" />
        <Card image={photo} name="Name" description="Description" price="100" />
        <Card image={photo} name="Name" description="Description" price="100" />
        <Card image={photo} name="Name" description="Description" price="100" />
        <Card image={photo} name="Name" description="Description" price="100" />
        <Card image={photo} name="Name" description="Description" price="100" />
        <Card image={photo} name="Name" description="Description" price="100" />
        <Card image={photo} name="Name" description="Description" price="100" />
      </div>
    </div>
  );
};

export default Dashboard;
