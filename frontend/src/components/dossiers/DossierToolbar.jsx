import { Stack, TextField, Button } from "@mui/material";

export default function DossierToolbar({
    recherche,
    setRecherche,
    onNouveau
}) {

    return (

        <Stack
            direction="row"
            justifyContent="space-between"
            alignItems="center"
            sx={{ mb: 2 }}
        >

            <TextField
                label="Rechercher un séjour"
                size="small"
                value={recherche}
                onChange={(e) => setRecherche(e.target.value)}
                sx={{ width: 300 }}
            />

            <Button
                variant="contained"
                onClick={onNouveau}
            >
                Nouveau dossier
            </Button>

        </Stack>

    );

}