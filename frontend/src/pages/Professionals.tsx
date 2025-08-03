import { Plus } from 'lucide-react'

const Professionals: React.FC = () => {
  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">Professionnels</h1>
          <p className="text-gray-600">Gestion de l'équipe médicale</p>
        </div>
        <button className="btn-primary flex items-center space-x-2">
          <Plus size={20} />
          <span>Nouveau professionnel</span>
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div className="card">
          <h3 className="text-lg font-medium text-gray-900">Dr. Martin</h3>
          <p className="text-gray-600">Médecin - Cardiologie</p>
          <div className="mt-4 flex space-x-2">
            <button className="text-primary-600 hover:text-primary-900 text-sm">Modifier</button>
            <button className="text-red-600 hover:text-red-900 text-sm">Supprimer</button>
          </div>
        </div>

        <div className="card">
          <h3 className="text-lg font-medium text-gray-900">Dr. Dubois</h3>
          <p className="text-gray-600">Médecin - Radiologie</p>
          <div className="mt-4 flex space-x-2">
            <button className="text-primary-600 hover:text-primary-900 text-sm">Modifier</button>
            <button className="text-red-600 hover:text-red-900 text-sm">Supprimer</button>
          </div>
        </div>

        <div className="card">
          <h3 className="text-lg font-medium text-gray-900">Marie Dupont</h3>
          <p className="text-gray-600">Manipulatrice - Radiologie</p>
          <div className="mt-4 flex space-x-2">
            <button className="text-primary-600 hover:text-primary-900 text-sm">Modifier</button>
            <button className="text-red-600 hover:text-red-900 text-sm">Supprimer</button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Professionals