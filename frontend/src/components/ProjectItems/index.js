import React from 'react'
import * as SC from './styles'

import ProjectItem from '../ProjectItem/index'

function ProjectItems(props) {
  const { data } = props

  return (
    <div>{data.map((d, key) => <ProjectItem key={key} data={d}/> )}</div>
  )
}

export default ProjectItems