import { mockDiscs, mockUser } from '../data/mockDiscs'

function Dashboard() {
  return (
    <div>
      <h1>Sua coleção, {mockUser.name}</h1>
      <ul>
        {mockDiscs.map((disc) => (
          <li key={disc.id}>
            {disc.title} - {disc.artist} ({disc.year}) - {disc.format}
          </li>
        ))}
      </ul>
    </div>
  )
}

export default Dashboard