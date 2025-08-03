import { Routes, Route } from 'react-router-dom'
import { AuthProvider } from './contexts/AuthContext'
import PrivateRoute from './components/PrivateRoute'
import Layout from './components/Layout'
import Login from './pages/Login'
import Dashboard from './pages/Dashboard'
import Procedures from './pages/Procedures'
import Rooms from './pages/Rooms'
import Professionals from './pages/Professionals'
import ProcedureTypes from './pages/ProcedureTypes'

function App() {
  return (
    <AuthProvider>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/" element={<PrivateRoute><Layout /></PrivateRoute>}>
          <Route index element={<Dashboard />} />
          <Route path="procedures" element={<Procedures />} />
          <Route path="rooms" element={<Rooms />} />
          <Route path="professionals" element={<Professionals />} />
          <Route path="procedure-types" element={<ProcedureTypes />} />
        </Route>
      </Routes>
    </AuthProvider>
  )
}

export default App