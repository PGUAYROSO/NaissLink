import { useEffect, useState } from "react";

import PageHeader from "../components/common/PageHeader";
import CrudDataGrid from "../components/common/CrudDataGrid";

import {
    listerTypesDocuments,
    supprimerTypeDocument
} from "../services/typeDocumentService";

export default function TypesDocuments() {

    const [typesDocuments, setTypesDocuments] = useState([]);

    const [loading, setLoading] = useState(false);

    //----------------------------------------------------
    // Chargement
    //----------------------------------------------------

    async function charger() {

        try {

            setLoading(true);

            const data = await listerTypesDocuments();

            setTypesDocuments(data);

        } catch (e) {

            console.error(e);

        } finally {

            setLoading(false);

        }

    }

    useEffect(() => {

        charger();

    }, []);

    //----------------------------------------------------
    // Nouveau
    //----------------------------------------------------

    function nouveau() {

        alert("Ouverture du dialogue");

    }

    //----------------------------------------------------
    // Modifier
    //----------------------------------------------------

    function modifier(typeDocument) {

        alert(typeDocument.libelle);

    }

    //----------------------------------------------------
    // Supprimer
    //----------------------------------------------------

    async function supprimer(typeDocument) {

        if (!window.confirm(
            `Supprimer ${typeDocument.libelle} ?`
        )) {
            return;
        }

        await supprimerTypeDocument(typeDocument.id);

        charger();

    }

    //----------------------------------------------------
    // Colonnes
    //----------------------------------------------------

    const columns = [

        {
            field: "code",
            headerName: "Code",
            flex: 1
        },

        {
            field: "libelle",
            headerName: "Libellé",
            flex: 2
        },

        {
            field: "ordre",
            headerName: "Ordre",
            width: 100
        },

        {
            field: "actif",
            headerName: "Actif",
            width: 100,

            valueFormatter: ({ value }) =>
                value ? "Oui" : "Non"
        }

    ];

    //----------------------------------------------------

    return (

        <>

            <PageHeader
                title="Types de documents"
            />

            <CrudDataGrid

                title="Référentiel"

                rows={typesDocuments}

                columns={columns}

                loading={loading}

                onAdd={nouveau}

                onEdit={modifier}

                onDelete={supprimer}

            />

        </>

    );

}