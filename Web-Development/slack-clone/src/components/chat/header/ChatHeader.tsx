import styled from "styled-components";
import ChatHeaderInfo from "./ChatHeaderInfo";
import ChatHeaderOptions from "./ChatHeaderOptions";

const ChatHeader = () => (
  <StyledContainer>
    <ChatHeaderInfo />
    <ChatHeaderOptions />
  </StyledContainer>
);

export default ChatHeader;

const StyledContainer = styled.div`
  position: sticky;
  top: 0;
  z-index: 10;
  background-color: white;
  display: flex;
  justify-content: space-between;
  padding: 1.25rem;
  border-bottom: 1px solid lightgray;
`;
