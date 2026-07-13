import { useNavigate } from "react-router-dom";
import { useState } from "react";

import {
  Box,
  Paper,
  Typography,
  TextField,
  Button,
} from "@mui/material";

import { login as loginService } from "../services/authService";
import { useAuth } from "../contexts/AuthContext";

export default function Login() {

    const { login } = useAuth();

    const navigate = useNavigate();

    const [identifiant, setIdentifiant] = useState("");
    const [motDePasse, setMotDePasse] = useState("");

  async function seConnecter() {
    try {
      const resultat = await loginService(
        identifiant,
        motDePasse
      );

      login(
    resultat.access_token,
    resultat.utilisateur
      );

      console.log(resultat);

      navigate("/dashboard");
    } catch (e) {
      console.error(e);
      alert("Login ou mot de passe incorrect.");
    }
  }

  return (
    <Box
      sx={{
        height: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        bgcolor: "background.default",
      }}
    >
      <Paper
        elevation={5}
        sx={{
          width: 420,
          p: 5,
        }}
      >
        <Typography variant="h4" align="center">
          NaissLink
        </Typography>

        <Typography
          align="center"
          sx={{ mb: 3 }}
        >
          Gestion des déclarations de naissance
        </Typography>

        <TextField
          fullWidth
          label="Login"
          margin="normal"
          value={identifiant}
          onChange={(e) =>
            setIdentifiant(e.target.value)
          }
        />

        <TextField
          fullWidth
          label="Mot de passe"
          type="password"
          margin="normal"
          value={motDePasse}
          onChange={(e) =>
            setMotDePasse(e.target.value)
          }
        />

        <Button
          fullWidth
          variant="contained"
          sx={{ mt: 3 }}
          onClick={seConnecter}
        >
          Se connecter
        </Button>
      </Paper>
    </Box>
  );
}