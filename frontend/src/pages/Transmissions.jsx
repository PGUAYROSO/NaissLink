import { useEffect, useState } from "react";

import { Typography } from "@mui/material";

import TransmissionToolbar from "../components/transmissions/TransmissionToolbar";
import TransmissionTable from "../components/transmissions/TransmissionTable";

import {
    listerTransmissions
} from "../services/transmissionService";

export default function Transmissions() {

    const [transmissions, setTransmissions] = useState([]);
    const [recherche, setRecherche] = useState("");

    useEffect(() => {

        chargerTransmissions();

    }, []);

    async function chargerTransmissions() {

        try {

            const data = await listerTransmissions();

            setTransmissions(data);

        } catch (e) {

            console.error(e);

        }

    }

    const transmissionsFiltrees = transmissions.filter((transmission) => {
    const texte = [
        transmission.numero_sejour ?? "",
        transmission.destinataire ?? "",
        transmission.mode ?? "",
        transmission.statut ?? ""
    ]
            .join(" ")
            .toLowerCase();

        return texte.includes(
            recherche.toLowerCase()
        );

    });

    return (

        <>

            <Typography
                variant="h4"
                sx={{ mb: 3 }}
            >
                Transmissions
            </Typography>

            <TransmissionToolbar
                recherche={recherche}
                setRecherche={setRecherche}

            />

            <TransmissionTable
                transmissions={transmissionsFiltrees}
                chargerTransmissions={chargerTransmissions}
            />

        </>

    );

}