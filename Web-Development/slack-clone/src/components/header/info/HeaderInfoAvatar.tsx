import { Avatar } from "@material-ui/core";
import { useStore } from "stores/store";
import styled from "styled-components";

const HeaderInfoAvatar = () => {
  const { user, signOut } = useStore().userStore;

  return (
    <StyledAvatar onClick={signOut} src={user?.photoURL} alt="avatar">
      {user?.displayName[0]}
    </StyledAvatar>
  );
};

export default HeaderInfoAvatar;

const StyledAvatar = styled(Avatar)`
  cursor: pointer;
  text-transform: capitalize;

  :hover {
    opacity: 0.8;
  }
`;
