import styled from 'styled-components'

export const ProjectItemBox = styled.div`
  display: flex;
  flex-direction: column;
  border: 1px solid grey;
  border-radius: 0.5rem;
  padding: 0.5rem;
  cursor: pointer;
  margin: 0.5rem 0rem;
`

export const ProjectItemModalContainer = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.5);
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
  background: ${({ theme }) => theme.body};
  filter: drop-shadow(4px 4px 4px rgba(0, 0, 0, 0.25));
  border-radius: 2rem;
  padding: 1rem;
  @media (max-width: 768px) {
    width: 18rem;
  }
`

export const ProjectItemModalCloseButton = styled.div`
  position: absolute;
  right: 1rem;
  cursor: pointer;
`

export const ProjectItemModalContent = styled.div`
  padding: 2rem 1rem;
`

export const ProjectItemModalBasicText = styled.p`
  font-size: 1rem;
  font-weight: bold;
`