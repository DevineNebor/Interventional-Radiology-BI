import { LogOut, User } from 'lucide-react'
import { useAuth } from '../contexts/AuthContext'

interface HeaderProps {
  user: any
}

const Header: React.FC<HeaderProps> = ({ user }) => {
  const { logout } = useAuth()

  return (
    <header className="bg-white shadow-sm border-b border-gray-200">
      <div className="flex h-16 items-center justify-between px-4 sm:px-6 lg:px-8">
        <div className="flex items-center">
          <h2 className="text-lg font-medium text-gray-900">Medical BI</h2>
        </div>
        
        <div className="flex items-center space-x-4">
          <div className="flex items-center space-x-2">
            <User size={20} className="text-gray-400" />
            <span className="text-sm text-gray-700">{user?.email}</span>
          </div>
          
          <button
            onClick={logout}
            className="flex items-center space-x-2 text-gray-500 hover:text-gray-700"
          >
            <LogOut size={20} />
            <span className="text-sm">Déconnexion</span>
          </button>
        </div>
      </div>
    </header>
  )
}

export default Header