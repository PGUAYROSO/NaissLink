import { useEffect, useState } from "react";

import {
    Typography,
    Paper,
    Chip,
    IconButton,
    Box
} from "@mui/material";

import VisibilityIcon from "@mui/icons-material/Visibility";

import { DataGrid } from "@mui/x-data-grid";

import { listerDossiers } from "../services/dossierService";

export default function Dossiers() {

    const [dossiers, setDossiers] = useState([]);

    useEffect(() => {

        async function charger() {

            try {

                const data = await listerDossiers();

                setDossiers(data);

            } catch (e) {

                console.error(e);

            }

        }

        charger();

    }, []);

    const columns = [

        {
            field: "numero_sejour",
            headerName: "N° séjour",
            flex: 1
        },

        {
            field: "statut",
            headerName: "Statut",
            flex: 1,
            renderCell: (params) => (

                <Chip
                    label={params.value}
                    color={
                        params.value === "TRANSMIS"
                            ? "success"
                            : "warning"
                    }
                    size="small"
                />

            )
        },

        {
            field: "nombre_documents",
            headerName: "Documents",
            type: "number",
            width: 120
        },

        {
            field: "nombre_transmissions",
            headerName: "Transmissions",
            type: "number",
            width: 140
        },

        {
            field: "cree_par",
            headerName: "Créé par",
            width: 150
        },

        {
            field: "date_creation",
            headerName: "Date création",
            width: 180,
                    valueFormatter: (value) => {
        if (!value) return "";

        return new Date(value).toLocaleString("fr-FR");
    }
},


        {
            field: "actions",
            headerName: "Actions",
            width: 100,
            sortable: false,

            renderCell: () => (

                <IconButton color="primary">

                    <VisibilityIcon />

                </IconButton>

            )

        }

    ];

    return (

        <>

            <Typography
                variant="h4"
                sx={{ mb: 3 }}
            >
                Dossiers documentaires
            </Typography>

            <Paper sx={{ height: 500 }}>

                <DataGrid

                    rows={dossiers}

                    columns={columns}

                    pageSizeOptions={[5, 10, 20]}

                    initialState={{
                        pagination: {
                            paginationModel: {
                                pageSize: 10
                            }
                        }
                    }}

                />

            </Paper>

        </>

    );

}