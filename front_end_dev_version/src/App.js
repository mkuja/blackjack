import React from 'react';
import Hand from './Hand';
import Card from './Card';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Button from 'react-bootstrap/Button';
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import divWithClassName from "react-bootstrap/cjs/divWithClassName";

let hand={
   name : 'Mikko',
   cards: [Card({src:require('./res/2H.png'), className: "first-card"}),
            Card({src:require('./res/6H.png'), className: "second-card"}),
            Card({src:require('./res/7H.png'), className: "third-card"}),
            Card({src:require('./res/AH.png'), className: "fourth-card"}),
            Card({src:require('./res/AH.png'), className: 'fifth-card'})],
   buttons: [React.createElement(Button, {variant:'primary', size:'sm'}, "More"),
            React.createElement(Button, {variant: 'primary', size:'sm'}, "Stay"),
            React.createElement(Button, {variant: 'secondary', size:'sm'}, "Split"),
            React.createElement(Button, {variant: 'secondary', size:'sm'}, "Insurance"),
            React.createElement(Button, {variant: 'secondary', size:'sm'}, "Give up")]
}

function isLoggedIn() {
   return false;
}

function logInDiv() {
   return(
      <div></div>
   )
}

function App() {
  return (
    <div className="main-container">
       {isLoggedIn() ? "true" : "false"}
       <div className="main-buttons">
         <ButtonGroup>
            <Button variant="secondary">New game</Button>
            <Button variant="secondary">Log in</Button>
            <Button variant="secondary">Stats</Button>
         </ButtonGroup>
       </div>
       <div className="player">
         <Hand name="Player" cards={hand.cards} buttons={hand.buttons}/>
         <Hand name="Player" isSplit cards={hand.cards} buttons={hand.buttons} className="split-hand"/>
       </div>
       <div className="player">
          <Hand name={"Computer"} cards={hand.cards} buttons={hand.buttons} isDealer />
       </div>
    </div>
  );
}

export default App;
