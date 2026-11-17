// Hero.jsx
import { Link } from 'react-router-dom'
import VinylDisc from './VinylDisc'
import ReviewCard from './ReviewCard'

function Hero() {
  return (
    <section className="hero">
      <div className="hero-text">
        <span className="tag">PARA COLECIONADORES</span>
        <h1>Sua coleção de discos e CDs, num só lugar.</h1>
        <p>O VinylLog é o site para catalogar suas mídias físicas...</p>
        <Link to="/cadastro" className="btn-primary">Criar minha conta</Link>
        <a href="#recursos">Saiba mais</a>
      </div>

      <div className="hero-visual">
        <VinylDisc />
        <ReviewCard
          title="Clube da Esquina"
          artist="Milton & Lô Borges"
          year={1972}
          stars={5}
          review="Diretamente de março de 1972, chiado charmoso. Uma das maiores obras do MPB.. Obra-prima!"
        />
      </div>
    </section>
  )
}

export default Hero