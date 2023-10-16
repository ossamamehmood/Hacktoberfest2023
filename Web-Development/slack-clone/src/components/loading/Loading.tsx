import { NoSsr } from "@material-ui/core";
import Image from "next/image";
import ClipLoader from "react-spinners/ClipLoader";
import styled from "styled-components";

const Loading = () => (
  <NoSsr>
    <StyledWrapper>
      <StyledContainer>
        <StyledImageContainer>
          <Image
            src="/images/logo.png"
            height={100}
            width={100}
            objectFit="contain"
            alt="logo"
          />
        </StyledImageContainer>

        <ClipLoader color="purple" size={60} />
      </StyledContainer>
    </StyledWrapper>
  </NoSsr>
);

export default Loading;

const StyledWrapper = styled.div`
  height: 100vh;
  display: grid;
  place-items: center;
`;

const StyledContainer = styled.div`
  padding-bottom: 6.25rem;
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const StyledImageContainer = styled.div`
  margin-bottom: 1rem;
`;
