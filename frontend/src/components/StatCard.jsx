import './StatCard.css'

function StatCard({ label, value, caption }) {
  return (
    <div className="stat-card">
      <span className="stat-card__label">{label}</span>
      <strong className="stat-card__value">{value}</strong>
      <span className="stat-card__caption">{caption}</span>
    </div>
  )
}

export default StatCard