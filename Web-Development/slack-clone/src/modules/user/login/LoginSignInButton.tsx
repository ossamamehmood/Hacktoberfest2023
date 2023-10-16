import { Button } from "@material-ui/core";
import { useStore } from "stores/store";
import styled from "styled-components";

const LoginSignInButton = () => {
  const { signIn } = useStore().userStore;

  return <StyledButton onClick={signIn}>Sign in with Google</StyledButton>;
};

export default LoginSignInButton;

const StyledButton = styled(Button)`
  &&& {
    margin-top: 1rem;
    text-transform: inherit;
    background: #0a8d48;
    color: white;
  }
`;
