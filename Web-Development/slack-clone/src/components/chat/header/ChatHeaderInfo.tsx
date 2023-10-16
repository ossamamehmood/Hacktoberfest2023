import StarBorderOutlinedIcon from "@material-ui/icons/StarBorderOutlined";
import { observer } from "mobx-react-lite";
import { useStore } from "stores/store";
import styled from "styled-components";

const ChatHeaderInfo = () => {
  const { selectedChannel } = useStore().channelStore;

  return (
    <StyledContainer>
      <StyledInfo>
        <StyledName>#{selectedChannel?.name}</StyledName>
        <StarBorderOutlinedIcon />
      </StyledInfo>
    </StyledContainer>
  );
};

export default observer(ChatHeaderInfo);

const StyledContainer = styled.div`
  display: flex;
  align-items: center;
`;

const StyledInfo = styled.h4`
  display: flex;
  text-transform: lowercase;
  margin-right: 1px;

  > svg {
    margin-left: 0.5rem;
    font-style: 1.125rem;
  }
`;

const StyledName = styled.strong``;
