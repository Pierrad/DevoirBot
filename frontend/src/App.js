import './App.css'
import React from 'react'

import ProjectListWrapper from './components/ProjectList/wrapper'


function App() {
  return (
    <div className="HighWrapper">
      <div>
        <h1>DevoirBot</h1>
      </div>
      <div>
        <ProjectListWrapper />
      </div>
    </div>
  )
}

export default App