import Header from "components/header/Header";
import Sidebar from "components/sidebar/Sidebar";
import React from "react";
import styled from "styled-components";

const DefaultLayout: React.FC = ({ children }) => (
  <StyledWrapper>
    <Header />
    <StyledBody>
      <Sidebar />
      {children}
    </StyledBody>
  </StyledWrapper>
);

export default DefaultLayout;

const StyledWrapper = styled.div`
  display: flex;
  flex-direction: column;
  height: 100vh;
`;

const StyledBody = styled.main`
  flex: 1;
  display: flex;
  overflow: hidden;
`;
