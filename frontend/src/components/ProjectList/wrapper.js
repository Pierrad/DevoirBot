import React, { useEffect, useState } from 'react';

import ProjectList from './index';

function ProjectListWrapper() {
  const [data, setData] = useState(null)

  useEffect(() => {
    fetch(`https://devoir-bot.herokuapp.com/projectWithTask`).then(res => res.json()).then(data => {
      setData(data.response)
    })
  }, [])

  return <ProjectList data={data}/>
}

export default ProjectListWrapper