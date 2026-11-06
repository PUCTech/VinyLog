import { useState } from 'react'
import DashboardHeader from '../components/DashboardHeader'
import DiscCard from '../components/DiscCard'
import StatCard from '../components/StatCard'
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

  const totalItems = mockDiscs.length
  const totalVinis = mockDiscs.filter((disc) => disc.format === 'Vinil').length
  const totalCDs = mockDiscs.filter((disc) => disc.format === 'CD').length
  const totalRated = mockDiscs.filter((disc) => disc.rating > 0).length

  return (
    <div>
      <DashboardHeader search={search} onSearchChange={setSearch} />
      <main style={{ padding: '32px' }}>
        <h1>Sua coleção, {mockUser.name}</h1>

        <div
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))',
            gap: '20px',
            margin: '24px 0 32px',
          }}
        >
          <StatCard
            label="Total de itens"
            value={totalItems}
            caption="discos no acervo"
          />
          <StatCard
            label="Formatos"
            value={`${totalCDs} CDs | ${totalVinis} Vinis`}
            caption="divisão do acervo"
          />
          <StatCard
            label="Avaliações"
            value={totalRated}
            caption="itens avaliados"
          />
        </div>

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