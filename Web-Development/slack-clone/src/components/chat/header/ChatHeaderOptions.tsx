import styled from "styled-components";
import InfoOutlinedIcon from "@material-ui/icons/InfoOutlined";

const ChatHeaderOptions = () => (
  <StyledContainer>
    <StyledOption>
      <InfoOutlinedIcon /> Details
    </StyledOption>
  </StyledContainer>
);

export default ChatHeaderOptions;

const StyledContainer = styled.div``;

const StyledOption = styled.p`
  display: flex;
  align-items: center;
  font-size: 0.875rem;

  > svg {
    margin-right: 0.25rem;
    font-size: 1rem;
  }
`;
