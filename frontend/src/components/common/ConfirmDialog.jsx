import {
    Dialog,
    DialogTitle,
    DialogContent,
    DialogContentText,
    DialogActions,
    Button
} from "@mui/material";

export default function ConfirmDialog({

    open,
    titre,
    message,
    onCancel,
    onConfirm

}) {

    return (

        <Dialog
            open={open}
            onClose={onCancel}
            maxWidth="xs"
            fullWidth
        >

            <DialogTitle>

                {titre}

            </DialogTitle>

            <DialogContent>

                <DialogContentText>

                    {message}

                </DialogContentText>

            </DialogContent>

            <DialogActions>

                <Button
                    onClick={onCancel}
                >
                    Annuler
                </Button>

                <Button
                    variant="contained"
                    color="error"
                    onClick={onConfirm}
                >
                    Supprimer
                </Button>

            </DialogActions>

        </Dialog>

    );

}