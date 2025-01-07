import { useState, useEffect } from 'react'
import { useParams } from 'react-router'
import { API_URL } from '../components/utils/config'
import './CardDetail.css'

function CardDetail() {
  const { cardId } = useParams()
  const [card, setCard] = useState(null)

  useEffect(() => {
    // Obtiene los detalles de la carta de la API
    const fetchCard = async () => {
      try {
        const response = await fetch(`${API_URL}/cards/${cardId}`)
        const data = await response.json()
        setCard(data)
      } catch (error) {
        console.error('Error al obtener los detalles de la carta:', error)
      }
    }
    fetchCard()
  }, [cardId])

  if (!card) return <div>Cargando...</div>

  return (
    <div className="card-detail-container">
      <div className="card-detail-grid">
        {/* Columna izquierda con la imagen */}
        <div className="card-image-container">
          <img 
            src={card.images.find(img => img.type === "large")?.url || card.images[0].url} 
            alt={card.name} 
            className="card-detail-image"
          />
        </div>

        {/* Columna derecha con la información */}
        <div className="card-info-container">
          <div className="card-header">
            <h1 className="card-title">{card.name}</h1>
            <span className="card-rarity">{card.rarity}</span>
          </div>

          <table className="card-specs-table">
            <tbody>
              <tr>
                <td className="spec-label">Supertipo:</td>
                <td>{card.supertype}</td>
              </tr>
              <tr>
                <td className="spec-label">Subtipos:</td>
                <td>{card.subtypes.join(", ")}</td>
              </tr>
              <tr>
                <td className="spec-label">Tipos:</td>
                <td>{card.types.join(", ")}</td>
              </tr>
              <tr>
                <td className="spec-label">Número:</td>
                <td>{card.number}</td>
              </tr>
            </tbody>
          </table>

          <div className="market-info">
            <h2 className="market-title">Información de Mercado</h2>
            <div className="market-links">
              {card.markets.map((market) => (
                <a 
                  key={market.id}
                  href={market.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="market-link"
                >
                  Ver precios en {market.market === 'tcgplayer' ? 'TCGPlayer' : 'Cardmarket'}
                </a>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default CardDetail