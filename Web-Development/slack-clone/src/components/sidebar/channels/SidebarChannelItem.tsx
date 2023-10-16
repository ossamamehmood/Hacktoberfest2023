import React from "react";
import { useStore } from "stores/store";
import styled from "styled-components";
import { Channel } from "types/channel";

interface SidebarChannelItemProps {
  channel: Channel;
}

const SidebarChannelItem: React.FC<SidebarChannelItemProps> = ({ channel }) => {
  const { id, name } = channel;
  const { selectChannel } = useStore().channelStore;

  return (
    <StyledContainer onClick={() => selectChannel(id)}>
      <StyledName>
        <StyledHash>#</StyledHash>
        {name}
      </StyledName>
    </StyledContainer>
  );
};

export default SidebarChannelItem;

const StyledContainer = styled.div`
  display: flex;
  align-items: center;
  font-size: 0.75rem;
  padding-left: 2px;
  cursor: pointer;

  :hover {
    opacity: 0.9;
    background-color: var(--sidebar-option-color);
  }
`;

const StyledName = styled.h3`
  padding: 0.75rem 0;
  font-weight: 400;
`;

const StyledHash = styled.span`
  padding: 1rem;
`;
