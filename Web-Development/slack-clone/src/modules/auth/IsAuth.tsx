import Loading from "components/loading/Loading";
import { observer } from "mobx-react-lite";
import { useRouter } from "next/router";
import React, { useEffect } from "react";
import { useStore } from "stores/store";

const IsAuth: React.FC = ({ children }) => {
  const { user, loading } = useStore().userStore;
  const router = useRouter();

  useEffect(() => {
    if (!user && !loading) {
      router.replace("/login");
    }
  }, [user, loading, router]);

  if (user) {
    return <>{children}</>;
  }

  return <Loading />;
};

export default observer(IsAuth);
