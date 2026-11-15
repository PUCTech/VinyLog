import logo from '../assets/images/logo.png'
import { mockUser } from '../data/mockDiscs'
import './DashboardHeader.css'

function DashboardHeader({ search, onSearchChange }) {
  return (
    <header className="dashboard-header">
      <img src={logo} alt="VinyLog" className="dashboard-header__logo" />

      <input
        type="search"
        className="dashboard-header__search"
        placeholder="Buscar no seu acervo..."
        value={search}
        onChange={(e) => onSearchChange(e.target.value)}
      />

      <button type="button" className="dashboard-header__add">
        + Adicionar Disco
      </button>

      <div className="dashboard-header__avatar">{mockUser.initials}</div>
    </header>
  )
}

export default DashboardHeader