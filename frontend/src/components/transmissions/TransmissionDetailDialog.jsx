import { useEffect, useState } from "react";

import {
    Dialog,
    DialogTitle,
    DialogContent,
    DialogActions,
    Button,
    Grid,
    Typography,
    Chip,
    Tabs,
    Tab,
    Box,
    CircularProgress,
    Alert
} from "@mui/material";

import {
    listerHistorique
} from "../../services/transmissionService";

export default function TransmissionDetailDialog({

    open,
    transmission,
    onClose

}) {

    const [onglet, setOnglet] = useState(0);

    const [historique, setHistorique] = useState([]);

    const [chargement, setChargement] = useState(false);

    useEffect(() => {

        if (!open || !transmission?.id)
            return;

        async function chargerHistorique() {

            try {

                setChargement(true);

                const data = await listerHistorique(
                    transmission.id
                );

                setHistorique(data);

            }

            catch (e) {

                console.error(e);

                setHistorique([]);

            }

            finally {

                setChargement(false);

            }

        }

        chargerHistorique();

    }, [open, transmission]);

    if (!transmission)
        return null;

    const couleurAction = (action) => {

        switch (action) {

            case "Transmission créée":
                return "#1976d2";

            case "Transmission réceptionnée":
                return "#2e7d32";

            case "Mise en instruction":
                return "#ed6c02";

            case "Complément demandé":
                return "#d32f2f";

            case "Transmission traitée":
                return "#6a1b9a";

            default:
                return "#1976d2";
        }

    };

    return (

        <Dialog
            open={open}
            onClose={onClose}
            maxWidth="md"
            fullWidth
        >

            <DialogTitle>

                Transmission

            </DialogTitle>

            <DialogContent>

                <Tabs

                    value={onglet}

                    onChange={(event, value) => setOnglet(value)}

                    sx={{ mb: 3 }}

                >

                    <Tab label="Informations" />

                    <Tab label="Historique" />

                    <Tab label="Documents" />

                </Tabs>

                {onglet === 0 && (

                    <Grid container spacing={2}>

                        <Grid size={{ xs: 12, md: 6 }}>

                            <Typography variant="subtitle2">
                                N° séjour
                            </Typography>

                            <Typography>

                                {transmission.numero_sejour}

                            </Typography>

                        </Grid>

                        <Grid size={{ xs: 12, md: 6 }}>

                            <Typography variant="subtitle2">
                                Commune
                            </Typography>

                            <Typography>

                                {transmission.destinataire}

                            </Typography>

                        </Grid>

                        <Grid size={{ xs: 12, md: 6 }}>

                            <Typography variant="subtitle2">
                                Mode
                            </Typography>

                            <Typography>

                                {transmission.mode}

                            </Typography>

                        </Grid>

                        <Grid size={{ xs: 12, md: 6 }}>

                            <Typography variant="subtitle2">
                                Statut
                            </Typography>

                            <Chip

                                label={transmission.statut}

                                color="primary"

                            />

                        </Grid>

                        <Grid size={{ xs: 12 }}>

                            <Typography variant="subtitle2">
                                Commentaire
                            </Typography>

                            <Typography>

                                {transmission.commentaire || "Aucun commentaire"}

                            </Typography>

                        </Grid>

                    </Grid>

                )}

                {onglet === 1 && (

                    <Box>

                        {chargement ? (

                            <Box
                                sx={{
                                    display: "flex",
                                    justifyContent: "center",
                                    mt: 4
                                }}
                            >

                                <CircularProgress />

                            </Box>

                        ) : historique.length === 0 ? (

                            <Alert severity="info">

                                Aucun historique disponible.

                            </Alert>

                        ) : (

                            historique.map((ligne) => (

                                <Box

                                    key={ligne.id}

                                    sx={{

                                        mb: 2,

                                        p: 2,

                                        borderLeft: `5px solid ${couleurAction(ligne.action)}`,

                                        bgcolor: "#fafafa",

                                        borderRadius: 2,

                                        boxShadow: 1,

                                        transition: "0.2s",

                                        "&:hover": {

                                            boxShadow: 4,

                                            transform: "translateX(3px)"

                                        }

                                    }}

                                >

                                    <Typography
                                        variant="subtitle1"
                                        fontWeight="bold"
                                    >

                                        {ligne.action}

                                    </Typography>

                                    <Typography
                                        variant="body2"
                                        color="text.secondary"
                                        sx={{ mt: 0.5 }}
                                    >

                                        👤 {ligne.utilisateur}

                                    </Typography>

                                    <Typography
                                        variant="caption"
                                        display="block"
                                        sx={{ mt: 0.5 }}
                                    >

                                        {
                                            new Date(
                                                ligne.date_action
                                            ).toLocaleString(
                                                "fr-FR",
                                                {
                                                    dateStyle: "short",
                                                    timeStyle: "short"
                                                }
                                            )
                                        }

                                    </Typography>

                                    {

                                        ligne.commentaire && (

                                            <Alert
                                                severity="info"
                                                sx={{ mt: 2 }}
                                            >

                                                {ligne.commentaire}

                                            </Alert>

                                        )

                                    }

                                </Box>

                            ))

                        )}

                    </Box>

                )}

                {onglet === 2 && (

                    <Box>

                        <Alert severity="info">

                            Aucun document disponible.

                        </Alert>

                    </Box>

                )}

            </DialogContent>

            <DialogActions>

                <Button

                    onClick={onClose}

                    variant="contained"

                >

                    Fermer

                </Button>

            </DialogActions>

        </Dialog>

    );

}