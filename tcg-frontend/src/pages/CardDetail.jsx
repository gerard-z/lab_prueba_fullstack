import { useState, useEffect } from 'react'
import { useParams } from 'react-router'
import { API_URL } from '../components/utils/config'

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
    <div className="card-detail">
      <h1>{card.name}</h1>
      <img src={card.images[0].url} alt={card.name} />
      <div className="card-info">
        {/* Aquí irán todos los detalles de la carta */}
      </div>
    </div>
  )
}

export default CardDetail