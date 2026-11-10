import './FilterTabs.css'

const FILTERS = ['Todos', 'Vinis', 'CDs', 'Favoritos']

function FilterTabs({ active, onChange }) {
  return (
    <div className="filter-tabs">
      {FILTERS.map((filter) => (
        <button
          key={filter}
          type="button"
          className={
            filter === active
              ? 'filter-tabs__button filter-tabs__button--active'
              : 'filter-tabs__button'
          }
          onClick={() => onChange(filter)}
        >
          {filter}
        </button>
      ))}
    </div>
  )
}

export default FilterTabs