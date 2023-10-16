import HelpOutlinedIcon from "@material-ui/icons/HelpOutline";
import styled from "styled-components";

const HeaderOptions = () => (
  <StyledContainer>
    <HelpOutlinedIcon />
  </StyledContainer>
);

export default HeaderOptions;

const StyledContainer = styled.div`
  flex: 0.3;
  display: flex;
  align-items: flex-end;

  > svg {
    margin-left: auto;
    margin-right: 20px;
  }
`;
