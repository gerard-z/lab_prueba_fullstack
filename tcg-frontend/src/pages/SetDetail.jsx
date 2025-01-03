import { useState, useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'
import { API_URL } from '../components/utils/config'

function SetDetail() {
  const { setId } = useParams()
  const [cards, setCards] = useState([])

  useEffect(() => {
    // Obtiene las cartas del set de la API
    const fetchCards = async () => {
      try {
        const response = await fetch(`${API_URL}/sets/${setId}/cards`)
        const data = await response.json()
        setCards(data)
      } catch (error) {
        console.error('Error al obtener las cartas del set:', error)
      }
    }
    fetchCards()
  }, [setId])

  return (
    <div>
      <h1>Cartas del Set</h1>
      <div className="cards-grid">
        {cards.map(card => (
          <Link key={card.id} to={`/card/${card.id}`}>
            <div className="card-item">
              <h3>{card.name}</h3>
            </div>
          </Link>
        ))}
      </div>
    </div>
  )
}

export default SetDetail