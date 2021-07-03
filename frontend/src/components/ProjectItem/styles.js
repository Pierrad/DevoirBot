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
  justify-content: center;
  align-items: center;
  width: 30rem;
  height: 20rem;
  position: fixed;
  z-index: 10;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  background-color: white;
  filter: drop-shadow(4px 4px 4px rgba(0, 0, 0, 0.25));
  border-radius: 2rem;
  padding: 1rem;
`