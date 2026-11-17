import './Features.css'

const recursos = [
  {
    id: 1,
    titulo: 'Dados completos',
    texto: 'Artista, ano, gravadora, faixas e muito mais de cada item.',
  },
  {
    id: 2,
    titulo: 'Suas avaliações',
    texto: 'Dê notas e escreva resenhas sobre cada disco.',
  },
  {
    id: 3,
    titulo: 'Discos e CDs',
    texto: 'Organize todas as suas mídias físicas em um só lugar.',
  },
]

function Features() {
  return (
    <section className="features" id="recursos">
      <h2>Tudo sobre cada disco.</h2>

      <div className="features-grid">
        {recursos.map((item) => (
          <div key={item.id} className="feature-card">
            <h3>{item.titulo}</h3>
            <p>{item.texto}</p>
          </div>
        ))}
      </div>
    </section>
  )
}

export default Features