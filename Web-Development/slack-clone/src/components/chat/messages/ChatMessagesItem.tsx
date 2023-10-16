import moment from "moment";
import Image from "next/image";
import React from "react";
import styled from "styled-components";
import { Message } from "types/message";

interface ChatMessagesItemProps {
  message: Message;
}

const ChatMessagesItem: React.FC<ChatMessagesItemProps> = ({ message }) => {
  const { photoURL, user, timestamp } = message;

  return (
    <StyledContainer>
      <StyledImage
        src={photoURL}
        width={50}
        height={50}
        objectFit="contain"
        alt="user"
      />
      <StyledContent>
        <StyledInfo>
          {user}
          <StyledDate>{moment(timestamp).format("lll")}</StyledDate>
        </StyledInfo>
        <StyledMessage>{message.message}</StyledMessage>
      </StyledContent>
    </StyledContainer>
  );
};

export default ChatMessagesItem;

const StyledContainer = styled.div`
  display: flex;
  align-items: center;
  padding: 1.25rem;
`;

const StyledImage = styled(Image)`
  border-radius: 0.5rem;
`;

const StyledContent = styled.div`
  padding-left: 0.5rem;
`;

const StyledInfo = styled.h4``;

const StyledMessage = styled.p``;

const StyledDate = styled.span`
  color: gray;
  font-weight: 300;
  margin-left: 0.25rem;
  font-size: 0.6rem;
`;
