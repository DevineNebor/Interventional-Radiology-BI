import { Plus } from 'lucide-react'

const ProcedureTypes: React.FC = () => {
  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">Types d'actes</h1>
          <p className="text-gray-600">Configuration des types de procédures</p>
        </div>
        <button className="btn-primary flex items-center space-x-2">
          <Plus size={20} />
          <span>Nouveau type</span>
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div className="card">
          <h3 className="text-lg font-medium text-gray-900">Angioplastie coronaire</h3>
          <p className="text-gray-600">Durée par défaut: 45 min</p>
          <p className="text-sm text-gray-500">Service: Cardiologie</p>
          <div className="mt-4 flex space-x-2">
            <button className="text-primary-600 hover:text-primary-900 text-sm">Modifier</button>
            <button className="text-red-600 hover:text-red-900 text-sm">Supprimer</button>
          </div>
        </div>

        <div className="card">
          <h3 className="text-lg font-medium text-gray-900">Scanner thoracique</h3>
          <p className="text-gray-600">Durée par défaut: 20 min</p>
          <p className="text-sm text-gray-500">Service: Radiologie</p>
          <div className="mt-4 flex space-x-2">
            <button className="text-primary-600 hover:text-primary-900 text-sm">Modifier</button>
            <button className="text-red-600 hover:text-red-900 text-sm">Supprimer</button>
          </div>
        </div>

        <div className="card">
          <h3 className="text-lg font-medium text-gray-900">IRM cérébrale</h3>
          <p className="text-gray-600">Durée par défaut: 30 min</p>
          <p className="text-sm text-gray-500">Service: Radiologie</p>
          <div className="mt-4 flex space-x-2">
            <button className="text-primary-600 hover:text-primary-900 text-sm">Modifier</button>
            <button className="text-red-600 hover:text-red-900 text-sm">Supprimer</button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default ProcedureTypes