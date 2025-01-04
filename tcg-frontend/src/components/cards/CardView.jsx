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
    <div className='card-view' style={{width: width, height: height}}>
      <img className='card-image' src={card.images[0].url} alt={card.name} />
      <h1 className='card-name'>{card.name}</h1>
      <div className="card-info">
        <p className='card-total'>{card.types.map(type => (
          <span key={type}>{type}</span>
        ))}</p>
        {/* <p className='set-ptcgo'><span>{card.supertype}</span></p> */}
      </div>
    </div>
  )
}

export default CardView