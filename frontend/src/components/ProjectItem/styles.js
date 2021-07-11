import styled from 'styled-components'

export const ProjectItemBox = styled.div`
  display: flex;
  flex-direction: column;
  border: 1px solid grey;
  border-radius: 0.5rem;
  padding: 0.5rem;
  cursor: pointer;
`

export const ProjectItemModal = styled.div`
  position: fixed;
  justify-content: center;
  align-items: center;
  width: 30rem;
  height: 20rem;
  z-index: 100;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
  filter: drop-shadow(4px 4px 4px rgba(0, 0, 0, 0.25));
  border-radius: 2rem;
  padding: 1rem;
`

export const ProjectItemModalCloseButton = styled.div`
  font-size: 2rem;
  border: 1px solid;
  position: absolute;
  right: 2rem;
  border-radius: 100%;
  padding: 0rem 0.8rem;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  p {
    margin: 0;
    margin-bottom: 0.2rem;
  }
`