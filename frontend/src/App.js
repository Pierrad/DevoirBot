import './App.css'
import React from 'react'

import ProjectListWrapper from './components/ProjectList/wrapper'


function App() {
  return (
    <div className="HighWrapper">
      <div className="Title">
        <h1>DevoirBot</h1>
      </div>
      <div className="ProjectList">
        <ProjectListWrapper />
      </div>
    </div>
  )
}

export default App