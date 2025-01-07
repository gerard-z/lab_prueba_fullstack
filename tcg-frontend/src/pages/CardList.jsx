import { useState, useEffect } from 'react'
import { Link, useSearchParams } from 'react-router'
import { API_URL } from '../components/utils/config'
import CardView from '../components/cards/CardView'
import Pagination from '../components/common/Pagination'
import SearchBar from '../components/common/SearchBar'
import './CardList.css'

function CardList() {
  const [cards, setCards] = useState([])
  const [currentPage, setCurrentPage] = useState(() => {
    // Recuperar la página guardada o usar 1 como valor predeterminado
    return parseInt(localStorage.getItem('cardListPage')) || 1
  })
  const [totalPages, setTotalPages] = useState(1)
  const [isLoading, setIsLoading] = useState(true)
  const cardsPerPage = 20 // Ajusta según necesites
  const [searchParams, setSearchParams] = useSearchParams()
  const searchQuery = searchParams.get('search') || ''

  useEffect(() => {
    const fetchTotalPages = async () => {
      console.log("searchQuery", searchQuery)
      try {
        let url = `${API_URL}/cards/size`
        if (searchQuery) {
          url = `${API_URL}/cards/search/count?q=${encodeURIComponent(searchQuery)}`
        }
        const response = await fetch(url)
        const data = await response.json()
        setTotalPages(Math.ceil(data.total / cardsPerPage))
      } catch (error) {
        console.error('Error al obtener el total de páginas:', error)
      }
    }
    localStorage.setItem('cardListPage', 1)
    fetchTotalPages()
  }, [searchQuery])

  useEffect(() => {
    const fetchCards = async () => {
      setIsLoading(true)
      try {
        let url = `${API_URL}/cards?skip=${(currentPage-1)*cardsPerPage}&limit=${cardsPerPage}`
        if (searchQuery) {
          url = `${API_URL}/cards/search?q=${encodeURIComponent(searchQuery)}&skip=${(currentPage-1)*cardsPerPage}&limit=${cardsPerPage}`
        }
        const response = await fetch(url)
        const data = await response.json()
        setCards(data)
      } catch (error) {
        console.error('Error al obtener las cartas:', error)
      }
      setIsLoading(false)
    }

    

    fetchCards()
  }, [currentPage, searchQuery])

  const handlePageChange = (newPage) => {
    setCurrentPage(newPage)
    localStorage.setItem('cardListPage', newPage)
    window.scrollTo(0, 0)
  }

  if (isLoading) return <div className="loading">Cargando...</div>

  return (
    <div className="container">
      {/* <SearchBar /> */}
      <h1>Lista de Cartas</h1>
      {cards.length === 0 ? (
        <p className="no-results">No se encontraron cartas</p>
      ) : (
        <>
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
        </>
      )}
    </div>
  )
}

export default CardList