import React, { useContext, useState } from "react";
import { Navigate } from "react-router-dom";
import { UserContext } from "../../UserContext";
import {
  InputAdornment,
  IconButton,
  OutlinedInput,
  InputLabel,
  FormControl,
  TextField,
  Container,
  FormHelperText,
  Grid,
  Stack,
  Button,
  Box,
} from "@mui/material";
import Visibility from "@mui/icons-material/Visibility";
import VisibilityOff from "@mui/icons-material/VisibilityOff";
import axiosInstance from "../../AxiosInstance";
import ImageInfo1 from "../../assets/logoweb.png";
import "./Login.css";

const Login = () => {
  const { user, setUser } = useContext(UserContext);
  const [showPassword, setShowPassword] = useState(false);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [usernameErr, setUsernameErr] = useState("");
  const [passwordErr, setPasswordErr] = useState("");

  const handleClickShowPassword = () => {
    setShowPassword(!showPassword);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    //console.log(username, password)
    setUsernameErr("");
    setPasswordErr("");
    try {
        var formData = new FormData()
        formData.append("username", username)
        formData.append("password", password)
      axiosInstance
        .post("/auth/login", formData, {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded', 
            'Accept': 'application/json'
          },
        })
        .then((response) => {
            localStorage.setItem("token", response.data.token)
            axiosInstance.post('/auth/verify-token', 
                JSON.stringify(response.data.token),
                { 
                    headers: { 
                        'Content-Type': 'application/json', 
                        'Accept': 'application/json'
                    },
                }
            ).then((res) => {
                console.log(res)
                setUser(res.data)
            })
        })
        .catch((err) => {
          //console.log(err.response.data)
          setUsernameErr(err.response.data.errors.username);
          setPasswordErr(err.response.data.errors.password);
        });
    } catch (error) {
      console.log(error);
    }
  };

  if (user) {
      return <Navigate to="/user-admin"/>
  }
  return (
    <Box
      sx={{
        display: "flex",
        width: "100%",
        height: "100vh",
        alignContent: "center",
      }}
    >
      <Grid
        container
        sx={{
          maxWidth: "1000px",
          maxHeight: "700px",
          margin: "auto",
          marginTop: "200px",
          borderRadius: "20px",
          backgroundColor: "#1B264D",
          boxShadow: "1px 2px 10px rgb(0 0 0 / 30%)",
          padding: "20px",
        }}
        spacing={6}
      >
        <Grid
          item
          xs={8}
          sx={{
            backgroundColor: "white",
            padding: "50px",
            borderRadius: "20px",
          }}
        >
          <Stack spacing={4}>
            <h1>
              <font style={{ color: "red" }}>Club</font> Management
            </h1>
            <h2>Đăng nhập</h2>
            <TextField
              label="Tài khoản"
              variant="outlined"
              onChange={(e) => {
                setUsername(e.target.value);
              }}
              helperText={usernameErr}
              error={usernameErr}
            />
            <FormControl variant="outlined" error={passwordErr}>
              <InputLabel htmlFor="outlined-adornment-password">
                Mật khẩu
              </InputLabel>
              <OutlinedInput
                id="outlined-adornment-password"
                type={showPassword ? "text" : "password"}
                value={password}
                onChange={(e) => {
                  setPassword(e.target.value);
                }}
                fullWidth={true}
                endAdornment={
                  <InputAdornment position="end">
                    <IconButton
                      aria-label="toggle password visibility"
                      onClick={handleClickShowPassword}
                      edge="end"
                    >
                      {showPassword ? <VisibilityOff /> : <Visibility />}
                    </IconButton>
                  </InputAdornment>
                }
                label="Password"
              />
              <FormHelperText id="outlined-adornment-password">
                {passwordErr}
              </FormHelperText>
            </FormControl>
            <Button
              variant="contained"
              sx={{ backgroundColor: "#1B264D" }}
              size="large"
              onClick={handleSubmit}
            >
              Đăng nhập
            </Button>
          </Stack>
        </Grid>
        <Grid item xs={4} sx={{ color: "white" }}>
          <Stack spacing={4}>
            <img
              src={ImageInfo1}
              alt="ảnh logo"
              style={{ marginRight: "35px" }}
            />
            <Stack spacing={2}>
              <h1>Hello, Friend!</h1>
              <p style={{ lineHeight: "22px" }}>
                Hãy tôi luyện thành một chiến binh, đừng khép mình lại.
              </p>
            </Stack>
          </Stack>
        </Grid>
      </Grid>
    </Box>
  );
};

export default Login;
