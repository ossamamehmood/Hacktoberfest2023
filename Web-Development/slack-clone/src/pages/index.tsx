import IsAuth from "modules/auth/IsAuth";
import Home from "modules/home/Home";
import { useEffect } from "react";
import { useStore } from "stores/store";

const HomePage = () => {
  const { channels, loadChannels } = useStore().channelStore;

  useEffect(() => {
    if (channels.length === 0) {
      loadChannels();
    }
  }, [channels, loadChannels]);

  return (
    <IsAuth>
      <Home />
    </IsAuth>
  );
};

export default HomePage;
