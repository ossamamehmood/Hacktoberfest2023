import { TextField } from "@material-ui/core";
import SearchIcon from "@material-ui/icons/Search";
import styled from "styled-components";

const HeaderSearch = () => (
  <StyledContainer>
    <SearchIcon />
    <StyledInput
      size="small"
      variant="filled"
      label="Search in MartsTech"
      InputProps={{ disableUnderline: true }}
    />
  </StyledContainer>
);

export default HeaderSearch;

const StyledContainer = styled.div`
  flex: 0.4;
  display: flex;
  align-items: center;
  padding: 0 3rem;
  border-radius: 6px;
  border: 1px gray solid;
  background-color: var(--header-search-color);
  color: gray;
  opacity: 1;
  text-align: center;
`;

const StyledInput = styled(TextField)`
  &&& {
    min-width: 100%;

    > label {
      color: gray;
    }

    > div > input {
      background-color: var(--header-search-color);
      color: white;
      border: none;
    }
  }
`;
