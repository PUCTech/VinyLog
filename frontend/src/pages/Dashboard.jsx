import { useState } from 'react'
import DashboardHeader from '../components/DashboardHeader'
import DiscCard from '../components/DiscCard'
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
        <div
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))',
            gap: '20px',
          }}
        >
          {filteredDiscs.map((disc) => (
            <DiscCard key={disc.id} disc={disc} />
          ))}
        </div>
      </main>
    </div>
  )
}

export default Dashboard