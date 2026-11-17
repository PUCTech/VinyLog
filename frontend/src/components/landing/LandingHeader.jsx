import { Link } from 'react-router-dom'
import logo from "../../assets/images/logo.png";
import './LandingHeader.css'

function LandingHeader() {
  return (
    <header className="landing-header">
      <img src={logo} alt="VinyLog" className="landing-logo" />
      <Link to="/login" className="landing-login-btn">Entrar</Link>
    </header>
  )
}

export default LandingHeader