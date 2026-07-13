import {
    AppBar,
    Toolbar,
    Typography,
    Box,
    Button
} from "@mui/material";

import { useAuth } from "../contexts/AuthContext";

export default function Header() {

    const { utilisateur, logout } = useAuth();

    return (

        <AppBar position="fixed">

            <Toolbar>

                <Typography
                    variant="h6"
                    sx={{ flexGrow: 1 }}
                >
                    NaissLink
                </Typography>

                <Box>

                    <Typography
                        component="span"
                        sx={{ mr: 3 }}
                    >
                        {utilisateur?.prenom} {utilisateur?.nom}
                    </Typography>

                    <Button
                        color="inherit"
                        onClick={logout}
                    >
                        Déconnexion
                    </Button>

                </Box>

            </Toolbar>

        </AppBar>

    );

}