import { Typography, Box } from "@mui/material";
import { useAuth } from "../contexts/AuthContext";

export default function Dashboard() {

    const { utilisateur } = useAuth();

    return (

        <Box sx={{ p: 5 }}>

            <Typography variant="h3">
                Bienvenue {utilisateur?.prenom}
            </Typography>

            <Typography sx={{ mt: 3 }}>
                Vous êtes connecté à NaissLink.
            </Typography>

            <Typography sx={{ mt: 2 }}>
                Rôle : {utilisateur?.role}
            </Typography>

        </Box>

    );

}