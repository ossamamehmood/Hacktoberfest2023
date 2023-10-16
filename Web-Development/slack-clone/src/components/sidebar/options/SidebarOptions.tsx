import AddIcon from "@material-ui/icons/Add";
import AppsIcon from "@material-ui/icons/Apps";
import BookmarkBorderIcon from "@material-ui/icons/BookmarkBorder";
import DraftsIcon from "@material-ui/icons/Drafts";
import ExpandLessIcon from "@material-ui/icons/ExpandLess";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
import FileCopyIcon from "@material-ui/icons/FileCopy";
import InboxIcon from "@material-ui/icons/Inbox";
import InsertCommentIcon from "@material-ui/icons/InsertComment";
import PeopleAltIcon from "@material-ui/icons/PeopleAlt";
import { useStore } from "stores/store";
import styled from "styled-components";
import SidebarOptionItem from "./SidebarOptionsItem";

const SidebarOptions = () => {
  const { createChannel } = useStore().channelStore;

  return (
    <StyledContainer>
      <SidebarOptionItem title="Threads" Icon={InsertCommentIcon} />
      <SidebarOptionItem title="Mentions & reactions" Icon={InboxIcon} />
      <SidebarOptionItem title="Saved items" Icon={DraftsIcon} />
      <SidebarOptionItem title="Channel browser" Icon={BookmarkBorderIcon} />
      <SidebarOptionItem title="People & user groups" Icon={PeopleAltIcon} />
      <SidebarOptionItem title="Apps" Icon={AppsIcon} />
      <SidebarOptionItem title="File browser" Icon={FileCopyIcon} />
      <SidebarOptionItem title="Show less" Icon={ExpandLessIcon} />
      <StyledSeparator />
      <SidebarOptionItem title="Channels" Icon={ExpandMoreIcon} />
      <StyledSeparator />
      <SidebarOptionItem
        title="Add Channel"
        Icon={AddIcon}
        onClick={createChannel}
      />
    </StyledContainer>
  );
};

export default SidebarOptions;

const StyledContainer = styled.div``;

const StyledSeparator = styled.hr`
  margin: 0.75rem 0;
  border: 1px solid var(--sidebar-color);
`;
