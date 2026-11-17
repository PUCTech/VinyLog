// ReviewCard.jsx
function ReviewCard({ title, artist, year, review, stars }) {
  return (
    <div className="review-card">
      <h4>{title}</h4>
      <p>{artist} · {year}</p>
      <div>{"★".repeat(stars)}</div>
      <p>"{review}"</p>
    </div>
  )
}

export default ReviewCard