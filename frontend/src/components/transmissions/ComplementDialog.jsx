import { useState, useEffect } from "react";

import {
    Dialog,
    DialogTitle,
    DialogContent,
    DialogActions,
    Button,
    TextField
} from "@mui/material";

export default function ComplementDialog({
    open,
    onClose,
    onValider
}) {

    const [commentaire, setCommentaire] = useState("");

    useEffect(() => {

        if (open) {
            setCommentaire("");
        }

    }, [open]);

    function valider() {

        if (!commentaire.trim()) {

            alert("Veuillez saisir un commentaire.");

            return;

        }

        onValider(commentaire);

    }

    return (

        <Dialog
            open={open}
            onClose={onClose}
            maxWidth="sm"
            fullWidth
        >

            <DialogTitle>
                Demande de complément
            </DialogTitle>

            <DialogContent>

                <TextField
                    autoFocus
                    fullWidth
                    multiline
                    rows={5}
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
                    onClick={valider}
                >
                    Envoyer
                </Button>

            </DialogActions>

        </Dialog>

    );

}