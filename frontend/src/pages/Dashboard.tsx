import { useState, useEffect } from 'react'
import { Activity, Clock, Users, TrendingUp } from 'lucide-react'

interface KPI {
  total_procedures: number
  total_duration: number
  average_duration: number
  daily_procedures: Array<{ date: string; count: number }>
  procedures_by_type: Array<{ procedure_type_id: number; count: number }>
}

const Dashboard: React.FC = () => {
  const [kpi, setKpi] = useState<KPI | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // TODO: Fetch KPI data from API
    // For now, using mock data
    setTimeout(() => {
      setKpi({
        total_procedures: 156,
        total_duration: 2340,
        average_duration: 15.0,
        daily_procedures: [
          { date: '2024-01-01', count: 8 },
          { date: '2024-01-02', count: 12 },
          { date: '2024-01-03', count: 10 },
        ],
        procedures_by_type: [
          { procedure_type_id: 1, count: 45 },
          { procedure_type_id: 2, count: 32 },
          { procedure_type_id: 3, count: 28 },
        ]
      })
      setLoading(false)
    }, 1000)
  }, [])

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
      </div>
    )
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900">Tableau de bord</h1>
        <p className="text-gray-600">Vue d'ensemble de l'activité médicale</p>
      </div>

      {/* KPI Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div className="card">
          <div className="flex items-center">
            <div className="flex-shrink-0">
              <Activity className="h-8 w-8 text-primary-600" />
            </div>
            <div className="ml-4">
              <p className="text-sm font-medium text-gray-500">Total Procédures</p>
              <p className="text-2xl font-semibold text-gray-900">
                {kpi?.total_procedures || 0}
              </p>
            </div>
          </div>
        </div>

        <div className="card">
          <div className="flex items-center">
            <div className="flex-shrink-0">
              <Clock className="h-8 w-8 text-green-600" />
            </div>
            <div className="ml-4">
              <p className="text-sm font-medium text-gray-500">Durée Totale</p>
              <p className="text-2xl font-semibold text-gray-900">
                {kpi?.total_duration || 0}h
              </p>
            </div>
          </div>
        </div>

        <div className="card">
          <div className="flex items-center">
            <div className="flex-shrink-0">
              <TrendingUp className="h-8 w-8 text-blue-600" />
            </div>
            <div className="ml-4">
              <p className="text-sm font-medium text-gray-500">Durée Moyenne</p>
              <p className="text-2xl font-semibold text-gray-900">
                {kpi?.average_duration || 0}min
              </p>
            </div>
          </div>
        </div>

        <div className="card">
          <div className="flex items-center">
            <div className="flex-shrink-0">
              <Users className="h-8 w-8 text-purple-600" />
            </div>
            <div className="ml-4">
              <p className="text-sm font-medium text-gray-500">Professionnels</p>
              <p className="text-2xl font-semibold text-gray-900">12</p>
            </div>
          </div>
        </div>
      </div>

      {/* Charts Section */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="card">
          <h3 className="text-lg font-medium text-gray-900 mb-4">
            Activité quotidienne
          </h3>
          <div className="h-64 flex items-center justify-center text-gray-500">
            Graphique en cours de développement...
          </div>
        </div>

        <div className="card">
          <h3 className="text-lg font-medium text-gray-900 mb-4">
            Répartition par type d'acte
          </h3>
          <div className="h-64 flex items-center justify-center text-gray-500">
            Graphique en cours de développement...
          </div>
        </div>
      </div>

      {/* Recent Activity */}
      <div className="card">
        <h3 className="text-lg font-medium text-gray-900 mb-4">
          Activité récente
        </h3>
        <div className="space-y-4">
          <div className="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
            <div>
              <p className="font-medium text-gray-900">Angioplastie coronaire</p>
              <p className="text-sm text-gray-500">Salle 1 - Dr. Martin</p>
            </div>
            <div className="text-right">
              <p className="text-sm font-medium text-gray-900">45 min</p>
              <p className="text-xs text-gray-500">14:30</p>
            </div>
          </div>
          
          <div className="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
            <div>
              <p className="font-medium text-gray-900">Scanner thoracique</p>
              <p className="text-sm text-gray-500">Salle 2 - Dr. Dubois</p>
            </div>
            <div className="text-right">
              <p className="text-sm font-medium text-gray-900">20 min</p>
              <p className="text-xs text-gray-500">13:15</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Dashboard