import { BrowserRouter as Router, Routes, Route } from 'react-router'
import SetList from './pages/SetList'
import SetDetail from './pages/SetDetail'
import CardDetail from './pages/CardDetail'
import './App.css'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<SetList />} />
        <Route path="/set/:setId" element={<SetDetail />} />
        <Route path="/card/:cardId" element={<CardDetail />} />
      </Routes>
    </Router>
  )
}

export default App
