import { useState, useEffect } from 'react'
import { Link } from 'react-router'
import { API_URL } from '../components/utils/config'
import CardView from '../components/cards/CardView'
import './CardList.css'

function CardList() {
  const [cards, setCards] = useState([])

  useEffect(() => {
    // Obtiene las cartas del set de la API
    const fetchCards = async () => {
      try {
        const response = await fetch(`${API_URL}/cards`)
        const data = await response.json()
        setCards(data)
      } catch (error) {
        console.error('Error al obtener las cartas:', error)
      }
    }
    fetchCards()
  }, [])

  return (
    <div className="container">
      <h1>Cartas del Set</h1>
      <div className="cards-grid">
        {cards.map(card => (
          <Link key={card.id} to={`/card/${card.id}`}>
            <CardView card={card} />
          </Link>
        ))}
      </div>
    </div>
  )
}

export default CardList