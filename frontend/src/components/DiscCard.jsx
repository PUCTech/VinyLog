import './DiscCard.css'

function DiscCard({ disc }) {
  const stars = '★'.repeat(disc.rating) + '☆'.repeat(5 - disc.rating)

  return (
    <article className="disc-card">
      <div className="disc-card__cover">
        <div className="disc-card__vinyl">
          <div className="disc-card__label" />
        </div>
        {disc.favorite && <span className="disc-card__favorite">♥</span>}
      </div>

      <h3 className="disc-card__title">{disc.title}</h3>
      <p className="disc-card__meta">
        {disc.artist} · {disc.year}
      </p>

      <div className="disc-card__footer">
        <span className="disc-card__stars" aria-label={`${disc.rating} de 5 estrelas`}>
          {stars}
        </span>
        <span
          className={
            disc.format === 'Vinil'
              ? 'disc-card__badge disc-card__badge--vinil'
              : 'disc-card__badge disc-card__badge--cd'
          }
        >
          {disc.format}
        </span>
      </div>
    </article>
  )
}

export default DiscCard