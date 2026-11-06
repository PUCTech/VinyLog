import { useState } from 'react'
import DashboardHeader from '../components/DashboardHeader'
import { mockDiscs, mockUser } from '../data/mockDiscs'

function Dashboard() {
  const [search, setSearch] = useState('')

  const filteredDiscs = mockDiscs.filter((disc) => {
    const text = search.toLowerCase()
    return (
      disc.title.toLowerCase().includes(text) ||
      disc.artist.toLowerCase().includes(text)
    )
  })

  return (
    <div>
      <DashboardHeader search={search} onSearchChange={setSearch} />
      <main style={{ padding: '32px' }}>
        <h1>Sua coleção, {mockUser.name}</h1>
        <ul>
          {filteredDiscs.map((disc) => (
            <li key={disc.id}>
              {disc.title} - {disc.artist} ({disc.year}) - {disc.format}
            </li>
          ))}
        </ul>
      </main>
    </div>
  )
}

export default Dashboard