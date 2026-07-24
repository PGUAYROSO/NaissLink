import { useState, useEffect } from "react";

import {
    Dialog,
    DialogTitle,
    DialogContent,
    DialogActions,
    Button,
    TextField,
    MenuItem
} from "@mui/material";

import { listerTypesDocuments } from "../../services/typeDocumentService";

export default function UploadDocumentDialog({

    open,
    onClose,
    onUpload

}) {

    const [typeDocument, setTypeDocument] = useState("");
    const [fichier, setFichier] = useState(null);
    const [typesDocuments, setTypesDocuments] = useState([]);

    useEffect(() => {

        async function chargerTypesDocuments() {

            try {

                const data = await listerTypesDocuments();

                setTypesDocuments(data);

            } catch (error) {

                console.error(
                    "Erreur lors du chargement des types de documents :",
                    error
                );

            }

        }

        if (open) {

            chargerTypesDocuments();

        }

    }, [open]);

    function envoyer() {

        if (!typeDocument || !fichier) return;

        onUpload({
            typeDocument,
            fichier
        });

        setTypeDocument("");
        setFichier(null);

    }

    return (

        <Dialog
            open={open}
            onClose={onClose}
            fullWidth
            maxWidth="sm"
        >

            <DialogTitle>

                Ajouter un document

            </DialogTitle>

            <DialogContent>

                <TextField

                    select

                    fullWidth

                    margin="normal"

                    label="Type de document"

                    value={typeDocument}

                    onChange={(e) =>
                        setTypeDocument(e.target.value)
                    }

                >

                    {typesDocuments
                        .filter(type => type.actif)
                        .sort((a, b) => a.ordre - b.ordre)
                        .map(type => (

                            <MenuItem
                                key={type.id}
                                value={type.code}
                            >
                                {type.libelle}
                            </MenuItem>

                        ))}

                </TextField>

                <Button
                    component="label"
                    variant="outlined"
                    fullWidth
                    sx={{ mt: 2 }}
                >

                    Choisir un fichier

                    <input
                        hidden
                        type="file"
                        onChange={(e) =>
                            setFichier(e.target.files[0])
                        }
                    />

                </Button>

                {

                    fichier && (

                        <p>

                            {fichier.name}

                        </p>

                    )

                }

            </DialogContent>

            <DialogActions>

                <Button onClick={onClose}>

                    Annuler

                </Button>

                <Button
                    variant="contained"
                    onClick={envoyer}
                >

                    Téléverser

                </Button>

            </DialogActions>

        </Dialog>

    );

}