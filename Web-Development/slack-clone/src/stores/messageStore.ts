import { db } from "config/firebase";
import {
  addDoc,
  collection,
  doc,
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
} from "firebase/firestore";
import { makeAutoObservable } from "mobx";
import { toast } from "react-toastify";
import { Message } from "types/message";
import { store } from "./store";

class MessageStore {
  messagesRegistery = new Map<string, Message>();
  messagesLimit = 10;
  hasMore = false;
  lastMessageTimestamp: FieldValue | null = null;
  unsubscribeMessagesSnapshot?: () => void;

  constructor() {
    makeAutoObservable(this);
  }

  reset = () => {
    this.messagesRegistery.clear();
    this.messagesLimit = 10;
    this.hasMore = false;
    this.lastMessageTimestamp = null;

    this.unsubscribeMessagesSnapshot && this.unsubscribeMessagesSnapshot();
    this.unsubscribeMessagesSnapshot = undefined;
  };

  get messages() {
    return Array.from(this.messagesRegistery.values())
      .sort((a, b) => a.timestamp?.getTime() - b.timestamp?.getTime())
      .reverse();
  }

  loadMessages = async (id: string) => {
    this.messagesRegistery.clear();
    this.unsubscribeMessagesSnapshot && this.unsubscribeMessagesSnapshot();

    const channelRef = doc(db, "channels", id);
    const messagesRef = collection(channelRef, "messages");

    const messagesQuery = query(
      messagesRef,
      orderBy("timestamp", "desc"),
      limit(this.messagesLimit)
    );

    this.unsubscribeMessagesSnapshot = onSnapshot(messagesQuery, (snapshot) => {
      this.setMessagesFromSnapshot(snapshot);
    });
  };

  loadMore = async () => {
    if (!this.hasMore) {
      return;
    }

    const { selectedChannel } = store.channelStore;

    if (!selectedChannel) {
      toast.error("An error occurred. Please try again.");
      return;
    }

    const channelRef = doc(db, "channels", selectedChannel.id);
    const messagesRef = collection(channelRef, "messages");

    const messagesQuery = query(
      messagesRef,
      orderBy("timestamp", "desc"),
      startAfter(this.lastMessageTimestamp),
      limit(this.messagesLimit)
    );

    const messagesSnapshot = await getDocs(messagesQuery);
    this.setMessagesFromSnapshot(messagesSnapshot);
  };

  private setMessagesFromSnapshot = (snapshot: QuerySnapshot<DocumentData>) => {
    if (snapshot.size < this.messagesLimit) {
      this.hasMore = false;
    } else {
      this.hasMore = true;
    }

    snapshot.docs.forEach((doc) => {
      if (this.messagesRegistery.has(doc.id)) {
        return;
      }

      if (!this.lastMessageTimestamp) {
        this.lastMessageTimestamp = doc.data().timestamp;
      } else {
        const lastTimestamp = new Date(
          // @ts-ignore
          this.lastMessageTimestamp?.toDate()
        ).getTime();

        const currentTimestamp = new Date(
          doc.data().timestamp?.toDate()
        ).getTime();

        if (currentTimestamp < lastTimestamp) {
          this.lastMessageTimestamp = doc.data().timestamp;
        }
      }

      const message = {
        id: doc.id,
        message: doc.data().message,
        user: doc.data().user,
        photoURL: doc.data().photoURL,
        timestamp: new Date(doc.data().timestamp?.toDate()),
      } as Message;

      this.messagesRegistery.set(message.id, message);
    });
  };

  sendMessage = (message: string) => {
    const { user } = store.userStore;
    const channel = store.channelStore.selectedChannel;

    if (!user || !channel) {
      toast.error("An error occurred. Please try again.");
      return false;
    }

    const channelRef = doc(db, "channels", channel.id);
    const messagesRef = collection(channelRef, "messages");

    addDoc(messagesRef, {
      message,
      user: user.displayName,
      photoURL: user.photoURL,
      timestamp: serverTimestamp(),
    });

    return true;
  };
}

export default MessageStore;
