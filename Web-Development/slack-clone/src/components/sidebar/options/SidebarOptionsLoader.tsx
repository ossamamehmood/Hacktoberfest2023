import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
import { observer } from "mobx-react-lite";
import { useStore } from "stores/store";
import SidebarOptionsItem from "./SidebarOptionsItem";

const SidebarOptionsLoader = () => {
  const { hasMore, loadMore } = useStore().channelStore;

  if (!hasMore) return null;

  return (
    <SidebarOptionsItem
      title="Load more"
      Icon={ExpandMoreIcon}
      onClick={loadMore}
    />
  );
};

export default observer(SidebarOptionsLoader);
