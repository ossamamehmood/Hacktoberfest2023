import AccessTimeIcon from "@material-ui/icons/AccessTime";
import styled from "styled-components";
import HeaderInfoAvatar from "./HeaderInfoAvatar";

const HeaderInfo = () => (
  <StyledContainer>
    <HeaderInfoAvatar />
    <AccessTimeIcon />
  </StyledContainer>
);

export default HeaderInfo;

const StyledContainer = styled.div`
  flex: 0.3;
  display: flex;
  align-items: center;
  margin-left: 1.25rem;

  > svg {
    margin-left: auto;
    margin-right: 1.75rem;
  }
`;
