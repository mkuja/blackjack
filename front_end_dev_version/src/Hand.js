import React, { Component } from 'react';
import './App.css';
import ButtonGroup from 'react-bootstrap/ButtonGroup'

class Hand extends Component {
   constructor(props){
      super(props);
      this.props = props;
      this.isSplit = props.isSplit ? " split-hand" : "";

   }

   render() {
      return(
         <div>
            <div className={"play-buttons" + this.isSplit}>{this.props.name}  {
               this.props.isDealer ?
                  "" :
                  <ButtonGroup>{this.props.buttons.map(button => button)}</ButtonGroup>
            }</div>
            <div className={"cards" + this.isSplit}>{this.props.cards.map(card => card)}</div>
         </div>
      )
   }
}

export default Hand