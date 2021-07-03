import styled from 'styled-components'

export const ProjectListBox = styled.div`
  display: flex;
  width: 100%;
`

export const ProjetListCard = styled.div`
  display: flex;
  flex-direction: column;
  padding: 3rem 2rem;
  border-radius: 0.5rem;
  border: 1px solid black;
  // height: 10rem;
  margin: 0 2rem;
  transition: all 0.2s ease 0s;
  &:hover {
    transform: translateY(-2px);
    box-shadow: rgba(84, 84, 84, 0.2) 0px 5px 30px;
  }
`

export const ProjectListCardName = styled.p`
  font-size: 2rem;
  margin: 0;
`
