import { useState, useEffect } from "react";
import { creerTransmission } from "../../services/transmissionService";

import {
    Button,
    Dialog,
    DialogActions,
    DialogContent,
    DialogTitle,
    MenuItem,
    TextField,
    Typography
} from "@mui/material";

export default function TransmissionDialog({
    open,
    dossier,
    onClose,
    onSuccess
}) {

    const [commune, setCommune] = useState(
        localStorage.getItem("naisslink_commune") || ""
    );

    const [commentaire, setCommentaire] = useState("");

    useEffect(() => {

        if (open) {

            setCommentaire("");

        }

    }, [open]);

    async function enregistrer() {

        try {

            if (!dossier) {

                alert("Aucun dossier sélectionné.");
                return;

            }

            await creerTransmission({

                numero_sejour: dossier.numero_sejour,
                commune,
                commentaire

            });

            localStorage.setItem(
                "naisslink_commune",
                commune
            );

            setCommentaire("");

            if (onSuccess) {

                await onSuccess();

            }

            onClose();

        } catch (e) {

            console.error(e);

            if (e.response?.data?.message) {

                alert(e.response.data.message);

            } else {

                alert("Erreur lors de la transmission.");

            }

        }

    }

    return (

        <Dialog
            open={open}
            onClose={onClose}
            fullWidth
            maxWidth="sm"
        >

            <DialogTitle>
                Nouvelle transmission
            </DialogTitle>

            <DialogContent>

                {dossier && (

                    <Typography sx={{ mb: 2 }}>

                        Dossier :
                        <strong> {dossier.numero_sejour}</strong>

                    </Typography>

                )}

                <TextField
                    select
                    fullWidth
                    margin="normal"
                    label="Commune destinataire"
                    value={commune}
                    onChange={(e) => setCommune(e.target.value)}
                >

                    <MenuItem value="Basse-Terre">
                        Basse-Terre
                    </MenuItem>

                    <MenuItem value="Baillif">
                        Baillif
                    </MenuItem>

                    <MenuItem value="Vieux-Habitants">
                        Vieux-Habitants
                    </MenuItem>

                    <MenuItem value="Capesterre-Belle-Eau">
                        Capesterre-Belle-Eau
                    </MenuItem>

                </TextField>

                <TextField
                    fullWidth
                    multiline
                    rows={4}
                    margin="normal"
                    label="Commentaire"
                    value={commentaire}
                    onChange={(e) => setCommentaire(e.target.value)}
                />

            </DialogContent>

            <DialogActions>

                <Button onClick={onClose}>
                    Annuler
                </Button>

                <Button
                    variant="contained"
                    onClick={enregistrer}
                >
                    Transmettre
                </Button>

            </DialogActions>

        </Dialog>

    );

}