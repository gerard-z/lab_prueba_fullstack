import './Pagination.css'

function Pagination({ currentPage, totalPages, onPageChange }) {
  const pages = []

  if (totalPages <= 1) {
    return null
  }
  
  // Crear array de páginas a mostrar
  for (let i = 1; i <= totalPages; i++) {
    if (
      i === 1 || // Primera página
      i === totalPages || // Última página
      (i >= currentPage - 2 && i <= currentPage + 2) // 2 páginas antes y después de la actual
    ) {
      pages.push(i)
    } else if (pages[pages.length - 1] !== '...') {
      pages.push('...')
    }
  }

  return (
    <div className="pagination">
      <button 
        onClick={() => onPageChange(currentPage - 1)}
        disabled={currentPage === 1}
        className="pagination-button"
      >
        Anterior
      </button>

      <div className="pagination-numbers">
        {pages.map((page, index) => (
          <button
            key={index}
            onClick={() => page !== '...' ? onPageChange(page) : null}
            className={`pagination-number ${
              page === currentPage ? 'active' : ''
            } ${page === '...' ? 'dots' : ''}`}
            disabled={page === '...'}
          >
            {page}
          </button>
        ))}
      </div>

      <button
        onClick={() => onPageChange(currentPage + 1)}
        disabled={currentPage === totalPages}
        className="pagination-button"
      >
        Siguiente
      </button>
    </div>
  )
}

export default Pagination 