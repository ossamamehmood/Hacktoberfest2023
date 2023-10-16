import { auth } from "config/firebase";
import { onAuthStateChanged } from "firebase/auth";
import React, { useEffect } from "react";
import { useStore } from "stores/store";

const AuthProvider: React.FC = ({ children }) => {
  const { setUser } = useStore().userStore;

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (user) => {
      setUser(user);
    });

    return unsubscribe;
  }, [setUser]);

  return <>{children}</>;
};

export default AuthProvider;
