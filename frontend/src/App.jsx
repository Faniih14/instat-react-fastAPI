import { useEffect, useState } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [message, setMessage] = useState('')
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    axios.get('http://localhost:8000/api/hello')
      .then(response => {
        setMessage(response.data.message)
        setLoading(false)
      })
      .catch(error => {
        console.error('Erreur:', error)
        setMessage('Erreur de connexion à FastAPI')
        setLoading(false)
      })
  }, [])

  return (
    <div className="text-center p-10">
      <h1 className="text-2xl font-bold text-blue-600">
        React + FastAPI
      </h1>
      <p className="mt-4 text-lg">
        Message de l'API : 
        {loading ? ' Chargement...' : ' ' + message}
      </p>
    </div>
  )
}

export default App