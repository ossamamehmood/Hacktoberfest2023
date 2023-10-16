import Image from "next/image";
import styled from "styled-components";
import LoginSignInButton from "./LoginSignInButton";

const Login = () => (
  <StyledWrapper>
    <StyledContainer>
      <Image
        src="/images/logo.png"
        height={100}
        width={100}
        objectFit="contain"
        alt="logo"
      />
      <StyledTitle>Sign in now</StyledTitle>
      <LoginSignInButton />
    </StyledContainer>
  </StyledWrapper>
);

export default Login;

const StyledWrapper = styled.div`
  background: #f8f8f8;
  height: 100vh;
  display: grid;
  place-items: center;
`;

const StyledContainer = styled.div`
  padding: 6.25rem;
  text-align: center;
  background: white;
  border-radius: 0.75rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
`;

const StyledTitle = styled.h1``;
