import React, { useState } from 'react'

import * as SC from './styles'

function ProjectItem(props) {
  const { data } = props

  const [modalOpen, setModalOpen] = useState(false)

  const handleClick = () => setModalOpen(!modalOpen)

  return (
    <>
      <SC.ProjectItemBox onClick={handleClick}>
        <p>{data.content}</p>
        <p>{data.date}</p>
      </SC.ProjectItemBox>
      {modalOpen && (
        <SC.ProjectItemModal>
          <p onClick={handleClick}>x</p>
          <p>{data.content}</p>
          <p>{data.date}</p>
        </SC.ProjectItemModal>
      )}
    </>
  )
}

export default ProjectItem