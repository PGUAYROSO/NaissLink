import { useState } from "react";

import {
    Dialog,
    DialogTitle,
    DialogContent,
    DialogActions,
    TextField,
    Button
} from "@mui/material";

export default function DossierDialog({

    open,
    onClose,
    onCreate

}) {

    const [numeroSejour, setNumeroSejour] = useState("");

    function creer() {

        onCreate(numeroSejour);

        setNumeroSejour("");

    }

    return (

        <Dialog
            open={open}
            onClose={onClose}
            maxWidth="sm"
            fullWidth
        >

            <DialogTitle>

                Nouveau dossier documentaire

            </DialogTitle>

            <DialogContent>

                <TextField

                    autoFocus

                    fullWidth

                    margin="normal"

                    label="Numéro de séjour"

                    value={numeroSejour}

                    onChange={(e) =>
                        setNumeroSejour(e.target.value)
                    }

                />

            </DialogContent>

            <DialogActions>

                <Button
                    onClick={onClose}
                >
                    Annuler
                </Button>

                <Button

                    variant="contained"

                    onClick={creer}

                >

                    Créer

                </Button>

            </DialogActions>

        </Dialog>

    );

}