// id: "sve"
// logo_url: "https://images.pokemontcg.io/sve/logo.png"
// name: "Scarlet & Violet Energies"
// printed_total: 16
// ptcgo_code: "SVE"
// release_date: "2023-03-31"
// series: "Scarlet & Violet"
// symbol_url: "https://images.pokemontcg.io/sve/symbol.png"
// total: 16
// updated_at: "2024-09-19 19:45:00"
import React from 'react'
import './SetView.css'

function SetView({set, width = 'auto', height = 'auto'}) {

  return (
    <div className='set-view' style={{width: width, height: height}}>
      <img className='set-image' src={set.logo_url} alt={set.name} />
      <h1 className='set-name'><img className='set-symbol' src={set.symbol_url} alt={set.name} />{set.name}</h1>
      <div className="set-info">
        <p className='set-date'>Fecha de lanzamiento: <span>{set.release_date}</span></p>
        <p className='set-print'>Cartas impresas: <span>{set.printed_total}</span></p>
        <p className='set-total'>Cartas totales: <span>{set.total}</span></p>
        <p className='set-ptcgo'>Código PTCGO: <span>{set.ptcgo_code}</span></p>        
      </div>
    </div>
  )
}

export default SetView