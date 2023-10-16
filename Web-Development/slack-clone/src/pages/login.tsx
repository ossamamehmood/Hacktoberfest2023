import IsNotAuth from "modules/auth/IsNotAuth";
import Login from "modules/user/login/Login";

const LoginPage = () => (
  <IsNotAuth>
    <Login />
  </IsNotAuth>
);

export default LoginPage;
