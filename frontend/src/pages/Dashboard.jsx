import {
    Grid,
    Paper,
    Typography,
    Box
} from "@mui/material";

import {
    Folder,
    Send,
    Schedule,
    ErrorOutlineOutlined,
    ChildCare
} from "@mui/icons-material";

const cartes = [

    {
        titre: "Dossiers en cours",
        valeur: 28,
        icone: <Folder fontSize="large" color="primary" />
    },

    {
        titre: "Transmissions envoyées",
        valeur: 15,
        icone: <Send fontSize="large" color="success" />
    },

    {
        titre: "En attente mairie",
        valeur: 4,
        icone: <Schedule fontSize="large" color="warning" />
    },

    {
        titre: "Compléments demandés",
        valeur: 2,
        icone: <ErrorOutlineOutlined fontSize="large" color="error" />
    },

    {
        titre: "Naissances aujourd'hui",
        valeur: 6,
        icone: <ChildCare fontSize="large" color="secondary" />
    }

];

export default function Dashboard() {

    return (

        <Box>

            <Typography
                variant="h4"
                fontWeight="bold"
                gutterBottom
            >
                Tableau de bord
            </Typography>

            <Typography
                color="text.secondary"
                sx={{ mb: 4 }}
            >
                Bienvenue sur NaissLink
            </Typography>

            <Grid container spacing={3}>

                {cartes.map((carte) => (

                    <Grid
                        item
                        xs={12}
                        sm={6}
                        md={4}
                        lg={3}
                        key={carte.titre}
                    >

                        <Paper
                            elevation={2}
                            sx={{
                                p: 3,
                                borderRadius: 3,
                                height: 170,
                                display: "flex",
                                flexDirection: "column",
                                justifyContent: "space-between",
                                transition: "0.2s",

                                "&:hover": {

                                    transform: "translateY(-4px)",

                                    boxShadow: 6

                                }
                            }}
                        >

                            <Box>

                                {carte.icone}

                            </Box>

                            <Typography
                                variant="h3"
                                fontWeight="bold"
                            >
                                {carte.valeur}
                            </Typography>

                            <Typography
                                color="text.secondary"
                            >
                                {carte.titre}
                            </Typography>

                        </Paper>

                    </Grid>

                ))}

            </Grid>

            <Paper
                elevation={2}
                sx={{
                    mt: 5,
                    p: 3,
                    borderRadius: 3
                }}
            >

                <Typography
                    variant="h6"
                    gutterBottom
                >
                    Dernières activités
                </Typography>

                <Typography color="text.secondary">

                    • Transmission envoyée à la mairie de Basse-Terre

                </Typography>

                <Typography color="text.secondary">

                    • Dossier n°2026-00025 créé

                </Typography>

                <Typography color="text.secondary">

                    • Complément demandé par la mairie

                </Typography>

                <Typography color="text.secondary">

                    • Déclaration de naissance validée

                </Typography>

            </Paper>

        </Box>

    );

}