import {
    Paper,
    Chip,
    IconButton
} from "@mui/material";

import VisibilityIcon from "@mui/icons-material/Visibility";
import SendIcon from "@mui/icons-material/Send";

import { DataGrid } from "@mui/x-data-grid";
import { useNavigate } from "react-router-dom";

export default function DossierTable({ dossiers, onTransmettre }) {

    const navigate = useNavigate();

    const columns = [

        {
            field: "numero_sejour",
            headerName: "N° séjour",
            flex: 1
        },

        {
            field: "statut",
            headerName: "Statut",
            width: 140,
            renderCell: (params) => (

                <Chip
                    label={params.value}
                    color={
                        params.value === "BROUILLON"
                            ? "warning"
                            : "success"
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
            width: 120,
            sortable: false,
            filterable: false,

            renderCell: (params) => (

                <>

                    <IconButton
                        color="primary"
                        onClick={() =>
                            navigate(`/dossiers/${params.row.numero_sejour}`)
                        }
                    >
                        <VisibilityIcon />
                    </IconButton>

                    <IconButton
                        color="success"
                        onClick={() => onTransmettre(params.row)}
                    >
                        <SendIcon />
                    </IconButton>

                </>

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