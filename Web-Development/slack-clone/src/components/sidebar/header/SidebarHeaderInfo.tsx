import FiberMenualRecordIcon from "@material-ui/icons/FiberManualRecord";
import { useStore } from "stores/store";
import styled from "styled-components";

const SidebarHeaderInfo = () => {
  const { user } = useStore().userStore;

  return (
    <StyledContainer>
      <StyledGroupTitle>MartsTech HQ</StyledGroupTitle>
      <StyledDisplayName>
        <StyledStatus />
        {user?.displayName}
      </StyledDisplayName>
    </StyledContainer>
  );
};

export default SidebarHeaderInfo;

const StyledContainer = styled.div`
  flex: 1;
`;

const StyledGroupTitle = styled.h2`
  font-size: 1rem;
  font-weight: 900;
  margin-bottom: 0.25rem;
`;

const StyledDisplayName = styled.h3`
  display: flex;
  align-items: center;
  font-size: 0.9rem;
  font-weight: 400;
`;

const StyledStatus = styled(FiberMenualRecordIcon)`
  &&& {
    font-size: 0.875rem;
    margin-top: 1px;
    margin-right: 2px;
    color: green;
  }
`;
