import React, { useState } from 'react'
import useDarkMode from 'use-dark-mode'

import * as SC from './styles'

function ProjectItem(props) {
  const { data } = props

  const [modalOpen, setModalOpen] = useState(false)
  const darkmode = useDarkMode(true)

  const handleClick = () => {
    setModalOpen(!modalOpen)
  }

  return (
    <>
      <SC.ProjectItemBox onClick={handleClick}>
        <p>{data.content}</p>
        <p>{data.date}</p>
      </SC.ProjectItemBox>
      {modalOpen && (
        <SC.ProjectItemModalContainer>
          <SC.ProjectItemModal>
            <SC.ProjectItemModalCloseButton onClick={handleClick}>
              {darkmode.value
                ? <img src="cancel_light.png" alt='Hide modal' />
                : <img src="cancel_black.png" alt='Hide modal' />
              }
            </SC.ProjectItemModalCloseButton>
            <SC.ProjectItemModalContent>
              <SC.ProjectItemModalBasicText>A faire : </SC.ProjectItemModalBasicText>
              <p>{data.content}</p>
              <SC.ProjectItemModalBasicText>Pour le : </SC.ProjectItemModalBasicText>
              <p>{data.date}</p>
            </SC.ProjectItemModalContent>
            
          </SC.ProjectItemModal>
        </SC.ProjectItemModalContainer>
      )}
    </>
  )
}

export default ProjectItem