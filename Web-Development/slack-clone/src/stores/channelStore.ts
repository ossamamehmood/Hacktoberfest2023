import { db } from "config/firebase";
import {
  addDoc,
  collection,
  DocumentData,
  FieldValue,
  getDocs,
  limit,
  onSnapshot,
  orderBy,
  query,
  QuerySnapshot,
  serverTimestamp,
  startAfter,
  where,
} from "firebase/firestore";
import { makeAutoObservable, reaction } from "mobx";
import { toast } from "react-toastify";
import { Channel } from "types/channel";
import { store } from "./store";

class ChannelStore {
  channelsRegistery = new Map<string, Channel>();
  selectedChannel: Channel | null = null;
  channelsLimit = 6;
  hasMore = false;
  lastChannelTimestamp: FieldValue | null = null;
  unsubscribeChannelsSnapshot?: () => void;

  constructor() {
    makeAutoObservable(this);

    reaction(
      () => this.selectedChannel,
      async (channel) => {
        if (channel) {
          store.messageStore.loadMessages(channel.id);
        }
      }
    );
  }

  reset = () => {
    this.channelsRegistery.clear();
    this.selectedChannel = null;
    this.channelsLimit = 6;
    this.hasMore = false;
    this.lastChannelTimestamp = null;

    this.unsubscribeChannelsSnapshot && this.unsubscribeChannelsSnapshot();
    this.unsubscribeChannelsSnapshot = undefined;
  };

  get channels() {
    return Array.from(this.channelsRegistery.values()).sort(
      (a, b) => b.timestamp?.getTime() - a.timestamp?.getTime()
    );
  }

  loadChannels = () => {
    if (this.channelsRegistery.size !== 0) {
      return;
    }

    const channelsQuery = query(
      collection(db, "channels"),
      orderBy("timestamp", "desc"),
      limit(this.channelsLimit)
    );

    this.unsubscribeChannelsSnapshot = onSnapshot(channelsQuery, (snapshot) => {
      this.setChannelsFromSnapshot(snapshot);
    });
  };

  loadMore = async () => {
    if (!this.hasMore) {
      return;
    }

    const channelsQuery = query(
      collection(db, "channels"),
      orderBy("timestamp", "desc"),
      startAfter(this.lastChannelTimestamp),
      limit(this.channelsLimit)
    );

    const channelsSnapshot = await getDocs(channelsQuery);
    this.setChannelsFromSnapshot(channelsSnapshot);
  };

  private setChannelsFromSnapshot = (snapshot: QuerySnapshot<DocumentData>) => {
    if (snapshot.size < this.channelsLimit) {
      this.hasMore = false;
    } else {
      this.hasMore = true;
    }

    snapshot.docs.forEach((doc) => {
      if (!this.lastChannelTimestamp) {
        this.lastChannelTimestamp = doc.data().timestamp;
      } else {
        const lastTimestamp = new Date(
          // @ts-ignore
          this.lastChannelTimestamp?.toDate()
        ).getTime();

        const currentTimestamp = new Date(
          doc.data().timestamp?.toDate()
        ).getTime();

        if (currentTimestamp < lastTimestamp) {
          this.lastChannelTimestamp = doc.data().timestamp;
        }
      }

      const channel = {
        id: doc.id,
        name: doc.data().name,
        timestamp: new Date(doc.data().timestamp?.toDate()),
      } as Channel;

      this.channelsRegistery.set(channel.id, channel);
    });
  };

  selectChannel = async (id: string) => {
    if (this.channelsRegistery.has(id)) {
      this.selectedChannel = this.channelsRegistery.get(id) as Channel;
    } else {
      this.selectedChannel = null;
    }
  };

  createChannel = async () => {
    const channelName = prompt("Please enter the channel name.");

    if (!channelName) {
      return;
    }

    const { user } = store.userStore;

    if (!user) {
      toast.error("An error occurred. Please try again.");
      return;
    }

    const exists = await this.channelExists(channelName);

    if (exists) {
      toast.error("Channel already exists.");
      return;
    }

    await addDoc(collection(db, "channels"), {
      name: channelName,
      timestamp: serverTimestamp(),
    });
  };

  private channelExists = async (channelName: string) => {
    const exists = !!this.channels.find(
      (channel) => channel.name === channelName
    );

    if (exists) {
      return true;
    }

    const channelsQuery = query(
      collection(db, "channels"),
      where("name", "==", channelName)
    );

    const channelsSnapshot = await getDocs(channelsQuery);

    if (!channelsSnapshot.empty) {
      return true;
    }

    return false;
  };
}

export default ChannelStore;
