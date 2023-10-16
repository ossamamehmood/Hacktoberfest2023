import { observer } from "mobx-react-lite";
import React, { useState } from "react";
import { useStore } from "stores/store";
import styled from "styled-components";

const ChatInput = () => {
  const { selectedChannel } = useStore().channelStore;
  const { sendMessage } = useStore().messageStore;
  const [input, setInput] = useState("");

  const handleSendMessage = (
    e: React.MouseEvent<HTMLButtonElement, MouseEvent>
  ) => {
    e.preventDefault();

    if (input === "") {
      return;
    }
    const success = sendMessage(input);

    if (success) {
      setInput("");
    }
  };

  return (
    <StyledContainer>
      <StyledInput
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder={`Message #${selectedChannel?.name || ""}`}
        type="text"
      />
      <button hidden type="submit" onClick={handleSendMessage}>
        Send Message
      </button>
    </StyledContainer>
  );
};

export default observer(ChatInput);

const StyledContainer = styled.form`
  border-radius: 1.25rem;
  position: relative;
  display: flex;
  justify-content: center;
`;

const StyledInput = styled.input`
  position: fixed;
  bottom: 2rem;
  width: 60%;
  border: 1px solid gray;
  border-radius: 3px;
  padding: 1.25rem;
  outline: none;
`;
