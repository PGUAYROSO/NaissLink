import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import PageHeader from "../components/common/PageHeader";

import DossierInformations from "../components/dossier/DossierInformations";
import DossierTabs from "../components/dossier/DossierTabs";

import { consulterDossier } from "../services/dossierService";

export default function Dossier() {

    const { numeroSejour } = useParams();

    const [dossier, setDossier] = useState(null);

    useEffect(() => {

        async function charger() {

            try {

                const data = await consulterDossier(numeroSejour);

                setDossier(data);

            } catch (e) {

                console.error(e);

            }

        }

        charger();

    }, [numeroSejour]);

    if (!dossier) {

        return <>Chargement...</>;

    }

    return (

        <>

            <PageHeader
                title="Dossier documentaire"
            />

            <DossierInformations
                dossier={dossier}
            />

            <DossierTabs
                numeroSejour={dossier.numero_sejour}
            />

        </>

    );

}