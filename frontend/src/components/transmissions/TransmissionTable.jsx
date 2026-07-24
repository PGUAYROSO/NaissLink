import { useState } from "react";

import {
    Box,
    Chip,
    IconButton,
    Stack
} from "@mui/material";

import { DataGrid } from "@mui/x-data-grid";

import VisibilityIcon from "@mui/icons-material/Visibility";
import MoveToInboxIcon from "@mui/icons-material/MoveToInbox";
import AssignmentIcon from "@mui/icons-material/Assignment";
import WarningIcon from "@mui/icons-material/Warning";
import CheckCircleIcon from "@mui/icons-material/CheckCircle";
import ComplementDialog from "./ComplementDialog";
import {demanderComplement} from "../../services/transmissionService";

import {
    receptionnerTransmission,
    mettreEnInstruction,
    traiterTransmission
} from "../../services/transmissionService";

import TransmissionDetailDialog from "./TransmissionDetailDialog";

export default function TransmissionTable({
    transmissions,
    chargerTransmissions
}) {

    const [dialogOpen, setDialogOpen] = useState(false);
    const [transmissionSelectionnee, setTransmissionSelectionnee] = useState(null);
    const [complementOpen, setComplementOpen] = useState(false);
    const [transmissionComplement, setTransmissionComplement] = useState(null);

    function couleurStatut(statut) {

        switch (statut) {

            case "EN_ATTENTE":
                return "warning";

            case "RECEPTIONNEE":
                return "info";

            case "EN_INSTRUCTION":
                return "secondary";

            case "COMPLEMENT":
                return "error";

            case "TRAITEE":
                return "success";

            default:
                return "default";

        }

    }

    async function receptionner(id) {

        try {

        await receptionnerTransmission(id);

        await chargerTransmissions();

    } catch (e) {

            console.error("Erreur complète :", e);
            console.error("Réponse :", e.response);

        alert(
            e.response?.data?.message ||
            e.response?.data?.erreur ||
            e.message
        );

    }

}

    async function instruction(id) {

        try {

            await mettreEnInstruction(id);

            await chargerTransmissions();

        } catch (e) {

            console.error(e);

            alert("Impossible de mettre la transmission en instruction.");

        }

    }

    async function traiter(id) {

        try {

            await traiterTransmission(id);

            await chargerTransmissions();

        } catch (e) {

            console.error(e);

            alert("Impossible de traiter la transmission.");

        }

    }

    function consulter(transmission) {

        setTransmissionSelectionnee(transmission);

        setDialogOpen(true);

    }

    function ouvrirComplement(transmission) {

        setTransmissionComplement(transmission);

        setComplementOpen(true);

}

    async function validerComplement(commentaire) {

    try {

        await demanderComplement(
            transmissionComplement.id,
            commentaire
        );

        setComplementOpen(false);

        await chargerTransmissions();

    } catch (e) {

        console.error(e);

        alert("Impossible de demander un complément.");

    }

}

    const columns = [

        {
            field: "numero_sejour",
            headerName: "N° séjour",
            width: 160
        },

        {
            field: "destinataire",
            headerName: "Commune",
            flex: 1,
            minWidth: 180
        },

        {
            field: "mode",
            headerName: "Mode",
            width: 120
        },

        {
            field: "statut",
            headerName: "Statut",
            width: 170,

            renderCell: (params) => (

                <Chip
                    label={params.value}
                    color={couleurStatut(params.value)}
                    size="small"
                />

            )

        },

        {
            field: "date_creation",
            headerName: "Date",
            width: 180,

            valueFormatter: (params) => {

                const valeur = params?.value ?? params;

                if (!valeur) return "";

                return new Date(valeur).toLocaleString("fr-FR");

            }

        },

        {
            field: "actions",
            headerName: "Actions",
            sortable: false,
            filterable: false,
            width: 230,

            renderCell: (params) => {

                const statut = params.row.statut;

                return (

                    <Stack direction="row" spacing={0.5}>

                        <IconButton
                              size="small"
                              color="primary"
                              title="Consulter"
                              onClick={() => consulter(params.row)}
>
    <VisibilityIcon />
</IconButton>

                        {statut === "EN_ATTENTE" && (

                            <IconButton
                                size="small"
                                color="primary"
                                title="Réceptionner"
                                onClick={() => receptionner(params.row.id)}
                            >
                                <MoveToInboxIcon />
                            </IconButton>

                        )}

                        {statut === "RECEPTIONNEE" && (

                            <IconButton
                                size="small"
                                color="secondary"
                                title="Mettre en instruction"
                                onClick={() => instruction(params.row.id)}
                            >
                                <AssignmentIcon />
                            </IconButton>

                        )}

                        {statut === "EN_INSTRUCTION" && (

                            <>

                                <IconButton
                                    size="small"
                                    color="warning"
                                    title="Demander un complément"
                                    onClick={() => ouvrirComplement(params.row)}
                                >
                                    <WarningIcon />
                                </IconButton>

                                <IconButton
                                    size="small"
                                    color="success"
                                    title="Traiter"
                                    onClick={() => traiter(params.row.id)}
                                >
                                    <CheckCircleIcon />
                                </IconButton>

                            </>

                        )}

                        {statut === "COMPLEMENT" && (

                            <IconButton
                                color="success"
                            sx={{
                                bgcolor: "success.light",
                                "&:hover": {
                                    bgcolor: "success.main",
                                    color: "white"
                                }
                            }}
                                title="Traiter"
                                onClick={() => traiter(params.row.id)}
                            >
                                <CheckCircleIcon />
                            </IconButton>

                        )}

                    </Stack>

                );

            }

        }

    ];

    return (

        <>

            <TransmissionDetailDialog
                open={dialogOpen}
                transmission={transmissionSelectionnee}
                onClose={() => setDialogOpen(false)}
            />

            <ComplementDialog
                open={complementOpen}
                onClose={() => setComplementOpen(false)}
                onValider={validerComplement}
            />

            <Box sx={{ height: 550, width: "100%" }}>

                <DataGrid
                    rows={transmissions}
                    columns={columns}
                    getRowId={(row) => row.id}
                    pageSizeOptions={[10, 20, 50]}
                    initialState={{
                        pagination: {
                            paginationModel: {
                                pageSize: 10
                            }
                        }
                    }}
                    disableRowSelectionOnClick
                />

            </Box>

        </>

    );

}