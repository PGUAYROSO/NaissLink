import {
    Paper,
    Chip,
    IconButton
} from "@mui/material";

import VisibilityIcon from "@mui/icons-material/Visibility";

import { DataGrid } from "@mui/x-data-grid";

export default function DossierTable({ dossiers }) {

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
            width: 120,
            type: "number"
        },

        {
            field: "nombre_transmissions",
            headerName: "Transmissions",
            width: 150,
            type: "number"
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

    );

}