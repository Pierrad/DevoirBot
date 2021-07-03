import React from 'react'
import * as SC from './styles'

import ProjectItem from '../ProjectItems/index'

function ProjectList(props) {
  const { data } = props

  return (
    data && (
      <SC.ProjectListBox>
        {Object.keys(data).map((key) => (
          <SC.ProjetListCard>
            <SC.ProjectListCardName>{data[key].name}</SC.ProjectListCardName>
            <ProjectItem data={data[key].tasks} />
          </SC.ProjetListCard>
        ))}
      </SC.ProjectListBox>
    )
  )
}

export default ProjectList