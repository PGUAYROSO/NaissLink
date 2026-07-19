import {
    Box,
    Button,
    TextField
} from "@mui/material";

interface Props {
    recherche: string;
    setRecherche: (value: string) => void;
    onNouvelle: () => void;
}

export default function TransmissionToolbar({
    recherche,
    setRecherche,
    onNouvelle
}: Props) {

    return (

        <Box
            display="flex"
            justifyContent="space-between"
            mb={2}
        >

            <TextField
                label="Rechercher"
                value={recherche}
                onChange={(e) =>
                    setRecherche(e.target.value)
                }
                size="small"
            />

            <Button
                variant="contained"
                onClick={onNouvelle}
            >
                Nouvelle transmission
            </Button>

        </Box>

    );

}