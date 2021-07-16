import React from 'react'
import useDarkMode from 'use-dark-mode'
import Switch from 'react-switch'

function SwitchTheme(props) {
  const { className } = props

  const darkmode = useDarkMode(true)

  const handleChange = () => {
    darkmode.toggle()
  }

  return (
    <Switch
      className={className}
      onChange={handleChange}
      checked={!darkmode.value}
      uncheckedHandleIcon={<img width="95%" src="moon.png" alt="Moon toggle"/>}
      checkedHandleIcon={<img width="95%" src="sun.png" alt="Sun toggle"/>}
      uncheckedIcon={false}
      checkedIcon={false}
      offColor="#8C30F5"
      onColor="#F6AE2D"
    />
  )
}

export default SwitchTheme
