import {
    Box,
    Button,
    IconButton,
    TextField
} from "@mui/material";

import {
    DataGrid
} from "@mui/x-data-grid";

import AddIcon from "@mui/icons-material/Add";
import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";

import { useMemo, useState } from "react";

import SectionCard from "./SectionCard";

export default function CrudDataGrid({

    title,

    rows,

    columns,

    onAdd,

    onEdit,

    onDelete,

    loading = false

}) {

    const [filtre, setFiltre] = useState("");

    //--------------------------------------------------------
    // Filtrage
    //--------------------------------------------------------

    const lignes = useMemo(() => {

        if (!filtre)
            return rows;

        const recherche = filtre.toLowerCase();

        return rows.filter((ligne) =>

            Object.values(ligne)

                .join(" ")

                .toLowerCase()

                .includes(recherche)

        );

    }, [rows, filtre]);

    //--------------------------------------------------------
    // Colonnes
    //--------------------------------------------------------

    const gridColumns = [

        ...columns,

        {

            field: "actions",

            headerName: "Actions",

            width: 130,

            sortable: false,

            renderCell: (params) => (

                <>

                    <IconButton
                        color="primary"
                        onClick={() => onEdit(params.row)}
                    >
                        <EditIcon />
                    </IconButton>

                    <IconButton
                        color="error"
                        onClick={() => onDelete(params.row)}
                    >
                        <DeleteIcon />
                    </IconButton>

                </>

            )

        }

    ];

    //--------------------------------------------------------
    // Interface
    //--------------------------------------------------------

    return (

        <SectionCard title={title}>

            <Box

                sx={{

                    display: "flex",

                    justifyContent: "space-between",

                    mb: 2,

                    gap: 2

                }}

            >

                <TextField

                    label="Rechercher"

                    size="small"

                    value={filtre}

                    onChange={(e) =>
                        setFiltre(e.target.value)
                    }

                    sx={{ width: 350 }}

                />

                <Button

                    variant="contained"

                    startIcon={<AddIcon />}

                    onClick={onAdd}

                >

                    Nouveau

                </Button>

            </Box>

            <DataGrid

                autoHeight

                loading={loading}

                rows={lignes}

                columns={gridColumns}

                pageSizeOptions={[5, 10, 20]}

                initialState={{

                    pagination: {

                        paginationModel: {

                            pageSize: 10

                        }

                    }

                }}

                disableRowSelectionOnClick

            />

        </SectionCard>

    );

}