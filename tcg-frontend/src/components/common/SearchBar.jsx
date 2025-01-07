import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router'
import './SearchBar.css'

function SearchBar() {
  const [searchQuery, setSearchQuery] = useState('')
  const navigate = useNavigate()

  useEffect(() => {
    const timeoutId = setTimeout(() => {
      if (searchQuery) {
        navigate(`/card?search=${encodeURIComponent(searchQuery)}`)
      } else {
        navigate(`/card`)
      }
    }, 300)

    return () => clearTimeout(timeoutId)
  }, [searchQuery])

  return (
    <div className="search-container">
      <input
        type="text"
        className="search-input"
        placeholder="Buscar por nombre o rareza..."
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
      />
    </div>
  )
}

export default SearchBar 