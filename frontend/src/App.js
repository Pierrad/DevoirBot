import './App.css'
import React from 'react'
import useDarkMode from 'use-dark-mode'
import { ThemeProvider } from "styled-components"

import ProjectListWrapper from './components/ProjectList/wrapper'
import SwitchTheme from './components/SwitchTheme/index'
import { GlobalStyles, lightTheme, darkTheme } from "./Theme"


function App() {
  const darkmode = useDarkMode(true)
  const theme = darkmode.value ? darkTheme : lightTheme

  return (
    <ThemeProvider theme={theme}>
      <GlobalStyles />
      <div className="HighWrapper">
        <div className="Header">
          <h1>DevoirBot</h1>
          <SwitchTheme className="SwitchTheme"/>
        </div>
        <div className="ProjectList">
          <ProjectListWrapper />
        </div>
      </div>
    </ThemeProvider>
    
  )
}

export default App