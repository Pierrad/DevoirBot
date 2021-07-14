import React, { useEffect, useState } from 'react';

import ProjectList from './index';

function ProjectListWrapper() {
  const [data, setData] = useState(null)

  useEffect(() => {
    fetch(`${process.env.REACT_APP_API_URL}/projectWithTask`).then(res => res.json()).then(data => {
      setData(data.response)
    })
  }, [])

  return <ProjectList data={data}/>
}

export default ProjectListWrapper