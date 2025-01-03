import { Link, NavLink, BrowserRouter as Router, Routes, Route } from 'react-router'
import SetList from './pages/SetList'
import SetDetail from './pages/SetDetail'
import CardDetail from './pages/CardDetail'
import { useTheme } from './hooks/utils/useTheme'
import { FaMoon, FaSun } from 'react-icons/fa'
import './App.css'

function App() {

  const { nightMode, toggleNightMode } = useTheme()

  return (
    <Router>
      <header>    
        <Link to="/">Pokemon Trading Card Game</Link>
        <nav>
          <NavLink  to="/">Inicio</NavLink >
          <NavLink  to="/cards">Cartas</NavLink >
          <button onClick={toggleNightMode} className="night-mode-button">
            {nightMode ? <FaSun className="text-yellow-500 text-2xl" /> : <FaMoon className="text-gray-500 text-2xl" />}
          </button>
        </nav>
      </header>
      <Routes>
        <Route path="/" element={<SetList />} />
        <Route path="/set/:setId" element={<SetDetail />} />
        <Route path="/card/:cardId" element={<CardDetail />} />
      </Routes>
    </Router>
  )
}

export default App
