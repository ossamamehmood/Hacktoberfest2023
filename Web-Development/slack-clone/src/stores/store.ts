import { createContext, useContext } from "react";
import ChannelStore from "./channelStore";
import MessageStore from "./messageStore";
import UserStore from "./userStore";

interface Store {
  userStore: UserStore;
  channelStore: ChannelStore;
  messageStore: MessageStore;
}

export const store: Store = {
  userStore: new UserStore(),
  channelStore: new ChannelStore(),
  messageStore: new MessageStore(),
};

export const StoreContext = createContext(store);

export const useStore = () => useContext(StoreContext);

export const resetStore = () => {
  const { userStore, channelStore, messageStore } = store;

  userStore.reset();
  channelStore.reset();
  messageStore.reset();
};
