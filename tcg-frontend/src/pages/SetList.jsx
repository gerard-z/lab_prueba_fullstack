import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { API_URL } from '../components/utils/config'
function SetList() {
  const [sets, setSets] = useState([])

  useEffect(() => {
    // Obtiene los sets de la API
    const fetchSets = async () => {
      try {
        const response = await fetch(`${API_URL}/sets`)
        const data = await response.json()
        setSets(data)
      } catch (error) {
        console.error('Error al obtener los sets:', error)
      }
    }
    
    fetchSets()
  }, [])

  return (
    <div>
      <h1>Sets de TCG</h1>
      <div className="sets-grid">
        {sets.map(set => (
          <Link key={set.id} to={`/set/${set.id}`}>
            <div className="set-card">
              <h2>{set.name}</h2>
              {/* Más información del set */}
            </div>
          </Link>
        ))}
      </div>
    </div>
  )
}

export default SetList