import { useEffect, useState } from "react";

import { Typography } from "@mui/material";

import DossierToolbar from "../components/dossiers/DossierToolbar";
import DossierTable from "../components/dossiers/DossierTable";

import DossierDialog from "../components/dossiers/DossierDialog";

import {
    listerDossiers,
    creerDossier
} from "../services/dossierService";

export default function Dossiers() {

    const [dossiers, setDossiers] = useState([]);
    const [recherche, setRecherche] = useState("");
    const [dialogOuvert, setDialogOuvert] = useState(false);

    useEffect(() => {

        charger();

    }, []);

    async function charger() {

            try {

                const data = await listerDossiers();

                setDossiers(data);

            } catch (e) {

                console.error(e);

            }

        }

    const dossiersFiltres = dossiers.filter((dossier) =>
        dossier.numero_sejour
            .toLowerCase()
            .includes(recherche.toLowerCase())
    );

    function nouveauDossier() {

    setDialogOuvert(true);

}

    async function creerNouveauDossier(numeroSejour) {

    try {

        await creerDossier(numeroSejour);

        setDialogOuvert(false);

        await charger();

    } catch (e) {

        console.error(e);

        alert("Impossible de créer le dossier.");

    }

}

    return (

        <>

            <Typography
                variant="h4"
                sx={{ mb: 3 }}
            >
                Dossiers documentaires
            </Typography>

            <DossierToolbar
                recherche={recherche}
                setRecherche={setRecherche}
                onNouveau={nouveauDossier}
            />

            <DossierTable
                dossiers={dossiersFiltres}

            />
            <DossierDialog

                open={dialogOuvert}

                onClose={() => setDialogOuvert(false)}

                onCreate={creerNouveauDossier}

            />

        </>

    );

}