import { Chip } from "@mui/material";

import SectionCard from "../common/SectionCard";
import InfoField from "../common/InfoField";

export default function DossierInformations({ dossier }) {

    return (

        <SectionCard title="Informations générales">

            <InfoField
                label="N° séjour"
                value={dossier.numero_sejour}
            />

            <InfoField
                label="Créé par"
                value={dossier.cree_par}
            />

            <InfoField
                label="Date création"
                value={
                    new Date(
                        dossier.date_creation
                    ).toLocaleString("fr-FR")
                }
            />

            <InfoField
                label="Commentaire"
                value={dossier.commentaire}
            />

            <Chip
                label={dossier.statut}
                color={
                    dossier.statut === "TRANSMIS"
                        ? "success"
                        : "warning"
                }
                sx={{ mt: 2 }}
            />

        </SectionCard>

    );

}