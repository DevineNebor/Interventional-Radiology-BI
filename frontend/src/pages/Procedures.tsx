import { useState } from 'react'
import { Plus, Search, Filter } from 'lucide-react'

const Procedures: React.FC = () => {
  const [searchTerm, setSearchTerm] = useState('')

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">Procédures</h1>
          <p className="text-gray-600">Gestion des actes médicaux</p>
        </div>
        <button className="btn-primary flex items-center space-x-2">
          <Plus size={20} />
          <span>Nouvelle procédure</span>
        </button>
      </div>

      {/* Search and Filters */}
      <div className="flex space-x-4">
        <div className="flex-1">
          <div className="relative">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" size={20} />
            <input
              type="text"
              placeholder="Rechercher une procédure..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="input-field pl-10"
            />
          </div>
        </div>
        <button className="btn-secondary flex items-center space-x-2">
          <Filter size={20} />
          <span>Filtres</span>
        </button>
      </div>

      {/* Procedures Table */}
      <div className="card">
        <div className="overflow-x-auto">
          <table className="min-w-full divide-y divide-gray-200">
            <thead className="bg-gray-50">
              <tr>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Type d'acte
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Salle
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Professionnel
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Durée
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Date
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Actions
                </th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              <tr>
                <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                  Angioplastie coronaire
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  Salle 1
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  Dr. Martin
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  45 min
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  15/01/2024
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
                  <button className="text-primary-600 hover:text-primary-900">Modifier</button>
                </td>
              </tr>
              <tr>
                <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                  Scanner thoracique
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  Salle 2
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  Dr. Dubois
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  20 min
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  14/01/2024
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
                  <button className="text-primary-600 hover:text-primary-900">Modifier</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  )
}

export default Procedures