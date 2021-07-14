import styled from 'styled-components'

export const ProjectListBox = styled.div`
  display: flex;
  width: 100%;
  flex-wrap: wrap;
  justify-content: center;
`

export const ProjetListCard = styled.div`
  display: flex;
  flex-direction: column;
  padding: 2rem 2rem;
  border-radius: 0.5rem;
  border: 1px solid black;
  height: 12rem;
  width: 10rem;
  margin: 0 2rem 1rem 0;
  transition: all 0.2s ease 0s;
  overflow: scroll;
  &:hover {
    box-shadow: rgba(84, 84, 84, 0.2) 0px 5px 30px;
  }
  @media (max-width: 768px) {
    margin: 0 0 1rem 0;
  }
`

export const ProjectListCardName = styled.p`
  font-size: 2rem;
  margin: 0;
  color: ${(props) => props.color};
`
