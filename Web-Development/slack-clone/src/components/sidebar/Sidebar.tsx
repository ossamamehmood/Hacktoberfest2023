import styled from "styled-components";
import SidebarChannels from "./channels/SidebarChannels";
import SidebarHeader from "./header/SidebarHeader";
import SidebarOptions from "./options/SidebarOptions";
import SidebarOptionsLoader from "./options/SidebarOptionsLoader";

const Sidebar = () => (
  <StyledContainer>
    <SidebarHeader />
    <SidebarOptions />
    <SidebarChannels />
    <SidebarOptionsLoader />
  </StyledContainer>
);

export default Sidebar;

const StyledContainer = styled.section`
  width: 16rem;
  color: white;
  background-color: var(--slack-color);
  border-top: 1px solid var(--sidebar-color);
  overflow: scroll;

  ::-webkit-scrollbar {
    display: none;
  }
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
`;
