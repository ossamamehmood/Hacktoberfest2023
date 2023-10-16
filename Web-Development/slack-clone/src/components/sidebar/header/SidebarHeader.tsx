import CreateIcon from "@material-ui/icons/Create";
import styled from "styled-components";
import SidebarHeaderInfo from "./SidebarHeaderInfo";

const SidebarHeader = () => (
  <StyledContainer>
    <SidebarHeaderInfo />
    <CreateIcon />
  </StyledContainer>
);

export default SidebarHeader;

const StyledContainer = styled.div`
  display: flex;
  border-bottom: 1px solid var(--sidebar-color);
  padding: 0.75rem;

  > svg {
    background-color: white;
    color: var(--sidebar-color);
    border-radius: 50%;
    height: 2rem;
    width: 2rem;
    font-size: 1.125rem;
    padding: 0.4rem;
    margin-top: auto;
    margin-bottom: auto;
  }
`;
