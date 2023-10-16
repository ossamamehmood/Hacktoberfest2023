import { SvgIconTypeMap } from "@material-ui/core";
import { OverridableComponent } from "@material-ui/core/OverridableComponent";
import React from "react";
import styled from "styled-components";

interface SidebarOptionsItemProps {
  title: string;
  Icon: OverridableComponent<SvgIconTypeMap<{}, "svg">>;
  onClick?: () => any;
}

const SidebarOptionItem: React.FC<SidebarOptionsItemProps> = ({
  title,
  Icon,
  onClick,
}) => (
  <StyledContainer onClick={onClick}>
    <StyledIconContainer>
      <Icon fontSize="small" />
    </StyledIconContainer>
    <StyledTitle>{title}</StyledTitle>
  </StyledContainer>
);

export default SidebarOptionItem;

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

const StyledIconContainer = styled.div`
  margin: 0.75rem;
`;

const StyledTitle = styled.h3`
  font-weight: 500;
`;
