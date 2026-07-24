import { useState } from "react";

import {
    Box,
    Tabs,
    Tab
} from "@mui/material";

import DescriptionIcon from "@mui/icons-material/Description";
import SendIcon from "@mui/icons-material/Send";
import HistoryIcon from "@mui/icons-material/History";

import DossierDocuments from "../dossier/DossierDocuments";
import DossierTransmissions from "../dossier/DossierTransmissions";
import DossierHistorique from "../dossier/DossierHistorique";

export default function DossierTabs({ numeroSejour }) {

    const [onglet, setOnglet] = useState(0);

    return (

        <Box sx={{ mt: 3 }}>

            <Tabs
                value={onglet}
                onChange={(event, value) => setOnglet(value)}
                variant="scrollable"
                scrollButtons="auto"
            >

                <Tab
                    icon={<DescriptionIcon />}
                    iconPosition="start"
                    label="Documents"
                />

                <Tab
                    icon={<SendIcon />}
                    iconPosition="start"
                    label="Transmissions"
                />

                <Tab
                    icon={<HistoryIcon />}
                    iconPosition="start"
                    label="Historique"
                />

            </Tabs>

            <Box sx={{ mt: 3 }}>

                {onglet === 0 && (

                    <DossierDocuments
                        numeroSejour={numeroSejour}
                    />

                )}

                {onglet === 1 && (

                    <DossierTransmissions
                        numeroSejour={numeroSejour}
                    />

                )}

                {onglet === 2 && (

                    <DossierHistorique
                        numeroSejour={numeroSejour}
                    />

                )}

            </Box>

        </Box>

    );

}