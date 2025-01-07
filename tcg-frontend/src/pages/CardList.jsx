import { useState, useEffect } from 'react'
import { Link } from 'react-router'
import { API_URL } from '../components/utils/config'
import CardView from '../components/cards/CardView'
import Pagination from '../components/common/Pagination'
import './CardList.css'

function CardList() {
  const [cards, setCards] = useState([])
  const [currentPage, setCurrentPage] = useState(1)
  const [totalPages, setTotalPages] = useState(1)
  const [isLoading, setIsLoading] = useState(true)
  const cardsPerPage = 20 // Ajusta según necesites

  useEffect(() => {
    const fetchTotalCards = async () => {
      const response = await fetch(`${API_URL}/cards/size`)
      const data = await response.json()
      setTotalPages(Math.ceil(data.total / cardsPerPage))
    }
    fetchTotalCards()
  }, [])

  useEffect(() => {
    const fetchCards = async () => {
      setIsLoading(true)
      try {
        const response = await fetch(
          `${API_URL}/cards?skip=${(currentPage-1)*cardsPerPage}&limit=${cardsPerPage}`
        )
        const data = await response.json()
        setCards(data)
      } catch (error) {
        console.error('Error al obtener las cartas:', error)
      }
      setIsLoading(false)
    }
    fetchCards()
  }, [currentPage, cardsPerPage])

  const handlePageChange = (newPage) => {
    setCurrentPage(newPage)
    window.scrollTo(0, 0)
  }

  if (isLoading) return <div className="loading">Cargando...</div>

  return (
    <div className="container">
      <h1>Lista de Cartas</h1>
      <div className="cards-grid">
        {cards.map(card => (
          <Link key={card.id} to={`/card/${card.id}`}>
            <CardView card={card} />
          </Link>
        ))}
      </div>
      
      <Pagination 
        currentPage={currentPage}
        totalPages={totalPages}
        onPageChange={handlePageChange}
      />
    </div>
  )
}

export default CardList