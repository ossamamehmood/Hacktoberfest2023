import { observer } from "mobx-react-lite";
import { useStore } from "stores/store";
import styled from "styled-components";
import ChatHeader from "./header/ChatHeader";
import ChatInput from "./input/ChatInput";
import ChatMessages from "./messages/ChatMessages";

const Chat = () => {
  const { selectedChannel } = useStore().channelStore;

  if (!selectedChannel) {
    return null;
  }

  return (
    <StyledContainer>
      <ChatHeader />
      <ChatMessages />
      <ChatInput />
    </StyledContainer>
  );
};

export default observer(Chat);

const StyledContainer = styled.section`
  flex: 0.7;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  overflow: scroll;

  ::-webkit-scrollbar {
    display: none;
  }
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
`;
