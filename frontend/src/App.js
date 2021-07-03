import './App.css'
import React from 'react'

import ProjectListWrapper from './components/ProjectList/wrapper'


function App() {
  return (
    <div className="HighWrapper">
      <header>
        <h1>DevoirBot</h1>
      </header>
      <div>
        <ProjectListWrapper />
      </div>
    </div>
  )
}

export default App