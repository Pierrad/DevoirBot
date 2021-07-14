import React, { useState, useEffect } from 'react'
import * as SC from './styles'
import PacmanLoader from "react-spinners/PacmanLoader"

import ProjectItem from '../ProjectItems/index'


function ProjectList(props) {
  const { data } = props
  const [color, setColor] = useState(null)
  const colorLoader = '#' + Math.floor(Math.random() * 16777215).toString(16)

  const loader = `
    display: block;
    margin: 0 auto;
  `

  useEffect(() => {
    if (data) { 
      setColor([...Array(Object.keys(data).length).keys()].map((key) => '#' + Math.floor(Math.random() * 16777215).toString(16)))
    } 
  }, [data])

  return (
    (data && (
      <SC.ProjectListBox>
        {Object.keys(data).map((key, i) => (
          <>
            <SC.ProjetListCard key={i}>
              <SC.ProjectListCardName color={color ? color[i] : '#000'}>{data[key].name}</SC.ProjectListCardName>
              <ProjectItem data={data[key].tasks} />
            </SC.ProjetListCard>
          </>
        ))}
      </SC.ProjectListBox>
    )) || <PacmanLoader color={colorLoader} loading={true} css={loader} size={40}/>
  )
}

export default ProjectList