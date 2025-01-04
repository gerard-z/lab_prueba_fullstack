// id: "sv3-1"
// name: "Oddish"
// images{ 
//   card_id: "sv3-1"
//   id: 533
//   type: "small"
//   url: "https://images.pokemontcg.io/sv3/1.png"
// }
// number: "1"
// rarity: "Common"
// set_id: "sv3"
// subtypes: ['Basic']
// supertype: "Pokémon"
// types: ['Grass']
import React from 'react'
import './CardView.css'

function CardView({card, width = 'auto', height = 'auto'}) {

  return (
    <div className='set-view' style={{width: width, height: height}}>
      <img className='set-image' src={card.images[0].url} alt={card.name} />
      <h1 className='set-name'>{card.name}</h1>
      <div className="set-info">
        <p className='set-date'><span>{card.release_date}</span></p>
        <p className='set-print'><span>{card.rarity}</span></p>
        <p className='set-total'>{card.subtypes.map(type => (
          <span key={type}>{type}</span>
        ))}</p>
        <p className='set-total'>{card.types.map(type => (
          <span key={type}>{type}</span>
        ))}</p>
        <p className='set-ptcgo'><span>{card.supertype}</span></p>        
      </div>
    </div>
  )
}

export default CardView