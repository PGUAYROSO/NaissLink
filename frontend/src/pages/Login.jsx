import { useState } from "react";

import {
    Box,
    Paper,
    Typography,
    TextField,
    Button
} from "@mui/material";

import { login as loginService } from "../services/authService";
import { useAuth } from "../contexts/AuthContext";

export default function Login() {

    const { login } = useAuth();

    const [identifiant, setIdentifiant] = useState("");
    const [motDePasse, setMotDePasse] = useState("");

    async function seConnecter() {

        try {

            const resultat = await loginService(
                identifiant,
                motDePasse
            );

            login(
                resultat.data.access_token,
                resultat.data.utilisateur
            );

            console.log(resultat);

        } catch (e) {

            console.error(e);

            alert("Identifiants incorrects.");

        }

    }

    return (

        <Box
            sx={{
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                height: "100vh",
                backgroundColor: "background.default"
            }}
        >

            <Paper
                elevation={4}
                sx={{
                    p: 5,
                    width: 420
                }}
            >

                <Typography
                    variant="h4"
                    align="center"
                >
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
                    type="password"
                    label="Mot de passe"
                    margin="normal"
                    value={motDePasse}
                    onChange={(e) =>
                        setMotDePasse(e.target.value)
                    }
                />

                <Button
                    variant="contained"
                    fullWidth
                    sx={{ mt: 3 }}
                    onClick={seConnecter}
                >
                    Se connecter
                </Button>

            </Paper>

        </Box>

    );

}