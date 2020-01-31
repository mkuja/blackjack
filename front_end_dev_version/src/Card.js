import React from 'react';


function Card(props) {
   return (
      <img width="80px" src={props.src} className={props.className}
      />
   );

}

export default Card;