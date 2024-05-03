import "./DescriptionBox.css";

const DescriptionBox = () => {
  return (
    <div className="descriptionbox">
      <div className="descriptionbox-navigator">
        <div className="descriptionbox-nav-box">Description</div>
        <div className="descriptionbox-nav-box fade">Reviews (122) </div>
      </div>
      <div className="descriptionbox-description">
        <p>
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Aliquid
          pariatur atque tenetur iusto minima necessitatibus fugit voluptas
          sequi amet eum. Pariatur sed error minima, porro ut assumenda
          accusantium nulla. Dolorum?
        </p>
        <p>
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Veniam
          labore alias rerum unde dolorem molestiae aut maiores libero quasi
          corrupti voluptate magni dolorum, earum obcaecati fugit deserunt.
          Illo, error quam.
        </p>
      </div>
    </div>
  );
};

export default DescriptionBox;
