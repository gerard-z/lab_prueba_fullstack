import React from 'react'
import './SetView.css'

const clearSetListPage = () => {
  localStorage.removeItem('setDetailPage')
}

function SetView({set, width = 'auto', height = 'auto'}) {

  return (
    <div  onClick={clearSetListPage} className='set-view' style={{width: width, height: height}}>
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