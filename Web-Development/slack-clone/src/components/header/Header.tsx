import styled from "styled-components";
import HeaderInfo from "./info/HeaderInfo";
import HeaderOptions from "./options/HeaderOptions";
import HeaderSearch from "./search/HeaderSearch";

const Header = () => (
  <StyledHeader>
    <HeaderInfo />
    <HeaderSearch />
    <HeaderOptions />
  </StyledHeader>
);

export default Header;

const StyledHeader = styled.header`
  position: sticky;
  top: 0;
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding: 0.75rem 0;
  background-color: var(--slack-color);
  color: white;
`;
