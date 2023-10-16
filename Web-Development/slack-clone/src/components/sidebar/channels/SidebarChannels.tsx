import { observer } from "mobx-react-lite";
import { useStore } from "stores/store";
import styled from "styled-components";
import SidebarChannelItem from "./SidebarChannelItem";

const SidebarChannels = () => {
  const { channels } = useStore().channelStore;

  return (
    <StyledContainer>
      {channels.map((channel) => (
        <SidebarChannelItem key={channel.id} channel={channel} />
      ))}
    </StyledContainer>
  );
};

export default observer(SidebarChannels);

const StyledContainer = styled.div``;
