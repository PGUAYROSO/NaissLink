import { useEffect, useState } from "react";
import { listerTypesDocuments } from "../../services/typeDocumentService";

import {
    Button,
    Paper,
    IconButton
} from "@mui/material";

import VisibilityIcon from "@mui/icons-material/Visibility";
import DownloadIcon from "@mui/icons-material/Download";
import DeleteIcon from "@mui/icons-material/Delete";

import { DataGrid } from "@mui/x-data-grid";

import SectionCard from "../common/SectionCard";
import UploadDocumentDialog from "./UploadDocumentDialog";
import ConfirmDialog from "../common/ConfirmDialog";

import {
    listerDocuments,
    uploadDocument,
    visualiserDocument,
    telechargerDocument,
    supprimerDocument
} from "../../services/documentService";

export default function DossierDocuments({ numeroSejour }) {

    const [documents, setDocuments] = useState([]);
    const [dialogOuvert, setDialogOuvert] = useState(false);
    const [dialogSuppression, setDialogSuppression] = useState(false);
    const [documentSelectionne, setDocumentSelectionne] = useState(null);
    const [typesDocuments, setTypesDocuments] = useState([]);

    //---------------------------------------------------
    // Chargement
    //---------------------------------------------------

    async function charger() {

        try {

            const data = await listerDocuments(numeroSejour);

            setDocuments(data);

        } catch (e) {

            console.error(e);

        }

    }

    useEffect(() => {

    charger();
    chargerTypesDocuments();

        }, [numeroSejour]);

    //---------------------------------------------------
    // Upload
    //---------------------------------------------------

    async function envoyerDocument({ typeDocument, fichier }) {

        try {

            const formData = new FormData();

            formData.append("numero_sejour", numeroSejour);
            formData.append("type_document", typeDocument);
            formData.append("fichier", fichier);

            await uploadDocument(formData);

            setDialogOuvert(false);

            charger();

        } catch (e) {

                console.error(e);

                console.error(e.response);

                console.error(e.response?.data);

            alert(
                e.response?.data?.message ||
                e.response?.data?.erreur ||
                e.message
        );

}

    }

    //---------------------------------------------------
    // Visualisation
    //---------------------------------------------------

    async function ouvrirDocument(documentId) {

        try {

            const blob = await visualiserDocument(documentId);

            const url = URL.createObjectURL(blob);

            window.open(url, "_blank");

        } catch (e) {

            console.error(e);

            alert("Impossible d'ouvrir le document.");

        }

    }

    //---------------------------------------------------
    // Téléchargement
    //---------------------------------------------------

    async function downloaderDocument(doc) {

        try {

            const blob = await telechargerDocument(doc.id);

            const url = URL.createObjectURL(blob);

            const lien = document.createElement("a");

            lien.href = url;
            lien.download = doc.nom;

            document.body.appendChild(lien);

            lien.click();

            document.body.removeChild(lien);

            URL.revokeObjectURL(url);

        } catch (e) {

            console.error(e);

            alert("Impossible de télécharger le document.");

        }

    }

    //---------------------------------------------------
    // Suppression
    //---------------------------------------------------

    async function supprimerDocumentSelectionne() {

        try {

            await supprimerDocument(documentSelectionne.id);

            setDialogSuppression(false);

            setDocumentSelectionne(null);

            charger();

        } catch (e) {

            console.error(e);

            alert("Impossible de supprimer le document.");

        }

    }

    //---------------------------------------------------
    // Charger Types Documents
    //---------------------------------------------------

    async function chargerTypesDocuments() {

    try {

        const data = await listerTypesDocuments();

        setTypesDocuments(data);

    } catch (e) {

        console.error(e);

    }

}

    //---------------------------------------------------
    // Colonnes DataGrid
    //---------------------------------------------------

    const columns = [

        {
            field: "nom",
            headerName: "Nom",
            flex: 1,
            minWidth: 260
        },

        {
            field: "type_document",
            headerName: "Type",
            width: 250,

                valueGetter: (value) => {

        const type = typesDocuments.find(
            t => t.code === value
        );

                return type ? type.libelle : value;

            }

        },

        {
            field: "taille",
            headerName: "Taille",
            width: 120,

            valueFormatter: ({ value }) => {

                if (!value) return "";

                if (value < 1024)
                    return `${value} o`;

                if (value < 1024 * 1024)
                    return `${(value / 1024).toFixed(1)} Ko`;

                return `${(value / 1024 / 1024).toFixed(1)} Mo`;

            }

        },

        {
            field: "date_upload",
            headerName: "Date d'ajout",
            width: 180,

            valueFormatter: ({ value }) =>
                value
                    ? new Date(value).toLocaleString("fr-FR")
                    : ""

        },

        {
            field: "actions",
            headerName: "Actions",
            width: 160,
            sortable: false,

            renderCell: (params) => (

                <>

                    <IconButton
                        color="primary"
                        onClick={() =>
                            ouvrirDocument(params.row.id)
                        }
                    >
                        <VisibilityIcon />
                    </IconButton>

                    <IconButton
                        color="primary"
                        onClick={() =>
                            downloaderDocument(params.row)
                        }
                    >
                        <DownloadIcon />
                    </IconButton>

                    <IconButton
                        color="error"
                        onClick={() => {

                            setDocumentSelectionne(params.row);

                            setDialogSuppression(true);

                        }}
                    >
                        <DeleteIcon />
                    </IconButton>

                </>

            )

        }

    ];

    //---------------------------------------------------
    // Interface
    //---------------------------------------------------

    return (

        <SectionCard title="Documents">

            <Paper sx={{ height: 400, mb: 2 }}>

                <DataGrid

                    rows={documents}

                    columns={columns}

                    pageSizeOptions={[5, 10, 20]}

                    initialState={{
                        pagination: {
                            paginationModel: {
                                pageSize: 5
                            }
                        }
                    }}

                />

            </Paper>

            <Button
                variant="contained"
                onClick={() => setDialogOuvert(true)}
            >
                Ajouter un document
            </Button>

            <UploadDocumentDialog
                open={dialogOuvert}
                onClose={() => setDialogOuvert(false)}
                onUpload={envoyerDocument}
            />

            <ConfirmDialog
                open={dialogSuppression}
                titre="Suppression d'un document"
                message={
                    documentSelectionne
                        ? `Voulez-vous vraiment supprimer "${documentSelectionne.nom}" ?`
                        : ""
                }
                onCancel={() => {

                    setDialogSuppression(false);

                    setDocumentSelectionne(null);

                }}
                onConfirm={supprimerDocumentSelectionne}
            />

        </SectionCard>

    );

}